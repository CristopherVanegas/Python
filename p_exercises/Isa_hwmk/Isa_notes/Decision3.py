nota = input('¿Cuál es su nota?')
nota = float(nota)

if nota >= 69.5:
    print('!Aprobaste!')
elif nota >= 60 and nota < 69.5:
    print('Puedes realizar recuperación')
else:
    print('Lo siento, pero puedes recuperar en el proximo parcial, animos x0x0')