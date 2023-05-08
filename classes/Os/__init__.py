import os
class Os():
    def __init__(self,path):
        self.dir_path = os.path.abspath(path)


    def clearDir(self):


        for file_name in os.listdir(self.dir_path):
            file_path = os.path.join(self.dir_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Erro ao excluir {file_path}: {e}")

        if not os.listdir(self.dir_path):
            print(f"O diretório {self.dir_path} foi limpo com sucesso.")
        else:
            print(f"O diretório {self.dir_path} não pôde ser limpo.")