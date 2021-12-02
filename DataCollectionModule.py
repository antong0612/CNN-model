import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, angleList, speedList
countFolder = 0
imgList = []
angleList = []
speedList = []

#GET CURRNET  DIRECTORY PATH
myDirectory = os.path.join(os.getcwd(), 'training-images')
#print(myDirectory)

#CREATE A NEW FOLDER BASED ON THE PREVIOUS FOLDER COUNT
while os.path.exists(os.path.join(myDirectory, f'IMG{str(countFolder)}')):
    countFolder += 1
newPath = myDirectory + "/IMG" + str(countFolder)
os.makedirs(newPath)

#SAVE IMAGES IN THE FOLDER
def saveData(img, angle, speed):
    global imgList, angleList, speedList
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace('.','')
    fileName = os.path.join(newPath, f'Image_{timestamp}.jpg')
    cv2.imwrite(fileName, img)
    imgList.append(fileName)
    angleList.append(angle)
    speedList.append(speed)


#SAVE THE LOG FILE WHEN THE SESSIONS ENDS
def saveLog():
    global imgList, angleList
    rawData1 = {
        'Image': imgList,
        'Angle': angleList,
    }
    rawData2 = {
        'Image': imgList,
        'Speed': speedList
    }
    df1 = pd.DataFrame(rawData1)
    df1.to_csv(os.path.join(myDirectory,f'log_angle_{str(countFolder)}.csv'), index=False, header=False)
    df2 = pd.DataFrame(rawData2)
    df2.to_csv(os.path.join(myDirectory,f'log_speed_{str(countFolder)}.csv'), index=False, header=False)
    print('Log Saved')
    print('Total Images:', len(imgList))
