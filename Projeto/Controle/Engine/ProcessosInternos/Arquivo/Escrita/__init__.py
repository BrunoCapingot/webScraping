import os
import pytesseract
from PIL import Image

class Escrita():
    def __init__(self):
        self.dirImage = None

    def imageToText(self):
        image_dir = 'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/imagens/'
        output_dir = 'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/textos/'
        pytesseract.pytesseract.tesseract_cmd = 'caminho_para_tesseract.exe'
        lang = 'por'
        for filename in os.listdir(image_dir):
            if filename.endswith('.jpg'):
                image_path = os.path.join(image_dir, filename)
                image = Image.open(image_path)
                text = pytesseract.image_to_string(image, lang=lang)
                text_filename = os.path.splitext(filename)[0] + '.txt'
                text_path = os.path.join(output_dir, text_filename)

                with open(text_path, 'w', encoding='utf-8') as file:
                    file.write(text)


