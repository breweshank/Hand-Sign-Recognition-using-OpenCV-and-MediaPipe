import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils


def recognize_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    
    if (thumb_tip.y < index_finger_tip.y < middle_finger_tip.y and
        ring_finger_tip.y < pinky_tip.y):
        return "Thumbs Up"
    elif (thumb_tip.x < index_finger_tip.x and
          thumb_tip.y > index_finger_tip.y):
        return "Peace"
    
    elif (all(finger_tip.y < wrist.y for finger_tip in 
              [thumb_tip, index_finger_tip, middle_finger_tip, ring_finger_tip, pinky_tip])):
        return "Bye-Bye"
    elif (pinky_tip.y < wrist.y and
          all(finger_tip.y > wrist.y for finger_tip in 
              [thumb_tip, index_finger_tip, middle_finger_tip, ring_finger_tip])):
        return "Washroom"
    else:
        return "Not Like"

# Initialize webcam
cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Draw landmarks and recognize gestures
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            cv2.putText(frame, gesture, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow("Hand Sign Recognition", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
