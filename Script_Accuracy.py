
import os
from pathlib import Path
import random
import shutil
import statistics
import numpy as np
from deepface import DeepFace
from pandas import DataFrame

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

distance_metrics = "cosine"
model_detection = "mtcnn"

PATH_BD = Path().absolute() / 'C2FPW'
PATH_RESULTS = Path().absolute() / 'Test-2/Results/Test-Accuracy-2/'
if(not PATH_RESULTS.exists()):
    os.mkdir(PATH_RESULTS)

COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

if __name__ == "__main__":  
    files = os.listdir(PATH_BD)
    subjects = []
    for file in files:
        if(file[0:4] not in subjects and file != '.gitignore'):
            subjects.append(file[0:4])
    subjects.sort()
    for sub in subjects:
        print('Subject: ', sub)
        results = DataFrame(columns=COLUMNS)
        images = []
        for file in files:
            if(file[0:4] == sub):
                images.append(file)
        random_image = random.choice(images)
        images.remove(random_image)

        for image in images:
            img1_path = str(PATH_BD / random_image)
            for recognizer in models_recognition:
                print('Detector: mtcnn' + '\n' + 'Recognizer: ' + recognizer + '\n')
                img2_path = str(PATH_BD / image)
                try:
                    result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = "mtcnn")
                    line = [random_image, random_image[10:14], image, image[10:14], distance_metrics[0], "mtcnn", recognizer, result.get('distance'), result.get('verified')]
                    results.loc[len(results)] = line
                except Exception as exception:
                    print('Exception:' + str(exception))
        name_csv = sub + '.csv'
        path_csv = PATH_RESULTS / name_csv
        results.to_csv(path_csv)
    

