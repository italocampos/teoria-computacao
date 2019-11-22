def automaton_1a(string):
	# Defining initial configuration
	state = 0
	alphabet = '01'

	# Runing automaton
	for c in string:
		if state == 0:
			if c == '0':
				state = 0
			elif c == '1':
				state = 1
		elif state == 1:
			if c == '0':
				state = 2
			else:
				state = 'invalid'
		elif state == 2:
			if c == '0':
				state = 3
			else:
				state = 'invalid'
		elif state == 3:
			if c == '0':
				state = 3
			elif c == '1':
				state = 1

		if state == 'invalid' or c not in alphabet:
			return False
	
	# Checking final states
	return state in [0, 3]


def automaton_1b(string):
	# Defining initial configuration
	state = 0
	alphabet = 'ab'

	# Runing automaton
	for c in string:
		if state == 0:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 0
		elif state == 1:
			if c == 'a':
				state = 2
			elif c == 'b':
				state = 1
		elif state == 2:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 0

		if c not in alphabet:
			return False
	
	# Checking final states
	return state in [0]


def automaton_2a(string):
	# Defining initial configuration
	state = 0
	alphabet = 'abc'

	# Runing automaton
	for c in string:
		if state == 0:
			if c == 'a':
				state = 1
			else:
				state = 'invalid'
		elif state == 1:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 2
			elif c == 'c':
				state = 3
		elif state == 2:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 2
			elif c == 'c':
				state = 3
		elif state == 3:
			if c == 'a':
				state = 1
			elif c == 'c':
				state = 3
			else:
				state = 'invalid'

		if state == 'invalid' or c not in alphabet:
			return False
	
	# Checking final states
	return state in [0, 1, 2, 3]


def automaton_2b(string):
	# Defining initial configuration
	state = 0
	alphabet = 'abc'

	# Runing automaton
	for c in string:
		if state == 0:
			if c == 'a':
				state = 1
			elif c in ['b', 'c']:
				state = 4
		elif state == 1:
			if c == 'a':
				state = 2
			else:
				state = 'invalid'
		elif state == 2:
			if c == 'a':
				state = 3
			else:
				state = 'invalid'
		elif state == 3:
			if c in ['b', 'c']:
				state = 3
			else:
				state = 'invalid'
		if state == 4:
			if c == 'a':
				state = 5
			elif c in ['b', 'c']:
				state = 4
		elif state == 5:
			if c == 'a':
				state = 6
			else:
				state = 'invalid'
		elif state == 6:
			if c == 'a':
				state = 7
			else:
				state = 'invalid'
		elif state == 7:
			state = 'invalid'

		if state == 'invalid' or c not in alphabet:
			return False
	
	# Checking final states
	return state in [3, 7]


def automaton_2c(string):
	# Defining initial configuration
	state = 0
	alphabet = 'ab'

	# Runing automaton
	for c in string:
		if state == 0:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 4
		elif state == 1:
			if c == 'a':
				state = 2
			elif c == 'b':
				state = 3
		elif state == 2:
			if c == 'a':
				state = 2
			elif c == 'b':
				state = 4
		elif state == 3:
			if c == 'b':
				state = 3
			else:
				state = 'invalid'
		elif state == 4:
			state = 'invalid'

		if state == 'invalid' or c not in alphabet:
			return False
	
	# Checking final states
	return state in [1, 3, 4]


def automaton_2d(string):
	# Defining initial configuration
	state = 0
	alphabet = 'abc'

	# Runing automaton
	for c in string:
		if state == 0:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 3
			else:
				state = 'invalid'
		elif state == 1:
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 3
			elif c == 'c':
				state = 2
		elif state == 2:
			if c == 'c':
				state = 2
			else:
				state = 'invalid'
		elif state == 3:
			if c == 'a':
				state = 2
			elif c == 'b':
				state = 3
			else:
				state = 'invalid'

		if state == 'invalid' or c not in alphabet:
			return False
	
	# Checking final states
	return state in [1, 2]


def automaton_3(string):
	# Defining initial configuration
	state = 0
	position = 0

	# Runing automaton
	for c in string:
		if state == 0:
			if c == ' ':
				state = 1
			else:
				state = 0
		elif state == 1:
			if c == 'c':
				state = 2
			else:
				state = 0
		elif state == 2:
			if c == 'o':
				state = 3
			else:
				state = 0
		elif state == 3:
			if c == 'm':
				state = 4
			else:
				state = 0
		elif state == 4:
			if c == 'p':
				state = 5
			else:
				state = 0
		elif state == 5:
			if c == 'u':
				state = 6
			else:
				state = 0
		elif state == 6:
			if c == 't':
				state = 7
			else:
				state = 0
		elif state == 7:
			if c == 'a':
				state = 8
			else:
				state = 0
		elif state == 8:
			if c == 'd':
				state = 9
			else:
				state = 0
		elif state == 9:
			if c == 'o':
				state = 10
			else:
				state = 0
		elif state == 10:
			if c == 'r':
				state = 11
			else:
				state = 0
		elif state == 11:
			if c == ' ':
				state = 12
			else:
				state = 0
		elif state == 12:
			print('FOUND AT POSITION', position)
			if c == 'c':
				state = 2
			else:
				state = 0

		position += 1

'''Texto teste:
O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.
'''