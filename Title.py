import pyfiglet

def print_title():
    ascii_art = pyfiglet.figlet_format("Tiny Shell!",font='starwars')
    print(ascii_art)
    print('Nhập "Help" để xem danh sách các lệnh hỗ trợ.')
    print('')
    print('')
