import matplotlib.pyplot as plt
from pathlib import Path
import pandas
import shutil
import os

thresholds = [
    0.4,
    0.4,
    0.3,
    0.1,
    0.23,
    0.015,
    0.68,
    0.07,
    0.5932763306134152
]

if __name__ == "__main__":

    option_test = input('Para qual teste será realizado o plot? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n>>')

    if(option_test == '1'):
        path_tests = Path().absolute() / 'Test-1/Results/'
        print('Pasta de resultados disponíveis no Test-1:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder = 'Test-1/Results/' + option_folder
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-1/Results/' + 'Images-' + option_folder + '-ByAge'
    elif(option_test == '2'):
        path_tests = Path().absolute() / 'Test-2/Results/'
        print('Pasta de resultados disponíveis no Test-2:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder = 'Test-2/Results/' + option_folder
        COLUMNS = ['Image 1', 'Year 1', 'Image 2', 'Year 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-2/Results/' + 'Images-' + option_folder + '-ByAge'
    elif(option_test == '3'):
        path_tests = Path().absolute() / 'Test-3/Results/'
        print('Pasta de resultados disponíveis no Test-3:')
        for path in path_tests.iterdir():
            if path.is_dir() and (str(path).find('Results\Test')!=-1):
                path_str = str(path)
                print('-', path_str[path_str.index('\Results')+len('\Results/'):], '\n')
        option_folder = input('Qual a pasta de resultados será analisada? (ex: Test1A): ')
        name_folder = 'Test-3/Results/' + option_folder
        COLUMNS = ['Image 1', 'Age 1', 'Image 2', 'Age 2', 'Distance Metric', 'Detection Model', 'Recognition Model', 'Distance Result', 'Recognition Result']
        name_folder_write = 'Test-3/Results/' + 'Images-' + option_folder + '-ByAge'
    else:
        print('Opçao inválida.')
        exit()
        
    PATH_DIRECTORY = Path().absolute() / name_folder
    PATH_DIRECTORY_WRITE = Path().absolute() / name_folder_write

    if(PATH_DIRECTORY.exists()):
        files = PATH_DIRECTORY.glob('*.csv')
    else:
        print('Pasta de resultado não existe.')
        exit()
    
    if(PATH_DIRECTORY_WRITE.exists()):
        shutil.rmtree(PATH_DIRECTORY_WRITE)
    os.mkdir(PATH_DIRECTORY_WRITE)

    fig_VGG, axs_VGG = plt.subplots()
    fig_Facenet, axs_Facenet = plt.subplots()
    fig_Facenet512, axs_Facenet512 = plt.subplots()
    fig_OpenFace, axs_OpenFace = plt.subplots()
    fig_DeepFace, axs_DeepFace = plt.subplots()
    fig_DeepID, axs_DeepID = plt.subplots()
    fig_ArcFace, axs_ArcFace = plt.subplots()
    fig_Dlib, axs_Dlib = plt.subplots()
    fig_SFace, axs_SFace = plt.subplots()

    axs_VGG.set_title('Resultados - VGG-Face')
    axs_Facenet.set_title('Resultados - Facenet')
    axs_Facenet512.set_title('Resultados - Facenet512')
    axs_OpenFace.set_title('Resultados - OpenFace')
    axs_DeepFace.set_title('Resultados - DeepFace')
    axs_DeepID.set_title('Resultados - DeepID')
    axs_ArcFace.set_title('Resultados - ArcFace')
    axs_Dlib.set_title('Resultados - Dlib')
    axs_SFace.set_title('Resultados - SFace')

    axs_VGG.set_xlabel('Idade')
    axs_VGG.set_ylabel('Distância')
    axs_Facenet.set_xlabel('Idade')
    axs_Facenet.set_ylabel('Distancia')
    axs_Facenet512.set_xlabel('Idade')
    axs_Facenet512.set_ylabel('Distância')
    axs_OpenFace.set_xlabel('Idade')
    axs_OpenFace.set_ylabel('Distância')
    axs_DeepFace.set_xlabel('Idade')
    axs_DeepFace.set_ylabel('Distância')
    axs_DeepID.set_xlabel('Idade')
    axs_DeepID.set_ylabel('Distância')
    axs_ArcFace.set_xlabel('Idade')
    axs_ArcFace.set_ylabel('Distância')
    axs_Dlib.set_xlabel('Idade')
    axs_Dlib.set_ylabel('Distância')
    axs_SFace.set_xlabel('Idade')
    axs_SFace.set_ylabel('Distância')

    fig_VGG.set_figwidth(35)
    fig_VGG.set_figheight(30)
    fig_Facenet.set_figwidth(35)
    fig_Facenet.set_figheight(30)
    fig_Facenet512.set_figwidth(35)
    fig_Facenet512.set_figheight(30)
    fig_OpenFace.set_figwidth(35)
    fig_OpenFace.set_figheight(30)
    fig_DeepFace.set_figwidth(35)
    fig_DeepFace.set_figheight(30)
    fig_DeepID.set_figwidth(35)
    fig_DeepID.set_figheight(30)
    fig_ArcFace.set_figwidth(35)
    fig_ArcFace.set_figheight(30)
    fig_Dlib.set_figwidth(35)
    fig_Dlib.set_figheight(30)
    fig_SFace.set_figwidth(35)
    fig_SFace.set_figheight(30)


    for file in files:
        plots = {
            "VGG-Face": [], 
            "Facenet": [], 
            "Facenet512": [], 
            "OpenFace": [], 
            "DeepFace": [], 
            "DeepID": [], 
            "ArcFace": [], 
            "Dlib": [], 
            "SFace": []
        }
        ages = {
            "VGG-Face": [], 
            "Facenet": [], 
            "Facenet512": [], 
            "OpenFace": [], 
            "DeepFace": [], 
            "DeepID": [], 
            "ArcFace": [], 
            "Dlib": [], 
            "SFace": []
        }
        csv_file = pandas.read_csv(file)
        for i in range(len(csv_file)):
            if(option_test == '1' or option_test == '2'):
                subject = csv_file[COLUMNS[0]][i][0:4]
                age = int(csv_file[COLUMNS[3]][i]) - int(csv_file[COLUMNS[0]][i][5:9])
            else:
                subject = csv_file[COLUMNS[0]][i][0:3]
                age = int(csv_file[COLUMNS[3]][i])

            plots[csv_file[COLUMNS[6]][i]].append(float(csv_file[COLUMNS[7]][i]))
            ages[csv_file[COLUMNS[6]][i]].append(age)
            
        axs_VGG.plot(ages['VGG-Face'], plots['VGG-Face'], label=subject)
        axs_Facenet.plot(ages['Facenet'], plots['Facenet'], label=subject)
        axs_Facenet512.plot(ages['Facenet512'], plots['Facenet512'], label=subject)
        axs_OpenFace.plot(ages['OpenFace'], plots['OpenFace'], label=subject)
        axs_DeepFace.plot(ages['DeepFace'], plots['DeepFace'], label=subject)
        axs_DeepID.plot(ages['DeepID'], plots['DeepID'], label=subject)
        axs_ArcFace.plot(ages['ArcFace'], plots['ArcFace'], label=subject)
        axs_Dlib.plot(ages['Dlib'], plots['Dlib'], label=subject)
        axs_SFace.plot(ages['SFace'], plots['SFace'], label=subject)

    axs_VGG.legend()
    axs_Facenet.legend()
    axs_Facenet512.legend()
    axs_OpenFace.legend()
    axs_DeepFace.legend()
    axs_DeepID.legend()
    axs_ArcFace.legend()
    axs_Dlib.legend()
    axs_SFace.legend()

    fig_VGG.savefig(PATH_DIRECTORY_WRITE/'VGG-Face')
    fig_Facenet.savefig(PATH_DIRECTORY_WRITE/'Facenet')
    fig_Facenet512.savefig(PATH_DIRECTORY_WRITE/'Facenet512')
    fig_OpenFace.savefig(PATH_DIRECTORY_WRITE/'OpenFace')
    fig_DeepFace.savefig(PATH_DIRECTORY_WRITE/'DeepFace')
    fig_DeepID.savefig(PATH_DIRECTORY_WRITE/'DeepID')
    fig_ArcFace.savefig(PATH_DIRECTORY_WRITE/'ArcFace')
    fig_Dlib.savefig(PATH_DIRECTORY_WRITE/'Dlib')
    fig_SFace.savefig(PATH_DIRECTORY_WRITE/'SFace')