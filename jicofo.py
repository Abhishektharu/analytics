import pandas as pd
from datetime import datetime
import re

# Define the regex pattern to match the log line structure
pattern = r'(\w+)\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d+)\s+(\w+):\s+\[(\d+)\]\s+(.*)'

def parse_jicofo_log_line(log_line):
    match = re.match(pattern, log_line)
    
    if match:
        service, date, time, log_level, thread, message = match.groups()
        timestamp_str = f"{date} {time}"
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        
        return {
            "service": service,
            "timestamp": timestamp,
            "log_level": log_level,
            "thread": thread,
            "message": message
        }
    else:
        return None

# Define a function to read and analyze the jicofo.log file
def analyze_jicofo_log(log_file):
    # Initialize an empty list to store parsed log data
    log_data = []
    
    # Open the log file and read each line
    with open(log_file, 'r') as file:
        for line in file:
            # Parse each log line
            parsed_log = parse_jicofo_log_line(line)
            if parsed_log:
                log_data.append(parsed_log)
    
    # Convert the list of parsed log data into a pandas DataFrame
    df = pd.DataFrame(log_data)
    
    # Split 'timestamp' into 'Date' and 'Time' columns
    df['Date'] = df['timestamp'].dt.date
    df['Time'] = df['timestamp'].dt.time
    
    return df


