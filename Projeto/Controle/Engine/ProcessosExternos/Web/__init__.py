from .Driver import Driver



class Web():
    def __init__(self):
        self.driver = Driver()



    def getLinksAbertos(self):
        urls = []
        for aba in self.driver.window_handles:
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
        
    def defTypeElement(self,y):

        if '/html' in y:
            self.PreComando = self.driver.find_element(By.XPATH,value='{}'.format(y)).click()
            return self.PreComando

        elif 'pdfDownloadLinkUrl' in y:
            links = self.getLinksAbertos()
            for i, link in enumerate(links):
                if '.pdf' in link:
                    return link


    def driverOpen(self,x):
        self.driver.get(x)

