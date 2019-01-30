# todo 优化pdf大小 (调用命令行工具)

import os,datetime
name = 'rmrb_spider'

cc = "gswin32c.exe -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=" \
     "{} {}".format(os.path.abspath('.') + '\\pdf\\{}'.format(
    name + '--' + datetime.datetime.now().strftime('%Y-%m-%d') + '\\result1.pdf'),
                    os.path.abspath('.') + '\\pdf\\{}'.format(
                        name + '--' + datetime.datetime.now().strftime('%Y-%m-%d') + '\\result.pdf'))
os.system("{}".format(cc))