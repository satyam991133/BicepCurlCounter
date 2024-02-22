

import cv2
import cvzone
import mediapipe
from cvzone.PoseModule import PoseDetector
import numpy as np


# Declare all the Variables here !

cap = cv2.VideoCapture(0);
detector = PoseDetector(detectionCon=0.69)
barColor = (255, 0 , 0)
percentageColor = (90 , 90 , 90)
direction = 1;
curlCount = 0;

# [25-160] angles between wrist , elbow  and shoulder

while True :
     _,img = cap.read();
     img = detections = detector.findPose(img);

     landMarkList , bbox = detector.findPosition(img , draw = False);

     if landMarkList:
         # print(landMarkList);

         angle = detector.findAngle(img , 16 , 14 , 12);

         # print(angle);


         # BarValue of the rectange
         barValue = np.interp(angle  , (30 , 160) , (60 , 300 + 60));

         # Bar percentage
         percentageValue =  np.interp(angle  , (30 , 160) , (100 , 0));

         # Color Rectangle Bar according to barvalue from [0,100]
         cv2.rectangle(img , (560 , int(barValue)) , (560 + 40 , 300 + 60) , barColor , cv2.FILLED);

         # Create Recatnge of 300 * 40
         cv2.rectangle(img , (560 , 60) , ( 560 + 40  , 60 + 300) , (0,0,0) , 5);

         cvzone.putTextRect(img , f"{int(percentageValue)} %" , (540 , 40) , 1.6 , 2 , percentageColor  , border = 4 , colorB = (251 , 230 , 240) )

         # Logic for counting Bicep Curls
         if percentageValue == 100:
             if direction == 0 :
                 curlCount+=0.5
                 direction^=1;
                 barColor = (0 , 255 , 0);
         elif percentageValue == 0:
             if direction == 1:
                 curlCount+=0.5
                 direction^=1;
                 barColor = (0 , 255 , 0);
         else :
             barColor = (0 , 0 , 255);

         print(curlCount);

     # Print
     cvzone.putTextRect(img , 'BICEP CURL COUNTER !!' , (50 , 40) , 2 , 3 , (255 , 255 , 255) , (255 , 0 , 0) , border = 6 , colorB = (0 , 0 , 0));
     cvzone.putTextRect(img,  f'Curl Count : {int(curlCount)}' , (50, 120), 2, 3, (255, 255, 255), (0 , 105 , 0), border=6, colorB=(0, 0, 0));


     cv2.imshow('Bicep Curl Counter',img)

     # To close the Camera press `s`
     if cv2.waitKey(1) == ord('s'):
        break


# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows() 










