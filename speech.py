import speech_recognition as st

def command():
    a = st.Recognizer()
    with st.Microphone () as source:
        a.adjust_for_ambient_noise(source ,duration=1)
        print("Listening...")
        a.pause_threshold=1
        audio = a.listen(source)
        try:
            print("Recognizing...")
            text = a.recognize_google(audio,language='en-in')
            print(f"user said:{text}\n")
        except Exception as e:
            print(e)
            print("Unable to recognize your voice")
while True:
    command() 