#!python3.7
import cv2 

face_cascade_path = "../detect-folder/" + \
    "haarcascade_frontalface_default.xml"
eye_cascade_path = "../detect-folder/" + \
    "haarcascade_eye.xml"

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

image = cv2.imread("../image-folder/AbeHiroshi.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image_gray)

for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h),
    (255, 0, 0), 2)
    face = image[y:y+h, x:x+w]
    face_gray = image_gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex+ew, ey+eh),
        (0, 255, 0), 2)

cv2.imwrite("../image-folder/abe_detect_rectangle.png", image)