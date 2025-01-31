import sys
import os
import re

def extract_logs(input_file, output_file, target_date):
    """
    Extract logs for the specified date and save them to the output file.
    
    :param input_file: The path to the large log file.
    :param output_file: The path to the output file where logs will be saved.
    :param target_date: The date (YYYY-MM-DD) to filter logs by.
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Extract the date from the line
                log_date = line.split(" ")[0]
                if log_date == target_date:
                    outfile.write(line)
        
        print(f"Logs for {target_date} have been extracted to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Ensure the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)
    
    target_date = sys.argv[1]
    
    # Validate the date format (YYYY-MM-DD) using a regular expression
    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(date_pattern, target_date):
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)
    
    # Set the input and output paths relative to the current directory
    input_file = os.path.join('..', 'input', 'test_logs.log')  # Input folder is outside src
    output_file = os.path.join('..', 'output', f'output_{target_date}.log')  # Output folder is outside src
    
    # Ensure output folder exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    extract_logs(input_file, output_file, target_date)

if __name__ == "__main__":
    main()
