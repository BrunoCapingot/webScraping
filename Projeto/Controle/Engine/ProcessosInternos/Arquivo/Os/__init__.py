import os

class Os():
    def __init__(self):
        self.caminho = None

    def setDiretorio(self,caminho):
        self.caminho = caminho

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

    def mover_arquivos(self, destino, dataInput):
        for arquivos in dataInput:
            for arquivo in arquivos:
                print(os.listdir(os.getcwd()))
                caminho_origem = os.path.join('PdfDownload', arquivo)
                caminho_destino = os.path.join(destino, arquivo)
                os.rename(caminho_origem, caminho_destino)
