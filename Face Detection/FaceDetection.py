import cv2 as cv

# Load the cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv.imread('pic1.jpg',cv.IMREAD_UNCHANGED)
# Convert into grayscale
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(imgGray, 1.3, 4)
# Draw rectangle around the faces
i=0;
font=cv.FONT_HERSHEY_DUPLEX
for (x, y, w, h) in faces:
    person='person{}'.format(i+1)
    #set the coordinate of x and y , and the color in RBG , thick of rectangular

    size=w/302
    (text_width, text_height)=cv.getTextSize(person,font,size,1)[0]

    cv.rectangle(img, (x, y), (w+x, h+y), (0,128,0), 2)
    cv.rectangle(img, (x, y-2), (w + x,  y-text_height-10), (0, 128, 0), -1)
    cv.putText(img,person,(x,y-10),font,size,(255,255,255),1,cv.LINE_AA)

    i=i+1
# Display the output
cv.imshow('Faces', img)

print("Number Of persons in the Pictures are",i)

cv.waitKey(0)