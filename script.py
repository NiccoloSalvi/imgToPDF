from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image
import os

mergedObject = PdfFileMerger()
path = os.getcwd()
okFiles = []
extensions = ["jpg", "jpeg", "png"]

def removePDFs():
    for f in os.listdir(path):
        if '.' in f:
            ex = f.split('.')
            if ex[1] == "pdf":
                os.remove(f)

def removeImgs():
    for f in os.listdir(path + "/img/"):
        if '.' in f:
            os.remove(path + "/img/" + f)

def JPGtoPDF(okFiles):
    for f in okFiles:
        img = Image.open(path + "/img/" + f)
        onlyFile = f.split('.')
        imgConverted = img.convert('RGB')
        imgConverted.save(onlyFile[0] + ".pdf")
        mergedObject.append(PdfFileReader(onlyFile[0] + ".pdf", 'rb'))
    removePDFs()
    removeImgs()
    mergedObject.write(nomeFile + ".pdf")
    os.startfile(nomeFile + ".pdf")
    
for f in os.listdir(path + "/img/"):
    if '.' in f:
        ex = f.split('.')
        if ex[1] in extensions:
            okFiles.append(f)

nomeFile = input('File name: ')
JPGtoPDF(okFiles)
