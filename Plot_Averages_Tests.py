from pathlib import Path
import pandas
import numpy as np
import matplotlib.pyplot as plt
import shutil
import os

thresholds = {
    'VGG-Face':0.4, 
    'Facenet':0.4, 
    'Facenet512':0.3, 
    'OpenFace':0.1, 
    'DeepFace':0.23, 
    'DeepID':0.015, 
    'ArcFace':0.68, 
    'Dlib':0.7, 
    'SFace':0.5932763306134152
}

COLUMNS = ['Subject', 'Ages', 'Ages GAP', 'Age Before GAP', 'Age After GAP', 'Recognized', 'Total Comparisons', 'Average (3)', 'Difference Average (3)', 'Average (4)', 'Difference Average (4)', 'Average (5)', 'Difference Average (5)']

if __name__ == "__main__":

    option_test = input('Em qual teste será realizado o plot de médias? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n>>')

    if(option_test == '1'):
        path_tests = Path().absolute() / 'Test-1/Results/'
        print('Pasta de resultados disoníveis no Test-1:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Analyser')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Analyser-')+len('Analyser-'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (É preciso que esteja gerado a pasta de Analyser desses resultados)(ex: Test1A): ')
        name_folder_read = 'Test-1/Results/Analyser-' + option_folder
        PATH_DIRECTORY_READ = Path().absolute() / name_folder_read
        name_folder_write = 'Test-1/Results/Images-' + option_folder
    elif(option_test == '2'):
        path_tests = Path().absolute() / 'Test-2/Results/'
        print('Pasta de resultados disoníveis no Test-2:')
        for path in path_tests.iterdir():
             if path.is_dir() and (str(path).find('Results\Analyser')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Analyser-')+len('Analyser-'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (É preciso que esteja gerado a pasta de Analyser desses resultados)(ex: Test1A): ')
        name_folder_read = 'Test-2/Results/Analyser-' + option_folder
        PATH_DIRECTORY_READ = Path().absolute() / name_folder_read
        name_folder_write = 'Test-2/Results/Images-' + option_folder
    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        print('Pasta de resultados disoníveis no Test-3:')
        for path in path_tests.iterdir():
             if path.is_dir() and (str(path).find('Results\Analyser')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('Analyser-')+len('Analyser-'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (É preciso que esteja gerado a pasta de Analyser desses resultados)(ex: Test1A): ')
        name_folder_read = 'Test-3/Results/Analyser-' + option_folder
        PATH_DIRECTORY_READ = Path().absolute() / name_folder_read
        name_folder_write = 'Test-3/Results/Images-' + option_folder
    else:
        print('Opçao inválida.')
        exit()

    if(PATH_DIRECTORY_READ.exists()):
        files = PATH_DIRECTORY_READ.glob('Analyser_*.csv')
    else:
        print('Pasta de resultado analyser não existe.')
        exit()

    PATH_DIRECTORY_M3 = Path().absolute() / (name_folder_write + '-M3')
    PATH_DIRECTORY_M4 = Path().absolute() / (name_folder_write + '-M4')
    PATH_DIRECTORY_M5 = Path().absolute() / (name_folder_write + '-M5') 
    if(PATH_DIRECTORY_M3.exists()):
        shutil.rmtree(PATH_DIRECTORY_M3)
    if(PATH_DIRECTORY_M4.exists()):
        shutil.rmtree(PATH_DIRECTORY_M4)
    if(PATH_DIRECTORY_M5.exists()):
        shutil.rmtree(PATH_DIRECTORY_M5)
    os.mkdir(PATH_DIRECTORY_M3)
    os.mkdir(PATH_DIRECTORY_M4)
    os.mkdir(PATH_DIRECTORY_M5)


    for file in files:
        csv_file = pandas.read_csv(file)
        plt.figure()
        file_name = str(file)
        name_model = file_name[file_name.index('Analyser_')+len('Analyser_'):file_name.index('.csv')]
        for i in range(len(csv_file)):
            subject = str(csv_file['Subject'][i])
            average_m3 = [float(item) for item in csv_file[COLUMNS[7]][i][csv_file[COLUMNS[7]][i].index('[') + 1:csv_file[COLUMNS[7]][i].index(']')].strip().split(",")]
            average_m3[:] = [x*100 / thresholds[name_model] for x in average_m3]
            average_m4 = [float(item) for item in csv_file[COLUMNS[9]][i][csv_file[COLUMNS[9]][i].index('[') + 1:csv_file[COLUMNS[9]][i].index(']')].strip().split(",")]
            average_m4[:] = [x*100 / thresholds[name_model] for x in average_m4]
            average_m5 = [float(item) for item in csv_file[COLUMNS[11]][i][csv_file[COLUMNS[11]][i].index('[') + 1:csv_file[COLUMNS[11]][i].index(']')].strip().split(",")]
            average_m5[:] = [x*100 / thresholds[name_model] for x in average_m5]
            # Average 3
            plt.title("Sujeito: "+ subject + ". Modelo: " + name_model + ".\nMédia de 3.")
            plt.xlabel("Média nº")
            plt.ylabel("Distâncias (% do Threshold)")
            plt.bar(range(len(average_m3)), average_m3)
            plt.plot([0, len(average_m3)-1], [100, 100], "-", color='b', label='Limite')
            name_plot = str(PATH_DIRECTORY_M3) +  '/' + subject + '-' + name_model
            plt.savefig(name_plot)
            plt.close()
            # Average 4
            plt.title("Sujeito: "+ subject + ". Modelo: " + name_model + ".\nMédia de 4.")
            plt.xlabel("Média nº")
            plt.ylabel("Distâncias (% do Threshold)")
            plt.bar(range(len(average_m4)), average_m4)
            plt.plot([0, len(average_m4)-1], [100, 100], "-", color='b', label='Limite')
            name_plot = str(PATH_DIRECTORY_M4) +  '/' + subject + '-' + name_model
            plt.savefig(name_plot)
            plt.close()
            # Average 5
            plt.title("Sujeito: "+ subject + ". Modelo: " + name_model + ".\nMédia de 5.")
            plt.xlabel("Média nº")
            plt.ylabel("Distâncias (% do Threshold)")
            plt.bar(range(len(average_m5)), average_m5)
            plt.plot([0, len(average_m5)-1], [100, 100], "-", color='b', label='Limite')
            name_plot = str(PATH_DIRECTORY_M5) +  '/' + subject + '-' + name_model
            plt.savefig(name_plot)
            plt.close()


    