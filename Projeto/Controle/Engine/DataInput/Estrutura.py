class Estrutura():
    def __init__(self):
        self.estrutura = None
        self.indexNumerico = 0
        self.indexString = ''

    def setDataEstrutucture(self,dataInput):
        list = []
        for x in dataInput:
            list.append(x)
        self.estrutura = list[0][1]

    def setIndexNumerico(self,numericIndex):
        self.indexNumerico = numericIndex

    def setIndexString(self,string):
        self.indexString = string

    def setEstrutura(self):
        self.estrutura = self.estrutura[0][1][self.indexNumerico][self.indexString]

    def getEstrutura(self):
        return self.estrutura[self.indexNumerico]

    def getEstructureComand(self):
        return self.estrutura[self.indexNumerico][self.indexString]

