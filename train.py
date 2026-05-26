from ultralytics import YOLO

# load model
model = YOLO("yolov8n.pt")

# train model
model.train(
    data="D:/Leaf_Annotation_Project/data.yaml",
    epochs=10
)