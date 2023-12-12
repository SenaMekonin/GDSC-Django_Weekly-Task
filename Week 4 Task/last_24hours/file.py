import os
import shutil
from datetime import datetime, timedelta
def files_list(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
# Check is modified or created in last 24 hours
def modified_or_created(file_path):
    mc_time = datetime.now() - timedelta(hours=24)
    data = os.stat(file_path)
    return datetime.fromtimestamp(data.st_mtime) >= mc_time or datetime.fromtimestamp(data.st_ctime) >= mc_time
# Update file
def upd_file(file_path):
    with open(file_path, 'a') as file:
        file.write('\n Updated at:' + str(datetime.now()))
# Create folder
def new_folder():
    folder_name = "last_24hours"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name
# Move file to last_24hours
def move_file(file_path, des_folder):
    shutil.move(file_path, os.path.join(des_folder, os.path.basename(file_path)))

def main():
    current_directory = os.getcwd()
    last_24hours_folder = new_folder()

    files_to_update = [file for file in files_list(current_directory) if modified_or_created(file)]

    for file_path in files_to_update:
        upd_file(file_path)
        move_file(file_path, last_24hours_folder)
if __name__ == "__main__":
    main()

