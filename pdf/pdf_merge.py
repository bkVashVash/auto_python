# todo 合并pdf文件, ---- 其实应该封装成函数的

import PyPDF2
import os
import datetime
from .str_sort import sort_string

# 这个叫什么都行
name = 'rmrb_spider'

pdfFiles = []
for filename in os.listdir(
        os.path.abspath('.') + '\\pdf\\{}'.format(name + '--' + datetime.datetime.now().strftime('%Y-%m-%d'))):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

# todo 对 数字-字符串 进行排序
pdfFiles = sort_string(pdfFiles)
writer = PyPDF2.PdfFileWriter()

for pdf in pdfFiles:
    reader = PyPDF2.PdfFileReader(
        os.path.abspath('.') + '\\pdf\\{}'.format(name + '--' + datetime.datetime.now().strftime('%Y-%m-%d'))
        + '\\' + pdf, strict=False)
    for i in range(reader.numPages):
        page = reader.getPage(i)
        page.compressContentStreams()
        writer.addPage(page)

with open(os.path.abspath('.') + '\\pdf\\{}'.format(
        name + '--' + datetime.datetime.now().strftime('%Y-%m-%d')) + '\\result.pdf', 'wb') as f:
    writer.write(f)