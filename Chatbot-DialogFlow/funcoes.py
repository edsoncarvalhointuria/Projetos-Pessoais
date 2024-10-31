from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Função que analisa tamanho do texto em relação à imagem
def quebra_de_linha(item, x_figura, draw, font, is_obs=False):
    itens = item.split(" ")
    texto_final = "\n"
    for i, texto in enumerate(itens):
        tamanho = draw.textlength(texto_final[texto_final.rindex("\n")+1:] + ", ", font)
        if tamanho > x_figura-40:
            texto_final += "\n"
        if is_obs:
            texto_final += texto + " " if i+1 != len(itens) else texto + "."
        else:
            texto_final += texto + ", " if i+1 != len(itens) else texto + "."
    return texto_final[1:]

# Função para criar a imagem do recibo
def desenhar_recibo(num_pedido, itens, qtd, total):
    # Configurações da imagem
    fundo = "black"
    fonte_cor = "white"
    tamanho_x, tamanho_y = (500, 400)
    
    # Criar imagem vazia
    imagem = Image.new("RGB", (tamanho_x, tamanho_y), fundo)
    draw = ImageDraw.Draw(imagem)

    #Se não encontrar a fonte
    try:
        fonte_titulo = ImageFont.truetype("COOPBL.TTF", 20)
        fonte_texto = ImageFont.truetype("MAIAN.TTF", 16) 
    except:
        fonte_titulo = ImageFont.load_default(20)
        fonte_texto = ImageFont.load_default(16)
  
    # Título do recibo
    draw.text((10, 10), f"Pedido nº: {num_pedido}", font=fonte_titulo, fill=fonte_cor)

    itens_ajustado = []
    for texto in itens:
        resultado = quebra_de_linha(texto, x_figura=tamanho_x, draw=draw, font=fonte_texto, is_obs=True if "Observacoes" in texto else False)
        resultado = resultado.split("\n")
        if len(resultado) > 1:
            for quebra in resultado:
                print("entrei aqui2")
                itens_ajustado.append(quebra)
        else:
            itens_ajustado.append(texto)

    # Itens do pedido
    pedido_texto = [
        "",
        f"Data: {datetime.now().strftime("%d/%m/%Y")}",
        "---------------------------------------------------------------------------------------------------------",
        *itens_ajustado,
        "---------------------------------------------------------------------------------------------------------",
        f"Quantidade: {qtd}",
        f"Total: R${total}",
    ]

    # Desenhar o texto na imagem
    y_texto = 40
    for linha in pedido_texto:
        teste = draw.textlength(linha, fonte_texto)
        draw.text((10, y_texto), linha, font=fonte_texto, fill=fonte_cor)

        y_texto += 25
    return imagem