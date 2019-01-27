# import PyPDF2
#
#
# pdffile = open('2.pdf','rb')
# pdfreader = PyPDF2.PdfFileReader(pdffile)
#
# pageobj = pdfreader.getPage(0)
# print(pageobj.extractText().split('\n'))


from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    '''从pdf输出文本'''
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = open('2.pdf','rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()