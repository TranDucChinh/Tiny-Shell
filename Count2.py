import tkinter as tk
import time
import argparse

def count(n):
    for i in range(0, n +1):
        label.config(text=str(n-i))
        window.update()
        time.sleep(1)

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="The number to count to")
args = parser.parse_args()

window = tk.Tk()
window.title("Countdown "+str(args.n))
window.geometry("400x300")

label = tk.Label(window, font=("Arial", 200))
label.pack()

count(args.n)

window.mainloop()