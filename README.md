# AutoFileSorter

AutoFileSorter is a simple Python script that automatically organizes your files by type.  
It moves PDFs, images, and screenshots into categorized folders inside your Documents directory, and moves development files into a separate `dev` folder.

---

## Features

- Sorts files from your Downloads folder (or any folder you specify)
- Moves:
  - PDFs to `Documents/pdfs`
  - Images to `Documents/images`
  - Screenshots to `Documents/screenshots`
  - Development files (e.g., `.py`, `.js`, `.html`, etc.) to a separate `dev` folder
- Easy to customize and extend

---

## How It Works

The script scans your source folder (e.g., Downloads), checks each file’s type, and moves it to the appropriate destination folder.

---

## Setup

1. **Install Python**  
   Make sure you have [Python 3.x](https://www.python.org/downloads/) installed.

2. **Download the Script**  
   Download or copy the `filesort.py` script to your computer.

3. **Edit Paths**  
   Open `filesort.py` and set the variables at the top to match your system:

---

## Automate (Optional)

To run this script automatically at intervals, use Windows Task Scheduler or a similar tool.  
If you need help setting this up on MacOS or Linux, see [this guide]([https://www.howtogeek.com/123393/how-to-create-scheduled-tasks-with-the-task-scheduler-gui/](https://dev.to/brumor/automating-stuff-on-your-computer-with-cron-jobs-with-any-language-1eoc)) or ask for instructions.

---

## Contributing

Feel free to fork this project and submit pull requests for improvements!

---

## License

This project is open source and free to use.

---

**Enjoy a tidier, more organized computer!**
