import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# list the voice in pyttsx3
for index, voice in enumerate(voices):
    print(f"{index}: Name: {voice.name}, Gender: {getattr(voice, 'gender', 'Unknown')}, ID: {voice.id}")
