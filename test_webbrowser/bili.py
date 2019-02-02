import sys,webbrowser
import pyperclip

# todo 实现搜索
if len(sys.argv) > 1:
    # todo 如果关键字是多个
    address = sys.argv[1:]
    for i in address:
        webbrowser.open('https://search.bilibili.com/all?keyword=' + i)
else:
    # todo 如果关键字是 1 个
    address = pyperclip.paste()
    webbrowser.open('https://search.bilibili.com/all?keyword=' + address)

# todo 模拟命令行运行

# if __name__ == '__main__':
#     import os
#     os.system("python bili.py 亮剑")

