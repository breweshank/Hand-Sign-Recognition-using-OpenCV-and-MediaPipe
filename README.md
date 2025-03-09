# Hand Gesture Recognition with OpenCV & MediaPipe

## Description
This project utilizes OpenCV and MediaPipe to recognize hand gestures in real-time using a webcam. The program detects hand landmarks and classifies gestures into predefined categories based on the positioning of fingers.

## Features
- Real-time hand tracking and gesture recognition
- Gesture classification into categories like "Thumbs Up," "Peace," "Bye-Bye," and more
- Simple and efficient implementation using Python

## Installation
Ensure you have Python installed, then install the necessary dependencies:
```sh
pip install opencv-python mediapipe
```

## How to Run
1. Connect a webcam to your system.
2. Run the Python script:
   ```sh
   Hand Sign.py
   ```
3. The application will display recognized gestures on the screen.
4. Press 'q' to exit.

## Gesture Recognition Details
- **Thumbs Up**: Thumb is higher than the other fingers.
- **Peace Sign**: Index and middle fingers extended, other fingers folded.
- **Bye-Bye**: All fingers above the wrist.
- **Washroom Sign**: Pinky above the wrist, other fingers below.
- **Default**: No recognized gesture.

## Code Breakdown
- **Initialize MediaPipe Hands**: Loads the hand detection model.
- **Define Gesture Logic**: Uses landmark positions to classify gestures.
- **Video Processing**: Captures video, detects hands, and overlays gesture labels in real-time.

## Troubleshooting
- Change `cv2.VideoCapture(1)` to `cv2.VideoCapture(0)` if the webcam doesn't open.
- Ensure good lighting for better hand tracking.
- Adjust `min_detection_confidence` for improved accuracy.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Developed by Eshank Ryshabh

