import cv2
import glob, os
import time

os.chdir("Imgs")
while True :
    for file in glob.glob("*.jpg"):
        img = cv2.imread(file)
        cv2.imshow('Img',img)
        cv2.waitKey(5)
        print(file)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# img = cv2.imread('Imgs/lena.jpg')

# cv2.imshow('Img',img)

# print('Shape: ', img.shape)
# print('Size: ' , img.size)
# print('Type: ' , img.dtype)

# cv2.waitKey()

# cv2.destroyAllWindows()

