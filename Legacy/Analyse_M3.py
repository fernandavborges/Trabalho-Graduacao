from pathlib import Path
import pandas
import numpy as np



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


PATH_DIRECTORY_READ = Path().absolute() / 'Results/CSVs-M3/'
COLUMNS_READ = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Image 3', 'Year 3', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Average Result', 'Recognition Result']
files_read = PATH_DIRECTORY_READ.glob('*.csv')

COLUMNS_WRITE = ['Subject', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Ascent', 'Descent']


results = pandas.DataFrame(columns=COLUMNS_WRITE)
for file in files_read:
    csv_file = pandas.read_csv(file)
    subject = csv_file[COLUMNS_READ[0]][0][5:9]
    
    for recognizer in models_recognition:
        averages = []
        ascent, descent = False, False
        n_ascent, n_descent = 0, 0
        for i in range(len(csv_file)):
            if csv_file[COLUMNS_READ[8]][i] == recognizer:
                averages.append(csv_file[COLUMNS_READ[9]][i])
        if(subject == 'S008'):
            auxiliar = averages

        for i in range(1, len(averages)):
            if averages[i] > averages[i-1]:
                if(descent == False):
                    ascent = True
                    n_ascent = n_ascent + averages[i] - averages[i-1]
            else:
                if(ascent == True):
                    n_descent = n_descent + averages[i-1] - averages[i]
                    descent = True

        if(descent == True and ascent == True):
            results = results.append({'Subject':subject, 'Distance Metric': 'cosine', 'Detection Model': 'mtcnn', 'Recognition Model': recognizer, 'Ascent': n_ascent, 'Descent': n_descent}, ignore_index=True)

name_csv = 'Results_M3.csv'
path_csv = PATH_DIRECTORY_READ / name_csv
save = results.to_csv(path_csv)

print(auxiliar)