from gtts import gTTS
import os
import sys
import playsound

def main():

    fileToRead = "input.txt"
    language = 'en'

    with open(fileToRead, 'r') as f:
        StringToSay = f.read()

    say(StringToSay, language)

def say(StringToSay, language):

    filename = "output.mp3"
    tts = gTTS(StringToSay, language)

    with open(filename, 'wb') as f:
        tts.write_to_fp(f)

    playsound.playsound(filename, True)

    #os.remove(filename)

if __name__ == '__main__':
    try:
        main()
    except Exception:
        sys.exit()
        