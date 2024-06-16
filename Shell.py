from Command import *
from Title import *

def main():
    clear_screen()
    print_title()
    while True:
        command = input("Nhập lệnh: ").strip()
        if command == "Exit":
            break
        
        elif command == "Help":
            help()

        elif command.startswith("Create file "):
            file_name = command[12:].strip()
            create_file(file_name)

        elif command.startswith("Create directory "):
            dir_name = command[17:].strip()
            create_directory(dir_name)

        elif command == "List files":
            list_files()

        elif command.startswith("Change to "):
            path = command[10:].strip()
            change_directory(path)

        elif command == "Clear screen":
            clear_screen()
            print_title()

        elif command == "Datetime":
            print_current_datetime()

        elif command == "Calculator":
            open_calculator()

        elif command == "Clock":    
            open_clock()

        elif command == "Camera":
            open_camera()

        elif command.startswith("Countdown "):
            countdown_time = command[10:].strip()
            countdown(int(countdown_time))

        elif command == "Manager":  
            manager()
        else:
            print("Lệnh không hợp lệ.")
        print('')

if __name__ == "__main__":
    main()
