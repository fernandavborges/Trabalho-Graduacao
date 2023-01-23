"""

Script created to download the images from the Data Bases used for the Google Drive TG.

References:     https://www.youtube.com/playlist?list=PL3JVwFmb_BnTamTxXbmlwpspYdpmaHdbz
                https://developers.google.com/drive/api/guides/about-sdk

"""

import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
import pandas as pd

""" Google Drive API configurations """
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

""" Creating Client-Server Service with Google Drive """
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

""" Searches all files present from the specified Google Drive folder (Image Bank) """
folder_ids = [
'1pfuNPjkNEbRWSRGXzqBP_x-iuEg-Af5e', # Our Data Base
'1WlI7VQJxZdINqDXuQNuB3OCxVyu1_U_d', # FGNET Data Base
'1UlVtszFNNaF4ZpMJAFKldKQu3hbxbQH5', # HDA-PlasticSurgery - Eyebrow Data Base
'1k2B6O2ILA48pPDHJMK-Qf5bSDHqq8Yuy', # HDA-PlasticSurgery - Eyelid Data Base
'1rhs-haPL7vDHs2T-0liRTjCSXIRFJ8-v', # HDA-PlasticSurgery - Facelift Data Base
'1nXRbxeuEn6SKskWcxiApeO8PbSteCYfr', # HDA-PlasticSurgery - FacialBones Data Base
'15bs8YYF6MvK2VvCsa10Zo_UhLYJl-bcW' # HDA-PlasticSurgery - Nose Data Base
]
    
names_folder = [
'../Banco-de-Imagens',
'../FGNET',
'../HDA-PlasticSurgery/Eyebrow',
'../HDA-PlasticSurgery/Eyelid',
'../HDA-PlasticSurgery/Facelift',
'../HDA-PlasticSurgery/FacialBones',
'../HDA-PlasticSurgery/Nose'
]    

""" Create folder if not exist """
for folder in names_folder:
    if not os.path.exists(folder):
        os.makedirs(folder)

for folder_id, name_folder in zip(folder_ids, names_folder):

    query = f"parents = '{folder_id}'"

    response = service.files().list(q=query).execute()
    files = response.get('files')

    """ Checks by going through the folders which files are in the folder """
    nextPageToken = response.get('nextPageToken')
    while nextPageToken:
        response = service.files().list(q=query, pageToken=nextPageToken).execute()
        files.extend(response.get('files'))
        nextPageToken = response.get('nextPageToken')

    """ Transforms 'files' into a DataFrame to help with organization and visualization"""
    df = pd.DataFrame(files)

    """ Collects necessary information from 'files' to download files: ids and name """
    ids = df['id'].values.astype('str') 
    names = df['name'].values.astype('str') 

    """ Download the images and save them in the folder. 
        Obs: Remember to change the name of the folder where the database is to be saved. """
    for file_id, file_name in zip(ids, names):
        request = service.files().get_media(fileId=file_id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)

        done = False
        """ Download """
        while not done:
            status, done = downloader.next_chunk()
            #print('Downloader progress {0}'.format(status.progress()*100))
        fh.seek(0)

        """ Save """
        with open(os.path.join(name_folder, file_name), 'wb') as f:
            f.write(fh.read())
            f.close()
