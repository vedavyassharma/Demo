import numpy as np
import cv2
import mediapipe as mp

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

def calculate_angle(a, b, c):
    """
    Calculate the angle between three points (a, b, c).
    """
    a = np.array(a)  # First point
    b = np.array(b)  # Middle point (joint)
    c = np.array(c)  # Third point

    # Calculate angle in degrees
    radian_angle = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radian_angle))

    # Ensure the angle is within 0-180 degrees
    if angle > 180.0:
        angle = 360 - angle
    return angle

def get_pose_angles(landmarks):
    """
    Extracts key body angles required to classify NCC postures.
    """
    # Key points for both sides of the body
    left_shoulder = [landmarks[11].x, landmarks[11].y]
    left_elbow = [landmarks[13].x, landmarks[13].y]
    left_wrist = [landmarks[15].x, landmarks[15].y]

    right_shoulder = [landmarks[12].x, landmarks[12].y]
    right_elbow = [landmarks[14].x, landmarks[14].y]
    right_wrist = [landmarks[16].x, landmarks[16].y]

    left_hip = [landmarks[23].x, landmarks[23].y]
    left_knee = [landmarks[25].x, landmarks[25].y]
    left_ankle = [landmarks[27].x, landmarks[27].y]

    right_hip = [landmarks[24].x, landmarks[24].y]
    right_knee = [landmarks[26].x, landmarks[26].y]
    right_ankle = [landmarks[28].x, landmarks[28].y]

    # Calculate angles
    left_arm_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
    right_arm_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

    left_leg_angle = calculate_angle(left_hip, left_knee, left_ankle)
    right_leg_angle = calculate_angle(right_hip, right_knee, right_ankle)

    return left_arm_angle, right_arm_angle, left_leg_angle, right_leg_angle

def analyze_pose(landmarks):
    """
    Analyzes the posture based on landmark angles and classifies as 'Saavdhan' or 'Vishram'.
    """
    left_arm, right_arm, left_leg, right_leg = get_pose_angles(landmarks)

    # NCC Saavdhan posture (Arms straight, legs together)
    if 160 <= left_arm <= 180 and 160 <= right_arm <= 180 and 170 <= left_leg <= 180 and 170 <= right_leg <= 180:
        return "Saavdhan"

    # NCC Vishram posture (Hands behind back, relaxed leg stance)
    elif 70 <= left_arm <= 120 and 70 <= right_arm <= 120 and 150 <= left_leg <= 180 and 150 <= right_leg <= 180:
        return "Vishram"

    return "Unknown"

if __name__ == "__main__":
    # Start webcam to test the posture detection
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            posture = analyze_pose(landmarks)

            # Display detected posture
            cv2.putText(frame, f"Posture: {posture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Posture Detection Test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
