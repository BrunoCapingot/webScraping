import time
from Web import Web

dicionarioPrintipal = {
    'agronomia': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [

        '/html/body/div[2]/main/div/div[2]/div[2]/section/div/div/div[2]/form/div[2]/div[1]/div[1]/h2/a',
        '//*[@id="content-section"]/div/div[1]/ul[2]/li[4]/strong/a',
        'pdfDownloadLinkUrl',
        'finishWeb',
    ]},
    'cienciasDaComputacao': {'https://www.ifgoiano.edu.br/home/index.php/cursos-superiores-morrinhos.html': [
        '//*[@id="adminForm"]/div[2]/div[2]/div[1]/h2/a',
        '//*[@id="content-section"]/div/div[1]/ul[2]/li[2]/strong/a',
        'pdfDownloadLinkUrl',
        'finishWeb',
    ]}

}
if __name__ == '__main__':
    for x in dicionarioPrintipal.keys():
        print('Etapa: ' + x + ' iniciada com sucesso"')
        web = Web(dicionarioPrintipal.get(x))
        web.Scraping()
        del web
        print('Etapa: ' + x + ' finalizada com sucesso"')


