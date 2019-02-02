# todo 获取时时 坐标 和 rgb值  ,
# todo  实现自动在后台填表

import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# todo 获取时时 坐标 和 rgb值  
# print(pyautogui.position())
# try:
#     while True:
#         x,y = pyautogui.position()
#         cc = 'x:' + str(x) + ' ' + 'y:' + str(y)
#         pixel_color = pyautogui.screenshot().getpixel((x,y))
#         cc += '  rgb:' + str(pixel_color[0])
#         cc += ',' + str(pixel_color[1])
#         cc += ',' + str(pixel_color[2])
#
#         print(cc,end='')
#         time.sleep(1)
#         print('\b' * len(cc),end='',flush=True)
#
# except KeyboardInterrupt:
#     print('完成！！')


# todo  实现自动在后台填表

year = (687,440)
make_sure = (1050,835)

form_data = [{'qishu':'20190202','date':'2019-02-02',
              'laiyuan':'http://www.cnepaper.com/yjhlb/'}]

for i in form_data:
    time.sleep(5)
    pyautogui.click(year)
    pyautogui.click(year)

    time.sleep(1)
    pyautogui.typewrite(['\t','\t'])
    time.sleep(1)
    pyautogui.typewrite(i['qishu'] + '\t')
    pyautogui.typewrite(i['date'] + '\t')
    pyautogui.typewrite(['\t'])
    pyautogui.typewrite(i['laiyuan'] + '\t')

