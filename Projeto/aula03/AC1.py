import cv2
import glob, os
import time

os.chdir("Imgs")
while True :

    for file in glob.glob("*.jpg"):
        img = cv2.imread(file)
        cv2.imshow('Img',img)
        cv2.waitKey(5000)
        print(file)
        
    if 0xFF == ord('q') | 0xFF == ord('Q'): 
        print("batata")
        cv2.destroyAllWindows()
        break

