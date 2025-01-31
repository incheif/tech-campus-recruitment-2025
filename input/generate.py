import random
from datetime import datetime, timedelta

def generate_log_file(filename, num_days, entries_per_day):
    log_levels = ["INFO", "ERROR", "WARN"]
    start_date = datetime(2023, 10, 1)

    with open(filename, 'w') as f:
        for day in range(num_days):
            # Generate the date for the current day
            date = start_date + timedelta(days=day)
            
            # For each day, create multiple log entries
            for entry in range(entries_per_day):
                # Generate a random time within the day
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                timestamp = date.replace(hour=hour, minute=minute, second=second)
                
                # Randomly choose a log level
                log_level = random.choice(log_levels)
                
                # Random log message
                log_message = f"Sample log message {day * entries_per_day + entry + 1}"
                
                # Write the log entry to the file
                f.write(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {log_level} {log_message}\n")

    print(f"Log file '{filename}' with {num_days * entries_per_day} entries has been created.")

# Generate a log file with logs for 10 days, and 5 log entries per day
generate_log_file("test_logs.log", 490, 30)
