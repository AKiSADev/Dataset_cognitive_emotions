import os
from shutil import copyfile
import cv2
import random

dataset_final_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE'
dataset_balanced = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED'

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
    ]


for em in emotions:
    print(em)
    print("DIRECTORIES:")
    if not os.path.isdir(dataset_balanced + '\\' + em):
        os.makedirs(dataset_balanced + '\\' + em)
    for root, dirs, files in os.walk(dataset_final_path + '\\' + em, topdown=False):
        file_number = len(files)
        print("FILE NUMBER: " + str(file_number))
        if file_number < 1000:
            for f in files:
                originalImage = cv2.imread(os.path.join(root, f))
                flipHorizontal = cv2.flip(originalImage, 1)
                cv2.imwrite(dataset_balanced + '\\' + em + '\\flipped_'+ f, flipHorizontal)
                source = os.path.join(root, f)
                dst = dataset_balanced + '\\' + em + '\\' + f
                copyfile(source, dst)
        if file_number >= 1000 and file_number <= 2000:
            max_flip = 2000 - file_number
            count = 0
            for  f in files:
                if count < max_flip:
                    print("FILE NAME: " + f)
                    originalImage = cv2.imread(os.path.join(root, f))
                    flipHorizontal = cv2.flip(originalImage, 1)
                    cv2.imwrite(dataset_balanced + '\\' + em + '\\flipped_'+ f, flipHorizontal)
                    count += 1                    
                source = os.path.join(root, f)
                dst = dataset_balanced + '\\' + em + '\\' + f
                copyfile(source, dst)  
        if file_number > 2000:
            print("> 2000")
            i = 0
            while i < 2000:
                print(str(i))
                f = random.choice(os.listdir(root))
                if os.path.isfile(dataset_balanced + '\\' + em + '\\' + f) == False:
                    source = os.path.join(root, f)
                    dst = dataset_balanced + '\\' + em + '\\' + f
                    copyfile(source, dst)
                    i += 1  
                