#text to speech to give to the model

import speech_recognition as sr
recognizer = sr.Recognizer()
#run for imput to gpt 

#when running it will use the microphone to turn speech into text
def mic():
    with sr.Microphone() as source:

        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)

        except sr.UnknownValueError:
            text = None 
        except sr.RequestError as e:
            text = None

    
    return text 

    


