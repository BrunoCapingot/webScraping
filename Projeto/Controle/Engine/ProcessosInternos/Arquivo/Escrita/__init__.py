from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.pilha import Stack
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.Pdf import Pdf
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.Mapa import Mapa
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os

import csv

class Escrita:
    def __init__(self):
        self.os = Os()
        self.pdf = Pdf()
        self.mapa = Mapa()
        self._dirSaveEscrita = None
        self._dirOrigemEscrita = None
        self._arqOrientado = None
        self._elementos = {
            'EMENTA': Stack(), 'BIBLIOGRAFIA BÁSICA': Stack(),
            'BIBLIOGRAFIA COMPLEMENTAR': Stack(), '-': Stack()
        }
        self._mapa_pilha = Stack()
        self._dados = None
        # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def setArquivo(self, nomeArquivo):
        self._arqOrientado = nomeArquivo

    def setSaveEscrita(self, caminho):
        self._dirSaveEscrita = caminho

    def setDirOrigemExcrita(self, caminho):
        self._dirOrigemEscrita = caminho

    def extrairTexto(self):
        diretorio_textos = r'\webScraping\Projeto\Controle\Download\Textos'
        diretorio_pdf = r'\webScraping\Projeto\Controle\Download\projetoPedagogicoCurso'
        self.os.setHomePonteiro()
        self.os.setDiretorio(diretorio_pdf)
        print(self.os.getPonteiro())
        nomes = self.os.getDirNameItens()
        for x in nomes:
            self.os.setHomePonteiro()
            self.os.setDiretorio(diretorio_pdf)
            print('{}-> Excutando extração de texto'.format(x))
            path_arquivo = self.os.getArqPath(x)
            self.pdf.setLocal(caminhoFracionado=diretorio_pdf)
            self.pdf.setNome(nomeArquivo=x)
            arquivo = self.pdf.open()
            conteudo = self.pdf.getContentInCondicao(condicao='extrairTexto', x=x, pdf=arquivo)
            self.os.setTxtName(str(x).replace('.pdf', ''))
            self.os.setHomePonteiro()
            self.os.setDiretorio(diretorio_textos)
            self.os.saveArqTxtInDir(str(conteudo), self.os.getPonteiro())

    def prepararArquivos(self):
        """condicionais de busca para cada arquivo"""
        diretorioOrigem = r'\webScraping\Projeto\Controle\Download\Textos'
        self.os.setHomePonteiro()
        self.os.setDiretorio(diretorioOrigem)
        nomes = self.os.getDirNameItens()
        self.mapa.setEstrutura('prepararArquivo')
        for nomeArq in nomes:
            for index in self.mapa.getCondicional().items():
                arquivo = index[0]
                if nomeArq == arquivo:
                    condicoes = index[1]
                    self.os.setHomePonteiro()
                    self.os.openArq(diretorioOrigem + '\\' + nomeArq, 'r', 'utf-8')
                    self._arqOrientado = self.os.getConteudoArquivo()
                    self.os.closeArq()
                    self.mapearDadosCondicionados(condicoesPack=condicoes)
        print('\nMapa do arquivo  {}  em relação a condicionais-->  {}\n'.format(nomeArq, self._mapa_pilha))
        print('\nIniciando mapeamento dos Dados  {}  em relação a condicionais--|\n'.format(nomeArq))
        self.mapearDados()



    def mapearDadosCondicionados(self, condicoesPack):
        diretorioDestino = r'webScraping\Projeto\Controle\Download\Csv'
        suport = 0
        dados = self._arqOrientado.split('\n')
        for linha in dados:
            for condicoes in condicoesPack:
                if condicoesPack.index(condicoes) == 0:
                    for palavraDeBusca in condicoes:
                        if palavraDeBusca in linha:
                            self._elementos[palavraDeBusca].push(str(suport)+','+palavraDeBusca)
                            # self.os.escreverInArq(diretorioDestino + '\\' + nomeArq.replace('txt', 'csv'), 'w', 'utf-8',str(dados_separados))
            # Marcador de linha
            suport += 1
            self.ordenarPilha(dict=self._elementos)

    def ordenarPilha(self, dict):
        lista = list()
        for key in dict.keys():
            if not dict[key].isEmpty():
                a = dict[key].pop()
                lista.append(a)
        lista = sorted(lista)
        lista.reverse()
        for x in range(0,len(lista)):
            self._mapa_pilha.push(lista[x])
        #print('Pilha mapeada -> {}'.format(self._mapa_pilha))
        # self.os.setHomePonteiro()
        # self.os.saveArqInDir(str(self.csv.getList()), diretorioDestino, nomeArq.replace('.txt', '.csv'))

    def mapearDados(self):
        while not self._mapa_pilha.isEmpty():
            dado = self._mapa_pilha.pop().split(',')
            print(dado)
            print(self._dados[dado[0]])
            suport = dado[0]
            palavra_de_busca = dado[1]
