from pathlib import Path
import pandas
import numpy as np
import matplotlib.pyplot as plt


COLUMNS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)']

PATH_DIRECTORY = Path().absolute() / 'Results/Clusters/'

files_read = PATH_DIRECTORY.glob('*.csv')

for file in files_read:
    name_file = str(file)
    csv_file = pandas.read_csv(file)
    if(len(csv_file) != 0):
        figure, axs = plt.subplots(3, 1, sharex=False, sharey=False)
        if(len(csv_file) < 10): 
            figure.set_figwidth(10)
            figure.set_figheight(25)
        elif(len(csv_file) < 20): 
            figure.set_figwidth(25)
            figure.set_figheight(30)
        else:
            figure.set_figwidth(35)
            figure.set_figheight(40)
        axs[0].set_title(name_file[name_file.index('Cluster_'):-4] + ' - Average 3')
        axs[1].set_title(name_file[name_file.index('Cluster_'):-4] + ' - Average 4')
        axs[2].set_title(name_file[name_file.index('Cluster_'):-4] + ' - Average 5')
        axs[2].set_xlabel('Média nº')
        axs[0].set_ylabel("Distâncias")
        axs[1].set_ylabel("Distâncias")
        axs[2].set_ylabel("Distâncias")

        for i in range(len(csv_file)):
            subject = csv_file[COLUMNS[0]][i]
            average_3 = [float(item) for item in csv_file[COLUMNS[7]][i][csv_file[COLUMNS[7]][i].index('[') + 1:csv_file[COLUMNS[7]][i].index(']')].strip().split(", ")]
            average_4 = [float(item) for item in csv_file[COLUMNS[9]][i][csv_file[COLUMNS[9]][i].index('[') + 1:csv_file[COLUMNS[9]][i].index(']')].strip().split(", ")]
            average_5 = [float(item) for item in csv_file[COLUMNS[11]][i][csv_file[COLUMNS[11]][i].index('[') + 1:csv_file[COLUMNS[11]][i].index(']')].strip().split(", ")]

            axs[0].plot(range(len(average_3)), average_3, label=subject)
            axs[1].plot(range(len(average_4)), average_4, label=subject)
            axs[2].plot(range(len(average_5)), average_5, label=subject)
        
        axs[0].legend()
        axs[1].legend()
        axs[2].legend()

        name_fig = name_file[name_file.index('Cluster'):-4]
        name_plot = PATH_DIRECTORY.parent /name_fig
        figure.savefig(name_plot)
        figure.clear()



