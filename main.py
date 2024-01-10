import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()

# Below Two line is for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening . . . . . . . ')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'date' in command:
        today = datetime.date.today().strftime('%B %d, %Y')  # Format the date as "Month Day, Year"
        talk('Today\'s date is ' + today)

    elif 'tell me about' in command:
        person = command.replace('tell me about ', '')
        try:
            info = wikipedia.summary(person, 2)  # Get a concise summary
            print(info)
            talk(info)  # Assuming you have a 'talk' function for text-to-speech
        except wikipedia.exceptions.DisambiguationError as e:
            print("Multiple topics found:")
            print(e.options)
            # You can optionally ask the user to clarify which topic they want
        except wikipedia.exceptions.PageError:
            print("No Wikipedia page found for that person.")

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'restart my computer' in command:
        subprocess.call(["shutdown", "/r"])

    elif 'open yahoo' in command:
        webbrowser.open("https://in.search.yahoo.com/?fr2=inr")

    elif 'send a email' in command:
        webbrowser.open("https://mail.google.com/mail/u/0/")

    elif 'open map' in command:
        webbrowser.open("https://www.google.com/maps")

    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    elif "open calculator" in command:
        talk("Ok")
        webbrowser.open("https://www.google.com/search?q=google+calculator&oq=google+calcu&gs_lcrp=EgZjaHJvbWUqEggAEAAYQxiDARixAxiABBiKBTISCAAQABhDGIMBGLEDGIAEGIoFMgYIARBFGDkyDQgCEAAYgwEYsQMYgAQyDAgDEAAYQxiABBiKBTIHCAQQABiABDINCAUQABiDARixAxiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABKgCALACAA&sourceid=chrome&ie=UTF-8")

    elif 'do you love me' in command:
        talk('I am an Artificial Intelligence Not a Human')

    elif "how are you" in command:
        talk("I'm fine")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')

while True:
    run_alexa()