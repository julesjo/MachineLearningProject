import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Now")
    audio = r3.listen(source)
    print(r2.recognize_google(audio))


if 'Blue Iris' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Starting to Listen")
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            #SpeechToText()
            #wb.get().open_new(get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print("Failed".format(e))

def SpeechToText():
    r3 = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            get = r3.recognize_google(audio)
            print(get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print("Failed".format(e))

if 'Blue Iris Play Video' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = "https://youtube.com"
    with sr.Microphone() as source:
        print("Starting to Listen")
        audio = r1.listen(source)
        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print("Failed".format(e))
