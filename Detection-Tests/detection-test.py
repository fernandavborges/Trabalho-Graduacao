from deepface import DeepFace
import os
import matplotlib.pyplot as plt

detection_models = [
  #'opencv', 
  #'ssd', 
  #'dlib', 
  'mtcnn'
  #'retinaface', 
  #'mediapipe'
]

folder = '../Banco-de-Imagens/'
images = os.listdir(folder)
log_file = open("Logs/detection_failures.txt", "w")
for i in detection_models:
    images_failure = []
    for image in images:  
        if(image[0] == 'S'):
            print(i + ': Image ' + image)
            try:
                face = DeepFace.detectFace(img_path = '../Banco-de-Imagens/' + image, detector_backend = i)
            except Exception as exception:
                print('Detection failure.')
                print('Exception: ' + str(exception)+'\n')
                images_failure.append(image)

    log_file.write('Images not detected with detection model - ' + i)
    log_file.write('\n')
    for im in images_failure:
        log_file.write(im)
        log_file.write('\n')
    log_file.write('\n')

log_file.close()