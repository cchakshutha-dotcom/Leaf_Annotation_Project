from ultralytics import YOLO
import cv2

# 🔹 Load your trained model
model = YOLO("D:/Leaf_Annotation_Project/runs/detect/train3/weights/best.pt")

print("🚀 Starting webcam detection...")

# 🔹 Start webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# if camera not opening
if not cap.isOpened():
    print("❌ Webcam not detected. Trying another camera...")
    cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    # 🔹 Run prediction on frame
    results = model(frame)

    # 🔹 Plot results (boxes + labels)
    annotated_frame = results[0].plot()

    # 🔹 Show output
    cv2.imshow("🌿 Leaf Disease Detection", annotated_frame)

    # 🔹 Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 🔹 Release everything
cap.release()
cv2.destroyAllWindows()

print("✅ Webcam detection stopped")