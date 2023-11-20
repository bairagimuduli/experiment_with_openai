import speech_recognition as sr
import os
import webbrowser


def say(text):
    os.system(f"say {text}")


def take():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "I couldn't understand. Please try again."
        except sr.RequestError:
            return "I am unable to process your request at the moment."


def word_after_open(phrase):
    words = phrase.split()
    if 'open' in words:
        open_index = words.index('open')
        if open_index + 1 < len(words):
            return words[open_index + 1]
    return None


if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis AI.")
    while True:
        print("Listening...")
        query = take()
        print(query)
        if "open" in query:
            site = word_after_open(query)
            if site:
                print(f"Opening {site}...")
                say(f"Opening {site}")
                webbrowser.open(f"https://{site}.com")
            else:
                print("Please specify a website.")
