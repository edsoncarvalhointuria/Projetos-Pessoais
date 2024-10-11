from conquistaconstrucoes import app
from flask import render_template, redirect, url_for, request, flash
from .forms import EnviarEmail
import yagmail
import os

email_pessoal = "jacksonconquistaconstrucoes@gmail.com"
endereco_pessoal = "Rua Desembargador Áureo Cerqueira Leite, 152, São Paulo - SP"
telefone_pessoal = "(11) 95961-4465"

senha_app = os.environ['SENHA_APP']




@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/contato", methods=["POST", "GET"])
def contato():
    tel = "telefone"
    form_enviar_email = EnviarEmail()
    if form_enviar_email.validate_on_submit():
        formulario = request.form
        nome_cliente = formulario.get('nome')
        email_cliente = formulario.get('email')
        telefone_cliente = formulario.get('telefone')
        mensagem_cliente = formulario.get('mensagem')

        if nome_cliente and email_cliente and telefone_cliente and mensagem_cliente:
            body = f"Email Cliente: {email_cliente}\nNome Cliente: {nome_cliente}\nTelefone Cliente: {telefone_cliente}\n\nMensagem Cliente:\n"+mensagem_cliente
            username = yagmail.SMTP(email_pessoal, senha_app)
            subject = f"ORÇAMENTO - {nome_cliente} - {telefone_cliente}"
            username.send(to=email_pessoal, subject=subject, contents=body)
            
            flash("Email enviado, retornaremos em breve", category="alert-success")
            
    return render_template('contato.html', form_enviar_email=form_enviar_email, contato_infos={'telefone_pessoal':telefone_pessoal, 'endereco_pessoal':endereco_pessoal, 'email_pessoal':email_pessoal})

@app.route("/enviar")
def enviar_email():
    print(request.form)
    return render_template('contato.html')

@app.route("/sobrenos")
def sobre_nos():
    return render_template('sobrenos.html')

@app.route("/servicos")
def nossos_servicos():
    lista_servicos=[("Elétrica", "Instalações e reparos elétricos com segurança e eficiência.", "fas fa-bolt fa-3x"), 
                    ("Emissão de Laudo Técnico", "Laudos técnicos precisos e confiáveis para garantir a conformidade das suas obras.", "fas fa-file-alt fa-3x"),
                    ("Hidráulica", "Soluções completas para sua rede de água e esgoto.", "fas fa-water fa-3x"), 
                    ("Gesso", "Trabalhos em gesso com acabamentos perfeitos.", "fas fa-hard-hat fa-3x"), 
                    ("Pintura", "Pintura residencial e comercial com acabamento profissional.", "fas fa-paint-roller fa-3x"), 
                    ("Azulejo", "Colocação e reparo de azulejos para cozinhas, banheiros e mais.", "fas fa-th fa-3x"), 
                    ("Cerâmica", "Revestimentos cerâmicos com precisão e qualidade.", "fas fa-th-large fa-3x"), 
                    ("Porcelanato", "Instalação de porcelanato com acabamentos sofisticados.", "fas fa-th fa-3x"), 
                    ("Tubulação de Gás", "Execução e reparos em tubulações de gás com segurança garantida.", "fas fa-gas-pump fa-3x"), 
                    ("Vidro Temperado", "Fornecimento e instalação de vidros temperados de alta resistência.", "fas fa-window-maximize fa-3x"),
                    ]
    centro = False
    if len(lista_servicos)%3 == 1:
        centro = True

    return render_template('servicos.html', lista_servicos=lista_servicos, centro=centro)

@app.route('/google71cdbdd016a1c5b4.html')
def arquivo_google():
    return render_template('google71cdbdd016a1c5b4.html')
