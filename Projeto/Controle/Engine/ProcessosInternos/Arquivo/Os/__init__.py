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

    def moveArqPara(self):
        pass