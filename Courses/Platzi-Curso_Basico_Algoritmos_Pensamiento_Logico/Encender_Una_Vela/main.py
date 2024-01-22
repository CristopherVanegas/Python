state = 'off'

def encenderVela(state):
	if(state == 'off'):
		print(f'Estado de la vela: {state}!')
		buscarCerillos()
		state == 'on'
		print('Vela encendida')
	else:
		state == 'off'

def buscarCerillos():
	print('ok, buscando cerillos para encender la vela!')

encenderVela(state)

