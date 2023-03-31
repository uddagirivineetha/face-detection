import cv2
cascade_classifier=cv2.CascadeClassifier("C:\\Users\\ASUS\\Downloads\\haarcascade_frontalface_default.xml")
#cascade_classifier=cv2.CascadeClassifier("C:\\Users\\ASUS\\Downloads\\haarcascade_smile.xml")
#cascade_classifier=cv2.CascadeClassifier("C:\\Users\\ASUS\\Downloads\\haarcascade_eye.xml")
cap=cv2.VideoCapture(0)

while True:
    #Capture frame-by-frame
    ret,frame=cap.read()
    #Our operation on the frame come here 
    gray=cv2.cvtColor(frame,0)
    detections=cascade_classifier.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    if(len(detections) > 0):
        (x,y,w,h)= detections[0]
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    #Disply the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
# when everything done ,release the capture
cap.release()
cv2.destroyALLWindows()
    