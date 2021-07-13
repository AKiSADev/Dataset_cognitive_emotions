import os
import cv2
import numpy as np

dataset_balanced_divided = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED_SPLITTED'
dataset_balanced_divided_cropped = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED_SPLITTED_CROPPED'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
]

directs = [
    'TRAIN',
    'TEST',
    'VALIDATION'
]

        # if not os.path.isdir(dataset_balanced_divided + '\\' + em + '\\' + d):
        #     os.makedirs(dataset_balanced_divided + '\\' + em + '\\' + d)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

for d in directs:
    for em in emotions:
        entries = os.scandir(dataset_balanced_divided + '\\' + em + '\\' + d + '\\')
        for en in entries:
            if en.is_file():
                imagePath = dataset_balanced_divided + '\\' + em + '\\' + d + '\\' + en.name
                image = cv2.imread(imagePath)
                if image is not None:
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor=1.3,
                        minNeighbors=3,
                        minSize=(30, 30)
                    )
                    count=0
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 0)
                        roi_color = image[y:y+h, x:x+w]
                        print(str(roi_color))
                        print("[INFO] Object found. Saving locally.")
                        if not os.path.isdir(dataset_balanced_divided_cropped + '\\' + d + '\\' + em ):
                            os.makedirs(dataset_balanced_divided_cropped + '\\' + d + '\\' + em )                    
                        complete_to_path = dataset_balanced_divided_cropped + '\\' + d + '\\' + em + '\\' +  os.path.splitext(en.name)[0]
                        roi_color = cv2.resize(roi_color, (224, 224), interpolation=cv2.INTER_AREA)
                        cv2.imwrite(complete_to_path + "_" + str(count) + '_.jpg', roi_color)
                        count += 1