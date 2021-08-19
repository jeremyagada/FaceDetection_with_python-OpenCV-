import cv2
trained_face_data = cv2.CascadeClassifier('C:\\Users\\jeremy\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml')
#img = cv2.imread(r"C:\Users\jeremy\Desktop\ml course\faceDetection\WIN_20210811_18_37_39_Pro.jpg")
#


webcam = cv2.VideoCapture(0)
#key = cv2.waitKey(1)
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0,  225), 2)
    cv2.imshow('img', frame)
    
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()
"""""



 

cv2.imshow("img", img)
"""""
print("Code Completed")
