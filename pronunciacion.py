import tkinter as tk
import pyaudio
import wave
import speech_recognition as sr

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Captura de Voz")
        self.frames = []
        self.recording = False

        # Botón para iniciar/detener grabación
        self.record_button = tk.Button(self.root, text="Grabar", command=self.toggle_recording)
        self.record_button.pack()

        # Inicializar PyAudio
        self.audio = pyaudio.PyAudio()

        # Configuración de grabación
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

    def toggle_recording(self):
        if not self.recording:
            # Comenzar grabación
            self.recording = True

            # Abrir archivo para guardar grabación
            self.frames = []
            wf = wave.open("grabacion.wav", "wb")
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)

            # Iniciar stream de audio
            stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                     rate=self.RATE, input=True,
                                     frames_per_buffer=self.CHUNK)

            # Grabar audio mientras se presiona el botón de grabación
            while self.recording:
                data = stream.read(self.CHUNK)
                wf.writeframes(data)
                self.frames.append(data)

            # Detener stream de audio y cerrar archivo de grabación
            stream.stop_stream()
            stream.close()
            wf.close()

            # Comparar pronunciación con muestra de audio usando SpeechRecognition
            r = sr.Recognizer()
            with sr.AudioFile("grabacion.wav") as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)

                # Comparar texto con muestra de texto deseada (por ejemplo: "Hola mundo")
                if text == "Hola mundo":
                    print("Pronunciación correcta!")
                else:
                    print("Pronunciación incorrecta :(")

        else:
            # Detener grabación
            self.recording = False

    def run(self):
        self.root.mainloop()

app = App()
app.run()
