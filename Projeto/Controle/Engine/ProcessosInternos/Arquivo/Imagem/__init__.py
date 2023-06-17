from pdf2image import convert_from_path
import os



class Imagem:
    def __init__(self):
        self.pdfName = None

    #agronomia
    #cienciasDaComputação
    #tecnologiaEmAlimentos
    #tecnologiaEmSistemasDaInternet


    def extractPdfToImage(self):
        listPath = [r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/BachareladoemAgronomia.pdf',
                    r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/BachareladoemCienciadaComputacao.pdf',
                    r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/TecnologiaemAlimentos.pdf',
                    r'C:/Users/CPGT/Desktop/webScraping/Projeto/Controle/Download/matrizes_curriculares/TecnologiaemSistemasparaInternet.pdf'
                    ]
        camino_destino = r'C:\Users\CPGT\Desktop\webScraping\Projeto\Controle\Imagens'
        for pdf_path in listPath:
            pdf_name = pdf_path.replace('.pdf','')
            images = convert_from_path(pdf_path)
            print('Convertendo pdf: {}'.format(pdf_name))
            for i, image in enumerate(images):
                image = image.convert('L')
                image.save(os.path.join(camino_destino, f'{pdf_name.split("/")[-1]}_pagina_{i + 1}.jpg'), 'JPEG')


