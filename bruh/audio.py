import threading
import pyaudio
import wave

class Recorder:
    def __init__(self):
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.seconds = 3
        self.filename = "output.wav"
        self.frames = []
        self.recording = False
        self.thread = None
        self.pyaudioproc = None

    def start_recording(self):
        
        def recording_thread(self):
            self.recording = True
            self.pyaudioproc = pyaudio.PyAudio()
            print('[*] Recording.')
            stream = self.pyaudioproc.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
            self.frames = []
            while self.recording:
                data = stream.read(self.chunk)
                self.frames.append(data)
            stream.stop_stream()
            stream.close()
            self.pyaudioproc.terminate()
            print('[*] Finished recording.')

        self.thread = threading.Thread(target=recording_thread, args=(self,))
        self.thread.start()

    def stop_recording(self):
        self.recording = False
        self.thread.join()

    def get_audiofile(self):
        return self.filename

    def store_recording(self):
        print("[*] Writing to file.")
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.pyaudioproc.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print("[*] Wrote to file.")
