# ============================================================================
# TrustLens - AI Image Detection System
# Configuration File
# Developed by: Hack Elite for Cryptera Hackathon
# ============================================================================

"""
Central configuration file for TrustLens application.
Modify these settings to customize the application behavior.
"""

import os

# ============================================================================
# Application Settings
# ============================================================================
APP_TITLE = "TrustLens"
APP_SUBTITLE = "AI Image Detection System"
APP_DESCRIPTION = "Advanced image authentication using deep learning"
TEAM_NAME = "Hack Elite"
HACKATHON_NAME = "Cryptera"

# ============================================================================
# Model Paths
# ============================================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# EfficientNet Models
EFFICIENTNET_MODEL_PATH = os.path.join(
    BASE_DIR, 
    'EfficientNet_Models', 
    'efficientnetb3_binary_classifier_8.h5'
)

EFFICIENTNET_ART_MODEL_PATH = os.path.join(
    BASE_DIR, 
    'EfficientNet_Models', 
    'EfficientNet_fine_tune_art_model.h5'
)

# CNN Model Weights
CNN_MODEL_WEIGHTS_PATH = os.path.join(
    BASE_DIR, 
    'CNN_model_weight', 
    'model_weights.weights.h5'
)

# ============================================================================
# Model Configuration
# ============================================================================

# Image preprocessing sizes
CNN_IMAGE_SIZE = (256, 256)
EFFICIENTNET_IMAGE_SIZE = (300, 300)
EFFICIENTNET_ART_IMAGE_SIZE = (224, 224)

# Prediction threshold (0.5 = 50% confidence)
PREDICTION_THRESHOLD = 0.5

# Model names for UI
MODEL_NAMES = {
    'cnn': 'CNN',
    'efficientnet': 'EfficientNet',
    'efficientnet_art': 'EfficientNet Art'
}

# ============================================================================
# UI Configuration
# ============================================================================

# Supported image formats
SUPPORTED_IMAGE_FORMATS = ['png', 'jpg', 'jpeg']

# Style paths
STYLE_CSS_PATH = os.path.join(BASE_DIR, 'styles', 'style.css')
ROBOT_IMAGE_PATH = os.path.join(BASE_DIR, 'styles', 'robot.png')
DETECTIVE_MAG_SVG_PATH = os.path.join(BASE_DIR, 'styles', 'detectiveMag.svg')

# ============================================================================
# Performance Settings
# ============================================================================

# Enable model caching for faster loading
ENABLE_MODEL_CACHING = True

# Maximum upload file size (in MB)
MAX_UPLOAD_SIZE_MB = 10

# ============================================================================
# Feature Flags (for future enhancements)
# ============================================================================

# Enable batch processing
ENABLE_BATCH_PROCESSING = False

# Enable API mode
ENABLE_API_MODE = False

# Enable detailed analytics
ENABLE_ANALYTICS = False

# ============================================================================
# Logging Configuration
# ============================================================================

# Enable debug logging
DEBUG_MODE = False

# Log file path
LOG_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'trustlens.log')
