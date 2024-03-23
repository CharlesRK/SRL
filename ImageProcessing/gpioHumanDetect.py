import RPi.GPIO as GPIO
from ultralytics import YOLO
import cv2
import math 

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(18, GPIO.OUT)  # Set pin 18 to be an output pin

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# model
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


frame_counter = 0  # Initialize a frame counter

while True:
    success, img = cap.read()
    if not success:
        break
    if frame_counter % 10 == 0:  # Process only every 10th frame
        results = model(img, stream=True)
        person_detected = any(box.cls[0] == 0 for r in results for box in r.boxes)  # Check if any person is detected
        if person_detected:
            GPIO.output(18, GPIO.HIGH)  # Set GPIO pin 18 to HIGH
        else:
            GPIO.output(18, GPIO.LOW)  # Set GPIO pin 18 to LOW if no person is detected

    # Existing code to display the image...

    frame_counter += 1  # Increment the frame counter after processing

cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()  # Clean up GPIO




