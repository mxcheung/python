from datetime import datetime

# Example list of UTC timestamps as strings
timestamps = [
    "2024-10-21T12:34:56Z",
    "2024-10-21T15:30:00Z",
    "2024-10-21T09:12:45Z"
]

# Convert the timestamp strings to datetime objects
datetime_objects = [datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ") for ts in timestamps]

# Find the minimum and maximum timestamps
min_timestamp = min(datetime_objects)
max_timestamp = max(datetime_objects)

# Calculate the duration in seconds
duration_seconds = int((max_timestamp - min_timestamp).total_seconds())

# Return the duration as an integer
print(f"Duration in seconds: {duration_seconds}")
