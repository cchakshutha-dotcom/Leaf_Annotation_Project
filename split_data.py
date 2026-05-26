import os
import random
import shutil

base_path = "D:/Leaf_Annotation_Project"

image_folders = ["rust", "powdery", "virus", "healthy"]

# create folders
os.makedirs(base_path + "/images/train", exist_ok=True)
os.makedirs(base_path + "/images/val", exist_ok=True)
os.makedirs(base_path + "/labels/train", exist_ok=True)
os.makedirs(base_path + "/labels/val", exist_ok=True)

all_images = []

# collect images
for folder in image_folders:
    folder_path = os.path.join(base_path, "images", folder)
    for file in os.listdir(folder_path):
        if file.endswith(".jpg"):
            all_images.append((folder, file))

# shuffle
random.shuffle(all_images)

# split
split_index = int(0.8 * len(all_images))
train_data = all_images[:split_index]
val_data = all_images[split_index:]

def move_files(data, img_dest, lbl_dest):
    for folder, file in data:
        img_src = os.path.join(base_path, "images", folder, file)
        lbl_src = os.path.join(base_path, "annotations", file.replace(".jpg", ".txt"))

        shutil.copy(img_src, os.path.join(img_dest, file))

        if os.path.exists(lbl_src):
            shutil.copy(lbl_src, os.path.join(lbl_dest, file.replace(".jpg", ".txt")))

# move files
move_files(train_data, base_path + "/images/train", base_path + "/labels/train")
move_files(val_data, base_path + "/images/val", base_path + "/labels/val")

print("✅ DONE! Data split automatically.")