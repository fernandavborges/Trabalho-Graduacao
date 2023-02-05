import os
from pathlib import Path
import pandas
from pandas import DataFrame
import numpy as np

distance_metrics = [
  "cosine", 
  "euclidean", 
  "euclidean_l2"
]
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

PATH_DIRECTORY_READ = Path().absolute() / 'Results/CSV-1'
files_read = PATH_DIRECTORY_READ.glob('*.csv')
COLUMNS_READ = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

COLUMNS_WRITE = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Image 3', 'Year 3', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Average Result', 'Recognition Result']
results_folder = Path().absolute() / 'Results/CSVs-M3/'

subject = ''

# para cada CSV, que corresponde a um sujeito
for file in files_read:
    csv_file = pandas.read_csv(file)
    subject = csv_file[COLUMNS_READ[0]][0][5:9]
    results = DataFrame(columns=COLUMNS_WRITE)

    # para cada modelo de reconhecimento
    for iterator in zip(models_recognition, thresholds):
        results_recognizer = []
        imagens = []
        medias = []
        # olhando cada linha do CSV do sujeito
        for i in range(len(csv_file)):
            if csv_file[COLUMNS_READ[6]][i] == iterator[0]:
                # salva todos os resultados
                results_recognizer.append(csv_file[COLUMNS_READ[7]][i])
                # e imagens usadas na comparacao
                imagens.append(csv_file[COLUMNS_READ[0]][i])
        for i in range(len(results_recognizer)-2):
            # faz a média de 3 em 3 resultados
            media = sum(results_recognizer[i:i+3])/len(results_recognizer[i:i+3])
            if media < iterator[1]:
              average_result = 'True'
            else:
              average_result = 'False'
            results = results.append({'Image 1':imagens[i], 'Year 1':imagens[i][15:19], 'Image 2':imagens[i+1], 'Year 2':imagens[i+1][15:19], 'Image 3':imagens[i+2], 'Year 3':imagens[i+2][15:19], 'Distance Metric':distance_metrics[0], 'Detection Model':models_detection[3], 'Recognition Model':iterator[0], 'Average Result':media, 'Recognition Result':average_result}, ignore_index=True)
        #print("'Recognition Model': ")
        #print(iterator[0])
        #print("Results_recognizer: ")
        #print(results_recognizer)

    #print("Salvo")
    #print(results)
    name_csv = subject + '.csv'
    path_csv = results_folder / name_csv
    save = results.to_csv(path_csv)