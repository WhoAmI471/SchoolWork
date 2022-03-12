def check_pin(pin):
    for i in pin:
        if len(pin) == 4 and pin != '1234' and pin.count(i) < 4:
            return True
        else:
            return False

def check_pass(password):
    if len(password) >= 8 and password.isalnum() == True and password.isalpha() == False:
        return True
    else:
        return False

def check_mail(mail):
    count = mail.count('@') + mail.count('.')

    if count >= 2:
        return True
    else:
        return False

def check_name(name):
    for letter in name.lower():
        if letter not in "йцукенгшщзхъфывапролджэячсмитьбюё ":
            return False
    return True