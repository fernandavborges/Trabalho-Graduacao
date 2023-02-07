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


PATH_DIRECTORY_READ = Path().absolute() / 'Results/CSVs/'
COLUMNS_READ = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
files_read = PATH_DIRECTORY_READ.glob('*.csv')

PATH_DIRECTORY_WRITE = Path().absolute() / 'Results/Analyser/'
COLUMNS_WRITE = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Recognized', 'Total Comparisons', 'Average (3)', 'Average (4)', 'Average (5)']
files_write = PATH_DIRECTORY_WRITE.glob('Analyser_*.csv')

path_files = []
for file in files_read:
    path_files.append(str(file))

for recognizer in models_recognition:
    results = pandas.DataFrame(columns=COLUMNS_WRITE)
    k = 0
    for file in path_files:
        recognized = 0
        first_age = True
        results_recognizer = []
        ages, ages_gap= [], []
        age_before, age_after = 0, 0
        average_3, average_4, average_5 = [], [], []

        csv_file = pandas.read_csv(file)
        born_year = int(csv_file[COLUMNS_READ[0]][0][10:14])
        subject = csv_file[COLUMNS_READ[0]][0][5:9]

        for i in range(len(csv_file)):
            age = csv_file[COLUMNS_READ[1]][i] - born_year
            if age not in ages:
                ages.append(age)
            age = csv_file[COLUMNS_READ[3]][i] - born_year
            if age not in ages:
                ages.append(age)

            if csv_file[COLUMNS_READ[6]][i] == recognizer:
                results_recognizer.append(csv_file[COLUMNS_READ[7]][i])
                if(csv_file[COLUMNS_READ[8]][i] == True):
                    recognized = recognized + 1

        for i in range(len(results_recognizer)-2):
            average_3.append(sum(results_recognizer[i:i+3])/len(results_recognizer[i:i+3]))
        for i in range(len(results_recognizer)-3):
            average_4.append(sum(results_recognizer[i:i+4])/len(results_recognizer[i:i+4]))
        for i in range(len(results_recognizer)-4):
            average_5.append(sum(results_recognizer[i:i+5])/len(results_recognizer[i:i+5]))

        for i in range(1, len(ages)):
            if len(ages_gap) != 0:
                if(ages[i]-ages[i-1] > max(ages_gap)):
                    age_before = ages[i-1]
                    age_after = ages[i]
            ages_gap.append(ages[i]-ages[i-1])
        
        results.loc[k] = [subject, ages, ages_gap, age_before, age_after, recognized, len(results_recognizer), average_3, average_4, average_5]
        k = k + 1
    name_csv = 'Analyser_' + recognizer +'.csv'
    path_csv = PATH_DIRECTORY_WRITE / name_csv
    results.to_csv(path_csv)


# Another CSV, but with informations more general

COLUMNS = ['Recognition Model', 'Average Reconition', 'Average GAP']
results = pandas.DataFrame(columns=COLUMNS)

gaps = []
csv_file = pandas.read_csv(path_csv)
for i in range(len(csv_file)):
    data = [int(item) for item in csv_file[COLUMNS_WRITE[2]][i][csv_file[COLUMNS_WRITE[2]][i].index('[') + 1:csv_file[COLUMNS_WRITE[2]][i].index(']')].strip().split(", ")]
    gaps.append(max(data))

k = 0
for file in files_write:
    reconitions = []
    name_file = str(file)
    model = name_file[name_file.index('_')+1:-4]
    csv_file = pandas.read_csv(file)
    for i in range(len(csv_file)):
        reconitions.append(csv_file[COLUMNS_WRITE[5]][i])
    results.loc[k] = [model, sum(reconitions)/len(reconitions), sum(gaps)/len(gaps)]
    k = k + 1

name_csv = 'Final.csv'
path_csv = PATH_DIRECTORY_WRITE / name_csv
results.to_csv(path_csv)