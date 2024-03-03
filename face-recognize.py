import numpy as np
import cv2
import pickle
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="s@ifull@# @nik",
    database="hospital"
)
def searchForIndividualDataset(name):
    mycursor.execute("SELECT * FROM desease")
    myresult = mycursor.fetchall()
    print("ID  ", "Name  ", "Fever")
    for row in myresult:
        if row[1] == name:
            print(row)

mycursor = mydb.cursor()

face_cascade = cv2.CascadeClassifier('cascades\data\haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trianner.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}


# Dictionary to store counts for each detected name
name_counts = {name: 0 for name in labels.values()}


cap = cv2.VideoCapture(0)
count = 0
while True:
    count += 1
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=3.0, minNeighbors=5)
   
    for (x,y,w,h) in faces:
        # Identify Faces with the co ordinates /start/
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]                   #(ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        # Identify Faces with the co ordinates /end/

        id_,conf = recognizer.predict(roi_gray)
        if conf >= 50 and conf <= 90:
            #print(id_)
            print(labels[id_])
            #print(conf)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            name_counts[name] += 1
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

        # Save Faces /start/
        #img_item = "8.png"
        #cv2.imwrite(img_item, roi_color)
        # Save Faces /start/

        # Making the rectangle around the face /start/
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)           #draw the rectangle
        # Making the rectangle around the face /end/

    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        print("Count: ", count)
        break


# Finding the name with the maximum count
max_name = max(name_counts, key=name_counts.get)
print("Detected as:", max_name)

searchForIndividualDataset(max_name)

cap.release()
cv2.destroyAllWindows()
