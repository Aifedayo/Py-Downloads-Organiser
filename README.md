# Py-Files-Organiser

## Overview

Is your Files folder cluttered with files of all types—documents, images, videos, and more? Manually organizing them can be tedious and time-consuming. **Py-Files-Organiser** is a Python script designed to automatically sort and organize your files into categorized folders based on their file types.

This script runs daily at midnight using a cron job, keeping your folder tidy and well-organized without any manual effort.

## Features

- **Automatic Sorting**: Automatically organizes files into folders based on their extensions (e.g., `.pdf` files go to `Documents`, `.jpg` files go to `Images`, etc.).
- **Automatic Folder Creation**: Creates folders for new categories if they don’t already exist.
- **Customizable**: Extend the file type categories by adding new extensions and folders.
- **Logging**: Keeps a log of all file movements and errors for easy tracking.

## Problem Statement

My Downloads folder was chaotic, filled with files of different types. Sorting them manually would have been a long and repetitive process, so I created **Py-Files-organiser** to automate the task, letting me keep my files organized without lifting a finger.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Py-Downloads-organiser.git
    cd Py-Downloads-organiser
    ```

2. **Install required dependencies**:
   The script uses Python's built-in modules (`os`, `shutil`, `logging`), so no additional installations are needed.

3. **Edit the script**:
   Open the Python script `organiser.py` and update the path to your Downloads folder:

   ```python
   downloads_folder = '/path/to/your/Downloads'
   ```

4. **Make the script executable** (optional):
   ```bash
   chmod +x PyDownloadsorganiser.py
   ```

## Usage

You can run the script manually:

```bash
python3 organiser.py <folder name:e.g Downloads> 
```

### Set up a Cron Job

The cron job has been automatically set to run the script every day at midnight (12 AM)
You can change this in the cron_job.py script

## Logging

The script automatically logs all activities to a log file. The log file records details such as:
- Which files were moved?
- Which folders were created?
- Any errors that occurred.

You can find the log file at `cwd/logs/`.

## Customization

To add new file categories or extensions, modify the `file_categories` dictionary in the script:

```python
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
}
```

You can add new extensions or create entirely new categories as needed.

## Future Improvements

- **Real-time Monitoring**: Implement a real-time file system monitoring feature using libraries like `watchdog`.
- **User Interface**: Develop a simple GUI to make it easier for non-technical users to customize and use the script.
- **Advanced File Categorization**: Add more specific file categories and subfolders for different file types.



