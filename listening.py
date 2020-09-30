import speech_recognition

xavier_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Xavier: I'm Listening")
	audio = xavier_ear.listen(mic)

try:
	you = xavier_ear.recognize_google(audio)
except:
	you = "I don't understand, try again"

print("You: " + you)