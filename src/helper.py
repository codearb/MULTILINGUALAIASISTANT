import speech_recognition as sr
import ollama
from gtts import gTTS

print("perfect!!")

def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    

def text_to_speech(text):
    print('creating audio...')
    tts=gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")
    print("done")

def llm_model_object(user_text):
    print('thinking...')
    result = ollama.generate(model="llama3.2:latest", prompt = user_text)
    
    result=result['response']
    
    return result
    
    
    
    