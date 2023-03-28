"""
    This script creates the image bank that will be used for Tests.
"""

import os
from pathlib import Path
import random
import shutil

if __name__ == "__main__":
    option_test = input('Para qual teste será criado o Banco de Imagens? \n 1. Teste 1 \n 2. Teste 2 \n 3. Teste 3 \n>>')
    
    if(option_test == '1'):
        PATH_DIRECTORY_BD = Path().absolute() / 'C2FPW'
        files = os.listdir(PATH_DIRECTORY_BD)
        NEW_BD_PATH = Path().absolute() / 'Test-1/BD'
    elif(option_test == '2'):
        PATH_DIRECTORY_BD = Path().absolute() / 'C2FPW'
        files = os.listdir(PATH_DIRECTORY_BD)
        NEW_BD_PATH = Path().absolute() / 'Test-2/BD'
    elif(option_test == '3'):
        PATH_DIRECTORY_BD = Path().absolute() / 'FGNET'
        files = os.listdir(PATH_DIRECTORY_BD)
        NEW_BD_PATH = Path().absolute() / 'Test-3/BD-FGNET'
    else:
        print('Opção inválida.')
        exit()

    if(NEW_BD_PATH.exists()):
        shutil.rmtree(NEW_BD_PATH)
    os.mkdir(NEW_BD_PATH)

    files.sort()

    option_dataset = input('\nComo criar o banco de imagens? \n 1. Pelas extremidades (Professor) \n 2. Aleatoriamente (Liz) \n>>')
    if(option_dataset == '1'):
        if(option_test == '1' or option_test == '3'):
            print('\nCriando o dataset com todos os sujeitos, sendo necessário sortear depois quais serão usados para resultado.')
            n_images = int(input('\nNúmero de imagens por sujeito (É esperado um valor par): '))
            selected = []
            if(option_test == '1'):
                rejected_subjects = []
            else:
                rejected_subjects = ['064A', '050A']
            for file in files:
                if(file[0:4] not in selected and file[0:4] not in rejected_subjects and file != '.gitignore'):
                    selected.append(file[0:4])
            selected.sort()
            for select in selected:
                images, random_1, random_2 = [], [], []
                for file in files:
                    if(file[0:4] == select):
                        images.append(file)
                for i in range(int(n_images/2)):
                    shutil.copy(PATH_DIRECTORY_BD / images[i], NEW_BD_PATH)
                    shutil.copy(PATH_DIRECTORY_BD / images[-(i+1)], NEW_BD_PATH)

        else:
            print('\nNão é preciso selecionar sujeitos para esse teste. Pegando todos os sujeitos.')
            selected = []
            for file in files:
                if(file[0:4] not in selected and file != '.gitignore'):
                    selected.append(file[0:4])
            selected.sort()
            for select in selected:
                images, random_1, random_2 = [], [], []
                for file in files:
                    if(file[0:4] == select):
                        images.append(file)
                for i in range(len(images)):
                    shutil.copy(PATH_DIRECTORY_BD / images[i], NEW_BD_PATH)
            

    elif(option_dataset == '2'):
        if(option_test == '1' or option_test == '3'):
            if(option_test == '1'):
                rejected_subjects = []
            else:
                rejected_subjects = ['064A', '050A']

            subjects = []
            n_subjects = int(input('\nNúmero de sujeitos a serem selecionados: '))
            n_images = int(input('\nNúmero de imagens por sujeito (É esperado um valor par): '))
            for file in files:
                if(file[0:4] not in subjects and file[0:4] not in rejected_subjects and file != '.gitignore'):
                    subjects.append(file[0:4])
            # randomly selects the desired amount among the available subjects
            subjects.sort()
            print('Sujeitos disponíveis: ', subjects)
            random.seed()
            selected = random.sample(subjects, k=n_subjects)
            print('Sujeitos escolhidos: ', selected)
        else:
            print('\nComo o teste 2 é realizado em todo o sujeitos, o banco de imagens será criado com todos.')
            selected = []
            for file in files:
                if(file[0:4] not in selected and file != '.gitignore'):
                    selected.append(file[0:4])
            selected.sort()
            for select in selected:
                images, random_1, random_2 = [], [], []
                for file in files:
                    if(file[0:4] == select):
                        images.append(file)
                for i in range(len(images)):
                    shutil.copy(PATH_DIRECTORY_BD / images[i], NEW_BD_PATH)
            exit()

        for select in selected:
            images, random_1, random_2 = [], [], []
            for file in files:
                if(file[0:4] == select):
                    images.append(file)
            # Take the first and last (extremes)
            shutil.copy(PATH_DIRECTORY_BD / images[0], NEW_BD_PATH)
            shutil.copy(PATH_DIRECTORY_BD / images[-1], NEW_BD_PATH)

            random_1 = random.sample(images[1:int(len(images)/2)], k=int((n_images-2)/2))
            for i in random_1:
                shutil.copy(PATH_DIRECTORY_BD / i, NEW_BD_PATH)

            random_2 = random.sample(images[int(len(images)/2):-1], k=int((n_images-2)/2))
            for i in random_2:
                shutil.copy(PATH_DIRECTORY_BD / i, NEW_BD_PATH)

    else:
        print('Opção inválida.')
        exit()
