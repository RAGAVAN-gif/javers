import speech_recognition as sr
import pyttsx3
import pyjokes

assis_name="karen"
boss_name="Ragavan"

def say(text):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()

def say2(text):
    engine2=pyttsx3.init()
    voice=engine2.getProperty('voices')
    engine2.setProperty('voice',voice[1].id)
    engine2.setProperty('rate',100)
    engine2.say(text)
    engine2.runAndWait()


def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening......")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("Recognizing.......")
            text=r.recognize_google(audio,language='en-in')
            print(f"User said :{text}\n")
        except Exception as e:
            print(e)
            print("can not recognize your voice")
            return "None"
        return text
def tell_joke():
    joke=pyjokes.get_joke()
    return joke

def respond(text):
    if 'hello' in text:
        say("HI SIR !")
    elif 'are you free' in text:
        say("yes sir")
    elif 'fine' in text or 'good' in text:
        say("It's good to know that your fine")
    elif 'who are you' in text:
        say("my name is{}".format(assis_name))
    elif 'who is your boss' in text:
        say(boss_name)
    elif 'tell a joke' in text:
        say2(tell_joke())

 
while True: 
    text=takecommand()
    respond(text)