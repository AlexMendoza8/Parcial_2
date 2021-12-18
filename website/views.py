from flask import Blueprint, render_template, request,jsonify
from .resources import Listar

# Instanciar
v = Listar()

views = Blueprint('views', __name__)

@views.route('/vacunas_list_resource',methods=['GET'])
def get_palabras():
    
    lista= v.get_all()

    return jsonify(lista)


@views.route('/', methods=['GET'])
def home():   

    list = v.get_all()
    
    return render_template("home.html", vacunas = list)

