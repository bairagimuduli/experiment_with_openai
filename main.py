import speech_recognition as sr
import os
import webbrowser
from youtubesearchpython import VideosSearch


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


# Function to extract the phrase following a command in a given sentence
def word_after_command(phrase, command):
    words = phrase.split()
    if command in words:
        index = words.index(command)
        if index + 1 < len(words):
            return ' '.join(words[index + 1:])  # Get all words after the command as a single string
    return None


if __name__ == '__main__':
    # Jarvis introduction
    print("Hello, I am Jarvis AI.")
    say("Hello, I am Jarvis A.I.")
    while True:
        print("Listening...")
        # Capture user input through microphone
        query = take()
        print(query)
        # Check if the query contains the word 'open'
        if "open" in query:
            # Extract the word following 'open' to identify the website
            site = word_after_command(query, "open")
            if site:
                # Open the specified website in the default browser
                print(f"Opening {site}...")
                say(f"Opening {site}")
                webbrowser.open(f"https://{site}.com")
            else:
                # If no website specified after 'open'
                print("Please specify a website.")

        elif "play" in query:
            song = word_after_command(query, "play")
            if song:
                print(f"Searching for {song} on YouTube...")
                say(f"Playing {song} on YouTube")
                # Search for the song on YouTube
                videosSearch = VideosSearch(song, limit=1)
                videosResult = videosSearch.result()
                if videosResult:
                    first_video_url = videosResult['result'][0]['link']
                    print(f"Playing {first_video_url}...")
                    webbrowser.open(first_video_url)  # Open the first video URL in the default browser
                else:
                    print("No results found.")
            else:
                print("Please specify a song to play.")
