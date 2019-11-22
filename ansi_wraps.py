import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def clear_what():
    print('\x1b[2J', end='')


def clear():
    print('\033[2J', end='')


class Color:
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    l_black = '\u001b[30;1m'
    l_red = '\u001b[31;1m'
    l_green = '\u001b[32;1m'
    l_yellow = '\u001b[33;1m'
    l_blue = '\u001b[34;1m'
    l_magenta = '\u001b[35;1m'
    l_cyan = '\u001b[36;1m'
    l_white = '\u001b[37;1m'
    reset = '\u001b[0m'


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