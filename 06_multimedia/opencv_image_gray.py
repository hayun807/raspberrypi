import cv2

img = cv2.imread('hoyeon.jpg')
img2 = cv2.resize(img, (600,400))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('hoyeon', img2)
cv2.imshow('hoyeon', gray)


while True:
    if cv2.waitKey(0) == 13:
        break

# while True:
#     if cv2.waitKey() == ord('q') :
#         break

cv2.imwrite('hoyeon', gray)

cv2.destroyAllWindows()