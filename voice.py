from gtts import gTTS
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import time
import requests
import speech_recognition as sr
from dotenv import load_dotenv


load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("VOICE_ID")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY not found! Please add it to your .env file.")
if not VOICE_ID:
    raise ValueError("VOICE_ID not found! Please add it to your .env file.")


def listen_speech():
    """Listen to user's voice and convert it to text using Google Speech Recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.6
        recognizer.energy_threshold = 300

        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't hear that. You can type either in Hindi or English.")
        return ""
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""


def speak_text(text: str):
    """Convert text to speech using ElevenLabs or fallback to gTTS."""
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "voice_settings": {"stability": 0.7, "similarity_boost": 0.8}
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            filename = "temp.mp3"
            with open(filename, "wb") as f:
                f.write(response.content)
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.quit()
            os.remove(filename)
        else:
            print(f"ElevenLabs unavailable ({response.status_code}) — switching to Google TTS fallback.")
            tts = gTTS(text=text, lang='hi' if any(ch in text for ch in 'अआइईउऊएऐओऔकखगघचछजझटठडढणतथदधनपफबभमयरलवशषसह') else 'en')
            tts.save("temp.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("temp.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.quit()
            os.remove("temp.mp3")

    except Exception as e:
        print(f"Speech synthesis error: {e}")



# if __name__ == "__main__":
#     # Test speaking directly
#     speak_text("Namaste Sir! Good morning. Kal humne site ka flooring complete kar liya tha.")
 
