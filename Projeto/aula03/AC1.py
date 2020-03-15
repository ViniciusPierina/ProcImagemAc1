import cv2
import glob, os
import time

water = cv2.imread('Watermark/watermark.jpg')
water = cv2.resize(water,(50,50))
os.chdir("Imgs")
while True :
    for file in glob.glob("*.jpg"):
        img = cv2.imread(file)

        img = cv2.copyMakeBorder(img,40,10,10,10,cv2.BORDER_CONSTANT,value=[255,255,255])

        img = cv2.resize(img,(512,512))

        img = cv2.putText(img,'Processamento de Imagens', 
            (10,25), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1,
            (0,0,0),
            2)

        x_offset=450
        y_offset=450
        img[y_offset:y_offset+water.shape[0], x_offset:x_offset+water.shape[1]] = water

        cv2.imshow('Img',img)
        print(img.shape)

        key = cv2.waitKey(5000)
        if key == 113:
            break
        elif key == 81:
            break

    if key == 113  :
        print("batata")
        cv2.destroyAllWindows()
        break
    if key == 81  :
        print("batata")
        cv2.destroyAllWindows()
        break
        