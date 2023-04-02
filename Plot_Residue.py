from pathlib import Path
import pandas
import numpy as np
import matplotlib.pyplot as plt
import os
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

COLUMNS = ['Subject', 'Recognition Model', 'Results', 'Residue', 'Absolute Residue']
PATH_RESIDUES = Path().absolute() / 'Results-Residue/'

if __name__ == "__main__":


    if PATH_RESIDUES.exists():
        print('Resultados de resíduos disponíveis para plotar:')
        files_read = PATH_RESIDUES.glob('*.csv')
        for path in files_read:
            if str(path).find('Residue-')!=-1:
                path_str = str(path)
                print('-', path_str[path_str.index('Residue-')+len('Residue-'):-4], '\n')
        option_folder = input('Qual a pasta de resultados será analisada?(ex: Test2-Test1A): ')
        name_file = 'Results-Residue/Residue-' + option_folder + '.csv'
        FILE_READ = Path().absolute() / name_file
    else:
        print('Nenhum resultado de resíduos gerado para plotar.')
    
    if(not FILE_READ.exists()):
        print('Arquivo de resultado não existe.')
        exit()
    else:
        os.mkdir(PATH_RESIDUES / option_folder)
        PATH_RESULTS = PATH_RESIDUES / option_folder

    csv_file = pandas.read_csv(FILE_READ)
    if(len(csv_file) != 0):
        for model in models_recognition:
            residues = []
            abs_residues = []
            for i in range(len(csv_file)):
                if(csv_file[COLUMNS[1]][i] == model):
                    residues.append(csv_file[COLUMNS[3]][i]) 
                    abs_residues.append(csv_file[COLUMNS[4]][i])       
            plt.figure(figsize=(20,15))
            plt.rcParams.update({'font.size': 15})
            plt.rcParams['xtick.labelsize'] = 15
            plt.rcParams['ytick.labelsize'] = 15
            plt.title('Histograma - ' + name_file[name_file.index('Residue-'):-4] +'. Modelo: ' + model)
            plt.xlabel('Resíduo')
            plt.ylabel("Frequência")
            plt.hist(residues, 10, rwidth=0.9)
            name_fig = name_file[name_file.index('Residue-'):-4] + '-' + model
            name_plot = PATH_RESULTS / name_fig
            plt.savefig(name_plot)
            plt.clf()
            plt.title('Histograma - ' + name_file[name_file.index('Residue-'):-4] +'. Modelo: ' + model + '- Absoluto')
            plt.hist(abs_residues, 10, rwidth=0.9)
            name_fig = name_file[name_file.index('Residue-'):-4] + '-' + model + '-Absolute'
            name_plot = PATH_RESULTS / name_fig
            plt.savefig(name_plot)





