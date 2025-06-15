import speech_recognition as sr
from playsound import playsound

COMMAND_WORDS = {"музыка", "музыку"}

def listen_and_play(audio_file="music.mp3"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU").lower()
        print(f"Распознано: {text}")
        if any(word in text for word in COMMAND_WORDS):
            playsound(audio_file)
    except sr.UnknownValueError:
        print("Не удалось распознать речь.")
    except sr.RequestError:
        print("Сервис распознавания недоступен.")

if __name__ == "__main__":
    listen_and_play()
