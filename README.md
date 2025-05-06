# AutoFileSorter

AutoFileSorter is a simple Python script that automatically organizes your files by type.  
It moves PDFs, images, and screenshots into categorized folders inside your Documents directory, and moves development files into a separate `dev` folder.

![hippo](https://github.com/yahyazaceria/AutoFileSorter/blob/main/AutoFileSorter_Demo.gif)

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
   Fork or clone the `AutoFileSorter` repository to your computer.

3. **Edit Paths**  
   Open `filesort.py` and set the variables at the top to match your system:
- `DOCUMENTS_PATH = r'/Users/yourusername/Documents'`
- `DEV_PATH = r'/Users/yourusername/dev'`
- `SOURCE_PATH = r'/Users/yourusername/Downloads'`

Replace `yourusername` with your actual username.

4. **(Optional) Customize File Types**  
Add or remove file extensions in the `file_types` dictionary as needed.

---

## Usage

1. **Open Terminal**
2. Navigate to the folder containing `filesort.py`: `cd /path/to/your/project`

3. **Run the script:**

---

## Automate (Mac/Linux) 

1. Open your crontab in nano:
   env EDITOR=nano crontab -e

2. Add this line at the end to run AutoFileSorter every 10 minutes:
   `*/10 * * * * /usr/bin/python3 /Users/yourusername/path/to/filesort.py`

   Replace `/usr/bin/python3` with the output of `which python3`, and `/Users/yourusername/path/to/filesort.py` with the full path to your script.
   - To run it every hour, use:
     `0 * * * * /usr/bin/python3 /Users/yourusername/path/to/filesort.py`
   - To run it every day at 7:30am, use:
     `30 7 * * * /usr/bin/python3 /Users/yourusername/path/to/filesort.py`

3. Save and exit nano:
   - Press Ctrl+O, then Enter to save.
   - Press Ctrl+X to exit.

4. To list your current cron jobs:
   crontab -l

5. To remove all your cron jobs:
   crontab -r


_Use Task Scheduler to automate on Windows_

---

## Contributing

Feel free to fork this project and submit pull requests for improvements!

---

## License

This project is open source and free to use.

---

**Enjoy a tidier, more organized computer!**
