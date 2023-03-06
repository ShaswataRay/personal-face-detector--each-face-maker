import cv2
o = 1

img = cv2.imread("4friends.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascading = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = face_cascading.detectMultiScale(gray)
z = len(faces)
z = z + 1
print(len(faces))

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)

    i = o
    if i < z:
        l = str(o)
        roi_color = img[y: y+h, x: x+w]   
        b = cv2.imwrite(l + ".jpg", roi_color)

    o = o + 1
    
cv2.imshow("img", img)
cv2.waitKey(0)