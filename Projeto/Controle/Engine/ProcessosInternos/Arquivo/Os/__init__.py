import csv
import os


class Os:
    def __init__(self):
        self.caminho = None
        self.suportList = []
        self.ponteiro = None
        self.txtName = None
        self.arquivo = None
        self.arquivoClose = None

    def setDiretorio(self, diretorioFracionado):
        self.caminho = diretorioFracionado
        self.ponteiro = self.ponteiro + diretorioFracionado
        print('Os-> Diretorio convertido para: {}'.format(self.caminho))
        print('Os-> Ponteiro diretorio aponta para: {}'.format(self.ponteiro))

    def escreverInArq(self, caminho, modo, codificacao, conteudo):
        """caminho modo codificação"""
        self.openArq(caminho=caminho, modo=modo, codificacao=codificacao)
        self.arquivo.write(conteudo+'\n')
        self.closeArq()
        return None

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
        for nomes in os.listdir(self.ponteiro):
            self.suportList.append(nomes)
        return self.suportList

    def getArqPath(self, arquivo):
        return self.ponteiro+'\\'+arquivo

    def setHomePonteiro(self,):
        self.ponteiro = os.path.join(os.path.expanduser("~"), "Desktop")

    def getPonteiro(self):
        return self.ponteiro

    def saveArqTxtInDir(self, conteudoTxt, caminhoString):
        caminho = os.path.join(caminhoString)
        file_path = os.path.join(caminho, '{}.txt'.format(self.txtName))
        # print('Salvando arquivo txt gerado em: {}'.format(file_path))
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudoTxt)
        print(f"O arquivo foi salvo em: {file_path}")

    def saveArqInDir(self, conteudo, caminho, name):
        caminho = os.path.join(caminho)
        nome = str(name).split('.')
        extensao = nome[1]
        nome = nome[0]
        file_path = os.path.join(caminho, '{}.{}'.format(nome, extensao))
        # print('Salvando arquivo txt gerado em: {}'.format(file_path))
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        print(f"O arquivo foi salvo em: {file_path}")

    def getConteudoArquivo(self):
        conteudo = self.arquivo.read()
        return conteudo

    def openArq(self, caminho, modo, codificacao):
        self.setHomePonteiro()
        self.arquivo = open(self.getPonteiro()+'\\'+caminho, modo, encoding=codificacao)
        return None

    def closeArq(self):
        self.arquivo.close()
        return None

    def save_arq_csv_in_dir(self, conteudo_csv, caminho, nome_arquivo):
        caminho = os.path.join(caminho)
        nome = str(nome_arquivo).split('.')
        extensao = nome[1]
        nome = nome[0]
        file_path = os.path.join(caminho, '{}.{}'.format(nome, extensao))
        with open(file_path, 'w', encoding='utf-8', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(conteudo_csv)
        print(f"O arquivo CSV foi salvo em: {file_path}")

