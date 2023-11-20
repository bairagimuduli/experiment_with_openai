import speech_recognition as sr
import os
import webbrowser


# Function to speak out the given text
def say(text):
    os.system(f"say {text}")


# Function to capture voice input and convert it to text
def take():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            # Using Google's speech recognition API to transcribe audio to text
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "I couldn't understand. Please try again."
        except sr.RequestError:
            return "I am unable to process your request at the moment."


# Function to extract the word following 'open' in a given phrase
def word_after_open(phrase):
    words = phrase.split()
    if 'open' in words:
        open_index = words.index('open')
        if open_index + 1 < len(words):
            return words[open_index + 1]
    return None


if __name__ == '__main__':
    print('PyCharm')
    # Jarvis introduction
    say("Hello, I am Jarvis AI.")
    while True:
        print("Listening...")
        # Capture user input through microphone
        query = take()
        print(query)
        # Check if the query contains the word 'open'
        if "open" in query:
            # Extract the word following 'open' to identify the website
            site = word_after_open(query)
            if site:
                # Open the specified website in the default browser
                print(f"Opening {site}...")
                say(f"Opening {site}")
                webbrowser.open(f"https://{site}.com")
            else:
                # If no website specified after 'open'
                print("Please specify a website.")
