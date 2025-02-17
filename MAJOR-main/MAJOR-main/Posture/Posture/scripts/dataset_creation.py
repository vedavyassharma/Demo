import cv2
import os
import tkinter as tk
from tkinter import simpledialog

# Define the dataset directory
dataset_dir = "datasets/NCC_postures"
os.makedirs(dataset_dir, exist_ok=True)

# Define the posture types
postures = ['Saavdhan', 'Vishram', 'Dahine Salute', 'Bahiye Salute', 'Saamne Salute']
posture_dict = {i: posture for i, posture in enumerate(postures)}

# Initialize webcam
cap = cv2.VideoCapture(0)

# Function to get posture selection via a GUI dialog
def get_posture_selection():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    posture_type = simpledialog.askinteger("Posture Selection", 
                                           "Enter posture number (0: Saavdhan, 1: Vishram, 2: Dahine Salute, 3: Bahiye Salute, 4: Saamne Salute)")
    root.destroy()
    
    if posture_type is not None and 0 <= posture_type < len(postures):
        return posture_type
    return None

# Function to capture and save images with labels
def capture_images():
    print("Press 'q' to quit the capture process.")

    # Get the user's posture selection
    posture_type = get_posture_selection()
    if posture_type is None:
        print("Invalid selection. Exiting.")
        return

    print(f"Capturing images for: {posture_dict[posture_type]}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error accessing webcam.")
            break

        # Display the frame
        cv2.imshow('Capture NCC Posture', frame)

        # Auto-save images in sequence
        count = len([f for f in os.listdir(dataset_dir) if f.startswith(posture_dict[posture_type])]) + 1
        image_name = f"{dataset_dir}/{posture_dict[posture_type]}_{count}.jpg"
        cv2.imwrite(image_name, frame)
        print(f"Image saved as {image_name}")

        # Press 'q' to exit
        if cv2.waitKey(500) & 0xFF == ord('q'):  # Captures every 0.5 sec
            break

    cap.release()
    cv2.destroyAllWindows()

# Start capturing images
if __name__ == "__main__":
    capture_images()
