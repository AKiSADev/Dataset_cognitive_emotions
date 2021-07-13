# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:54:18 2021

@author: vivia
"""

import cv2
import os


dataset_path = 'E:\\TESI\\TESI_LAMBONI_VIVIANA\\DATASET'

emotions = [
    #'BOREDOM',
    #'CONFUSION',
    #'ENTHUSIASM',
    'FRUSTRATION',
    #'INTEREST',
    #'NEUTRAL',
    #'PERPLEXITY',
    #'SURPRISE'
    ]

baum = 'BAUM1'


for em in emotions:
    print(dataset_path + '\\' + em + '\\' + baum + '\\')
    if os.path.isdir(dataset_path + '\\' + em + '\\' + baum + '\\'):
        entries = os.scandir(dataset_path + '\\' + em + '\\' + baum + '\\')
        for en in entries:
            if en.is_dir():
                print(en.name)
                print(en.is_dir())
                files = os.scandir(dataset_path + '\\' + em + '\\' + baum + '\\' + en.name)
                for f in files:
                    if f.is_file():
                        print(dataset_path + '\\' + em + '\\' + baum + '\\' + en.name + '\\' + f.name)
                        vidcap = cv2.VideoCapture(dataset_path + '\\' + em + '\\' + baum + '\\' + en.name + '\\' + f.name)
                                
                        vidcap.set(cv2.CAP_PROP_POS_FRAMES,0)
                        success,image = vidcap.read()
                        cv2.imwrite(dataset_path + '\\' + em + '\\' + baum + '\\' + f.name + "_" + em + "_first.jpg", image)  
                        
                        last_frame_num = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) - 1
                        
                        if (last_frame_num > 1):

                            print('FRAME COUNT = ' + str(last_frame_num + 1))
                            vidcap.set(cv2.CAP_PROP_POS_FRAMES, last_frame_num)
                            success,image = vidcap.read()
                            cv2.imwrite(dataset_path + '\\' + em + '\\' + baum + '\\' + f.name + "_" + em + "_end.jpg", image) 

                            middle_frame_num = (last_frame_num + 1) // 2
                            print(dataset_path + '\\' + em + '\\' + baum + '\\')
                            vidcap.set(cv2.CAP_PROP_POS_FRAMES, middle_frame_num)
                            success,image = vidcap.read()
                            cv2.imwrite(dataset_path + '\\' + em + '\\' + baum + '\\' + f.name + "_" + em + "_half.jpg", image) 


