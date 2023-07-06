from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.Mapa import Mapa

import PyPDF2


class Pdf:
    def __init__(self):
        self._os = Os()
        self._estrutura = Mapa()
        self._nome = None
        self._local = None
        self._conteudo = None
        self._linha = None
        self._text = None
        self._pdf = None

    def setLocal(self, caminhoFracionado):
        self._local = caminhoFracionado

    def open(self):
        self._os.setHomePonteiro()
        self._os.setDiretorio(self._local)
        path_arquivo = self._os.getArqPath(self._nome)
        print('Abrindo Pdf caminho-> {}'.format(path_arquivo))
        self._pdf = PyPDF2.PdfReader(path_arquivo)
        return self._pdf

    def setNome(self, nomeArquivo):
        self._nome = nomeArquivo

    def getConteudo(self):
        conteudo = ""
        for pagina in self._pdf.pages:
            conteudo += pagina.extract_text()
        self._conteudo = conteudo
        return self._conteudo

    def getContentInCondicao(self, condicao, x, pdf):
        tabelas = ''
        paginas = len(pdf.pages)
        self._estrutura.setEstrutura(condicao)
        mapa_arquivos = self._estrutura.getCondicional()
        for mapa in mapa_arquivos:
            if x == mapa_arquivos[mapa][0]:
                valor = mapa_arquivos[mapa][1]
                if type(valor) == int:
                    for k in range(0, paginas):
                        page = pdf.pages[k]
                        if mapa_arquivos[mapa][2] >= k >= mapa_arquivos[mapa][1]:
                            tabelas += page.extract_text()
                elif type(valor) == list:
                    for intervalo in valor:
                        for k in range(0, paginas):
                            page = pdf.pages[k]
                            if intervalo[1] >= k >= intervalo[0]:
                                tabelas += page.extract_text()
        self._conteudo = tabelas
        return self._conteudo

    def getInvertaloTexto(self, inicio, fim):
        return self._pdf.extract_text(int(inicio), int(fim))
