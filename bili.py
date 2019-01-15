import sys,webbrowser
import pyperclip

if len(sys.argv) > 1:
    address = sys.argv[1:]
    for i in address:
        webbrowser.open('https://search.bilibili.com/all?keyword=' + i)
else:
    address = pyperclip.paste()
    webbrowser.open('https://search.bilibili.com/all?keyword=' + address)


