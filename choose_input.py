# скрипт для использования буфера обмена или ручного ввода

import pyperclip

red = '\033[91m'
green = '\33[32m'
end = '\033[0m'

def chose_input():
    keyword = pyperclip.paste()
    print(f'Do you want to use {red}{keyword}{end} as keyword?\n'
          f'Press {green}"ENTER"{end} if {green}"YES"{end} or type you keyword')
    answer = input()
    # if len(answer) > 2:
    return answer if len(answer) > 2 else keyword

print(chose_input())
