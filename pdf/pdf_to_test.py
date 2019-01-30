# todo  输出pdf文本（中文），保存到变量

from urllib.request import urlopen
from io import StringIO
from io import open

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def readPDF(pdfFile):
    """从pdf输出文本"""
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


pdfFile = open('test.pdf','rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()