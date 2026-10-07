import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
import pyttsx3
import streamlit as st

# Initialize TTS engine in a way that avoids threading issues
def init_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    if voices:
        engine.setProperty("voice", voices[0].id)
    return engine

def speak_text(text):
    """Function to convert text to speech. Runs in main thread."""
    try:
        engine = init_engine()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

def get_greeting():
    """Returns appropriate greeting based on time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return "Good Morning!"
    elif hour >= 12 and hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def listen_in_background(q):
    """Listens for audio in a background thread."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        q.put({"type": "status", "value": "listening"})
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            q.put({"type": "audio_ready", "value": audio})
        except sr.WaitTimeoutError:
            q.put({"type": "error", "value": "Listening timed out."})
        except Exception as e:
            q.put({"type": "error", "value": str(e)})

def recognize_audio(audio):
    """Recognizes speech from audio data."""
    r = sr.Recognizer()
    try:
        query = r.recognize_google(audio, language="en-in")
        return query
    except sr.UnknownValueError:
        return "None"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

def process_command(query):
    query = query.lower()
    response = ""
    action = None

    if query == "none" or not query:
        return "I didn't catch that. Please try again.", None

    if "wikipedia" in query:
        search_query = query.replace("wikipedia", "").strip()
        if not search_query:
            search_query = query
        try:
            results = wikipedia.summary(search_query, sentences=2)
            response = f"According to Wikipedia: {results}"
        except Exception:
            response = "Sorry, I could not find that on Wikipedia."

    elif "youtube" in query:
        response = "Opening YouTube..."
        action = lambda: webbrowser.open("https://www.youtube.com")

    elif "google" in query:
        response = "Opening Google..."
        action = lambda: webbrowser.open("https://www.google.com")

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        response = f"Sir, the time is {strTime}"

    elif "quit" in query or "exit" in query or "sleep" in query:
        response = "Goodbye sir! Going to sleep."
        st.session_state.status = "sleeping"

    else:
        response = "I don't have a command for that yet."

    return response, action