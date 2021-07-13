# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:54:18 2021

@author: vivia
"""

import cv2
import os


dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\RISORSE_ESTERNE\\DATASET_ESTERNI'

emotions = [
    #'BOREDOM',
    #'CONFUSION',
    #'ENTHUSIASM',
    #'FRUSTRATION',
    'INTEREST',
    #'NEUTRAL',
    #'SURPRISE'
    ]

dynemo = 'DYNEMO'


for em in emotions:
    print("HERE: " + dataset_path + '\\' + dynemo + '\\' + em)
    if os.path.isdir(dataset_path  + '\\' + dynemo + '\\'  + em):
        print("IS DIR: " + dataset_path + '\\' + dynemo + '\\' + em)
        entries = os.scandir(dataset_path  + '\\' + dynemo + '\\' + em)
        for f in entries:
            print(f.name)                
            if f.is_file():
                print("HERE")
                print(dataset_path  + '\\' + dynemo + '\\' + em +  '\\' + f.name)
                vidcap = cv2.VideoCapture(dataset_path + '\\'  + dynemo + '\\' + em  + '\\' + f.name)
                        
                vidcap.set(cv2.CAP_PROP_POS_FRAMES,0)
                success,image = vidcap.read()
                cv2.imwrite(dataset_path  + '\\' + dynemo + '\\' + f.name + "_" + em + "_first.jpg", image)  
                
                last_frame_num = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) - 1
                
                if (last_frame_num > 1):

                    print('FRAME COUNT = ' + str(last_frame_num + 1))
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, last_frame_num)
                    success,image = vidcap.read()
                    cv2.imwrite(dataset_path  + '\\' + dynemo + '\\' + f.name + "_" + em + "_end.jpg", image) 

                    middle_frame_num = (last_frame_num + 1) // 2
                    print(dataset_path + '\\' + dynemo + '\\')
                    vidcap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame_num)
                    success,image = vidcap.read()
                    cv2.imwrite(dataset_path  + '\\' + dynemo + '\\' + f.name + "_" + em + "_half.jpg", image) 


