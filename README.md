🖋 LogNinja - Python Keylogger with GUI

📌 Overview

LogNinja is a simple yet powerful Python-based keylogger with a Graphical User Interface (GUI) built using Tkinter.
It uses the pynput library to monitor and record keystrokes in real-time and provides options to start, stop, and save logs.


✨ Features

Start & Stop Logging with one click

Real-time keystroke display in the GUI

Special key handling (Space, Enter, Tab, Backspace, Escape)

Thread-safe logging using threading.Lock

Log saving with timestamped filenames in a logs/ directory

Customizable Icons & Logo (supports .ico for Windows and .png for cross-platform use)

Responsive GUI with adjustable size

📂 Project Structure
bash
Copy
Edit
keylogger.py        # Main application code
logs/               # Folder where logs are saved
README.md           # Project documentation

⚙️ Requirements

Make sure you have Python 3.x installed and then install the dependencies:

bash
Copy
Edit
pip install pynput
tkinter is included in most Python installations by default.
If not, install it via your package manager:

Windows: Comes pre-installed with Python

Ubuntu/Debian: sudo apt-get install python3-tk

MacOS: Pre-installed with Python

🚀 How to Run

Clone the repository or download the script:

bash
Copy
Edit
git clone https://github.com/<your-username>/keylogger-gui.git
cd keylogger-gui
Run the script:

bash
Copy
Edit
python keylogger.py
Using the GUI:

Click Start Logging to begin capturing keystrokes

Click Stop Logging to stop

Click Save Log to store the log file in the logs/ directory
