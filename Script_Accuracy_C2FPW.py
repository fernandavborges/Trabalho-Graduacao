
import os
from pathlib import Path
import random
import pandas
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
PATH_RESULTS = Path().absolute() / 'Test-2/Results/Test-Accuracy/'
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

    true_positive = []
    true_negative = []

    results = DataFrame(columns=COLUMNS)
    for sub in subjects:
        images = []
        for file in files:
            if(file[0:4] == sub):
                images.append(file)
        random_image_1 = random.choice(images)
        images.remove(random_image_1)
        random_image_2 = random.choice(images)

        images.append(random_image_1)
        random_image_3 = random.choice(images)
        images.remove(random_image_3)
        random_image_4 = random.choice(images)

        while((random_image_1 == random_image_3 or random_image_1 == random_image_4) and (random_image_2 == random_image_3 or random_image_2 == random_image_4)):
            random_image_3 = random.choice(images.append(random_image_1))
            images.remove(random_image_3)
            random_image_4 = random.choice(images)

        img1_path = str(PATH_BD / random_image_1)
        img2_path = str(PATH_BD / random_image_2)
        img3_path = str(PATH_BD / random_image_3)
        img4_path = str(PATH_BD / random_image_4)
        
        for recognizer in models_recognition:
            result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = "mtcnn")
            line = [random_image_1, random_image_1[10:14], random_image_2, random_image_2[10:14], distance_metrics[0], "mtcnn", recognizer, result.get('distance'), result.get('verified')]
            results.loc[len(results)] = line
            true_positive.append(result.get('verified'))

            result = DeepFace.verify(img1_path = img3_path, img2_path = img4_path, model_name=recognizer, distance_metric = "cosine", detector_backend = "mtcnn")
            line = [random_image_3, random_image_3[10:14], random_image_4, random_image_4[10:14], distance_metrics[0], "mtcnn", recognizer, result.get('distance'), result.get('verified')]
            results.loc[len(results)] = line
            true_positive.append(result.get('verified'))
        

    print('Sujeitos reconhecidos corretamente:', true_positive.count('True'))
    print('True positive:', true_positive.count('True')/len(true_positive))

    images = []
    for file in files:
        images.append(file)
    
    for i in range(len(true_positive)):
        random_image_1 = random.choice(images)
        images.remove(random_image_1)
        random_image_2 = random.choice(images)

        while(random_image_1[:4] == random_image_2[:4]):
            random_image_2 = random.choice(images)
        images.remove(random_image_2)

        img1_path = str(PATH_BD / random_image_1)
        img2_path = str(PATH_BD / random_image_2)

        for recognizer in models_recognition:
            result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "cosine", detector_backend = "mtcnn")
            line = [random_image_1, random_image_1[10:14], random_image_2, random_image_2[10:14], distance_metrics[0], "mtcnn", recognizer, result.get('distance'), result.get('verified')]
            results.loc[len(results)] = line
            true_negative.append(result.get('verified'))
    
    print('Sujeitos não reconhecidos corretamente:', true_positive.count('False'))
    print('True negative:', true_positive.count('False')/len(true_positive))

    name_csv = 'Accuracy.csv'
    path_csv = PATH_RESULTS / name_csv
    results.to_csv(path_csv)
