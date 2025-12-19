import os
import shutil
import random

SOURCE_DIR = "D:\Eye_Detection\EyeVision\disease_prediction\ml\dataset"
TARGET_DIR = "D:\Eye_Detection\EyeVision\disease_prediction\ml\dataset1"
SPLIT_RATIO = 0.8

os.makedirs(TARGET_DIR, exist_ok=True)

for category in os.listdir(SOURCE_DIR):
    src_path = os.path.join(SOURCE_DIR, category)
    if not os.path.isdir(src_path):
        continue

    images = [
        f for f in os.listdir(src_path)
        if os.path.isfile(os.path.join(src_path, f))
    ]

    random.shuffle(images)
    split_index = int(len(images) * SPLIT_RATIO)

    train_images = images[:split_index]
    val_images = images[split_index:]

    train_dir = os.path.join(TARGET_DIR, "train", category)
    val_dir = os.path.join(TARGET_DIR, "val", category)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    for img in train_images:
        shutil.copy(
            os.path.join(src_path, img),
            os.path.join(train_dir, img)
        )

    for img in val_images:
        shutil.copy(
            os.path.join(src_path, img),
            os.path.join(val_dir, img)
        )

print("✅ Dataset split completed successfully")

