import pyttsx3
import speech_recognition as sr
import mysql.connector
from difflib import SequenceMatcher as SM
import random
import time
import tkinter as tk
import tkinter.font as tkFont

class Reconicimiento_autos:

	def __init__(self,root):
		self.recognizer = sr.Recognizer()
		self.microphone = sr.Microphone(device_index = 0)
		self.eng = pyttsx3.init()
		self.eng.setProperty("rate",140)#Configuracion de la velocidad de la pronunciacion
		self.eng.setProperty("volume",1.0)#Establecer el nivel de volumen de la voz
		self.eng.runAndWait()#Establecemos la voz a utilizar
		self.listVoices = self.eng.getProperty("voices")
		self.eng.setProperty("voice",self.listVoices[0].id)
		self.eng.say("RECONOCIMIENTO DE AUTOS")
		self.eng.runAndWait()
		self.conexion = mysql.connector.connect(host="localhost",user="root",passwd="",database="autos")
		self.cursor = self.conexion.cursor(buffered=True)
		root.title("Reconocimiento de placas") #setting title
        #----------------------- SETTING WINDOW------------------------
		width=450
		height=295
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
		root.geometry(alignstr)
		root.resizable(width=False, height=False)
		ft = tkFont.Font(family='Arial',size=12)
		self.lblResultados=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "0",anchor="w")
		self.lblResultados.place(x=210,y=0,width=120,height=30)
		self.lblPlaca=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "placa", anchor="w")
		self.lblPlaca.place(x=325,y=0,width=120,height=30)
		self.lblMarca=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblMarca.place(x=210,y=35,width=120,height=30)
		self.lblModelo=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblModelo.place(x=325,y=35,width=120,height=30)
		self.lblAnio=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblAnio.place(x=210,y=70,width=120,height=30)
		self.lblNumSerie=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblNumSerie.place(x=325,y=70,width=120,height=30)
		self.lblColor=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblColor.place(x=210,y=105,width=120,height=30)
		self.lblNoPuiertas=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblNoPuiertas.place(x=325,y=105,width=120,height=30)
		self.lblTipoMotor=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblTipoMotor.place(x=210,y=140,width=120,height=30)
		self.lblPropietario=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 text = "--", anchor="w")
		self.lblPropietario.place(x=325,y=140,width=120,height=30)
		buttonanalizar=tk.Button(root, font = ft, fg = "#005292", justify = "center",
                                 text = "Buscar")
		buttonanalizar.place(x=50,y=210,width=90,height=30)
		buttonanalizar["command"] = lambda: self.buscarPlaca()		
		self.micro = tk.PhotoImage(file='assets/micro.png') # Create a Label Widget to display the text or Image
		self.micro_full = tk.PhotoImage(file='assets/micro_full.png') # Create a Label Widget to display the text or Image
		self.lblImage=tk.Label(root, font = ft, fg = "#141414", justify = "center",
                                 image=self.micro, anchor="w")
		self.lblImage.place(x=10,y=10,width=150,height=150)

	def recognizeMicAudio(self):
		palabra = ""
		print("Escuchando placa...")
		with self.microphone as source:
			audio = self.recognizer.listen(source)
			palabra = self.recognizer.recognize_google(audio,language='es-MX')
		return palabra

	def buscarPlaca(self):
		self.lblImage["image"] = self.micro_full
		palabra = self.recognizeMicAudio()
		palabra = palabra.replace("silecio", "")
		palabra = palabra.replace(" ", "")
		palabra = palabra.upper()
		self.cursor.execute("SELECT * FROM placas WHERE placa like'%"+palabra+"%' ")
		nDatos = self.cursor.rowcount
		if (nDatos > 0):
			for fila in self.cursor:
				ide = fila[0]
				placa = fila[1]
				marca = fila[2]
				modelo = fila[3]
				anio = fila[4]
				num_serie = fila[5]
				color = fila[6]
				num_puertas = fila[7]
				tipo_motor = fila[8]
				nombre_propietario = fila[9]
				self.lblResultados["text"] =str(nDatos)
				self.lblPlaca["text"] = placa
				self.lblMarca["text"] = marca
				self.lblModelo["text"] = modelo
				self.lblAnio["text"] = anio
				self.lblNumSerie["text"] = num_serie
				self.lblColor["text"] = color
				self.lblNoPuiertas["text"] = num_puertas
				self.lblTipoMotor["text"] = tipo_motor
				self.lblPropietario["text"] =nombre_propietario
				similitud = SM(None, placa, palabra).ratio()
				print(similitud)
				if similitud > 0.7:
					self.eng.say(marca + " " + modelo + " color " + color + " a nombre de " + nombre_propietario)
					self.eng.runAndWait()
		else:
			self.lblResultados["text"] = 'Resultados:' + str(0)
		self.lblImage["image"] = self.micro

if __name__ == "__main__":
    root = tk.Tk()
    app = Reconicimiento_autos(root)
    root.mainloop()