# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:42:50 2021

@author: vivia
"""
import pandas as pd
import shutil as shu
import os

#PATH
path_to_baum2_excel = "E:\\TESI\\RISORSE_ESTERNE\\DOCUMENTI_DATASET_ESTERNI\\BAUM2_data.xlsx"
path_to_baum2_folder = 'E:\\TESI\\RISORSE_ESTERNE\\DATASET_ESTERNI\\BAUM2'
path_to_baum2_riorg_folder = 'E:\\TESI\RISORSE_ESTERNE\\DATASET_ESTERNI\\BAUM2_RIORGANIZZATO'

#funzione di ricerca all'interno dei file nel so
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

#lettura excel
baum2 = pd.read_excel(path_to_baum2_excel, sheet_name='Sheet1',usecols=['Clip Name', 'Emotion'])

#trasformazione dei dati in lista
baum2_list = baum2.values.tolist()

#trasformazione in dizionario, ricerca e copia nella directory
for item in baum2_list:
    photo = {"Clip Name":None, "Emotion":None}
    photo['Clip Name'] = item[0]
    photo['Emotion'] = item[1]
    
    print("photo name: " + photo['Clip Name'])
    print("photo Emotion: " + photo['Emotion'])
    
    folder_file = photo['Clip Name'].split('_')
    folder = folder_file[0]
    file = folder_file[1]
    
    print(path_to_baum2_folder + '\\' + folder + '\\' + 'avi')
    print(file)

    path_to_file = find(file + '.avi', path_to_baum2_folder + '\\' + folder + '\\' + 'avi')
    
    print(path_to_file)
    
    if (path_to_file):
        if not os.path.exists(path_to_baum2_riorg_folder + '\\' + photo['Emotion'] + '\\'):
            os.makedirs(path_to_baum2_riorg_folder + '\\' + photo['Emotion'] + '\\')
        print("to: " + path_to_baum2_riorg_folder + '\\' + photo['Emotion'])
        shu.copyfile(path_to_file, path_to_baum2_riorg_folder + '\\' + photo['Emotion'] + '\\' + photo['Clip Name'] + '.avi')
        