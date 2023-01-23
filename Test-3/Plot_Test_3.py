import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import os
import pandas
import numpy as np

PATH_DIRECTORY = Path(__file__).parents[0] / 'Results/CSVs'
files = PATH_DIRECTORY.glob('*.csv')
COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

models_recognition = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  #"Dlib", 
  "SFace"
]
models_detection = [
  "opencv", 
  "ssd", 
  "dlib", 
  "mtcnn", 
  "retinaface", 
  "mediapipe"
]

thresholds = [
    0.4,
    0.4,
    0.3,
    0.1,
    0.23,
    0.015,
    0.68,
    0.07,
    0.5932763306134152
]
subject = ''

for file in files:
    csv_file = pandas.read_csv(file)
    subject = csv_file[COLUMNS[0]][0][9:12]
    for iterator in zip(models_recognition, thresholds):
        results_recognizer = []
        years_old = []
        for i in range(len(csv_file)):
            if csv_file[COLUMNS[6]][i] == iterator[0]:
                results_recognizer.append(csv_file[COLUMNS[7]][i])
                years_old.append(csv_file[COLUMNS[1]][i])
        plt.figure()
        plt.xlabel("Anos")
        plt.ylabel("Distâncias")
        plt.title("Sujeito: "+ subject + ". Modelo: " + iterator[0] + ".")
        plt.bar(years_old, results_recognizer)
        plt.plot([years_old[0], years_old[-1]], [iterator[1], iterator[1]], "-", color='b', label='Limite')
        name_plot = str(Path(__file__).parents[0] / 'Results/Images') +  '/' +  iterator[0] + '-' + subject
        plt.savefig(name_plot)
        #plt.show()
        plt.close()