#! python3

'''
我喜欢鲁鲁修
我喜欢犬夜叉
我喜欢海贼王
'''

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

'''
* 我喜欢鲁鲁修
* 我喜欢犬夜叉
* 我喜欢海贼王
'''