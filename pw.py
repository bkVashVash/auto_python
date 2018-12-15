#! python3
# pw.py

passwords = {'email':'fghykkljhjghddde557666879',
             'blog':'jlklkgdffllkl;khghd7788990-',
             'luggage':'12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print(sys.argv)
    sys.exit()

print(sys.argv)
account = sys.argv[1]
print(account in passwords)
if account in passwords:
    pyperclip.copy(passwords[account])
    print('你的密码在黏贴板' + account)
else:
    print('没有这个账户')
