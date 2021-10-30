from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    for i in range(0 , len(session["usuarios"])):
        if session["usuarios"][i] == request.form.get("correo") and session["contra"][i] == request.form.get("contra"):
            return render_template("cv-form.html")
    return render_template("login.html")

@app.route("/create", methods = ["GET", "POST"])  #para poder ingresar tienen que entrar a login luego de crear la cuenta
def create():
    session["usuarios"] = []
    session["contra"] = []
    correo = request.form.get("correo")
    contra = request.form.get("contra")
    session["usuarios"].append(correo)
    session["contra"].append(contra)
    return render_template("signup.html")
    
@app.route("/CV-form")
def cvform():
    return render_template("cv-form.html")

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


    return render_template("cvgen.html", nombre=name, presentacion=presentacion,experiencia=experiencia,estudios=estudios,logros=logros,habilidades=habilidades, intereses=intereses, referencias=referencias, correo=correo, celular=celular)
