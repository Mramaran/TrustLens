# <p align="center"> 🔍 TrustLens - AI Image Detection System </p> 

<p align="center">
  <strong>Developed by Hack Elite for Cryptera Hackathon</strong>
</p>

## 🎯 Introduction
**TrustLens** is an advanced image authentication system that leverages cutting-edge deep learning models to distinguish between authentic photographs and AI-generated imagery. In an era where synthetic media is increasingly prevalent, TrustLens provides a reliable, accessible solution for verifying image authenticity.

Our system employs multiple neural network architectures to provide comprehensive analysis, ensuring high accuracy across diverse image types - from natural photographs to artistic creations.

## 🤖 Models Implemented
TrustLens utilizes three powerful deep learning models, each optimized for different scenarios:

1. **Custom CNN Architecture** - Lightweight and fast, optimized for general-purpose detection
2. **EfficientNet B3 Model** - High-accuracy model for complex image analysis
3. **EfficientNet Art Specialist** - Fine-tuned specifically for artistic and stylized images

## 👥 Team Hack Elite
This project was developed for the **Cryptera Hackathon** by **Hack Elite**.

*Building trust in digital media, one image at a time.*

## UI

https://github.com/user-attachments/assets/04928593-8632-4411-bda0-8b1748fc2ac4



## 📋 Project Overview
**TrustLens** addresses the growing challenge of AI-generated imagery in digital media. Our deep learning system provides:

- **Multi-Model Analysis**: Three specialized neural networks for comprehensive detection
- **High Accuracy**: 97-98% accuracy across different image types
- **User-Friendly Interface**: Intuitive Streamlit-based web application and browser extension
- **Real-Time Processing**: Instant analysis with confidence scores
- **Versatile Detection**: Handles photographs, art, and various AI-generation styles

The system preprocesses uploaded images, normalizes data, and applies advanced CNN and EfficientNet architectures to classify authenticity. Results include detailed confidence metrics and visual feedback.

## 📊 Datasets Used
TrustLens was trained on diverse, high-quality datasets to ensure robust performance:

**Primary Dataset:**
- [CIFAKE: Real and AI-Generated Synthetic Images](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images) - 120,000 images (60k real from CIFAR-10, 60k AI-generated via Stable Diffusion)

