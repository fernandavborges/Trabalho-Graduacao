from pathlib import Path
import pandas

PATH = Path().absolute() / 'Results/CSVs/'

COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
files_read_1 = PATH.glob('*.csv')

PATH_READ = Path().absolute() / 'Results/CSVs-SFace/'

files_read_2 = PATH_READ.glob('*.csv')

for file in zip(files_read_1, files_read_2):
    print(file)
    csv_file_1 = pandas.read_csv(file[0])
    csv_file_2 = pandas.read_csv(file[1])
    csv_file_1.drop(["Unnamed: 0"], axis=1, inplace=True)
    csv_file_2.drop(["Unnamed: 0"], axis=1, inplace=True)
    print(len(csv_file_1.axes[1]))
    print(len(csv_file_2.axes[1]))
    for i in range(len(csv_file_2)):
        line = [csv_file_2[COLUMNS[0]][i], csv_file_2[COLUMNS[1]][i], csv_file_2[COLUMNS[2]][i], csv_file_2[COLUMNS[3]][i], csv_file_2[COLUMNS[4]][i], csv_file_2[COLUMNS[5]][i], csv_file_2[COLUMNS[6]][i], csv_file_2[COLUMNS[7]][i], csv_file_2[COLUMNS[8]][i]]
        print(len(line))
        csv_file_1.loc[len(csv_file_1)] = line
    
    csv_file_1.to_csv(file[0])

