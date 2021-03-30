from tkinter import *
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

def Call_1():
    root.destroy()
    import Encrypt

def Call_2():
    root.destroy()
    import Decrypt

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
stream=cv2.VideoCapture("clip.mp4")
engine.setProperty('voice',voices[1].id)
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        engine.say(query)
        engine.runAndWait()  #User query will be printed.
        print(f"User said: {query}\n")
        ##while True:
        if 'encrypt' in query:
            import Encrypt
        elif 'decrypt' in query:
            import Decrypt
        
        

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

root=Tk()

F1=Frame(root,bg='black',width=600,height=600)

L1=Label(F1,bg='White',text='RAW',font=('Times New Roman',100,'bold'),width=200).pack(padx=50,pady=50)
L2=Label(F1,bg='White',text='Encryption',font=('arial',20,'bold')).pack(side=LEFT,padx=75,pady=80)
L3=Label(F1,bg='White',text='Decryption',font=('arial',20,'bold')).pack(side=RIGHT,padx=75,pady=80)
L4=Label(F1,bg='White',text='Voice',font=('arial',20,'bold')).pack(side=BOTTOM,padx=75,pady=80)

B1=Button(F1,text='Choose 1',fg='white',bg='grey',command=Call_1).place(x=125,y=500)
B2=Button(F1,text='Choose 2',fg='white',bg='grey',command=Call_2).place(x=425,y=500)
B2=Button(F1,text='Choose 3',fg='white',bg='grey',command=speak).place(x=250,y=250)


F1.pack(fill=BOTH,expand=1)
root.geometry('600x600+400+100')
root.mainloop()
