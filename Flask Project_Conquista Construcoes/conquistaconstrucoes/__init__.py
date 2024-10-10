from flask import Flask
import urllib

app = Flask(__name__)
app.config["SECRET_KEY"] = "194956a1fc0a12fd039c34a1035fdbee"

email_pessoal = "jacksonconquistaconstrucoes@gmail.com"

@app.context_processor
def dados_whats():
    telefone_pessoal = "5511959614465"
    mensagem_whats = "Olá, gostaria de fazer um orçamento. Pode me ajudar?"
    msg_link = urllib.parse.quote(mensagem_whats)
    whats = f"https://wa.me/{telefone_pessoal}?text={msg_link}"
    return {"whats":whats, "email_pessoal":email_pessoal, "msg_link":msg_link}

from conquistaconstrucoes import routes