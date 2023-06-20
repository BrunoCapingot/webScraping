import os
import os


class Os:
    def __init__(self):
        self.caminho = None
        self.suportList = []
        self.ponteiro = None
        self.txtName = None
        self.arquivoOpen = None
        self.arquivoClose = None

    def setDiretorio(self, caminho):
        self.caminho = caminho
        print('Diretorio convertido para: {}'.format(self.caminho))

    def limpaDir(self):
        for file_name in os.listdir(self.caminho):
            file_path = os.path.join(self.caminho, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Erro ao excluir {file_path}: {e}")

        if not os.listdir(self.caminho):
            print(f"O diretório {self.caminho} foi limpo com sucesso.")
        else:
            print(f"O diretório {self.caminho} não pôde ser limpo.")

    def setTxtName(self, name):
        self.txtName = name

    def getDirNameItens(self):
        self.suportList = []
        for nomes in os.listdir(self.caminho):
            self.suportList.append(nomes)
        return self.suportList

    def getArqPath(self, arquivo):
        return os.path.join(self.caminho, arquivo)

    def homeDir(self):
        self.ponteiro = os.path.join(os.path.expanduser("~"), "Desktop")
        return self.ponteiro

    def saveArqTxtInDir(self, conteudoTxt, caminhoString):
        caminho = os.path.join(self.homeDir() + caminhoString)
        file_path = os.path.join(caminho, '{}.txt'.format(self.txtName))
        # print('Salvando arquivo txt gerado em: {}'.format(file_path))
        with open(file_path, 'w') as arquivo:
            arquivo.write(conteudoTxt)
        print(f"O arquivo foi salvo em: {file_path}")

    def buscaConteudoTxt(self, caminho, modo):
        arquivo = open(caminho, modo)
        conteudo = arquivo.read()
        arquivo.close()
        return conteudo