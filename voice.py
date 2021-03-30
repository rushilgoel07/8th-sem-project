import tkinter
import pyttsx3
import cv2
import PIL
import threading
import imutils
import time
import speech_recognition as sr
#import PIL.Image , PIL.ImageTK
from PIL import ImageTk
from PIL import Image
from functools import partial
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
stream=cv2.VideoCapture("clip.mp4")
engine.setProperty('voice',voices[1].id)
def voice1():
    thread=threading.Thread(target=speak)
    thread.daemon=1
    thread.start()
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        frame=cv2.cvtColor(cv2.imread("voice.png"),cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")  
        frame=cv2.cvtColor(cv2.imread("voice.png"),cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,image=frame,anchor=tkinter.NW)  
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        engine.say(query)
        engine.runAndWait()  #User query will be printed.
        print(f"User said: {query}\n")
        ##while True:
        if 'he is out' in query:
            out()
        elif 'not out' in query:
            not_out()
        elif 'previous slow' in query:
            play(-2)
        elif 'previous fast' in query:
            play(-25)
        elif 'next fast' in query:
            play(25)
        elif 'next slow' in query:
            play(2)
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

#width and height of main screen
SET_WIDTH=650
SET_HEIGHT=358
#GUI starts here
window=tkinter.Tk()
window.title("DRS")
cv_img=cv2.cvtColor(cv2.imread("welcome3.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()
btn=tkinter.Button(window,text="VOICE ASSISTANT",width=50,command=voice1)
btn.pack()
btn=tkinter.Button(window,text="EXIT",width=50,command=quit)
btn.pack()
window.mainloop()
