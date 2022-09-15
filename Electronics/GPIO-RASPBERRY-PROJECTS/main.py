# importo la libreria GPIO para habilitar los pines del RPi
import RPi.GPIO as GPiO

# Consiguro el modo en que reconoceré los pines GPIO
GPIO.setmode(BOARD)

# Creo variables con las cuales reconoceré ciertos pines
pin = 7

# Configuro el pin  como salida con OUT = OUTPUT = SALIDA
GPIO.setup(pin, OUT)

# Configuro en que modo de salida estará el pin con ' .output - GPIO.HIGH & GPIO.LOW '
GPIO.output(pin, GPIO.HIGH)

while True:
    for x in range(0, 30):
