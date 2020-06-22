import os

upload_folder = 'opt/SGDF'
if os.path.isdir(upload_folder) == False:
    os.makedirs(upload_folder)
