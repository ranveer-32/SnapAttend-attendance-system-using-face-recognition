import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-8565a-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendencerealtime-8565a.appspot.com"
})

# Firebase storage bucket initialization
bucket = storage.bucket()

# Subject folders configuration
subjects = {
    "DAA": "images/DAA",
    "DBMS": "images/DBMS",
    "EDA": "images/EDA"
}

# To store encodings for all subjects
subject_encodings = {}

# Processing each subject folder
for subject, folderPath in subjects.items():
    print(f"Processing subject: {subject}")

    # Check if folder exists
    if not os.path.exists(folderPath):
        print(f"Folder for {subject} not found. Skipping.")
        continue

    # Reading images and IDs
    pathList = os.listdir(folderPath)
    print(f"Found {len(pathList)} files in {folderPath}")
    imgList = []
    studentIds = []

    for path in pathList:
        file_path = os.path.join(folderPath, path)

        # Ensure the file is an image
        if not path.lower().endswith(('.jpg', '.jpeg', '.png')):
            print(f"Skipping non-image file: {file_path}")
            continue

        img = cv2.imread(file_path)
        if img is None:
            print(f"Failed to read image: {file_path}")
            continue

        imgList.append(img)
        studentId = os.path.splitext(path)[0]
        studentIds.append(studentId)

        # Upload to Firebase Storage
        blob = bucket.blob(f"images/{subject}/{path}")
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to Firebase Storage")

    if not imgList:
        print(f"No valid images found in {folderPath}. Skipping.")
        continue

    # Encode images
    print(f"Encoding images for {subject}...")
    encodeList = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)

        if encode:  # Ensure at least one face is found
            encodeList.append(encode[0])
        else:
            print("No face found in one of the images. Skipping that image.")

    # Store encodings for the subject
    subject_encodings[subject] = [encodeList, studentIds]
    print(f"Encoding for {subject} completed.")

# Save subject-wise encodings
if subject_encodings:
    with open("SubjectEncodeFile.p", 'wb') as file:
        pickle.dump(subject_encodings, file)
    print("Subject-wise Encode File Saved")
else:
    print("No encodings were created. Please check your folders and images.")
