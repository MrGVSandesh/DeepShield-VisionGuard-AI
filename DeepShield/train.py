import os
import kagglehub
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Dense,
    Dropout,
    GlobalAveragePooling2D
)
from tensorflow.keras.optimizers import Adam

# ==========================================
# DOWNLOAD CIFAKE DATASET
# ==========================================

dataset_path = kagglehub.dataset_download(
    "birdy654/cifake-real-and-ai-generated-synthetic-images"
)

print("Dataset downloaded at:")
print(dataset_path)

# ==========================================
# DATASET PATHS
# ==========================================

TRAIN_DIR = os.path.join(dataset_path, "train")
TEST_DIR = os.path.join(dataset_path, "test")

# ==========================================
# SETTINGS
# ==========================================

IMG_SIZE = 128
BATCH_SIZE = 32
EPOCHS = 2

# ==========================================
# IMAGE GENERATORS
# ==========================================

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(
    rescale=1./255
)

# ==========================================
# LOAD DATA
# ==========================================

train_data = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

test_data = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

# ==========================================
# LOAD XCEPTION MODEL
# ==========================================

base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)

# Freeze pretrained layers
base_model.trainable = False

# ==========================================
# BUILD MODEL
# ==========================================

model = Sequential([

    base_model,

    GlobalAveragePooling2D(),

    Dense(256, activation='relu'),

    Dropout(0.5),

    Dense(1, activation='sigmoid')

])

# ==========================================
# COMPILE MODEL
# ==========================================

model.compile(
    optimizer=Adam(0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ==========================================
# MODEL SUMMARY
# ==========================================

model.summary()

# ==========================================
# TRAIN MODEL
# ==========================================

history = model.fit(
    train_data,
    validation_data=test_data,
    epochs=EPOCHS
)

# ==========================================
# SAVE MODEL
# ==========================================

os.makedirs("models", exist_ok=True)

model.save("models/cifake_detector.h5")

print("\nMODEL SAVED SUCCESSFULLY")

# ==========================================
# PLOT ACCURACY GRAPH
# ==========================================

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title("Model Accuracy")

plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend(["Train", "Validation"])

plt.show()