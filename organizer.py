#!/usr/bin/env python # To be able to run with python3 regardless of where it is installed

import os
import sys
import shutil

from logger import logging
from exception import CustomException
from cron_job import run_cron_job


if len(sys.argv) != 2:
    print("Usage: python3 organizer.py <folder to organizer e.g Desktop>")
    sys.exit(1)


path_ext = os.path.expanduser('~')
folder_name = os.path.join(path_ext, sys.argv[1]) # Folder name to organize

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.csv', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Installer': ['.deb', '.rpm', '.AppImage', '.iso', '.vsix', '.xz'],
    'Website': ['.html', ],
    'Keys': ['.pem'],
    'Unnamed Folder': ['']
}

run_cron_job() # Call the cron job at the top

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.info('Creating folder')


def organize_files():
    try:
        for filename in os.listdir(folder_name):

            file_path = os.path.join(folder_name, filename) # Get the full path of the file

            if os.path.isdir(file_path):
                continue

            _, file_ext = os.path.splitext(filename)

            for category, extensions in file_categories.items():
                if file_ext in extensions:
                    destination_folder = os.path.join(folder_name, category)
                    create_folder_if_not_exists(destination_folder) # Create the folder using the category name if it doesn't exist

                    new_file_path = os.path.join(destination_folder, filename) # 
                    shutil.move(file_path, new_file_path)
                    logging.info(f'Moved {filename} to {category}')
                    break


    except Exception as e:
        logging.error(f'Error occurred while organizing files: {str(e)}')
        raise CustomException(str(e), sys)

if __name__ == '__main__':
    try:
        organize_files()
    except KeyboardInterrupt:
        logging.info('User interrupted the script')
