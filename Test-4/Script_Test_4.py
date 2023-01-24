"""
    Script that performs the recognition tests for Test 4 (HDA-PlasticSurgery Database), and the recognition is always done between two images.
"""
from deepface import DeepFace
import os
from pathlib import Path
from pandas import DataFrame

# Chosing the database
PATH_DIRECTORY_BD = Path().absolute().parents[0]  / 'HDA-PlasticSurgery'
pastes = os.listdir(PATH_DIRECTORY_BD)

previous_image = ''
subject = ''
first_subject = True

COLUMNS = ['Surgery', 'Image 1', 'Image 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

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
  "Dlib", 
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

results_folder = Path().absolute() / 'Results/CSVs'
file_logs_name = Path().absolute() / 'Logs_Test_4.txt'

file_logs = open(file_logs_name, "w")

for paste in pastes:
    path = PATH_DIRECTORY_BD / paste
    files = os.listdir(path)
    results = DataFrame(columns=COLUMNS)
    for file in files:
      if(file != '.gitignore'):
        if(file[0:3] != subject):
            previous_image = ''
        subject = file[0:3]
        for recognizer in models_recognition:
            print('Detector: ' + models_detection[3] + '\n' + 'Recognizer: ' + recognizer + '\n')
            if previous_image != '':
                img1_path = str(PATH_DIRECTORY_BD / paste / previous_image)
                img2_path = str(PATH_DIRECTORY_BD / paste / file)

                try:
                    result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = "euclidean", detector_backend = models_detection[3])
                    results = results.append({'Surgery': paste, 'Image 1':img1_path, 'Image 2':img2_path, 'Distance Metric':distance_metrics[0], 'Detection Model':models_detection[3], 'Recognition Model':recognizer, 'Distance Result':result.get('distance'), 'Recognition Result':result.get('verified')}, ignore_index=True)
                except Exception as exception:
                    print('Exception:' + str(exception))
                    file_logs.write('Detector: ' + models_detection[3] + '. Recognizer: ' + recognizer + '.\n') 
                    file_logs.write('Image ' + previous_image + ' e ' + file + '\n') 
                    file_logs.write('Exception:' + str(exception) + '\n\n')
        previous_image = file
    name_csv = paste + '.csv'
    path_csv = results_folder / name_csv
    save = results.to_csv(path_csv)
    file_logs.close()
    