**Artistic & Specialized Datasets:**
- [Detecting AI-generated Artwork](https://www.kaggle.com/datasets/birdy654/detecting-ai-generated-artwork) - 3,410 images for art-specific detection
- [Midjourney Images & Prompts](https://www.kaggle.com/datasets/cyanex1702/midjourney-imagesprompt) - Extensive Midjourney-generated collection
- [DALLE Art Collections](https://www.kaggle.com/datasets/nikbearbrown/dalle-art-march-2023) - AI-generated art from DALL-E
- [ArtStyles Dataset](https://www.kaggle.com/datasets/norasami/artstylesdataset/data) - 360 images across Anime, Comic, and Semi-Realism styles
- [Paintings from 10 Artists](https://www.kaggle.com/datasets/binukandagedon/paintings-from-10-different-popular-artists) - Real artwork for comparison

## 🛠️ Technologies Used
- **Deep Learning**: TensorFlow 2.18.0, Keras
- **Web Framework**: Streamlit 1.40.0, FastAPI (for extension API)
- **Data Processing**: NumPy, Pillow, OpenCV
- **Model Architecture**: Custom CNN, EfficientNet B3
- **Development**: Python 3.x, Jupyter Notebooks
- **Version Control**: Git
- **Browser Extension**: Chrome/Edge compatible

## 📈 Model Performance

### Custom CNN Model
- **Accuracy**: 97.62%
- **Precision**: 97.6%
- **Recall**: 97.6%
- **F1 Score**: 97.6%

**Strengths**: Excellent at detecting real nature, animal, and human photographs. Fast inference time.  
**Limitations**: Occasional challenges with AI-generated headshots and fantasy art.

### EfficientNet B3 Model
- **Accuracy**: 97.72%
- **Precision**: 97.4%
- **Recall**: 98.05%
- **F1 Score**: 97.72%

**Strengths**: Superior performance on high-quality real art and AI-generated portraits. Handles complex scenes well.  
**Limitations**: Some difficulty with specific digital art styles (3D animated, neon, cyberpunk).

### EfficientNet Art Specialist
- **Accuracy**: 98%
- **Precision**: 97%
- **Recall**: 98%
- **F1 Score**: 98%

**Strengths**: Exceptional at identifying AI-generated art, animals, and nature imagery.  
**Limitations**: Optimized for fake detection; may require additional validation for real images.

> **Model Synergy**: The three models complement each other - where one struggles, another excels. This multi-model approach ensures comprehensive coverage across diverse image types.

## 🌟 Practical Applications

In today's digital landscape, **TrustLens** serves critical needs:

- **Media Verification**: News organizations can authenticate submitted images
- **Social Media Platforms**: Automated detection of synthetic content
- **Digital Forensics**: Support investigations involving manipulated imagery
- **Content Moderation**: Identify and flag AI-generated content
- **Academic Research**: Study AI-generated image characteristics
- **Personal Use**: Verify authenticity of images before sharing

**Fighting Misinformation**: TrustLens helps combat the spread of deepfakes and synthetic media, ensuring the integrity of visual information in journalism, social media, and public discourse.

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)
- Google Chrome or Microsoft Edge browser (for extension)

### Model Downloads
The pre-trained models are hosted on Google Drive for easy access. Download the following files and place them in the respective directories:

1. **CNN Model Weights**:
   - Download `model_weights.weights.h5` from [Google Drive Link](https://drive.google.com/your-link-here)
   - Copy to `CNN_model_weight/` folder

2. **EfficientNet Models**:
   - Download `efficientnetb3_binary_classifier_8.h5` from [Google Drive Link](https://drive.google.com/your-link-here)
   - Download `EfficientNet_fine_tune_art_model.h5` from [Google Drive Link](https://drive.google.com/your-link-here)
   - Copy to `EfficientNet_Models/` folder

*Note: Replace the placeholder links with the actual Google Drive sharing links for the model files.*

### Installation

1. **Navigate to your desired directory**
   ```bash
   cd your_directory
   ```

2. **Clone the TrustLens repository**
   ```bash
   git clone https://github.com/YourUsername/TrustLens.git
   ```

3. **Navigate to the project directory**
   ```bash
   cd TrustLens
   ```

4. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

5. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Launch TrustLens Web App**
   ```bash
   streamlit run app.py
   ```

8. **Access the web application**
   
   Open your browser and navigate to: `http://localhost:8501`

## 🔌 Browser Extension Setup

TrustLens also includes a browser extension for analyzing images directly from any webpage.

### Components
1. **Backend API (`api.py`)**: Runs locally to process images using the deep learning models.
2. **Browser Extension (`extension/`)**: Side panel UI that communicates with the backend.

### Setup Instructions

#### 1. Start the Backend Server
Open a terminal in the project root and run:
```bash
uvicorn api:app --reload
```
You should see: `Uvicorn running on http://127.0.0.1:8000`

#### 2. Install the Extension in Chrome/Edge
1. Open your browser and navigate to `chrome://extensions` (or `edge://extensions`).
2. Enable **Developer mode** (toggle in top right).
3. Click **Load unpacked**.
4. Select the `extension` folder inside this project directory.
5. The **TrustLens** icon should appear in your toolbar.

### Usage Guide

#### Method 1: Right-Click Analysis
1. Right-click on any image on a webpage.
2. Select **"Analyze with TrustLens"**.
3. The side panel will open with the analysis results.

#### Method 2: Extension Icon
1. Click the TrustLens extension icon in your toolbar.
2. The side panel will slide out from the right side of the browser.
3. Drag and drop an image file into the panel or click to upload.
4. Click **Analyze Image**.
5. View the Real vs AI prediction and confidence score.

### Troubleshooting
- **API Error**: Ensure the `api.py` server is running in your terminal.
- **Model Error**: Verify that model files exist in `EfficientNet_Models` and `CNN_model_weight`.
- **CORS Error**: The API is configured to accept requests from all extensions for simplified testing.

## 💡 Usage

### Web Application
1. Upload an image (PNG, JPG, or JPEG format)
2. Select a detection model:
   - **CNN** - Fast, general-purpose detection
   - **EfficientNet** - High accuracy for complex images
   - **EfficientNet Art** - Specialized for artistic content
3. View the prediction results with confidence scores
4. Analyze whether the image is authentic or AI-generated

### Browser Extension
Use the extension to analyze images directly from websites without downloading them.

## 🎨 Features

- **Multi-Model Selection**: Choose from three specialized models
- **Real-Time Analysis**: Instant predictions with confidence metrics
- **Elegant UI**: Clean, professional interface with blue theme
- **High Accuracy**: 97-98% accuracy across model types
- **Easy to Use**: Simple drag-and-drop interface
- **Browser Integration**: Extension for seamless web analysis

## 🔮 Future Enhancements

- Batch image processing
- Detailed analysis reports
- API endpoint for integration
- Mobile application
- Enhanced visualization tools

## 📄 License

This project is developed for the Cryptera Hackathon by Hack Elite.

## 🙏 Acknowledgments

- Original dataset creators and Kaggle community
- TensorFlow and Streamlit development teams
- Cryptera Hackathon organizers

---

<p align="center">
  <strong>TrustLens - Building Trust in Digital Media</strong><br>
  Developed with ❤️ by Hack Elite
</p>






