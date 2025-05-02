# AutoFileSorter

AutoFileSorter is a simple Python script that automatically organizes your files by type.  
It moves PDFs, images, and screenshots into categorized folders inside your Documents directory, and moves development files into a separate `dev` folder.

![hippo][/Users/Yahya/dev/AutoFileSorter/AutoFileSorter_Demo.gif](https://github.com/yahyazaceria/AutoFileSorter/blob/main/AutoFileSorter_Demo.gif)
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
      DOCUMENTS_PATH = r'/Users/yourusername/Documents'
      DEV_PATH = r'/Users/yourusername/dev'
      SOURCE_PATH = r'/Users/yourusername/Downloads'
Replace `yourusername` with your actual username.

4. **(Optional) Customize File Types**  
Add or remove file extensions in the `file_types` dictionary as needed.

---

## Usage

1. **Open Terminal**
2. Navigate to the folder containing `filesort.py`:
3. **Run the script:**

---

## Automate (Optional)

You can automate AutoFileSorter to run at regular intervals on **Mac** and **Linux** using `crontab`, a built-in task scheduler.

### How to Automate with Crontab (Mac & Linux)

1. **Find Your Python Path**  
Open Terminal and run:
Copy the output (e.g., `/usr/bin/python3`).

2. **Get the Full Path to Your Script**  
For example: `/Users/yourusername/path/to/filesort.py` or `/home/yourusername/path/to/filesort.py`

3. **Edit Your Crontab**  
In Terminal, type:
If prompted, choose an editor (nano is easiest).

4. **Add a Cron Job**  
At the end of the file, add a line like this:
- This example runs the script every 10 minutes.  
- To run it every hour: `0 * * * * ...`  
- To run it every day at 7:30am: `30 7 * * * ...`
- Adjust the schedule as you wish. [Use crontab.guru to build your schedule!](https://crontab.guru/)

5. **Save and Exit**  
- In nano: press `Ctrl+O` to save, then `Ctrl+X` to exit.
- In vim: press `Esc`, then type `:wq` and press Enter.

6. **Check Your Cron Jobs**  
To list your current scheduled jobs, run:

**That’s it! Your script will now run automatically at the interval you set.**

**Tips:**
- Make sure your script is executable:  
- If you use a virtual environment, specify the full path to the Python interpreter inside that environment.
- You can check that your script runs correctly by running it manually first.

---

## Contributing

Feel free to fork this project and submit pull requests for improvements!

---

## License

This project is open source and free to use.

---

**Enjoy a tidier, more organized computer!**
