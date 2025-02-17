import cv2
import mediapipe as mp
import pyttsx3
import time
from scripts.calculate_angles import analyze_pose  # Import the function for pose classification

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

# Function to give voice feedback
def give_feedback(feedback_text):
    """Provides audio feedback for posture correction."""
    print(feedback_text)
    engine.say(feedback_text)
    engine.runAndWait()

# Initialize webcam
cap = cv2.VideoCapture(0)

# Time tracking for feedback throttling
last_feedback_time = time.time()
last_posture = None  # Track last detected posture to avoid unnecessary feedback

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Check if landmarks are detected and classify posture
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        posture = analyze_pose(landmarks)  # Get posture classification

        # Provide feedback only when posture changes
        current_time = time.time()
        if posture != last_posture and (current_time - last_feedback_time > 10):
            feedback_text = "Posture not recognized. Adjust yourself."
            if posture == "Saavdhan":
                feedback_text = "You are in Saavdhan posture. Stand firm!"
            elif posture == "Vishram":
                feedback_text = "You are in Vishram posture. Relax your arms!"
            
            give_feedback(feedback_text)
            last_feedback_time = current_time  # Update last feedback time
            last_posture = posture  # Update last detected posture

        # Draw pose landmarks on the frame
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Display detected posture on the frame
        cv2.putText(image, f"Posture: {posture}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Pose Detection with Feedback", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
