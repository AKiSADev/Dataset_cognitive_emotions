import os
import cv2

dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET'

emotions = [
    # 'BOREDOM',
    # 'CONFUSION',
    # 'ENTHUSIASM',
    'FRUSTRATION',
    # 'INTEREST',
    # 'NEUTRAL',
    # 'SURPRISE'
    ]

baum = 'BAUM2\\PHOTOS'
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

for em in emotions:
    if os.path.isdir(dataset_path + '\\' + em + '\\' + baum + '\\'):
        entries = os.scandir(dataset_path + '\\' + em + '\\' + baum + '\\')
        for en in entries:
            if en.is_file():
                imagePath = dataset_path + '\\' + em + '\\' + baum + '\\' + en.name
                image = cv2.imread(imagePath)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.3,
                    minNeighbors=3,
                    minSize=(30, 30)
                )
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 0)
                    roi_color = image[y:y + h, x:x + w]
                    print("[INFO] Object found. Saving locally.")
                    to_path = dataset_path + '\\' + em + '\\' + baum 
                    complete_to_path = dataset_path + '\\' + em + '\\' + baum + '\\' +  os.path.splitext(en.name)[0]

                    print(complete_to_path + '_cropped.jpg')
                    cv2.imwrite(complete_to_path + '_cropped.jpg', roi_color)



    

