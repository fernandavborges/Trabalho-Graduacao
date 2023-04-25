from pathlib import Path
import pandas
import numpy as np
import shutil
import os
from pandas import DataFrame

PATH_DIRECTORY = Path().absolute()  / 'Results/CSVs'
csvs = PATH_DIRECTORY.glob('*.csv')

models_recognition = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace"
]

COLUMNS = ['Surgery', 'Image 1', 'Image 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
COLUMNS_WRITE = ['Surgery', 'Model', 'Accuracy', 'Average Result']

if __name__ == "__main__":

    results = DataFrame(columns=COLUMNS_WRITE)
    k = 0
    for file in csvs:
        csv_file = pandas.read_csv(file)
        for model in models_recognition:
            count_total = 0
            count_true = 0
            sum_result = 0
            for i in range(len(csv_file)):
                if(csv_file[COLUMNS[5]][i] == model):
                    count_total = count_total + 1
                    sum_result = sum_result + csv_file[COLUMNS[6]][i]
                    if(csv_file[COLUMNS[7]][i] == True):
                        count_true = count_true + 1
            results.loc[k] = [csv_file[COLUMNS[0]][i], model, count_true/count_total, sum_result/count_total]
            k = k + 1

    name_csv = 'FinalResult.csv'
    path_csv = Path().absolute() / 'Results' / name_csv
    results.to_csv(path_csv)

    csv_file = pandas.read_csv(path_csv)
    for model in models_recognition:
        count_total = 0
        sum_result = 0
        for i in range(len(csv_file)):
            if(csv_file[COLUMNS_WRITE[1]][i] == model):
                count_total = count_total + 1
                sum_result = sum_result + csv_file[COLUMNS_WRITE[2]][i]
        print('Model: ', model, '. Acurracy: ', sum_result/count_total)

