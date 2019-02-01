# todo 简单的倒计时小程序

import time, subprocess

timeleft = 10
while timeleft > 0:
    print(timeleft, end=' ')
    time.sleep(1)
    timeleft = timeleft - 1

subprocess.Popen([r"C:\Program Files\VideoLAN\VLC\vlc.exe",r'C:\Users\bk201\Music\JAM Project - THE HERO !! ~怒れる拳に火をつけろ~.mp3'],shell=True)