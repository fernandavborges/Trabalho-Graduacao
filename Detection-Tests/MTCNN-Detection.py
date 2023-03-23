from deepface import DeepFace
import os
import shutil
import matplotlib.pyplot as plt
from pathlib import Path
import cv2

PATH_RESULTS = Path().absolute() / 'Results-MTCNN'
if(PATH_RESULTS.exists()):
    shutil.rmtree(PATH_RESULTS)
os.mkdir(PATH_RESULTS)

folder = '../C2FPW/'
images = os.listdir(folder)
for image in images:  
    if(image[0] == 'S'):
        print('mtcnn' + ': Image ' + image)
        try:
            face = DeepFace.detectFace(img_path = '../C2FPW/' + image, detector_backend = 'mtcnn')
            path = str(PATH_RESULTS / image)
            plt.imshow(face)
            plt.imsave(path, face)
            plt.close()
        except Exception as exception:
            print('Detection failure.')
            print('Exception: ' + str(exception)+'\n')