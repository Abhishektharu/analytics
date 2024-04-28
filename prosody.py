import pandas as pd

# Define an empty list to store parsed log data
log_data = []

def prosody_log(log_file):
    # Open the log file and read each line
    with open(log_file, 'r') as file:
        for line in file:
            # Split each line into fields separated by spaces
            fields = line.strip().split()

            # Extract information from the fields
            timestamp = ' '.join(fields[:3])
            source = fields[3].rstrip(':')
            level = fields[4].rstrip(':')
            message = ' '.join(fields[5:])

            # Append the parsed data to the list
            log_data.append({
                "timestamp": timestamp,
                "thread_context": source,
                "log_level": level,
                "message": message
            })

    # Convert the list of parsed log data into a pandas DataFrame
    log_df = pd.DataFrame(log_data)

    # Split 'timestamp' into 'Date' and 'Time' columns
    log_df[['date', 'time']] = log_df['timestamp'].str.split(' ', n=1, expand=True)

    # Drop the original 'timestamp' column
    log_df.drop(columns=['timestamp'], inplace=True)

    return log_df
