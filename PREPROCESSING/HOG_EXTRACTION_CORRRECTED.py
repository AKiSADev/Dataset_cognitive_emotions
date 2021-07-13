from skimage.feature import hog
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import StratifiedKFold
import cv2
import os

dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET_FINALE_BALANCED_SPLITTED_RANDOM_CORRECTED_CROPPED'
csv_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\'

parts = [
    'TRAIN',
    'TEST',
    'VALIDATION'
]

emotions = [
    'BOREDOM',
    'CONFUSION',
    'ENTHUSIASM',
    'FRUSTRATION',
    'INTEREST',
    'NEUTRAL',
    'SURPRISE'
]

train_list = []
test_list = []

for p in parts:
  for em in emotions:
    entries = os.scandir(dataset_path + '/' + p + '/' + em + '/')
    for en in entries:
      
      image = cv2.imread(dataset_path + '/' + p + '/' + em + '/' + en.name)
      image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      fd = hog(image, orientations=8, pixels_per_cell=(8, 8),
                                    cells_per_block=(1, 1))
      fd = fd.tolist()
      fd.append(em)
      if p == 'TRAIN' or p=='VALIDATION':
        train_list.append(fd)
      else:
        test_list.append(fd)


train = pd.DataFrame(train_list)
test = pd.DataFrame(test_list)

train.to_csv(csv_path + "HOG_TRAIN_corrected.csv")
test.to_csv(csv_path + "HOG_TEST_corrected.csv")

print(train)
print(test)