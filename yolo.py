import torch
import cv2


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on frame
    results = model(frame)

    # Convert results to image
    annotated_frame = results.render()[0]

    # Show output
    cv2.imshow("YOLO Webcam", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
