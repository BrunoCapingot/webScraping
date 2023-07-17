from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.pilha import Stack
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.Pdf import Pdf
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Escrita.Estrutura.Mapa import Mapa
from Projeto.Controle.Engine.ProcessosInternos.Arquivo.Os import Os


class Escrita:
    def __init__(self):
        self._os = Os()
        self._pdf = Pdf()
        self._mapa = Mapa()
        self._mapa_pilha = Stack()
        self._dados = None
        self._arqOrientado = None
        self._dirSaveEscrita = None
        self._dirOrigemEscrita = None
        self._elementos = {
            'EMENTA': Stack(), 'BIBLIOGRAFIA BÁSICA': Stack(),
            'BIBLIOGRAFIA COMPLEMENTAR': Stack(), '-': Stack()
        }
        # pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def setArquivo(self, nomeArquivo):
        self._arqOrientado = nomeArquivo

    def setSaveEscrita(self, caminho):
        self._dirSaveEscrita = caminho

    def setDirOrigemExcrita(self, caminho):
        self._dirOrigemEscrita = caminho

    def setDados(self, dados):
        self._dados = dados

    def extrairTexto(self):
        diretorio_textos = self._mapa.getCamadaDois(referencia_zero='enderecos', referencia_um='texto')
        diretorio_pdf = self._mapa.getCamadaDois(referencia_zero='enderecos', referencia_um='projetoPedagogico')
        self._os.setHomePonteiro()
        self._os.setDiretorio(diretorio_pdf)
        print(self._os.getPonteiro())
        nomes = self._os.getDirNameItens()
        for x in nomes:
            self._os.setHomePonteiro()
            self._os.setDiretorio(diretorio_pdf)
            print('{}-> Excutando extração de texto'.format(x))
            path_arquivo = self._os.getArqPath(x)
            self._pdf.setLocal(caminhoFracionado=diretorio_pdf)
            self._pdf.setNome(nomeArquivo=x)
            arquivo = self._pdf.open()
            self.setDados(self._pdf.getConteudo())
            conteudo = self._pdf.getContentInCondicao(condicao='extrairTexto', x=x, pdf=arquivo)
            self._os.setTxtName(str(x).replace('.pdf', ''))
            self._os.setHomePonteiro()
            self._os.setDiretorio(diretorio_textos)
            self._os.saveArqTxtInDir(str(conteudo), self._os.getPonteiro())

    def prepararArquivos(self):
        """condicionais de busca para cada arquivo"""
        diretorioOrigem = self._mapa.getCamadaDois(referencia_zero='enderecos', referencia_um='texto')
        self._os.setHomePonteiro()
        self._os.setDiretorio(diretorioOrigem)
        nomes = self._os.getDirNameItens()
        indexList = self._mapa.getCamadaUm(referencia_zero='prepararArquivo')
        # self._mapa.setEstrutura('prepararArquivo')
        for nomeArq in nomes:
            for index in indexList:
                if nomeArq == index:
                    self._os.setHomePonteiro()
                    self._os.openArq(diretorioOrigem + '\\' + nomeArq, 'r', 'utf-8')
                    self._arqOrientado = self._os.getConteudoArquivo()
                    self._os.closeArq()
                    self.mapearDadosCondicionados(
                        self._mapa.getCamadaDois(referencia_zero='prepararArquivo',
                                                 referencia_um=nomeArq))
                    print('\nMapa do arquivo  {}  em relação a condicionais-->  {}\n'.format(nomeArq, self._mapa_pilha))
                    print('\nIniciando mapeamento dos Dados  {}  em relação a condicionais--|\n'.format(nomeArq))
                    self.mapearDados()

    def mapearDadosCondicionados(self, condicoesPack):
        diretorioDestino = self._mapa.getCamadaDois(referencia_zero='enderecos', referencia_um='csv')
        suport = 0
        dados = self._arqOrientado.split('\n')
        for linha in dados:
            for condicoes in condicoesPack:
                if condicoesPack.index(condicoes) == 0:
                    for palavraDeBusca in condicoes:
                        if palavraDeBusca in linha:
                            self._elementos[palavraDeBusca].push(str(suport) + ',' + palavraDeBusca)
                            #self._os.escreverInArq(diretorioDestino + '\\' + nomeArq.replace('txt', 'csv'), 'w', 'utf-8',str(dados_separados))
            # Marcador de linha
            suport += 1
            self.ordenarPilha(dict=self._elementos)

    def prepararCondicionais(self, condicoes):
        self._mapa.setEstruturaPrincipal(mapaCondicional=condicoes)
        self._pdf.setMapa(mapaCondicional=self._mapa.get_estruturaPrincipal())

    def ordenarPilha(self, dict):
        lista = list()
        for key in dict.keys():
            if not dict[key].isEmpty():
                a = dict[key].pop()
                lista.append(a)
        lista = sorted(lista)
        lista.reverse()
        for x in range(0, len(lista)):
            self._mapa_pilha.push(lista[x])


        #print('Pilha mapeada -> {}'.format(self._mapa_pilha))
        #self.os.setHomePonteiro()
        #self.os.saveArqInDir(str(self.csv.getList()), diretorioDestino, nomeArq.replace('.txt', '.csv'))

    def mapearDados(self):
        diretorioFracionado = self._mapa.getCamadaDois('enderecos', 'projetoPedagogico')
        self._os.setHomePonteiro()
        self._os.setDiretorio(diretorioFracionado=diretorioFracionado)
        nomes = self._os.getDirNameItens()
        for nomeArquivo in nomes:
            self._os.setHomePonteiro()
            self._os.setDiretorio(diretorioFracionado=diretorioFracionado)
            self._pdf.setNome(nomeArquivo=nomeArquivo)
            self._pdf.setLocal(caminhoFracionado=diretorioFracionado)
            pdf = self._pdf.open()
            self.setDados(self._pdf.getContentInCondicao('extrairTexto', nomeArquivo, pdf))
            self._dados = self._dados.split('\n')
            while not self._mapa_pilha.isEmpty():
                dado = self._mapa_pilha.pop().split(',')
                suport = int(dado[0])
                palavra_de_busca = dado[1]
                print('Linha {}-> {}'.format(suport, self._dados[suport]))
                if palavra_de_busca == 'BIBLIOGRAFIA BÁSICA':
                    print(suport)
                print('Linha {}-> {}'.format(suport, self._dados[suport]))
