# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:42:50 2021

@author: vivia
"""
import pandas as pd
import shutil as shu
import os

#PATH
path_to_baum1_excel = "E:\\TESI\\RISORSE_ESTERNE\\DOCUMENTI_DATASET_ESTERNI\\BAUM1_data.xlsx"
path_to_baum1_excel_2 = "E:\\TESI\\RISORSE_ESTERNE\\DOCUMENTI_DATASET_ESTERNI\\BAUM1a.xlsx"
path_to_baum1_folder = 'E:\\TESI\\RISORSE_ESTERNE\\DATASET_ESTERNI\\BAUM1'
path_to_baum1_riorg_folder = 'E:\\TESI\RISORSE_ESTERNE\\DATASET_ESTERNI\\BAUM1_RIORGANIZZATO'

#funzione di ricerca all'interno dei file nel so
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

#lettura excel
baum1 = pd.read_excel(path_to_baum1_excel, sheet_name='Sheet1',usecols=['Clip Name', 'Emotion'])
baum1a = pd.read_excel(path_to_baum1_excel_2, sheet_name='Sheet1',usecols=['Clip Name', 'Emotion'])
#trasformazione dei dati in lista
baum1_list = baum1.values.tolist()
baum1a_list = baum1a.values.tolist()

#trasformazione in dizionario, ricerca e copia nella directory
for item in baum1_list:
    photo = {"Clip Name":None, "Emotion":None}
    photo['Clip Name'] = item[0]
    photo['Emotion'] = item[1]
    
    print("photo name: " + photo['Clip Name'])
    print("photo Emotion: " + photo['Emotion'])

    path_to_file = find(photo['Clip Name'] + '.mp4', path_to_baum1_folder)
    
    print(path_to_file)
    
    if (path_to_file):
        if not os.path.exists(path_to_baum1_riorg_folder + '\\' + photo['Emotion'] + '\\'):
            os.makedirs(path_to_baum1_riorg_folder + '\\' + photo['Emotion'] + '\\')
        print("to: " + path_to_baum1_riorg_folder + '\\' + photo['Emotion'])
        shu.copyfile(path_to_file, path_to_baum1_riorg_folder + '\\' + photo['Emotion'] + '\\' + photo['Clip Name'] + '.mp4')
        
for item in baum1a_list:
    photo = {"Clip Name":None, "Emotion":None}
    photo['Clip Name'] = item[0]
    photo['Emotion'] = item[1]
    
    print("photo name: " + photo['Clip Name'])
    print("photo Emotion: " + photo['Emotion'])

    path_to_file = find(photo['Clip Name'] + '.mp4', path_to_baum1_folder)
    
    print(path_to_file)
    
    if (path_to_file):
        if not os.path.exists(path_to_baum1_riorg_folder + '\\' + photo['Emotion'] + '\\'):
            os.makedirs(path_to_baum1_riorg_folder + '\\' + photo['Emotion'] + '\\')
        print("to: " + path_to_baum1_riorg_folder + '\\' + photo['Emotion'])
        shu.copyfile(path_to_file, path_to_baum1_riorg_folder + '\\' + photo['Emotion'] + '\\' + photo['Clip Name'] + '.mp4')        