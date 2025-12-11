import os
from datetime import datetime

def create_html_report_path(base_folder="reports"):
    # Create folder base day
    today = datetime.now().strftime("%Y-%m-%d")
    day_folder = os.path.join(base_folder, today)
    os.makedirs(day_folder, exist_ok=True)

    # create timestamp file (hour-min-sec)
    timestamp = datetime.now().strftime("%H-%M-%S")
    new_report_path = os.path.join(day_folder, f"report_{timestamp}.html")

    return new_report_path, day_folder
