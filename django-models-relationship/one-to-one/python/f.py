import cv2
import dlib
import pyttsx3
import numpy as np
from scipy.spatial import distance

# -------------------- INITIAL SETUP --------------------

# Text-to-Speech
engine = pyttsx3.init()

# Camera
cap = cv2.VideoCapture(0)

# Face Detector
face_detector = dlib.get_frontal_face_detector()

# Landmark Predictor (Make sure file is in same folder)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Thresholds
EYE_THRESHOLD = 0.25
FRAME_THRESHOLD = 20

# Counters & Flags
count = 0
alarm_on = False

# -------------------- FUNCTIONS --------------------

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)


def mouth_aspect_ratio(mouth):
    A = distance.euclidean(mouth[2], mouth[10])
    B = distance.euclidean(mouth[4], mouth[8])
    C = distance.euclidean(mouth[0], mouth[6])
    return (A + B) / (2.0 * C)


# -------------------- MAIN LOOP --------------------

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to access camera")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    # If no face detected
    if len(faces) == 0:
        cv2.putText(frame, "No Face Detected", (50, 100),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)

    for face in faces:
        landmarks = predictor(gray, face)

        left_eye = []
        right_eye = []
        mouth = []

        # Left Eye (42–47)
        for i in range(42, 48):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            left_eye.append((x, y))

        # Right Eye (36–41)
        for i in range(36, 42):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            right_eye.append((x, y))

        # Mouth (48–67)
        for i in range(48, 68):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            mouth.append((x, y))

        # Calculate EAR & MAR
        left_EAR = eye_aspect_ratio(left_eye)
        right_EAR = eye_aspect_ratio(right_eye)
        EAR = (left_EAR + right_EAR) / 2.0
        EAR = round(EAR, 2)

        MAR = mouth_aspect_ratio(mouth)

        # Drowsiness Logic
        if EAR < EYE_THRESHOLD:
            count += 1
        else:
            count = 0
            alarm_on = False

        # Alert Trigger
        if count > FRAME_THRESHOLD:
            cv2.putText(frame, "DROWSINESS DETECTED!", (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

            if not alarm_on:
                alarm_on = True
                engine.say("Wake up")
                engine.runAndWait()

        # Display Info
        cv2.putText(frame, "Drowsiness Detector", (10, 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        cv2.putText(frame, f"EAR: {EAR}", (300, 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        cv2.putText(frame, f"MAR: {round(MAR,2)}", (300, 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

    # Show Frame
    cv2.imshow("Drowsiness Detector", frame)

    # Exit on ESC
    if cv2.waitKey(1) == 27:
        break

# -------------------- CLEANUP --------------------

cap.release()
cv2.destroyAllWindows()