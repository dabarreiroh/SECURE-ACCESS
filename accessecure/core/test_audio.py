import pyaudio
import wave

def audio():
    format=pyaudio.paInt16
    channels=2
    rate=44100
    chunk=1024
    duracion=10
    archivo="grabacion.wav"

    audio=pyaudio.PyAudio()
    stream=audio.open(format=format,channels=channels,rate=rate,input=True,frames_per_buffer=chunk)
    print("grabando...")
    frames=[]
    for i in range(0,int(rate/chunk*duracion)):
        data=stream.read(chunk)
        frames.append(data)
    print("grabación terminada")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wavefile=wave.open(archivo,'wb')
    wavefile.setnchannels(channels)
    wavefile.setsampwidth(audio.get_sample_size(format))
    wavefile.setframerate(rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
