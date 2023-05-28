from pdf2image import convert_from_path

class Imagem():
    def __init__(self):
        self.pdfName = None


    def extractPdfToImage(self):
        # Caminho para o arquivo PDF
        pdf_path = './Projeto/Controle/Download/matrizes_curriculares/BachareladoemCienciadaComputacao.pdf'

        # Converte as páginas do PDF em imagens

        images = convert_from_path(pdf_path)

        # Itera sobre as imagens e salva cada uma delas em um arquivo
        for i, image in enumerate(images):
            image.save(f'pagina_{i + 1}.jpg', 'JPEG')

