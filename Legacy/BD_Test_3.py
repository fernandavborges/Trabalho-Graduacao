"""
    This script creates the image bank that will be used for Test 3.
"""

import os
from pathlib import Path
import shutil
import random

PATH_DIRECTORY_BD = Path().absolute().parents[0] / 'FGNET'
files = os.listdir(PATH_DIRECTORY_BD)

NEW_BD_PATH = Path().absolute() / 'BD-FGNET'

if(NEW_BD_PATH.exists()):
    shutil.rmtree(NEW_BD_PATH)
os.mkdir(NEW_BD_PATH)

if __name__ == "__main__":
    option = input('How to create the dataset: \n 1. Extremities (Teacher) \n 2. Random (Liz) \n')
    rejected_subjects = ['064', '050']
    subjects = []
    n_images = int(input('Number of images per subject(An even number is expected): '))

    for file in files:
        if(file[0:4] not in subjects and file[0:4] not in rejected_subjects and file != '.gitignore'):
            subjects.append(file[0:4])


    subjects.sort()
    print('Subjects selected: ', subjects)

    if(option == '2'):
        random.seed()
        # Randomly selecting the images after taking the extremes, and taking care to take the same amount in the first half of the photos as in the second
        for select in subjects:
            images, random_1, random_2 = [], [], []
            for file in files:
                if(file[0:4] == select):
                    images.append(file)
            # Take the first and last (extremes)
            shutil.copy(PATH_DIRECTORY_BD / images[0], NEW_BD_PATH)
            shutil.copy(PATH_DIRECTORY_BD / images[-1], NEW_BD_PATH)

            random_1 = random.choices(images[1:int(len(images)/2)], k=int((n_images-2)/2))
            for i in random_1:
                shutil.copy(PATH_DIRECTORY_BD / i, NEW_BD_PATH)

            random_2 = random.choices(images[int(len(images)/2):-1], k=int((n_images-2)/2))
            for i in random_2:
                shutil.copy(PATH_DIRECTORY_BD / i, NEW_BD_PATH)

    elif(option == '1'):
        # Selecting images by extremes
        for select in subjects:
            images, random_1, random_2 = [], [], []
            for file in files:
                if(file[0:4] == select):
                    images.append(file)

            for i in range(int(n_images/2)):
                
                shutil.copy(PATH_DIRECTORY_BD / images[i], NEW_BD_PATH)
                shutil.copy(PATH_DIRECTORY_BD / images[-(i+1)], NEW_BD_PATH)
    else:
        print('Invalid chosen option.')
        exit()