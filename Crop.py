import cv2
import numpy as np
import os
cropping = False
 
x_start, y_start, x_end, y_end = 0, 0, 0, 0
 
image = cv2.imread('Slap_data_1/004/L1.jp2')
oriImage = image.copy()
#print(oriImage.shape)


def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
 
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
 
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
 
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
 
        refPoint = [(x_start, y_start), (x_end, y_end)]
 
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            # cv2.imshow("Cropped", roi)
            cv2.imwrite('temp.png', roi)
            
 
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", mouse_crop)
 
while True:
 
    # i = image.copy()
    i = image.copy()
 	# i = oriImage.copy()
    if not cropping:
        cv2.imshow("image", oriImage)
        #print("not cropping")
 
    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        #print("cropping")
        cv2.imshow("image", i)
 
    # cv2.waitKey(1)
    k = cv2.waitKey(1)
    if  k == ord('s'):
        temp = cv2.imread('temp.png')
        cv2.imshow("Cropped", temp)
        k = cv2.waitKey(0)
        if k == ord('n'):
            cv2.destroyWindow('Cropped')
        elif k == ord('1'):
            l = os.listdir('1_distal_phalanges')
            print(l)
            j = []
            for i in range(len(l)):
                m =l[i][2:-4]
                j.append(int(m))
            g = max(j)+1
            #print(g)
            cv2.imwrite('1_distal_phalanges/'+'1_'+str(g)+'.png', temp)
            cv2.destroyWindow('Cropped')
        elif k == ord('2'):
            l = os.listdir('2_proximal_phalanges')
            print(l)
            j = []
            for i in range(len(l)):
                m =l[i][2:-4]
                j.append(int(m))
            g = max(j)+1
            #print(g)
            cv2.imwrite('2_proximal_phalanges/'+'2_'+str(g)+'.png', temp)
            cv2.destroyWindow('Cropped')




 
# close all open windows
cv2.destroyAllWindows()