
# 🗂️ File Organizer Script

This script automatically **sorts files by type** into predefined folders. It’s a simple yet effective solution to keep your directories clean and organized.

## 🔧 Features

- Recognizes and organizes the following file types:
  - Images (`.jpg`, `.jpeg`, `.png`, `.gif`)
  - Documents (`.txt`, `.pdf`, `.docx`)
  - Audio files (`.mp3`, `.wav`)
  - Videos (`.mp4`, `.mov`)
- Creates folders if they don’t exist
- Moves files to the appropriate folder
- Logs all actions and errors to `file_organizer.log`

## 💼 Use Cases

Perfect for:

- Freelancers keeping work files organized
- Office workers sorting downloaded documents
- Basic automation needs for personal or business use

## ▶️ How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/Martin-vot/file-organizer.git
   ```

2. Edit the path to the directory you want to organize:
   ```python
   directory = 'path/to/your/directory'  # e.g. 'C:/Users/yourname/Downloads'
   ```

3. Run the script:
   ```bash
   python file_organizer.py
   ```

4. Check the results:
   - Files will be moved into subfolders inside the target directory
   - All logs are written to `file_organizer.log`

## 🛠️ Requirements

- Python 3.x
- Standard libraries (`os`, `shutil`, `logging`)

## 📁 Example Folder Structure

**Before:**
```
Downloads/
├── photo.jpg
├── contract.pdf
├── music.mp3
└── video.mp4
```

**After:**
```
Downloads/
├── images/
│   └── photo.jpg
├── documents/
│   └── contract.pdf
├── audio/
│   └── music.mp3
├── videos/
│   └── video.mp4
└── file_organizer.log
```

## 📬 Contact

Need similar scripts or custom automation solutions?  
Feel free to reach out via GitHub or at [martin@votapek.cz/LinkedIn/website].

---

*Made with Python & 💡 for automation lovers.*
