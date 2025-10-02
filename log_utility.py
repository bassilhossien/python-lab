import os
import json

def get_error_logs_from_log_file(log_file_path):
    """
    Reads a log file and returns a list of error messages.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        list: A list of error messages found in the log file.
    """
    error_logs = []
    if not os.path.exists(log_file_path):
        return error_logs

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            if "ERROR" in line:
                error_logs.append(line.strip())
    return error_logs

def get_tail_logs_from_log_file(log_file_path, num_lines=10):
    """
    Reads the last `num_lines` lines from a log file.

    Args:
        log_file_path (str): The path to the log file.
        num_lines (int): The number of lines to read from the end of the file.

    Returns:
        list: A list of the last `num_lines` lines from the log file.
    """
    if not os.path.exists(log_file_path):
        return []

    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()
        return [line.strip() for line in lines[-num_lines:]]
    
def line_to_dict(line):
    #2025-09-30 11:14:36,983 [ERROR] - 2025-09-30 11:14:36 [ERROR] - Scheduled task completed successfully.
    parts = line.split(" - ")
    if len(parts) < 3:
        return {}
    timestamp = parts[0].split(" [")[0]
    level = parts[0].split("[")[1].split("]")[0]
    return {
        "timestamp": timestamp,
        "level": level,
        "message": parts[2]
    }

def log_to_json(log_file_path, output_json_path):
    logs = get_error_logs_from_log_file(log_file_path)
    log_dicts = [line_to_dict(log) for log in logs if line_to_dict(log)]
    with open(output_json_path, 'w') as json_file:
        json.dump(log_dicts, json_file, indent=4)

def merge_dicts_deeply(dict1, dict2):
    """
    Merges two dictionaries deeply.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: The merged dictionary.
    """
    for key in dict2:
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            merge_dicts_deeply(dict1[key], dict2[key])
        else:
            dict1[key] = dict2[key]
    return dict1