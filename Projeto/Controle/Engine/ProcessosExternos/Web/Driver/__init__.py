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




    def driverClose(self):
        pass
    def driverOpen(self,link):
        self.driver.get(link)
    def driverQuit(self):
        pass