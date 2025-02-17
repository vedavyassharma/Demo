import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import pyttsx3
from scripts.calculate_angles import analyze_pose  # Importing posture analysis function

mp_pose = mp.solutions.pose

class NCCPostureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NCC Posture Detection and Correction")
        self.root.geometry("800x600")

        # Label to display webcam feed
        self.video_label = Label(self.root)
        self.video_label.pack()

        # Label for posture feedback
        self.feedback_label = Label(self.root, text="Posture Status: Initializing...", font=("Arial", 14), fg="blue")
        self.feedback_label.pack()

        # Initialize text-to-speech
        self.engine = pyttsx3.init()

        # Initialize webcam
        self.cap = cv2.VideoCapture(0)

        # Initialize MediaPipe Pose
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # Start webcam feed update
        self.update_video_feed()

    def update_video_feed(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert frame to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.pose.process(frame_rgb)

            posture = "Unknown"
            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                posture = analyze_pose(landmarks)  # Get posture classification

                # Draw landmarks on the frame
                mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Update feedback on the GUI
            self.feedback_label.config(text=f"Posture Status: {posture}")

            # Provide voice feedback only when posture changes
            if hasattr(self, "last_posture") and self.last_posture != posture:
                self.give_feedback(posture)

            self.last_posture = posture  # Store last detected posture

            # Convert processed image for Tkinter
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_video_feed)

    def give_feedback(self, posture):
        """Provide voice feedback based on detected posture."""
        feedback = "Posture not recognized. Please adjust."
        if posture == "Saavdhan":
            feedback = "You are in Saavdhan posture. Stand firm!"
        elif posture == "Vishram":
            feedback = "You are in Vishram posture. Relax your arms!"

        self.engine.say(feedback)
        self.engine.runAndWait()

    def start(self):
        self.root.mainloop()

    def __del__(self):
        """Release resources on closing the application."""
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = NCCPostureApp(root)
    app.start()
