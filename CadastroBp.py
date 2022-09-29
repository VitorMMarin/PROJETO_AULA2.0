#Importando o Blueprint
from flask import Blueprint, render_template
from ..extensions import db
from ..models.Cadastro import Cadastro
#Instanciando o Blueprint

CadastroBp = Blueprint('CadastroBp',__name__)
@CadastroBp.route('/Cadastro')
def Cadastro_lista():
#        return "teste"
        db.create_all()
        Cadastros_query=Cadastro.query.all()
        return render_template('cadastro_lista.html',Cadastros = Cadastros_query)