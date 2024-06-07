
import os
import datetime
import subprocess
import tkinter as tk
from Countdown import CountdownApp


def open_calculator():
    try:
        subprocess.Popen('calc.exe')
    except Exception as e:
        print(f"Lỗi khi mở máy tính: {e}")

def list_files():
    for item in os.listdir('.'):
        print(item)

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Đã chuyển đến thư mục: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Thư mục '{path}' không tồn tại.")
    except NotADirectoryError:
        print(f"'{path}' không phải là một thư mục.")

def clear_screen():
    os.system('cls')

def help():
    print("Các lệnh hỗ trợ:")
    print("1. List files: Liệt kê tất cả các tập tin và thư mục trong thư mục hiện tại.")
    print("2. Change to <path>: Chuyển đến thư mục con hoặc thư mục cha.")
    print("3. Clear screen: Xóa màn hình.")
    print("4. Exit: Thoát chương trình.")
    print("5. Create file <file_name>: Tạo một tệp mới.")
    print("6. Create directory <dir_name>: Tạo một thư mục mới.")
    print("7. Datetime: In ngày giờ hiện tại.")
    print("8. Calculator: Mở máy tính.")
    print("9. Clock: Mở đồng hồ.")
    print("10. Camera: Mở camera.") 
    print("11. Countdown <countdown_time>: Bắt đầu đếm ngược thời gian.")

def create_file(file_name):
    with open(file_name, 'w') as file:
        file.write('')
    print(f"Tệp '{file_name}' đã được tạo.")

def create_directory(dir_name):
    try:
        os.makedirs(dir_name)
        print(f"Thư mục '{dir_name}' đã được tạo.")
    except FileExistsError:
        print(f"Thư mục '{dir_name}' đã tồn tại.")

def print_current_datetime():
    now = datetime.datetime.now()
    print("Ngày giờ hiện tại:", now.strftime("%Y-%m-%d %H:%M:%S"))

def open_clock():
    try:
        subprocess.Popen('start "" /b "ms-clock:"', shell=True)
    except Exception as e:
        print(f"Lỗi khi mở đồng hồ: {e}")

def open_camera():
    try:
        subprocess.Popen('start "" /b "microsoft.windows.camera:"', shell=True)
    except Exception as e:
        print(f"Lỗi khi mở camera: {e}")

def countdown(countdown_time):
    root = tk.Tk()
    app = CountdownApp(root, countdown_time)
    root.mainloop()