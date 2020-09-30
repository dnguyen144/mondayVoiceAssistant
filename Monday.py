import speech_recognition
import pyttsx3
from datetime import date, datetime
import os
import webbrowser
from spotify_local import SpotifyLocal
import subprocess

monday_ear = speech_recognition.Recognizer()
monday_mouth = pyttsx3.init()
monday_brain = ""

d = '/Applications'
apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))



while True:
	with speech_recognition.Microphone() as mic:
		print("Monday: I'm Listening")
		audio = monday_ear.listen(mic)

	print("Monday: ...")

	try:
		you = monday_ear.recognize_google(audio)
	except:
		you = ""
		monday_brain = "I can't hear you, try again"


	if you == "":
		monday_brain = "I can't hear you, try again"

	if you == "take note"
		date = datetime.datetime.now()
		file_name = str(date).replace(":", "-") + "-note.txt"

	elif "Spotify" in you:
		app = 'Spotify'
		os.system('open ' + d +'/%s.app' %app.replace(' ','\ '))

		with SpotifyLocal() as s:
			pass
			
		monday_brain = "Open Spotify"


	elif "hello" in you:
		monday_brain = "hello Dat Nguyen"


	elif "today" in you:
		today = date.today()
		monday_brain = today.strftime("%B %d, %Y")


	elif "time" in you:
		now = datetime.now()
		monday_brain = now.strftime("%H hours %M minutes %S second")


	elif "president" in you:
		monday_brain= "Donald Trump"

	elif "open spotify" in you:



	elif "goodbye" in you:
		monday_brain = "Bye Dat Nguyen"
		print("Monday: " + monday_brain)
		monday_mouth.say(monday_brain)
		monday_mouth.runAndWait()
		break

	else:
		monday_brain="I don't understand, try again"

	print("Monday: " + monday_brain)
	monday_mouth.say(monday_brain)
	monday_mouth.runAndWait()