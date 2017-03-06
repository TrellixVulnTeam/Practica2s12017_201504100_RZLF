__author__ = "Mac"

#Si mientras trabajan en Python alguna vez les arroja un "IndentationError" es porque en alguna linea, los tabs al inicio de la sentencia estan erroneos, por ejemplo:
#Esto es valido:
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#		self.password = password
#Esto NO es valido y arroja un "IndentationError":
#class Usuario():
#	def __init__(self, nombre):
#		self.nombre = nombre
#	   self.password = password
#	   ^
#	   Esto no deberia de estar ahi, sino que tiene que estar igual de indentado que las demas sentencias.
#
#
#Recomiendo Sublime Text como IDE
#



from flask import Flask, request, Response
import os
app = Flask("EDD_codigo_ejemplo")

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo

@app.route('/metodoSuma',methods=['POST']) 
def misuma():
	numero1 = str(request.form['dato'])
	numero2 = str(request.form['dato2'])
	suma = float(numero1) + float(numero2)
	os.system("start calc")
	return "El resultado de la suma es : " + str(suma) + " !"

@app.route('/metodoCalcu',methods=['POST']) 
def micalcu():
	os.system("start calc")
	return "Se envio instruccion a Python que abriera calculadora !"

@app.route('/metodoWeb',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	return "Como estas " + str(parametro) + "!"

@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='eddchris2017.pythonanywhere.com')