from flask_wtf import FlaskForm
from wtforms.fields import EmailField, StringField, TelField, TextAreaField, SubmitField
from wtforms.validators import Email, DataRequired

class EnviarEmail(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = EmailField("Email", validators=[Email(), DataRequired()])
    telefone = TelField("Telefone", validators=[DataRequired()])
    mensagem = TextAreaField("Mensagem", validators=[DataRequired()])
    botao = SubmitField("Enviar")