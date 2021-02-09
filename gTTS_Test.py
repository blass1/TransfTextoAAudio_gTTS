from gtts import gTTS

tts = gTTS("TEXTO QUE QUIERO QUE SE GRABE EN MP3", lang="es")
tts.save("Prueba_tts.mp3")
tts.run()
print("Terminado")