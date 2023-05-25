import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

class Driver():
    def __init__(self):
        self.options = EdgeOptions()
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=self.options
        )

    def clickHtmlCompleto(self,comand):
        self.driver.find_element(By.CSS_SELECTOR, comand).click()


    def close(self):
        pass
    def open(self,link):
        self.driver.get(link)
    def quit(self):
        pass