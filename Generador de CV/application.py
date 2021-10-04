from flask import Flask, render_template, request
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/CV-template", methods=["POST"])
def cvgen():
    name = request.form.get("nombre")
    presentacion = request.form.get("presentacion")    
    experiencia = request.form.get("experiencia")   
    estudios = request.form.get("estudios")   
    logros = request.form.get("logros")   
    habilidades = request.form.get("habilidades")   
    intereses = request.form.get("intereses")   
    referencias = request.form.get("referencias")
    correo = request.form.get("correo")
    celular = request.form.get("celular")


    return render_template("hello.html", nombre=name, presentacion=presentacion,experiencia=experiencia,estudios=estudios,logros=logros,habilidades=habilidades, intereses=intereses, referencias=referencias, correo=correo, celular=celular)
