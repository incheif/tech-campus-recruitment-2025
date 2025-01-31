
---

### **📄 Discussion.md**
```markdown
# Efficient Log Retrieval from a Large File

## 🔹 Solutions Considered

### **1️⃣ Full File Download Approach**
**Idea:**  
- Download the **entire 1TB log file** first.
- Use Python’s `open()` to read and extract logs for the specified date.

**Issues:**  
❌ **Storage-Heavy:** Requires **1TB of disk space**.  
❌ **Slow Processing:** Searching through such a large file would take a long time.  

---

### **2️⃣ Line-by-Line Streaming Approach (Final Choice ✅)**
**Idea:**  
- Use `requests` with `stream=True` to **process logs line-by-line** without downloading the full file.  
- Filter out logs based on the **specified date**.  

**Why We Chose This?**  
✅ **Efficient Memory Usage:** No need to store the full file.  
✅ **Fast Processing:** Extracts relevant logs without scanning everything.  
✅ **Scalable:** Works even if the log file grows beyond 1TB.  

---

## 🔹 Final Solution Summary  

The final solution:
- **Streams the log file from the URL** instead of downloading it.
- **Writes the filtered logs** to `output/output_YYYY-MM-DD.txt` (outside `src/`).
- **Handles errors**, such as network failures or if the server doesn't support streaming.

---

## 🔹 Steps to Run

### **1️⃣ Install Dependencies**
Make sure Python is installed. If not, install it from [python.org](https://www.python.org/).  
Then, install `requests`:
```bash
pip install requests
```

### **2️⃣ Run the Script**
Navigate to the `src` directory and run:
```bash
cd src
python extract_logs.py 2024-12-01
```

### **3️⃣ Check the Output**
Logs will be saved in:
```
/project-root/output/output_2024-12-01.txt
```
Example output:
```
2024-12-01 14:23:45 INFO User logged in
2024-12-01 14:24:10 ERROR Failed to connect to the database
```

---

## 🔹 Error Handling  
❌ **If Streaming is Not Supported:**  
```bash
Streaming is not supported by the server. Full download required.
```
➡ **Solution:** Download the file manually.

❌ **If Network Error Occurs:**  
```bash
Error fetching logs: <detailed error>
```
➡ **Solution:** Check internet connection.

---

## 🚀 Conclusion  

The **line-by-line streaming approach** is the best solution for efficiently extracting logs from a **1TB file**, ensuring speed and minimal memory usage.
```

---
