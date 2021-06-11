import cv2
import time
import HandTrackingModule as htm

wCam,hCam=640,480

cap = cv2.VideoCapture(0) #Cámara frontal
cap.set(3, wCam)
cap.set(4, hCam)
pTime=0

detector = htm.handDetector(detectionCon=0.75)

tipIds=[4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    #print(lmList)


    if len(lmList)!=0:
        fingers=[]

        #Thumn
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #4 fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

            #print(fingers)
        totalFingers = fingers.count(1)

        #Detectar la A
        if (lmList[12][2]>lmList[9][2]) and (lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (lmList[8][2] > lmList[5][2]) and (lmList[4][1] > lmList[2][1]):
            cv2.putText(img, f'Letra A', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        #Detectar la B
        if (lmList[12][2]<lmList[10][2]) and (lmList[16][2] < lmList[14][2]) and (lmList[20][2] < lmList[18][2]) and (lmList[8][2] < lmList[6][2]) and (lmList[4][1] < lmList[2][1]):
            cv2.putText(img, f'Letra B', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        #Detectar la D
        if (lmList[12][2] > lmList[9][2]) and (lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (lmList[8][2] < lmList[5][2]) and (lmList[4][1] < lmList[2][1]):
            cv2.putText(img, f'Letra D', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la E (Checar)
        if (lmList[12][2] > lmList[11][2]) and (lmList[16][2] > lmList[15][2]) and (lmList[20][2] > lmList[19][2]) and (lmList[8][2] > lmList[7][2]) and (lmList[4][1] < lmList[2][1]):
            cv2.putText(img, f'Letra E', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la L
        if (lmList[12][2] > lmList[10][2]) and (lmList[16][2] > lmList[14][2]) and (lmList[20][2] > lmList[18][2]) and (lmList[8][2] < lmList[6][2]) and (lmList[4][1] > lmList[2][1]):
            cv2.putText(img, f'Letra L', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la F
        if (lmList[12][2]<lmList[10][2]) and (lmList[16][2] < lmList[14][2]) and (lmList[20][2] < lmList[18][2]) and (lmList[8][2] > lmList[6][2]) and (lmList[4][2] < lmList[2][2]) and (lmList[4][1] > lmList[2][1]):
            cv2.putText(img, f'Letra F', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la I
        if (lmList[12][2]>lmList[9][2]) and (lmList[16][2] > lmList[13][2]) and (lmList[20][2] < lmList[17][2]) and (lmList[8][2] > lmList[5][2]) and (lmList[4][1] < lmList[2][1]):
            cv2.putText(img, f'Letra I', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la S
        #if (lmList[12][2]>lmList[9][2]) and (lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (lmList[8][2] > lmList[5][2]) and (lmList[4][1] < lmList[2][1]):
            #cv2.putText(img, f'Letra S', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la U
        if (lmList[12][2]<lmList[9][2]) and (lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (lmList[8][2] < lmList[5][2]) and (lmList[4][1] < lmList[2][1]) and (lmList[8][1] <= lmList[6][1]):
            cv2.putText(img, f'Letra U', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Detectar la V (a ver si sale)
        if (lmList[12][2]<lmList[9][2]) and (lmList[16][2] > lmList[13][2]) and (lmList[20][2] > lmList[17][2]) and (lmList[8][2] < lmList[5][2]) and (lmList[4][1] < lmList[2][1]) and (lmList[8][1] > lmList[6][1]):
            cv2.putText(img, f'Letra V', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)