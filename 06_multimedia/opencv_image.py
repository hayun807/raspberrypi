import cv2

img = cv2.imread('hoyeon.jpg')
img2 = cv2.resize(img,(200,300))

edge1 = cv2.Canny(img,50,100)
edge2 = cv2.Canny(img,100,150)
edge3 = cv2.Canny(img,150,200)

cv2.imshow('hoyeon1',edge1)
cv2.imshow('hoyeon2',edge2)
cv2.imshow('hoyeon3',edge3)

cv2.waitKey(0)

cv2.destroyAllWindows()