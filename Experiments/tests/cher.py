text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = ''
text_cleaned = ''
words = text.split(' ')

for word in words:
    if word.isdigit() != True:
        just_words += word

if just_words in words:
    text_cleaned += just_words + ' '

print(words)
print(text_cleaned)