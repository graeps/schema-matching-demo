import os
import time


def delete_old_files(dir_to_clean_up, age_threshold=3600):
    """Delete files older than `age_threshold` seconds in the given directory.

    :param dir_to_clean_up: Directory to scan for old files.
    :param age_threshold: Time in seconds; default is 3600 seconds (1 hour).
    """
    # Get the current time
    current_time = time.time()
    for filename in os.listdir(dir_to_clean_up):
        file_path = os.path.join(dir_to_clean_up, filename)
        if os.path.isfile(file_path):
            file_mod_time = os.path.getmtime(file_path)
            file_age = current_time - file_mod_time
            if file_age > age_threshold:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
