from dotenv import load_dotenv
import openai
import os

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY

def transcribe(filepath):
    audio_file = open(filepath, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript.text