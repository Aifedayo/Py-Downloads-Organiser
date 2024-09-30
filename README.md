# Py-Downloads-Organiser

## Overview

Is your Downloads folder cluttered with files of all types—documents, images, videos, and more? Manually organizing them can be tedious and time-consuming. **Py-Downloads-Organizer** is a Python script designed to automatically sort and organize your downloaded files into categorized folders based on their file types.

This script runs daily at midnight using a cron job, keeping your Downloads folder tidy and well-organized without any manual effort.

## Features

- **Automatic Sorting**: Automatically organizes files into folders based on their extensions (e.g., `.pdf` files go to `Documents`, `.jpg` files go to `Images`, etc.).
- **Automatic Folder Creation**: Creates folders for new categories if they don’t already exist.
- **Customizable**: Extend the file type categories by adding new extensions and folders.
- **Logging**: Keeps a log of all file movements and errors for easy tracking.

## Problem Statement

My Downloads folder was chaotic, filled with files of different types. Sorting them manually would have been a long and repetitive process, so I created **Py-Downloads-Organizer** to automate the task, letting me keep my files organized without lifting a finger.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Py-Downloads-Organizer.git
    cd Py-Downloads-Organizer
    ```

2. **Install required dependencies**:
   The script uses Python's built-in modules (`os`, `shutil`, `logging`), so no additional installations are needed.

3. **Edit the script**:
   Open the Python script `PyDownloadsOrganizer.py` and update the path to your Downloads folder:

   ```python
   downloads_folder = '/path/to/your/Downloads'
   ```

4. **Make the script executable** (optional):
   ```bash
   chmod +x PyDownloadsOrganizer.py
   ```

## Usage

You can run the script manually:

```bash
python3 PyDownloadsOrganizer.py
```

Or, if you’ve set up a cron job (explained below), it will run automatically at 12 AM each day.

### Set up a Cron Job

To automatically run the script every day at midnight (12 AM):

1. Open your crontab:
   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script to run at 12 AM daily:
   ```bash
   0 0 * * * /usr/bin/python3 /path/to/PyDownloadsOrganizer.py
   ```

3. Save and exit the crontab. The script will now run daily at midnight.

## Logging

The script automatically logs all activities to a log file. The log file records details such as:
- Which files were moved.
- Which folders were created.
- Any errors that occurred.

You can find the log file at `/path/to/your/logfile.log`.

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



