from gtts import gTTS
import speech_recognition as sr

recognizer_instance = sr.Recognizer()

with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("Listen...")
    audio = recognizer_instance.listen(source)
    print("ok")
try:
    text = recognizer_instance.recognize_google(audio, language="it-IT")
    print("Google ha capito \n", text)
    tts = gTTS(text=text, lang='it')
    tts.save("tts_output_audio.mp3")
    print("save file ok")
except Exception as e:
    print(e)
