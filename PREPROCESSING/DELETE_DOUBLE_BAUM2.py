import os
import cv2

dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
    ]

baum = 'BAUM2\\PHOTOS'
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

for em in emotions:
    if os.path.isdir(dataset_path + '\\' + em + '\\' + baum + '\\'):
        entries = os.scandir(dataset_path + '\\' + em + '\\' + baum + '\\')
        for en in entries:
            if en.is_file():
                print("FILENAME " + en.name)
                if en.name.find("cropped_cropped") != -1:
                    print("CONTAINS " + en.name + " " + str(en.name.find("cropped")))
                    os.remove(dataset_path + '\\' + em + '\\' + baum + '\\' + en.name)
                if en.name.find("cropped_cropped_cropped") != -1:
                    print("CONTAINS " + en.name + " " + str(en.name.find("cropped")))
                    os.remove(dataset_path + '\\' + em + '\\' + baum + '\\' + en.name)
                if en.name.find("cropped") == -1:
                    print("CONTAINS " + en.name + " " + str(en.name.find("cropped")))
                    os.remove(dataset_path + '\\' + em + '\\' + baum + '\\' + en.name)