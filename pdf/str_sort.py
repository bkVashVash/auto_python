# todo  Python排序数值字符串

import re

re_digits = re.compile(r'(\d+)')


def embedded_numbers(s):
    pieces = re_digits.split(s)  # 切成数字和非数字
    pieces[1::2] = map(int, pieces[1::2])  # 将数字部分转成整数
    return pieces


def sort_string(lst):
    return sorted(lst, key=embedded_numbers)


if __name__ == '__main__':
    cc = ['第011版', '第010版','第02版']
    print(sort_string(cc))