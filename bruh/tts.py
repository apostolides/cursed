from dotenv import load_dotenv
from playsound import playsound  
import requests
import os

load_dotenv()
ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY")

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/htTdrmFCUc08FqY003r2"

outfile = os.path.dirname(__file__) + '/waifu_output.mp3'

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": ELEVENLABS_KEY
}

def uwu_speak(text):
    
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    with open(outfile, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    playsound(outfile)