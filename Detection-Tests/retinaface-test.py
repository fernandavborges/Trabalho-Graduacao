"""
        Test with the RetinaFace face detector directly from the retinaface library.
"""

import os
from retinaface import RetinaFace

folder = '../C2FPW/'
images = os.listdir(folder)
log_file = open("Logs/retinaface_failures.txt", "w")
images_failures = []

for image in images: 
    print('Imagem ' + image)
    try:
        faces = RetinaFace.detect_faces('../C2FPW/' + image)
    except:
        images_failures.append(image)
        print('Detection Failures.')
log_file.write('Images not detected with detection model - RetinaFace')
log_file.write('\n')
for im in images_failures:
    log_file.write(im)
    log_file.write('\n')
log_file.write('\n')