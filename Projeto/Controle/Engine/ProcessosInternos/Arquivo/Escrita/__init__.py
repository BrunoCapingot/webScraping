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

    def defineTextPdfPath(self):
        diretorio = r'C:\Users\CPGTEnterprise\Desktop\webScraping\Projeto\Controle\Download\matrizes_curriculares'
        self.os.setDiretorio(diretorio)
        nomes = self.os.getDirNameItens()
        listPrin = []
        for nome in nomes:
            listPrin.append(nome)
            if nome == 'BachareladoemAgronomia.pdf':
                listPrin.remove(nome)
            elif nome == 'BachareladoemCienciadaComputacao.pdf':
                listPrin.remove(nome)
            elif nome == 'TecnologiaemAlimentos.pdf':
                listPrin.remove(nome)
            elif nome == 'TecnologiaemSistemasparaInternet.pdf':
                listPrin.remove(nome)
        for arquivo in listPrin:
            diretorio = r'C:\Users\CPGTEnterprise\Desktop\webScraping\Projeto\Controle\Download\matrizes_curriculares'
            self.os.setDiretorio(diretorio)
            with open(diretorio+'\\'+arquivo,'rb') as _pdf:
                text = ''
                pdf = PyPDF2.PdfReader(_pdf)
                numeroPaginas = len(pdf.pages)
                for pagina in range(numeroPaginas):
                    page = pdf.pages[pagina]
                    text += page.extract_text()
                self.os.setTxtName(arquivo)
                self.os.saveArqTxtInDir(text,'\\webScraping\\Projeto\\Controle\\Download\\Textos\\')

    def defineImagemPath(self):
        diretorio = r'C:\Users\CPGTEnterprise\Desktop\webScraping\Projeto\Controle\Download\Imagens'
        self.os.setDiretorio(diretorio)
        nomes = self.os.getDirNameItens()
        for nome in nomes:
            self.dirImage = nome
            self.imageToText(self.dirImage)

    def imageToText(self, arquivo):
        imagem_path = self.os.getArqPath(arquivo)
        self.os.setTxtName(imagem_path.split('\\')[-1].replace('.jpg', ''))
        imagem = Image.open(imagem_path)
        texto = pytesseract.image_to_string(imagem)
        # celulas_tabela = self.segmentar_tabela(imagem)
        # Aplicar OCR em cada célula da tabela
        # for celula in celulas_tabela:
        #     texto = pytesseract.image_to_string(celula)
        texto = texto.replace("\n\n", "")
        self.os.saveArqTxtInDir(texto, self.dirSaveEscrita)

    """def segmentar_tabela(self,imagem):
        # Converter a imagem para escala de cinza
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # Aplicar binarização adaptativa na imagem em escala de cinza
        _, imagem_bin = cv2.threshold(imagem_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        # Aplicar detecção de contornos na imagem binarizada
        contornos, _ = cv2.findContours(imagem_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filtrar os contornos para selecionar apenas os que representam as células da tabela
        regioes_interesse = []
        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area > 1000:  # Defina um limiar adequado para filtrar as regiões de interesse
                x, y, w, h = cv2.boundingRect(contorno)
                regiao = imagem[y:y+h, x:x+w]
                regioes_interesse.append(regiao)

        return regioes_interesse
    """


