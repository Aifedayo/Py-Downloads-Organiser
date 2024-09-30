import os
import shutil
import logging

path_ext = os.path.expanduser('~')
downloads_path = os.path.join(path_ext, 'Downloads')

file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
}