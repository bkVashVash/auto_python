#! python3
# pw.py


import pyperclip
text = pyperclip.paste()

print(text)
text = text.split('\r\n')
print(text)

for i in range(len(text)):
    text[i] = '* ' + text[i]
print(text)
text = '\n'.join(text)
print(text)
pyperclip.copy(text)