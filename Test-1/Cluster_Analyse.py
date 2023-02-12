from pathlib import Path
import pandas
import numpy as np


COLUMNS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)']
PATH_DIRECTORY_READ= Path().absolute() / 'Results/Analyser/'
files_read = PATH_DIRECTORY_READ.glob('Analyser_*.csv')

PATH_DIRECTORY_WRITE= Path().absolute() / 'Results/Clusters/'


for file in files_read:
    cluster_1 = pandas.DataFrame(columns=COLUMNS)
    cluster_2 = pandas.DataFrame(columns=COLUMNS)
    cluster_3 = pandas.DataFrame(columns=COLUMNS)
    cluster_4 = pandas.DataFrame(columns=COLUMNS)

    csv_file = pandas.read_csv(file)

    for i in range(len(csv_file)):
        data = [int(item) for item in csv_file[COLUMNS[2]][i][csv_file[COLUMNS[2]][i].index('[') + 1:csv_file[COLUMNS[2]][i].index(']')].strip().split(", ")]
        line = [csv_file[COLUMNS[0]][i], csv_file[COLUMNS[1]][i], csv_file[COLUMNS[2]][i], csv_file[COLUMNS[3]][i], csv_file[COLUMNS[4]][i], csv_file[COLUMNS[5]][i], csv_file[COLUMNS[6]][i], csv_file[COLUMNS[7]][i], csv_file[COLUMNS[8]][i], csv_file[COLUMNS[9]][i], csv_file[COLUMNS[10]][i], csv_file[COLUMNS[11]][i], csv_file[COLUMNS[12]][i]]
        if(max(data) <= 15):
            cluster_1.loc[len(cluster_1)] = line
        elif(max(data) <= 30):
            cluster_2.loc[len(cluster_2)] = line
        elif(max(data) <= 45):
            cluster_3.loc[len(cluster_3)] = line
        else:
            cluster_4.loc[len(cluster_4)] = line
    name_file = str(file)
    model = name_file[name_file.index('_')+1:-4]
    name_csv_1 = 'Cluster_00_15_' + model + '.csv'
    cluster_1.to_csv(PATH_DIRECTORY_WRITE / name_csv_1)
    name_csv_2 = 'Cluster_16_30_' + model + '.csv'
    cluster_2.to_csv(PATH_DIRECTORY_WRITE / name_csv_2)
    name_csv_3 = 'Cluster_31_45_' + model + '.csv'
    cluster_3.to_csv(PATH_DIRECTORY_WRITE / name_csv_3)
    name_csv_4 = 'Cluster_46_--_' + model + '.csv'
    cluster_4.to_csv(PATH_DIRECTORY_WRITE / name_csv_4)