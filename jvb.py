import re
import pandas as pd

def read_log_file(log_file_path):
    # Read the log file
    with open(log_file_path, 'r') as file:
        log_data = file.readlines()

    # Define regular expressions to extract information
    timestamp_regex = r'JVB (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}.\d{3})'  # Updated regex to extract date and time separately
    info_regex = r'JVB \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3} (INFO|WARNING|ERROR): \[\d\] (.*)'

    # Initialize lists to store extracted data
    dates = []  # List to store dates
    times = []  # List to store times
    thread_contexts = []
    log_levels = []
    info_messages = []

    # Extract timestamps and information messages
    for line in log_data:
        timestamp_match = re.match(timestamp_regex, line)
        info_match = re.match(info_regex, line)
        if timestamp_match and info_match:
            date = timestamp_match.group(1)  # Extract date
            time = timestamp_match.group(2)  # Extract time
            dates.append(date)
            times.append(time)
            log_level = info_match.group(1)
            info = info_match.group(2)
            thread_context, info_message = info.split(': ', 1)  # Split info into thread context and message
            thread_contexts.append(thread_context)
            log_levels.append(log_level)
            info_messages.append(info_message)

    # Create a DataFrame
    df = pd.DataFrame({'date': dates, 'time': times, 'thread_Context': thread_contexts, 'log_level': log_levels, 'message': info_messages})

    return df
