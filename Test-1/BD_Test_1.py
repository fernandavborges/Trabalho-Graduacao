"""
    This script creates the image bank that will be used for Test 1.
"""

import os
from pathlib import Path
import random
import shutil

PATH_DIRECTORY_BD = Path().absolute().parents[0] / 'Banco-de-Imagens'
files = os.listdir(PATH_DIRECTORY_BD)

NEW_BD_PATH = Path().absolute() / 'BD'

# Subjects who did not admit the plastic and not even a specialist attested about
rejected_subjects = ['S077', 'S082']
subjects = []
n_subjects = 81 # final number of individuals to be selected
n_images = 10 # number of images per individual

for file in files:
    if(file[0:4] not in subjects and file[0:4] not in rejected_subjects):
        subjects.append(file[0:4])

# randomly selects the desired amount among the available subjects
subjects.sort()
print('Subjects available: ', subjects)
random.seed()
selected = random.sample(subjects, k=n_subjects)
print('Subjects selected: ', selected)

# Randomly selecting the images after taking the extremes, and taking care to take the same amount in the first half of the photos as in the second
# for select in selected:
#     images, random_1, random_2 = [], [], []
#     for file in files:
#         if(file[0:4] == select):
#             images.append(file)
#     # Take the first and last (extremes)
#     shutil.copy(PATH_DIRECTORY_BD / images[0], NEW_BD_PATH)
#     shutil.copy(PATH_DIRECTORY_BD / images[-1], NEW_BD_PATH)

#     random_1 = random.sample(images[1:int(len(images)/2)], k=int((n_images-2)/2))
#     for i in random_1:
#         shutil.copy(PATH_DIRECTORY_BD / i, NEW_BD_PATH)

#     random_2 = random.sample(images[int(len(images)/2):-1], k=int((n_images-2)/2))
#     for i in random_2:
#         shutil.copy(PATH_DIRECTORY_BD / i, NEW_BD_PATH)

# Selecting images by extremes
for select in selected:
    images, random_1, random_2 = [], [], []
    for file in files:
        if(file[0:4] == select):
            images.append(file)

    for i in range(int(n_images/2)):
        shutil.copy(PATH_DIRECTORY_BD / images[i], NEW_BD_PATH)
        shutil.copy(PATH_DIRECTORY_BD / images[-(i+1)], NEW_BD_PATH)