import pyttsx3

def say(text):
    engin = pyttsx3.init()
    voice = engin.getProperty('voices')
    engin.setProperty('voice',voice[0].id)
    engin.say(text)
    engin.runAndWait()
while True:
    text = input(print("Enter any text"))
    say(text)
