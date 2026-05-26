import os
import shutil
import random

BASE = "D:/Leaf_Annotation_Project"

# source folders
src_folders = [
    BASE + "/images/healthy",
    BASE + "/images/powdery",
    BASE + "/images/rust",
    BASE + "/images/virus"
]

# destination
train_img = BASE + "/images/train"
val_img = BASE + "/images/val"

train_lbl = BASE + "/labels/train"
val_lbl = BASE + "/labels/val"

os.makedirs(train_img, exist_ok=True)
os.makedirs(val_img, exist_ok=True)
os.makedirs(train_lbl, exist_ok=True)
os.makedirs(val_lbl, exist_ok=True)

all_files = []

# 🔥 TAKE ALL FILES (no filter issue)
for folder in src_folders:
    if os.path.exists(folder):
        for f in os.listdir(folder):
            all_files.append((folder, f))

# shuffle
random.shuffle(all_files)

# split
split = int(0.8 * len(all_files))
train = all_files[:split]
val = all_files[split:]

def copy_data(data, img_dest, lbl_dest):
    for folder, file in data:
        src_img = os.path.join(folder, file)
        dst_img = os.path.join(img_dest, file)

        # copy image (NO CONDITION)
        shutil.copy(src_img, dst_img)

        # try label
        name = os.path.splitext(file)[0]
        lbl_src = os.path.join(BASE, "labels", name + ".txt")
        lbl_dst = os.path.join(lbl_dest, name + ".txt")

        if os.path.exists(lbl_src):
            shutil.copy(lbl_src, lbl_dst)

copy_data(train, train_img, train_lbl)
copy_data(val, val_img, val_lbl)

print("🔥 SUCCESS: Images copied correctly!")