import os
import sys
import shutil

from logger import logging
from exception import CustomException

path_ext = os.path.expanduser('~')
downloads_path = os.path.join(path_ext, 'Downloads')

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx', '.csv'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
}

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.info('Creating folder')


def organize_files():
    try:
        for filename in os.listdir(downloads_path):
            file_path = os.path.join(downloads_path, filename)

            if os.path.isdir(file_path):
                continue

            _, file_ext = os.path.splitext(filename)

            for category, extensions in file_categories.items():
                if file_ext.lower() in extensions:
                    destination_folder = os.path.join(downloads_path, category)
                    create_folder_if_not_exists(destination_folder)

                    new_file_path = os.path.join(destination_folder, filename)
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