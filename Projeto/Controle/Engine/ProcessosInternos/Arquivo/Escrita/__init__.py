import os
from PIL import Image
import pytesseract


class Escrita():
    def __init__(self):
        self.dirImage = None


    def defineImagemPath(self):
        diretorio = r'C:\Users\CPGT\Desktop\webScraping\Projeto\Controle\Imagens'
        for nome in os.listdir(diretorio):
            self.dirImage = nome
            self.imageToText(diretorio, self.dirImage)

    def imageToText(self, caminho, arquivo):
        input_dir = r'{}'.format(caminho)
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        imagem_path = os.path.join(caminho, arquivo)
        try:
            imagem = Image.open(imagem_path)
            print("Tamanho da imagem:", imagem.size)
            print("Modo da imagem:", imagem.mode)

            # Aplicar OCR na imagem usando pytesseract
            texto = pytesseract.image_to_string(imagem)
            print("Texto extraído:", texto)

            # Salvar o texto em um arquivo
            nome_arquivo = os.path.splitext(arquivo)[0] + ".txt"
            caminho_arquivo = os.path.join(caminho, nome_arquivo)
            with open(caminho_arquivo, 'w') as arquivo_texto:
                arquivo_texto.write(texto)
            print("Texto salvo em:", caminho_arquivo)

        except IOError:
            print("Erro ao abrir a imagem.")

