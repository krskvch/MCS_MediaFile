from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import Table, SimpleDocTemplate
from MediaCore import FileListing
from MediaCore import Parser

def generator(numMessage):
    data = []
    data1 = []
    elements = []
    file = SimpleDocTemplate(FileListing.filesDict[int(numMessage)]+'.pdf', pagesize=A4)

    for key in Parser.outDict:
        data.append(key)
        data.append(Parser.outDict[key])
        data1.append(data)
        data = []
    repTable = Table(data1)
    repTable._argW[1] = 1.5 * inch
    elements.append(repTable)
    file.build(elements)







