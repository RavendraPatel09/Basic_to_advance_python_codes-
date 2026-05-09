import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

def get_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark
    
    thumb_is_open = landmarks[4].x > landmarks[3].x
    index_is_open = landmarks[8].y < landmarks[6].y
    middle_is_open = landmarks[12].y < landmarks[10].y
    ring_is_open = landmarks[16].y < landmarks[14].y
    pinky_is_open = landmarks[20].y < landmarks[18].y

    if index_is_open and middle_is_open and not ring_is_open and not pinky_is_open:
        return "PEACE"
    elif index_is_open and not middle_is_open and not ring_is_open and not pinky_is_open:
        return "ONE"
    elif all([index_is_open, middle_is_open, ring_is_open, pinky_is_open]) and not thumb_is_open:
        return "HI"
    elif not any([index_is_open, middle_is_open, ring_is_open, pinky_is_open]) and not thumb_is_open:
        return "FIST"
    elif thumb_is_open and not any([index_is_open, middle_is_open, ring_is_open, pinky_is_open]):
        return "THUMBS UP"
    
    return "..."

while cap.isOpened():
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            gesture_text = get_gesture(hand_lms)
            
            cv2.putText(
                img, 
                gesture_text, 
                (50, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                2, 
                (0, 255, 0), 
                3, 
                cv2.LINE_AA
            )

    cv2.imshow("Sign Language Translator", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#to run this code, make sure you have OpenCV, MediaPipe, and NumPy installed in your Python environment. You can install them using pip:
#pip install opencv-python mediapipe numpy
