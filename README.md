# Recursive File System Watcher (Python)

A snapshot-based file system watcher built from scratch in Python.  
It recursively scans a folder, tracks state over time, and detects changes without using external monitoring libraries.

---

## 🚀 What This Project Does

This watcher continuously monitors a root folder and all nested subfolders.  
It detects:

- File and folder creation  
- File and folder deletion  
- File modification (size / last modified time)  
- Rename and move operations (via logical matching)  

---

## 🧠 How It Works

Instead of using tools like `watchdog`, this project uses a **snapshot comparison approach**:

1. Take a full recursive snapshot of the folder  
2. Store it as the previous state  
3. Rescan the folder repeatedly  
4. Compare old vs new snapshots  
5. Detect differences using:
   - set operations (paths)
   - metadata comparison (size, mtime)
6. Infer rename/move using similarity matching  

---

## 🛠️ Tech Used

- Python  
- pathlib  
- time  
- datetime  

---

## 📂 Project Structure (Suggested)
