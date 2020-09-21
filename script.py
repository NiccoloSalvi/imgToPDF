# all the images must be saved in the directory <img>

from PyPDF2 import PdfFileMerger, PdfFileReader
from PIL import Image
import os

mergedObject = PdfFileMerger()
nomeFile = "pdfMerged" # nome del file merged
path = os.getcwd()
okFiles = [] # lista di file convertibili
extensions = ["jpg", "jpeg", "png"] # lista di estensioni accettabili

# rimuove gli altri i pdf delle singole pagine
def removePDFs():
    for f in os.listdir(path):
        if '.' in f: # se si tratta di un file e non di una cartella
            ex = f.split('.')
            if ex[1] == "pdf": # se l'estensione del file è accettabile
                os.remove(f)

def JPGtoPDF(okFiles):
    for f in okFiles:
        img = Image.open(path + "/img/" + f) # apertura immagine
        onlyFile = f.split('.') # nome del file
        imgConverted = img.convert('RGB') # conversione a colori
        imgConverted.save(onlyFile[0] + ".pdf") # nuova estensione del file
        mergedObject.append(PdfFileReader(onlyFile[0] + ".pdf", 'rb'))
    removePDFs()
    mergedObject.write(nomeFile + ".pdf") # creazione file merged
    os.startfile(nomeFile + ".pdf") # apre direttamente il file pdf
    
for f in os.listdir(path + "/img/"): # le immagini vengono salvate nella cartella img
    if '.' in f: # se si tratta di un file e non di una cartella
        ex = f.split('.')
        if ex[1] in extensions: # se l'estensione del file è accettabile
            okFiles.append(f) # aggiungi il file alla lista dei file accettabili

JPGtoPDF(okFiles) # traforma file in PDF
