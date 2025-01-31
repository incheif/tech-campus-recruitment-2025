import sys
import requests
import os

# URL of the log file
LOG_FILE_URL = "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3"

def extract_logs(date):
    """
    Extracts logs for a specific date without downloading the full file.
    Ensures the server supports streaming.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # Move outside src/
    output_dir = os.path.join(base_dir, "output")  # Ensure output is outside src/
    os.makedirs(output_dir, exist_ok=True)  # Create if not exists

    output_file = os.path.join(output_dir, f"output_{date}.txt")

    try:
        # Attempt to stream the file
        with requests.get(LOG_FILE_URL, stream=True, timeout=10) as response:
            response.raise_for_status()  # Raise an error if the request fails

            # Check if streaming is supported
            if "content-length" not in response.headers and "transfer-encoding" not in response.headers:
                raise ValueError("❌ Streaming is not supported by the server. Full download required.")

            found_logs = False
            with open(output_file, "w") as out_file:
                for line in response.iter_lines(decode_unicode=True):
                    if line and line.startswith(date):  # Ensure it's not empty
                        out_file.write(line + "\n")
                        found_logs = True

            print(f"✅ Logs for {date} saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching logs: {e}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date = sys.argv[1]
    extract_logs(date)
