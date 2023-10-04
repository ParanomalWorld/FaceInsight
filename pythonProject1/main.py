import os
import pickle

import cv2
import face_recognition
import numpy as np
import cvzone

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-insight-default-rtdb.firebaseio.com/",
    'storageBucket': "face-insight.appspot.com"
})

bucket = storage.bucket()

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

imageBacaground = cv2.imread('Resources/22backImage.jpeg')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
# print(len(imgModeList))


# Load the encoding file
print("Loading Encode File........")

file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print("Encode File Loaded..........")

modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, [0, 0], None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imageBacaground[162:162 + 480, 55:55 + 640] = img
    # imageBacaground[44:44 + 630, 808:808 + 414] = imgModeList[0]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #    print("matches" , matches)
        #    print("faceDis" , faceDis)

        matchIndex = np.argmin(faceDis)
        # print("Match Index --------->>" , matchIndex)

        if matches[matchIndex]:
            # print("Known Face Detected")
            # print(studentIds(matchIndex))
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imageBacaground = cvzone.cornerRect(imageBacaground, bbox, rt=0)
            id = studentIds[matchIndex]
            print(id)

            # Resize the mode image to match the target region (630, 414)
            resized_mode_image = cv2.resize(imgModeList[modeType], (414, 630))

            imageBacaground[44:44 + 630, 808:808 + 414] = resized_mode_image
            id = studentIds[matchIndex]

            if counter == 0:
                counter = 1
                modeType = 1

    if counter != 0:
        if counter == 1:
            # Get the data
            studentInfo = db.reference(f'Students/{id}').get()
            print(studentInfo)
            # Get the Image from storage

            blob = bucket.get_blob(f'Images/{id}.jpeg')
            array = np.frombuffer(blob.download_as_string(), np.uint8)
            imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

        cv2.putText(imageBacaground, str(studentInfo['total_attedndace']), (861, 125),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

        cv2.putText(imageBacaground, str(studentInfo['major']), (1006, 550),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        cv2.putText(imageBacaground, str(id), (1006, 493),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        cv2.putText(imageBacaground, str(studentInfo['standing']), (910, 625),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

        cv2.putText(imageBacaground, str(studentInfo['year']), (1025, 625),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

        cv2.putText(imageBacaground, str(studentInfo['starting_year']), (1125, 625),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

        (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
        offset = (414 - w) // 2
        text_x = 808 + offset  # Calculate the x-coordinate for centering the text
        cv2.putText(imageBacaground, str(studentInfo['name']), (text_x, 445),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

        # imageBacaground[175:175 + 216, 909:909 + 216] = imgStudent
        # Assuming imageBacaground is your background image and imgStudent is the student image

        # Define the target region's coordinates
        top_left_x = 909
        top_left_y = 175
        bottom_right_x = top_left_x + 216
        bottom_right_y = top_left_y + 216

        # Resize imgStudent to match the target region's size (216x216)
        imgStudent = cv2.resize(imgStudent, (216, 216))

        # Assign imgStudent to the specified region in imageBacaground
        imageBacaground[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = imgStudent

        counter += 1

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imageBacaground)
    cv2.waitKey(1)
