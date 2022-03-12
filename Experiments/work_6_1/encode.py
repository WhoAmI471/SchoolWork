alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
list_alphabet = list(alphabet)

def shift_encode(string):
    for letter in string:
        if list_alphabet.index(letter.lower()) < 31:
            number = list_alphabet[(list_alphabet.index(letter)) + 1]
            return number
        else :
            number = list_alphabet[0]
            return number
    return string

def shift_decode(encode):
    if encode.isalpha():
        number = ord(encode) - 1 % 32
        return chr(number)
    return encode

encode = ''
decode = ''
user_input = input()

for i in user_input:
    encode += shift_encode(i)
print(encode)

for j in encode:
    decode += shift_decode(j)
print(decode)