import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

class CountdownApp:
    def __init__(self, root, countdown_time):
        self.root = root
        self.frame = tk.Frame(root, width=500, height=100)
        self.frame.pack_propagate(False) 
        self.frame.pack()
        self.countdown_time = countdown_time
        self.remaining_time = countdown_time
        self.running = False
        self.paused = False

        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 200))
        self.countdown_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_countdown)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_countdown)
        self.pause_button.pack()

        self.continue_button = tk.Button(root, text="Continue", command=self.continue_countdown)
        self.continue_button.pack()

    def display_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.root, image=photo)
        self.image_label.image = photo 
        self.image_label.pack()

    def start_countdown(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.countdown)
            self.thread.start()

    def countdown(self):
        while self.remaining_time >= 0 and self.running:
            if not self.paused:
                self.countdown_label.config(text=str(self.remaining_time))
                time.sleep(1)
                self.remaining_time -= 1
            else:
                time.sleep(1)
        self.root.quit()

    def pause_countdown(self):
        self.paused = True

    def continue_countdown(self):
        self.paused = False