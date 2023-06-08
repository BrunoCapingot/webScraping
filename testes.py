import pytesseract
import cv2

class Escrita():
    def __init__(self):
        self.dirImage = None


    def imageToText(self):

        output_dir = r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/textos'
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

        dados = ''
        with open('BachareladoemAgronomia.png', 'rb') as data:
            dados = data.read()

        text = pytesseract.image_to_string(dados)
        print(text)
