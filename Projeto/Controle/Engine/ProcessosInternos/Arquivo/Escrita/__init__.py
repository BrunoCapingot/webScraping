from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os
# import pytesseract
import PyPDF2


class Escrita:
    def __init__(self):
        self.os = Os()
        self._dirSaveEscrita = None
        self._dirOrigemEscrita = None
        self._arqOrientado = None
        #pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def setArquivo(self, nomeArquivo):
        self._arqOrientado = nomeArquivo

    def setSaveEscrita(self, caminho):
        self._dirSaveEscrita = caminho

    def setDirOrigemExcrita(self, caminho):
        self._dirOrigemEscrita = caminho

    def extrairTexto(self):
        diretorio = r'C:\Users\CPGT\Desktop\webScraping\Projeto\Controle\Download\Textos'
        diretorio_fracionado = r'\webScraping\Projeto\Controle\Download\projetoPedagogicoCurso'
        self.os.setHomeDir()
        self.os.setDiretorio(diretorio_fracionado)
        nomes = self.os.getDirNameItens()
        for x in nomes:
            print('{}-> Excutando extração de texto'.format(x))
            path_arquivo = self.os.getArqPath(x)
            pdf = PyPDF2.PdfReader(path_arquivo)
            paginas = len(pdf.pages)
            texto = ''
            for k in range(0,paginas):
                page = pdf.pages[k]
                texto += page.extract_text()
            self.os.setTxtName(str(x).replace('.pdf',''))
            #texto = texto.replace('\n\n','\n')
            #texto = texto.split('\n')
            texto.replace('\n\n', '\n')
            texto = texto.lower()
            for k in texto.split('  '):
                print(k.index(0))
                #print(texto.index('ementa'))
                #print(texto[5313])
            self.os.saveArqTxtInDir(str(texto), diretorio)


    def prepararArquivos(self):
        diretorio_fracionado = r'\webScraping\Projeto\Controle\Download\Textos'
        self.os.setHomeDir()
        self.os.setDiretorio(diretorio_fracionado)
        nomes = self.os.getDirNameItens()
        texto = ''
        for nome in nomes:
            path_arquivo = self.os.getArqPath(nome)
            with open(path_arquivo,'r',encoding='utf-8') as arquivo:
                texto = arquivo.read()
            print(texto)
            input('Esperando')
