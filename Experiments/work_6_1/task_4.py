from validators import *

user_pin = str(input())
user_pass = input()
user_mail = input()
user_name = input()

print(
    f'{check_pin(user_pin)}\n'
    f'{check_pass(user_pass)}\n'
    f'{check_mail(user_mail)}\n'
    f'{check_name(user_name)}'
    )

