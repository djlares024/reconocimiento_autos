import pyttsx3
import speech_recognition as sr
import mysql.connector
from difflib import SequenceMatcher as SM
import random
import time

recognizer = sr.Recognizer()

microphone = sr.Microphone(device_index = 0)

eng = pyttsx3.init()

#Configuracion de la velocidad de la pronunciacion
eng.setProperty("rate",140)

#Establecer el nivel de volumen de la voz
eng.setProperty("volume",1.0)
#Establecemos la voz a utilizar
eng.runAndWait()
listVoices = eng.getProperty("voices")
eng.setProperty("voice",listVoices[0].id)

eng.say("RECONOCIMIENTO DE AUTOS")
eng.runAndWait()

def recognizeMicAudio():
	palabra = ""
	print("Escuchando placa...")
	with microphone as source:
		audio = recognizer.listen(source)
		palabra = recognizer.recognize_google(audio,language='es-MX')

	return palabra

#print(recognizeMicAudio())

conexion = mysql.connector.connect(host="localhost",user="root",passwd="",database="autos")
cursor = conexion.cursor(buffered=True)


palabra = ""

while palabra != "silencio":
	palabra = recognizeMicAudio()
	print(palabra)
	cursor.execute("SELECT * FROM placas WHERE id_placa like'%"+palabra+"%' ")
	nDatos = cursor.rowcount
	print("Se han encontrado",nDatos)

	for fila in cursor:
		ide = fila[0]
		entrada = fila[1]
		salida = fila[2]
		print(ide)
		print(entrada)
		print(salida)
		similitud = SM(None,entrada,palabra).ratio()
		print(similitud)
		if similitud > 0.7:
			eng.say(salida)
			eng.runAndWait()