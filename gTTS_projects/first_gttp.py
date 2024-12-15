# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
mytext = """Hola, soy Valery y estoy para explorar y adaptarme en el ambiente.
Funciono gracias a una placa Arduino, motor shields, baterías de litio y un control remoto o vía bluetooth.
¡Será un gusto ser de ayuda!"""

# Language in which you want to convert
language = 'es'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")