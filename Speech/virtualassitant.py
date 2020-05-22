#My Virtual Assitant
#gTTS, SpeechRecognition, Pyaudio, wikipedia

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignore any Warnings
warnings.filterwarnings('ignore');
friendName="blue iris"
HelpName="blue iris"
confirmInput = 'Did you say?'
introInput = "I am " + friendName + ", thank you for having me as your virtual friend!"
GeneralGreeting = "Hi, I am " + friendName + " How are you today?"

def StarterWords(input):
    Start_Words=['hey blue iris', "blue iris" , "hi"]
    input=input.lower();
    for phrase in Start_Words:
        if phrase in input:
            return True
    if input == friendName:
        return True
    if input == HelpName:
        return True
    return False

def recordAudio():
    r = sr.Recognizer();
    with sr.Microphone() as source:
        print("I am listening ...");
        audio = r.listen(source)
    #Google
    data = ''
    try:
        data = r.recognize_google(audio);
        #print(confirmInput + ": " + data);
    except sr.UnknownValueError:
        print("Blue Iris couldn't understand your speech")
    except sr.RequestError as e:
        print("Request error from Iris: " + e)
    return data

def IrisResponse(input):
    print(input)
    audioObject = gTTS(text=input, lang='en',slow=False)
    audioObject.save('BlueIris_Response.mp3')
    os.system('afplay BlueIris_Response.mp3')
    return audioObject

def GetCurrentDate():
    now=datetime.datetime.now();
    mydate=datetime.datetime.today();
    weekday=calendar.day_name[mydate.weekday()]
    monthNumber=now.month;
    dayNumber=now.day

    monthList=['January','Febraury','March','Apirl','May','June','July','August','September','October','November','December'];
    ordinalNumbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10h',
                    '11th','12th','13th','14th','15th','16th','17th','18th','19th','20th',
                    '21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
    ReturnString="Today is " + weekday + " " + monthList[monthNumber-1] + ' the ' + ordinalNumbers[dayNumber-1]
    return ReturnString

def SayHello(input):
    Greeting_Inputs=['hi','hey','hola','greetings','whatsup','hello'];
    Greeting_Response=['howdy','whats good','hola, como esta','greetings','how are you?','hello'];
    for word in input.split():
        if word.lower() in Greeting_Inputs:
            return random.choice(Greeting_Response) + "."
    return GeneralGreeting

def GetPerson(input):
    WordList=input.split()
    person = "None"
    for i in range(0,len(WordList)):
        if i+3 <= (len(WordList) -1):
            if ((WordList[i].lower() == 'who') and (WordList[i+1].lower() == 'is')):
                person = WordList[i+2] + " " + WordList[i+3];
                return person;
    return person
r1 = sr.Recognizer();

def react(input):
    if ('who is' in data.lower()):
        person = GetPerson(data)
        print(person)
        if person != 'None':
            wiki = wikipedia.summary(person, sentences=2);
            reaction=wiki;
        else:
            reaction='Sorry, I am having trouble understanding, Could you ask the question again please?';
    else:
        reaction = SayHello(data);
        reaction= "Talk More, I am here to listen " + reaction;
    return reaction


with sr.Microphone() as source:
    print("Speak Now")
    audio = r1.listen(source)
    print(r1.recognize_google(audio))

i=0
StarterWords(r1.recognize_google(audio))
while True:
    data = recordAudio()
    Today = GetCurrentDate();
    if(i==0):
        reaction= react(data.lower());
        FinalResponse="Hi, How are you? " + Today + "\n" + introInput + "\n" + confirmInput + " " + data + \
                      " Talk More, I am here to listen ";
        IrisResponse(FinalResponse);
        IrisResponse(reaction);
        i=i+1;
    else:
        if (data.lower() == 'stop'):
            exit(0);
        else:
            reaction=react(data.lower());
            IrisResponse(reaction);

