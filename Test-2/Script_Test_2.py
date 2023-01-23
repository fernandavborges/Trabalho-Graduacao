"""
    Script that performs the recognition tests for Test 2, and the recognition is always done between two images.
"""

from deepface import DeepFace
import os
from pathlib import Path
from pandas import DataFrame

# Taking the image bank created for this test
PATH_DIRECTORY = Path(__file__).parents[0] / 'BD'
files = os.listdir(PATH_DIRECTORY)

previous_image = ''
subject = ''
first_subject = True

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
COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']

results_folder = Path(__file__).parents[0] / 'Results/CSVs/'
file_logs_name = Path(__file__).parents[0] / 'Logs_Test_1.txt'
file_logs = open(file_logs_name, "w")

for file in files:
  if file[0:2]=='S0': 
      if(file[0:4] != subject and first_subject == False): # Changed subject - save csv with previous subject information
          name_csv = previous_image[0:4] + '.csv'
          path_csv = results_folder / name_csv
          save = results.to_csv(path_csv)
          results = DataFrame(columns=COLUMNS)
          previous_image = ''
      subject = file[0:4]

      if first_subject:
          results = DataFrame(columns=COLUMNS)
          first_subject = False

      for recognizer in models_recognition:
          print('Detector: mtcnn' + '\n' + 'Recognizer: ' + recognizer + '\n')

          if previous_image != '':
              img1_path = str(Path(__file__).parents[0] / 'BD' / previous_image)
              img2_path = str(Path(__file__).parents[0] / 'BD' / file)

              try:
                  result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path, model_name=recognizer, distance_metric = distance_metrics[0], detector_backend = models_detection[3])
                  results = results.append({'Image 1':img1_path, 'Year 1':previous_image[10:14], 'Image 2':img2_path, 'Year 2':file[10:14], 'Distance Metric':distance_metrics[0], 'Detection Model':models_detection[3], 'Recognition Model':recognizer, 'Distance Result':result.get('distance'), 'Recognition Result':result.get('verified')}, ignore_index=True)
              except Exception as exception:
                  print('Exception:' + str(exception))
                  file_logs.write('Detector: mtcnn' + '. Recognizer: ' + recognizer + '.\n') 
                  file_logs.write('Imagem ' + previous_image + ' e ' + file + '\n') 
                  file_logs.write('Exception:' + str(exception) + '\n\n')
  previous_image = file
name_csv = previous_image[0:4] + '.csv'
path_csv = results_folder / name_csv
save = results.to_csv(path_csv)
file_logs.close()
