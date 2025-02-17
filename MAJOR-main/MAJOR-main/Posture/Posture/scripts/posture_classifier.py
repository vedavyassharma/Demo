import os
import pandas as pd
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint

# Paths
dataset_path = r'C:\Users\divye\Posture\Posture\datasets'  # Absolute path to datasets folder
labels_csv = os.path.join(dataset_path, 'labels.csv')  # Path to labels.csv file
model_path = 'models/posture_model_resnet50.h5'  # Path to save the trained model

# Image dimensions
IMG_SIZE = (224, 224)  # Resize images to 224x224
BATCH_SIZE = 32

# Verify if labels.csv exists
if not os.path.exists(labels_csv):
    raise FileNotFoundError(f"Error: The file '{labels_csv}' was not found. Please verify the dataset structure.")

# Load labels
labels_df = pd.read_csv(labels_csv)

# Load images and preprocess
def load_images_and_labels(labels_df, dataset_path):
    images = []
    labels = []
    label_map = {label: idx for idx, label in enumerate(labels_df['label'].unique())}
    for _, row in labels_df.iterrows():
        img_path = os.path.join(dataset_path, row['label'], row['filename'])
        if not os.path.exists(img_path):
            print(f"Error: Image file '{img_path}' not found. Skipping.")
            continue
        img = load_img(img_path, target_size=IMG_SIZE)  # Load image with the specified target size
        img_array = img_to_array(img) / 255.0  # Normalize the image
        images.append(img_array)
        labels.append(label_map[row['label']])  # Convert label to index
    return np.array(images), np.array(labels)

# Load images and labels
X, y = load_images_and_labels(labels_df, dataset_path)

# Split dataset into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert labels to categorical format for ResNet
y_train = to_categorical(y_train, num_classes=len(labels_df['label'].unique()))
y_val = to_categorical(y_val, num_classes=len(labels_df['label'].unique()))

print(f"Training Samples: {len(X_train)}, Validation Samples: {len(X_val)}")

# Load ResNet50 base model
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # Freeze the base model

# Add custom layers on top of ResNet50
x = Flatten()(base_model.output)
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)
output = Dense(len(labels_df['label'].unique()), activation='softmax')(x)  # Output layer for multi-class classification
model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Add a checkpoint to save the best model
checkpoint = ModelCheckpoint(model_path, monitor='val_accuracy', save_best_only=True, verbose=1)

# Train the model
print("Training the ResNet50 model...")
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=10,
    batch_size=BATCH_SIZE,
    callbacks=[checkpoint]
)

print("Model training complete. Model saved at:", model_path)
