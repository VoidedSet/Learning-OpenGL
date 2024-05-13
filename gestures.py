import cv2
import mediapipe as mp

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Start capturing video from the webcam.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a later selfie-view display.
    image = cv2.flip(image, 1)
    # Convert the BGR image to RGB.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image_rgb.flags.writeable = False
    # Process the image to detect hands.
    results = hands.process(image_rgb)

    # Draw the hand landmarks.
    image_rgb.flags.writeable = True
    # Convert the RGB image back to BGR.
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extracting landmarks for the thumb and index finger
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Assuming translation gesture if thumb is to the right of index finger tip
            if thumb_tip.x > index_tip.x:
                direction = "Right"
            else:
                direction = "Left"

            # Printing translation gesture direction and constant strength
            print(f"Translation Gesture Detected: Direction - {direction}, Strength - 0.1f")

            with open("gesture.txt", "w") as file:
                file.write(f"{direction}")

    # Show the image with gesture recognition results.
    cv2.imshow('Hand Tracking and Gesture Recognition', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Release the video capture object and close all OpenCV windows.
cap.release()
cv2.destroyAllWindows()
