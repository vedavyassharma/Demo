import os
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split

# Define dataset path
dataset_path = os.path.join("datasets", "NCC_postures")  # Generalized for cross-platform use
labels_csv = os.path.join("datasets", "labels.csv")  # Labels file

# Image size for CNN model input
IMG_SIZE = (224, 224)

# Load labels from CSV
try:
    labels_df = pd.read_csv(labels_csv)
except FileNotFoundError:
    print(f"Error: Labels file '{labels_csv}' not found. Ensure the file exists.")
    labels_df = None

# Function to load images and labels
def load_images_and_labels(labels_df, dataset_path):
    images = []
    labels = []

    if labels_df is None:
        return np.array(images), np.array(labels)

    for _, row in labels_df.iterrows():
        img_path = os.path.join(dataset_path, row['label'], row['filename'])
        
        if not os.path.exists(img_path):
            print(f"Warning: Image file '{img_path}' not found. Skipping.")
            continue

        try:
            img = load_img(img_path, target_size=IMG_SIZE)
            img_array = img_to_array(img) / 255.0  # Normalize
            images.append(img_array)
            labels.append(1 if row['label'] == 'Correct' else 0)  # Binary labels: 1 for correct, 0 for incorrect
        except Exception as e:
            print(f"Error processing image {img_path}: {e}")

    return np.array(images), np.array(labels)

# Load dataset
X, y = load_images_and_labels(labels_df, dataset_path)

# Debugging output
print(f"Total images loaded: {len(X)}")

# Split dataset for training & validation
if len(X) > 0:
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Dataset Loaded: Training Samples: {len(X_train)}, Validation Samples: {len(X_val)}")
else:
    print("No images were loaded. Please check the dataset paths and CSV labels.")

