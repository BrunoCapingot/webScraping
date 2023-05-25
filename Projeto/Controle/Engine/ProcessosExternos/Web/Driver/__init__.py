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

    def getListLink(self):
        urls = []
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            urls.append(self.driver.current_url)
        return urls


    def clickFromCssSelector(self, comand):
        self.driver.find_element(By.CSS_SELECTOR, value=str(comand)).click()

    def clickFromXpath(self, comand):
        self.driver.find_element(By.XPATH, value=str(comand)).click()

    def close(self):
        self.driver.close()
    def open(self,link):
        self.driver.get(link)
    def quit(self):
        self.driver.quit()