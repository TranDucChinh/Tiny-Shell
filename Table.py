import tkinter as tk
from tkinter import ttk
import subprocess
import psutil
import threading

class ProcessManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.processes = {}
        self.title('Process Manager')
        self.counter=1
        self.tree = ttk.Treeview(self, columns=('Status',), height=15)
        self.tree.heading('#0', text='Process')
        self.tree.heading('#1', text='Status')
        self.tree.pack()

        
        self.start_button = tk.Button(self, text='Create Process', command=self.create_process)
        self.start_button.pack(side=tk.LEFT)

        self.command_entry = tk.Entry(self)
        self.command_entry.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(self, text='Stop Process', command=self.stop_process)
        self.stop_button.pack()
        
        self.resume_button = tk.Button(self, text='Resume Process', command=self.resume_process)
        self.resume_button.pack()

        self.kill_button = tk.Button(self, text='Kill Process', command=self.kill_process)
        self.kill_button.pack()

    def create_process(self):
        command = self.command_entry.get()
        self.command_entry.delete(0, tk.END)
        if command.startswith('Count ') and command[6:].isdigit():
            process_name = 'Process ' + str(self.counter) +": " + command
            self.counter+=1
            process = subprocess.Popen('python count.py '+command[6:])
            self.processes[process_name] = process
            self.tree.insert('', 'end', process_name, text=process_name, values=('Running',))
        elif command.startswith('Countdown ') and command[10:].isdigit():
            process_name = 'Process ' + str(self.counter) +": " + command
            self.counter+=1
            process = subprocess.Popen('python count2.py '+command[10:])
            self.processes[process_name] = process
            self.tree.insert('', 'end', process_name, text=process_name, values=('Running',))
        else:
            print('Lệnh '+command+' không hợp lệ.')
            self.command_entry.focus_set()

    def resume_process(self):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            process = self.processes[selected_item]
            p = psutil.Process(process.pid)
            p.resume()    
            self.tree.set(selected_item, 'Status', 'Running')
        else:
            print("No process selected")
    def stop_process(self):
        selected_items = self.tree.selection()
        if selected_items: 
            selected_item = selected_items[0]
            process = self.processes[selected_item]
            p = psutil.Process(process.pid)
            p.suspend()
            self.tree.set(selected_item, 'Status', 'Stopped')
        else:
            print("No process selected")

    def kill_process(self):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            process = self.processes[selected_item]
            process.kill()
            self.tree.delete(selected_item)
            del self.processes[selected_item]
        else:
            print("No process selected")

if __name__ == '__main__':
    app = ProcessManager()
    app.mainloop()