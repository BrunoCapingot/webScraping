from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os
from PIL import Image
import pytesseract
import PyPDF2


class Escrita():
    def __init__(self):
        self.dirImage = None
        self.os = Os()
        self.dirSaveEscrita = r'\webScraping\Projeto\Controle\Download\Textos'
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


