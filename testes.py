import cv2
import pytesseract

def extrair_dados_imagem(imagem):
    # Converter a imagem para escala de cinza
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar binarização adaptativa na imagem em escala de cinza
    _, imagem_bin = cv2.threshold(imagem_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Aplicar detecção de contornos na imagem binarizada
    contornos, _ = cv2.findContours(imagem_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrar os contornos para selecionar apenas os que representam as células da tabela
    regioes_interesse = []
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 1000:  # Defina um limiar adequado para filtrar as regiões de interesse
            x, y, w, h = cv2.boundingRect(contorno)
            regiao = imagem[y:y+h, x:x+w]
            regioes_interesse.append(regiao)

    # Extrair o texto de cada célula da tabela
    dados_extraidos = []
    for celula in regioes_interesse:
        texto = pytesseract.image_to_string(celula)
        dados_extraidos.append(texto)

    return dados_extraidos

# Carregar a imagem da tabela
imagem = cv2.imread("caminho/para/imagem.png")

# Extrair os dados da imagem
dados_extraidos = extrair_dados_imagem(imagem)

# Exibir os dados extraídos
for dado in dados_extraidos:
    print("Dado extraído:", dado)
