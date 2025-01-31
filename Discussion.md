### Problem Statement: Efficient Log Retrieval from a Large File

#### Solutions Considered:

1. **Reading Entire Log File into Memory**:
   - **Approach**: Read the entire log file into memory and filter logs for the given date.
   - **Pros**: Simple implementation.
   - **Cons**: Not feasible for large files (like 1 TB) due to memory constraints. This approach would consume excessive memory and might cause the program to crash or become unresponsive.

2. **Reading Log File Line-by-Line**:
   - **Approach**: Read the log file line by line and filter based on the date provided.
   - **Pros**: Efficient in terms of memory usage since only one line is processed at a time.
   - **Cons**: Slightly slower than reading the file in bulk because of multiple I/O operations.

3. **Using Indexing or Preprocessing**:
   - **Approach**: Preprocess the log file by creating an index (date-wise or timestamp-based) to quickly locate logs for a specific day.
   - **Pros**: Fast lookup once the index is created.
   - **Cons**: Requires extra storage and computation upfront to build the index, which might be impractical given the size of the log file (1 TB).

4. **Splitting the Log into Smaller Files**:
   - **Approach**: Split the log file into smaller chunks (e.g., daily logs) and query the specific chunk for the required date.
   - **Pros**: Efficient, as only the required chunk is loaded into memory.
   - **Cons**: Needs additional work to split and manage the chunks, and might be difficult to implement on such a large file.

#### Final Solution Summary:

The final solution involves reading the log file line by line and filtering the entries based on the specified date. This method minimizes memory usage, as only one line is loaded at a time, and it’s simple to implement. Given the constraints (1 TB file size and efficiency), this solution strikes a balance between memory usage and performance.

- **Why this solution**: 
   - **Memory Efficiency**: We avoid reading the entire file into memory, making this approach suitable for very large files.
   - **Simplicity**: The solution is straightforward to implement and doesn't require complex indexing or preprocessing.
   - **Scalability**: This approach can handle files that are too large to fit into memory and scales well for a wide range of file sizes.

#### Steps to Run:

1. **Clone the Repository**:
   - If you have a GitHub repository, start by cloning it to your local machine using the following command:
     ```bash
     git clone <repository-url>
     cd <repository-folder>
     ```

2. **Prepare the Log File**:
   - Ensure the log file (`test_logs.log`) exists in the current directory. You can use the provided log generation script to create a sample log file if you don't have one.

3. **Run the Script**:
   - Navigate to the directory containing your Python script and run it by passing the target date as an argument:
     ```bash
     python extract_logs.py 2024-12-01
     ```

4. **Output**:
   - The script will create a new file, `output/output_2024-12-01.txt`, containing all logs for the specified date.

5. **Error Handling**:
   - If the date is not provided or is invalid, the script will display an error message and exit.
   - If the log file is not found, the script will notify the user of the missing file.

6. **Customization**:
   - You can modify the script to accept different filenames or change the way logs are filtered based on different criteria (e.g., log level).

---

This approach should work efficiently even with large log files, and it’s simple to run for any user.
