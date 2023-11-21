import openai
import os
import webbrowser
import speech_recognition as sr
from youtubesearchpython import VideosSearch

# Initialize OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
#todo: open api key expired. Need to generate new one


# Function to speak out the given text
def speak(text):
    os.system(f"say {text}")


# Function to capture voice input and convert it to text
def listen():
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


# Function to generate AI response
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"]
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Function to handle 'open' command
def open_website(query):
    site = word_after_command(query, "open")
    if site:
        print(f"Opening {site}...")
        speak(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")
    else:
        print("Please specify a website.")


# Function to handle 'play' command
def play_song(query):
    song = word_after_command(query, "play")
    if song:
        print(f"Searching for {song} on YouTube...")
        speak(f"Playing {song} on YouTube")
        videosSearch = VideosSearch(song, limit=1)
        videosResult = videosSearch.result()
        if videosResult:
            first_video_url = videosResult['result'][0]['link']
            print(f"Playing {first_video_url}...")
            webbrowser.open(first_video_url)
        else:
            print("No results found.")
    else:
        print("Please specify a song to play.")


# Function to handle user interaction and AI response
def handle_user_query():
    print("Hello, I am Jarvis AI.")
    speak("Hello, I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = listen()
        print(query)
        if "open" in query:
            open_website(query)
        elif "play" in query:
            play_song(query)
        else:
            print(f"Searching for the query using A.I ...")
            speak(f"Searching for the query using A.I ...")
            response = generate_response(query)
            speak(response)
            print(response)


# Function to extract the phrase following a command in a given sentence
def word_after_command(phrase, command):
    words = phrase.split()
    if command in words:
        index = words.index(command)
        if index + 1 < len(words):
            return ' '.join(words[index + 1:])
    return None


if __name__ == '__main__':
    handle_user_query()
