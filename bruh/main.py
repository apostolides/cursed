from pynput import keyboard
from audio import Recorder
from transcribe import transcribe
from gpt import contact_the_eldritch_god
from tts import uwu_speak

STATE = "released"
recorder = Recorder()

def on_press(key):
    global STATE
    global keyboard_listener
    global recorder

    if key == keyboard.Key.space and STATE == "released":
        print("[*] Triggered HOLD.")
        STATE = "pressed"
        recorder.start_recording()

    elif key == keyboard.Key.f12:
        keyboard_listener.stop()
        recorder.stop_recording()

def on_release(key):
    global STATE
    global recorder
    if key == keyboard.Key.space:
        print("[*] Triggered RELEASED.")
        recorder.stop_recording()
        recorder.store_recording()
        try:
            txt = transcribe(recorder.get_audiofile())                                
            response = contact_the_eldritch_god(txt)
            uwu_speak(response)
        except Exception as e:
            print(e)
        STATE = "released"

keyboard_listener = keyboard.Listener(on_press=on_press,on_release=on_release)
keyboard_listener.start()
keyboard_listener.join()
