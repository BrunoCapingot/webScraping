import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from ClassesControle.Pdf import Pdf


class Web():
    def __init__(self):
        self.titulo = None
        self.dicionarioPrincipal = None
        self.options = EdgeOptions()
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=self.options
        )

    def getLinksAbertos(self):
        urls = []
        for aba in self.driver.current_window_handle:
            self.driver.switch_to.window(aba)
            urls.append(self.driver.current_url)
        return urls

    def driverClose(self):
        print('Finalizando driver!')
        self.driver.close()
        self.driver.quit()

    def setLink(self,link):
        self.dicionarioPrincipal = link

    def setTitle(self,title):
        self.titulo = title

    def visibleElement(self,text):
        self.driver.find_element(By.XPATH, "//*[text()='{}']".format(text)).click()
        



    def driverOpen(self,x):
        self.driver.get(x)
