#will take in text and convert it into audio 

import pyttsx3

def text_to_speech(text, rate=150, voice=None):

    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    
    if voice:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice].id)
    
    engine.say(text)
    engine.runAndWait()
