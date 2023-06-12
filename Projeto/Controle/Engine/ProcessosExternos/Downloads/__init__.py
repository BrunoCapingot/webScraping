from Projeto.Controle.Engine.ProcessosExternos.Downloads.Pdf import Pdf
import re

class Downloads():
    def __init__(self):
        self.pdf = Pdf()

    def remover_caracteres_especiais(self,texto):
        # Dicionário de substituição de caracteres acentuados
        substituicoes = {
            'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
            'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
            'ç': 'c', 'ñ': 'n', '.': ''
        }

        # Remove os acentos, caracteres especiais e espaços em branco
        texto_sem_acentos = ''.join(substituicoes.get(c, c) for c in texto)
        texto_sem_especiais = re.sub(r'[^a-zA-Z0-9]', '', texto_sem_acentos)
        texto_sem_espacos = texto_sem_especiais.replace(' ', '')


        return texto_sem_espacos

    def iniciarDownload(self,link,tituloPdf):
        self.pdf.setTitulo(self.remover_caracteres_especiais(tituloPdf))
        self.pdf.setLink(link)
        self.pdf.download()
