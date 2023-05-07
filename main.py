import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
import requests
class Pdf():
    def __init__(self,y):
        self.pdfLink = y
        self.pdfDownload()



    def pdfDownload(self):
        print(self.pdfLink)
        response = requests.get(''+str(self.pdfLink))

        if response.status_code == 200:
            with open('arquivo.pdf', 'wb') as f:
                f.write(response.content)
        else:
            print('Erro ao solicitar o arquivo PDF')


class Web():
    def __init__(self):
        options = EdgeOptions()
        self.driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

        #Tipos de dados

        #Selector 1-
        #content-section > div > div.item-page > ul:nth-child(21) > li:nth-child(4) > strong > a

        #Caminho Js 2-
        #document.querySelector("#content-section > div > div.item-page > ul:nth-child(21) > li:nth-child(4) > strong > a")

        #Estilos 3-
        """
            -webkit-text-size-adjust: 100%;
            -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            line-height: 1.5em!important;
            font-size: 1em;
            font-weight: bold;
            list-style: none;
            vertical-align: baseline;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            outline: medium none;
            background-color: transparent;
            color: #337ab7;
            text-decoration: none;
        """
        #XPATH-completo
        #/html/body/div[2]/main/div/div[2]/div[2]/section/div/div[1]/ul[2]/li[4]/strong/a

        #XPATH
        #// *[ @ id = "content-section"] / div / div[1] / ul[2] / li[4] / strong / a

        self.dicionarioPrintipal = {
            'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html':
                [
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',

                ],
            'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html':
                [
                    '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
                    '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',

                ]


        }


    def defTypeCommand(self,y):
        if 'id' in y:
            self.driver.find_element(By.XPATH, value='' + str(y)).click()
            return 'xpath'
        elif '/html' in y:
            self.driver.find_element(By.XPATH, value='' + str(y)).click()
            return 'xpath'
        elif 'content' in y:
            self.driver.find_element(By.CSS_SELECTOR, value='' + str(y)).click()
            return 'css_selector'
        elif 'pdfDownloadLinkUrl':
            self.driver.close()
            time.sleep(3)
            print(self.driver.current_url)
            #self.pdf = Pdf(self.driver.current_url)
            return 'pdfDownloadLinkUrl'
        return None
    def Scraping(self):

        for x in self.dicionarioPrintipal.keys():

            self.driver.get(x)
            time.sleep(5)

            for y in self.dicionarioPrintipal.get(x):
                print(y)
                print(self.driver.current_url)
                dadoTrabalhado = self.defTypeCommand(y)
                time.sleep(3)



    def close(self):
        self.driver.close()


if __name__ == '__main__':
    Web = Web()
    Web.Scraping()
