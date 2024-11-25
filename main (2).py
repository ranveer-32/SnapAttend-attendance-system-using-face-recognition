import os
import cv2
import firebase_admin
import numpy as np
import pickle
import face_recognition
from datetime import datetime
from firebase_admin import db, credentials, storage
from tkinter import Tk, filedialog

# Initialize Firebase
cred = credentials.Certificate('serviceAccountKey.json')  # Update with the path to your credentials
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendencerealtime-8565a-default-rtdb.firebaseio.com/',  # Update with your Firebase URL
    'storageBucket': 'faceattendencerealtime-8565a.appspot.com'  # Update with your Firebase Storage Bucket name
})
bucket = storage.bucket()

# Load the encoding file
print("Loading Encode File ...")
with open('EncodeFile.p', 'rb') as file:
    encodeListKnownWithIds = pickle.load(file)
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")


def upload_image():
    """Prompt the user to upload an image using a file dialog."""
    try:
        # Initialize Tkinter and suppress the main window
        root = Tk()
        root.withdraw()  # Hide the root window
        root.attributes('-topmost', True)  # Bring the file dialog to the front

        # Open the file dialog to select an image
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )

        # Return the selected file path or None if no file was selected
        if file_path:
            print(f"File selected: {file_path}")
            return file_path
        else:
            print("No file selected.")
            return None

    except Exception as e:
        print(f"Error during file upload: {e}")
        return None


def get_class_and_subject():
    """Prompt the teacher to select a class and subject."""
    print("Available Classes:")
    print("1. ThirdYear")
    class_choice = input("Select a class by number: ")

    if class_choice == "1":
        selected_class = "ThirdYear"
        print("Available Subjects:")
        print("1. DAA")
        print("2. EDA")
        print("3. DBMS")
        subject_choice = input("Select a subject by number: ")

        if subject_choice == "1":
            selected_subject = "DAA"
        elif subject_choice == "2":
            selected_subject = "EDA"
        elif subject_choice == "3":
            selected_subject = "DBMS"
        else:
            print("Invalid subject choice.")
            return None, None
    else:
        print("Invalid class choice.")
        return None, None

    return selected_class, selected_subject


def process_group_photo(image_path, selected_class, selected_subject):
    """Process a group photo to recognize multiple faces and mark attendance."""
    print(f"Processing group photo: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to read the image file.")
        return

    # Resize and convert to RGB for face_recognition
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Detect all face locations and encodings in the image
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    if not faceCurFrame:
        print("No faces detected in the image.")
        return

    print(f"Detected {len(faceCurFrame)} faces. Processing attendance...")

    # Process each detected face
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            id = studentIds[matchIndex]

            # Fetch student info from Firebase
            studentInfo = db.reference(f'Students/Classes/{selected_class}/{selected_subject}/{id}').get()
            if studentInfo:
                print(f"Marking attendance for {studentInfo.get('name')} in {selected_subject}.")

                # Update attendance data
                ref = db.reference(f'Students/Classes/{selected_class}/{selected_subject}/{id}')
                if 'total_attendance' in studentInfo:
                    studentInfo['total_attendance'] = int(studentInfo['total_attendance']) + 1
                    ref.child('total_attendance').set(studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                print(f"Student {id} not found in database.")
        else:
            print("Unrecognized face detected.")

    print("Attendance marking completed for all detected faces.")


if __name__ == "__main__":
    print("Starting Attendance System...")

    # Get class and subject selection
    selected_class, selected_subject = get_class_and_subject()
    if selected_class and selected_subject:
        print(f"Selected Class: {selected_class}, Subject: {selected_subject}")
        print("Please upload a group photo.")

        # Prompt the user to upload an image
        image_path = upload_image()
        if image_path:
            print("Processing the uploaded image...")
            process_group_photo(image_path, selected_class, selected_subject)
        else:
            print("No image uploaded. Exiting.")
    else:
        print("Class or subject not selected. Exiting.")
