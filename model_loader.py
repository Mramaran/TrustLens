# ============================================================================
# TrustLens - Model Loader & Inference Service
# Developed by: Hack Elite
# ============================================================================

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import io
from PIL import Image

# Global model cache
_models = {
    'cnn': None,
    'eff_net': None,
    'eff_net_art': None
}

def load_models():
    """Load all models into memory if not already loaded."""
    global _models
    
    if _models['eff_net'] is None:
        try:
            _models['eff_net'] = tf.keras.models.load_model('EfficientNet_Models/efficientnetb3_binary_classifier_8.h5')
            print("Loaded EfficientNet model")
        except Exception as e:
            print(f"Error loading EfficientNet: {e}")

    if _models['eff_net_art'] is None:
        try:
            _models['eff_net_art'] = tf.keras.models.load_model('EfficientNet_Models/EfficientNet_fine_tune_art_model.h5')
            print("Loaded EfficientNet Art model")
        except Exception as e:
            print(f"Error loading EfficientNet Art: {e}")

    # CNN model weights path (model is built in code)
    if _models['cnn'] is None:
        try:
            _models['cnn'] = 'CNN_model_weight/model_weights.weights.h5'
            print("Set CNN weights path")
        except Exception as e:
            print(f"Error setting CNN weights: {e}")
            
    return _models['eff_net'], _models['eff_net_art'], _models['cnn']

def predict_cnn(img_arr, weights_path):
    """Run inference using the custom CNN architecture."""
    my_model = Sequential()
    my_model.add(Conv2D(filters=16, kernel_size=(3, 3), strides=(1, 1), activation='relu', input_shape=(256, 256, 3)))
    my_model.add(BatchNormalization())
    my_model.add(MaxPooling2D())
    
    my_model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu')) 
    my_model.add(BatchNormalization())
    my_model.add(MaxPooling2D()) 

    my_model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu')) 
    my_model.add(BatchNormalization())
    my_model.add(MaxPooling2D())
    
    my_model.add(Flatten())
    my_model.add(Dense(512, activation='relu')) 
    my_model.add(Dropout(0.09)) 
    my_model.add(Dense(1, activation='sigmoid'))
    my_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Load the pre-trained weights
    my_model.load_weights(weights_path)

    prediction = my_model.predict(img_arr)
    return prediction

def predict_effnet(model, img_arr):
    """Run inference using EfficientNet."""
    # Strategy scope logic handled in individual calls if needed, 
    # but for simple inference on CPU/GPU, direct predict is usually fine.
    # If TPU logic is strict requirement we can add it back, but usually not needed for local inference.
    return model.predict(img_arr)

def preprocess_image(image_input, target_size):
    """
    Preprocess image for model inference.
    image_input: file path, file-like object, or PIL Image
    """
    if isinstance(image_input, (str, io.BytesIO)):
        img = load_img(image_input, target_size=target_size)
    elif isinstance(image_input, Image.Image):
        img = image_input.resize(target_size)
    else:
        raise ValueError("Unsupported image input type")
        
    img_arr = img_to_array(img)
    
    # Normalize for CNN (0-1 range) if needed. 
    # Note: app.py does normalization for CNN but not explicitly for EffNet (effnets usually expect specific preprocessing)
    # create_effnet_v2 helper usually includes preprocessing layer.
    # But trusting app.py logic:
    # CNN: / 255.0
    # EffNet: standard load_img (0-255 range usually, unless model has rescale)
    
    return img_arr

def analyze_image(image_file, model_type='cnn'):
    """
    Main entry point for analysis.
    image_file: file-like object or BytesIO
    model_type: 'cnn', 'efficientnet', 'efficientnet_art'
    """
    eff_net, eff_art, cnn_weights = load_models()
    
    if model_type == 'cnn':
        # CNN Logic
        img_arr = preprocess_image(image_file, (256, 256))
        img_arr = img_arr / 255.0  # Normalize
        img_arr = img_arr.reshape((1, 256, 256, 3))
        prediction = predict_cnn(img_arr, cnn_weights)
        
    elif model_type == 'efficientnet':
        # EffNet Logic
        img_arr = preprocess_image(image_file, (300, 300))
        img_arr = np.expand_dims(img_arr, axis=0)
        prediction = predict_effnet(eff_net, img_arr)
        
    elif model_type == 'efficientnet_art':
        # EffNet Art Logic
        img_arr = preprocess_image(image_file, (224, 224))
        img_arr = np.expand_dims(img_arr, axis=0)
        prediction = predict_effnet(eff_art, img_arr)
    
    else:
        raise ValueError("Invalid model type")
        
    score = float(prediction[0][0])
    label = "AI Generated" if score < 0.5 else "REAL"
    confidence = (1 - score) if score < 0.5 else score # This is a simplification, app uses raw probability
    
    return {
        "label": label,
        "score": score,
        "confidence": confidence,
        "model": model_type
    }
