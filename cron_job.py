import os


path_to_organizer = os.path.abspath("organizer.py")

cron_job = f"0 0 * * * /usr/bin/python3 /{path_to_organizer}"

existing_cron_jobs = os.popen('crontab -l').read()

if cron_job not in existing_cron_jobs:
    os.system(f'crontab -l; echo "{cron_job}" | crontab -')
    print("Cron job added successfully")
else:
    print("Cron job already exists")
