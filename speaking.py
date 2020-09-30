import pyttsx3

xavier_brain = "I can't hear you, try again"

xavier_mouth = pyttsx3.init()
xavier_mouth.say(xavier_brain)
xavier_mouth.runAndWait()