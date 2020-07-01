#!/usr/bin/env python

import time
import speech_recognition as sr
from playsound import playsound
import os
from gtts import gTTS
from random import random
import sys
import threading

exit_flag = threading.Event() 

def respond(text):
    text = text.replace("'","").lower()

    command, _, args = text.partition(" ")

    responses = {
        "hi": "hello",
        "alpha": "delta",
        "whats up": "not much",
        "pi": "3.14159",
        "what is the meaning of life": "42",
        "": "",
        "": "",
        "": "",
    }

    if command in ["exit", "leave", "quit", "done"]:
        say("Good Bye")
        exit_flag.set()
        return

    if command in ["eval", "evaluate", "solve", "execute"]:
        say(str(exec(args)))
        return

    if text in responses:
        say(responses[text])
    else:
        say(f"I heard {text}")

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio) 
        print(text)
        logToFile(text)
        respond(text)
    except sr.UnknownValueError:
        print("#")
    except:
        print("error")

def logToFile(text):
    with open("out.txt", "a", encoding="utf-8") as outfile:
        outfile.write(text + "\n")

def say(StringToSay, language="en"):

    filename = f"{random()}.mp3"
    tts = gTTS(StringToSay, language)

    with open(filename, 'wb') as f:
        tts.write_to_fp(f)

    playsound(filename, True)
    os.remove(filename)

def setup():
    with open("out.txt", "w", encoding="utf-8") as outfile:
        pass

    r = sr.Recognizer()
    m = sr.Microphone()

    with m as source:
        r.adjust_for_ambient_noise(source, duration=2)

    return r, m

def manualExit():
    while True:
        text = input().strip().lower()
        
        if text == "exit":
            exit_flag.set()
            return

def main():

    r, m = setup()

    r.listen_in_background(m, callback)
    
    threading.Thread(target=manualExit, daemon=True).start()

    print("ready")

    exit_flag.wait()

if __name__ == '__main__':
    main()
