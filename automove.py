import os
import time
check_time = 5
check_folder = 'C:\\Users\\HASSANIN\\Desktop\\clear'
receiver = 'C:\\Users\\hassanin\\Desktop\\receiver\\'
while True:
    unwanted = os.listdir(check_folder)
    if unwanted:
        for file in unwanted:

            name = os.path.join(check_folder, file)
            os.rename(name, receiver + file)
    time.sleep(check_time)
