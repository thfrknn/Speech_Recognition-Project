import os
import pyaudio
import wave
import keyboard
import speech_recognition as sr
from pydub import AudioSegment
from datetime import datetime

# Ses ayarları
format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024
waveOutputFilename = r"D:\\projects\\python\\handmade\\voice.wav"

# Tarih ve saat bilgilerini içeren dosya adını oluştur
now = datetime.now()
timestamp = now.strftime("%d.%m.%Y-%H.%M")
output_text_file = f"D:\\projects\\python\\handmade\\{timestamp}-transcript.txt"

def recordAudio(filename):
    audio = pyaudio.PyAudio()
    
    # Ses akışını aç
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    print("Press 't' to start recording...")
    
    frames = []
    recording = False
    
    while True:
        if keyboard.is_pressed('t'):
            if not recording:
                print("Recording started...")
                recording = True
                frames = []  # Önceki kayıtları temizle
            while recording:
                data = stream.read(chunk)
                frames.append(data)
                if keyboard.is_pressed('y'):
                    print("Recording stopped.")
                    recording = False
        elif keyboard.is_pressed('q'):
            print("Program terminated.")
            break

    # Ses akışını durdur
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Klasörün varlığını kontrol et ve oluştur
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Kayıt edilen sesi dosyaya yaz
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    
    print(f"Recording saved as {filename}.")

def transcribe_audio(audio_chunk, recognizer):
    temp_filename = "temp_chunk.wav"
    audio_chunk.export(temp_filename, format="wav")

    try:
        with sr.AudioFile(temp_filename) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="tr-TR")
                return text
            except sr.UnknownValueError:
                return "Could not understand audio"
            except sr.RequestError as e:
                return f"API error: {e}"
    finally:
        # Geçici dosyayı sil
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

def process_audio_file(audio_path, output_text_file):
    # Ses dosyasını yükle
    audio = AudioSegment.from_wav(audio_path)

    # Ses dosyasını 15 saniyelik parçalara böl
    chunk_length_ms = 15000  # 15 seconds
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    # Speech Recognition için bir tanıyıcı oluştur
    recognizer = sr.Recognizer()

    # Metni dosyaya yazmak için
    with open(output_text_file, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks):
            start_time = i * (chunk_length_ms / 1000)
            end_time = (i + 1) * (chunk_length_ms / 1000)
            chunk_filename = f"{int(start_time)}-{int(end_time)}.wav"
            
            print(f"Processing chunk {i + 1} ({chunk_filename})...")
            text = transcribe_audio(chunk, recognizer)
            
            f.write(f"Chunk {chunk_filename}:\n{text}\n\n")

    # Ses dosyasını sil
    os.remove(audio_path)
    print("Audio file deleted after processing.")

if __name__ == "__main__":
    # Ses kaydını yap
    recordAudio(waveOutputFilename)
    
    # Kayıt sonrası ses dosyasını işleyip transkripti oluştur
    process_audio_file(waveOutputFilename, output_text_file)
