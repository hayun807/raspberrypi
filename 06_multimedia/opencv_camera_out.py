import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

#fourcc(four character code)
#DIVX (avi) , MP4V(mp4) , X264(h264) , 
fourcc = cv2.VideoWriter_fourcc(*'DIVX') 

out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))

# ret,frame = cap.read()

# cv2.imshow('frame',frame)
# cv2.waitKey(0)
# cv2.imwrite('output.jpg',frame)

while True:
    ret,frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame',frame)
    out.write(frame)
    
    #1000 -> 1s , 10 -> 0.01s
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()