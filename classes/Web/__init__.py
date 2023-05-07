import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from classes.Pdf import Pdf

class Web():
    def __init__(self,links,title):
        print('Iniciando driver')
        self.titulo = title
        options = EdgeOptions()
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
        self.dicionarioPrintipal = links


    def driverClose(self):
        print('Finalizando driver!')
        self.driver.close()
        self.driver.quit()

    def defPdfLink(self):
        urls = []
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            urls.append(self.driver.current_url)
        for x in urls:
            if '.pdf' in x:
                self.pdf = Pdf(x,self.titulo)
                del self.pdf
    def comandoBuscaPorTipo(self,y):
        time.sleep(5)

        if 'id' in y:
            self.driver.find_element(By.XPATH, value='' + str(y)).click()
            return 'xpath'
        elif '/html' in y:
            self.driver.find_element(By.XPATH, value='' + str(y)).click()
            return 'xpath'
        elif 'content' in y:
            self.driver.find_element(By.CSS_SELECTOR, value='' + str(y)).click()
            return 'css_selector'
        elif 'pdfDownloadLinkUrl' in y:
            self.defPdfLink()
            return 'pdfDownloadLinkUrl'
        elif 'finishWeb' in y:
            self.driverClose()
            return 'finishWeb'

    def comandoBuscaPorTexto(self):
        pass


    def Scraping(self):

        for x in self.dicionarioPrintipal.keys():
            self.driver.get(x)
            [self.comandoBuscaPorTipo(y) for y in self.dicionarioPrintipal.get(x)]





