import speech_recognition
import pyttsx3
from time import sleep
from datetime import datetime

text_processor = pyttsx3.init()

text_processor.setProperty('rate', 150)

recognition_handler = speech_recognition.Recognizer()

botName = 'moshe peretz'

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognition_handler.adjust_for_ambient_noise(mic, duration=0)

            ToBeProcessed = recognition_handler.listen(mic)

            text = str(recognition_handler.recognize_google(ToBeProcessed)).lower()

            text_processor.say(f'did you say {text}')

            text_processor.runAndWait()

            ToBeProcessed = recognition_handler.listen(mic)

            textValidation = str(recognition_handler.recognize_google(ToBeProcessed)).lower()

            if textValidation == "yes":
                text_processor.say("gotcha")
                text_processor.runAndWait()
                sleep(0.3)

                if "what time is it" in text:
                    currentime = datetime.now().strftime("%H:%M")
                    text_processor.say(f"it's {currentime}")
                    text_processor.runAndWait()
                elif "what is your name" in text:
                    text_processor.say(f"my name is {botName}")
                    text_processor.runAndWait()
                elif "change your name" in text:
                    text_processor.say("to what")
                    text_processor.runAndWait()
                    listener = recognition_handler.listen(mic)
                    
                    response = str(recognition_handler.recognize_google(listener)).lower()
                    
                    text_processor.say(f"name has been changed to {response}")
                    
                    text_processor.runAndWait()
                    
                    botName = response
                elif "what can you do" in text or "help" in text:
                    text_processor.say(f"hey! im {botName}, i am artificial intelligence. my purpose is to make tasks more accessible using voice control")
                    
                elif "bye" in text:
                    text_processor.say("bye, see ya next time")
                    text_processor.runAndWait()
                    exit()
            else:
                text_processor.say("ok, so what did you mean")
                text_processor.runAndWait()



    except Exception:
        recognition_handler = speech_recognition.Recognizer()
