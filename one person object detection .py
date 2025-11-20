import torch
import cv2

# Load YOLOv5 small model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Only detect 'person' class
person_class_id = 0  # In COCO dataset, 'person' has class ID 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on frame
    results = model(frame)

    # Filter results to keep only humans
    persons = results.xyxy[0][results.xyxy[0][:, 5] == person_class_id]

    # Draw bounding boxes
    for *box, conf, cls in persons:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Person {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("YOLO Human Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
