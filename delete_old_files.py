import os
import time

def delete_files_in_directory(folder, delay):
    now=time.time()
    delay_seconds = delay*24*3600
    files=os.listdir(folder)
    for file in files:
        path=os.path.join(folder,file)
        if os.path.isfile(path):
            file_age=now-os.path.getmtime(path)
            if file_age> delay_seconds:
                os.remove(path)


folder_to_clean = "/home/mangeoire/Documents/programmes/Photo"
delay_in_days=1

delete_files_in_directory(folder_to_clean, delay_in_days)