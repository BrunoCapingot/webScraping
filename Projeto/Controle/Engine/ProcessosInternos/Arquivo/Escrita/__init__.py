import pytesseract
import cv2


class Escrita():
    def __init__(self):
        self.dirImage = None


    def imageToText(self):

        output_dir = './Controle/ImageText/textos'
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        imagem = cv2.imread("./Controle/PdfDownload/BachareladoemAgronomia.png")
        print(imagem)

        #imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        #text = pytesseract.image_to_string(imagem)
        text = ''
        #text = text.replace(' ', '')
        text = text.replace('\n', ' ')
        text = text.replace('/', '')
        text = text.replace('o', '')
        text = text.replace('°', '')
        text = text.replace('=', '')
        text = text.replace('[', '')
        text = text.replace(']', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace('|', ',')
        text = text.replace(', ,', ',')
        text = text.replace('i', '')
        text = text.replace('=', '')
        text = text.replace('!', '')
        with open('dados.txt', 'w') as escrita:
            escrita.write(text)
            escrita.close()
        """
        text = text.replace('i', '')
        

        text = text.replace('=', '')
        text = text.replace('!', '')"""


es = Escrita()
es.imageToText()