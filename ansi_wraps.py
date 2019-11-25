import ctypes
import os
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# \033 \x1b - escape character

def clear_test():
    print('\x1b[H\x1b[J', end='')
def test_2():
    print('\x1b[1;1H\x1b[J')
    print('\033[2J', end='')

def clear():
    os.system('cls')



class Color:
    bold = '\033[1m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    l_black = '\033[30;1m'
    l_red = '\033[31;1m'
    l_green = '\033[32;1m'
    l_yellow = '\033[33;1m'
    l_blue = '\033[34;1m'
    l_magenta = '\033[35;1m'
    l_cyan = '\033[36;1m'
    l_white = '\033[37;1m'
    reset = '\033[0m'


def print_colored(string, color, end=''):
    if color == 'black':
        print('\u001b[30m' + string + '\u001b[0m', end=end)
    elif color == 'red':
        print('\u001b[31m' + string + '\u001b[0m', end=end)
    elif color == 'green':
        print('\u001b[32m' + string + '\u001b[0m', end=end)
    elif color == 'yellow':
        print('\u001b[33m' + string + '\u001b[0m', end=end)
    elif color == 'blue':
        print('\u001b[34m' + string + '\u001b[0m', end=end)
    elif color == 'magenta':
        print('\u001b[35m' + string + '\u001b[0m', end=end)
    elif color == 'cyan':
        print('\u001b[36m' + string + '\u001b[0m', end=end)
    elif color == 'white':
        print('\u001b[37m' + string + '\u001b[0m', end=end)
    elif color == 'l_black':
        print('\u001b[30;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_red':
        print('\u001b[31;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_green':
        print('\u001b[32;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_yellow':
        print('\u001b[33;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_blue':
        print('\u001b[34;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_magenta':
        print('\u001b[35;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_cyan':
        print('\u001b[36;1m' + string + '\u001b[0m', end=end)
    elif color == 'l_white':
        print('\u001b[37;1m' + string + '\u001b[0m', end=end)
    else:
        print('NO SUCH COLOR!')
        # TODO: Raise error

'''
print_colored('Hello', 'black')
print_colored('Hello', 'red')
print_colored('Hello', 'green')
print_colored('Hello', 'yellow')
print_colored('Hello', 'blue')
print_colored('Hello', 'magenta')
print_colored('Hello', 'cyan')
print_colored('Hello', 'white')

print_colored('Hello', 'l_black')
print_colored('Hello', 'l_red')
print_colored('Hello', 'l_green')
print_colored('Hello', 'l_yellow')
print_colored('Hello', 'l_blue')
print_colored('Hello', 'l_magenta')
print_colored('Hello', 'l_cyan')
print_colored('Hello', 'l_white')
'''