''' This class models a Turing Machine. This class models a deterministic TM
and a non-determinis TM, dependeing of the transistions passed. The dictionary
TM has the form bellow:

TM = {'states': [], # set of (str) states
	'alphabet': [], # set of (str) tape alphabet
	'aux_alphabet': [], # set of (str) auxiliar alphabet writen in the tape
	'transitions': [('q0', 'a', 'A', 'L', 'q1'), ...]} # set of transition 
		where 'q0' is the 'from' state, 'a' is the read symbol from the tape,
		'A' is the symbol to write in the tape, 'L' is the move of the tape
		reader (must be ['L' or 'R']), and 'q1' is the 'to' state.
	'starter': ''} # starter state
	'final': []} # set of final (str) states

Each symbol of `TM['alphabet']` and `TM['aux_alphabet']` must have length = 1.
See `self.BLANK` and `self.BEGIN` to blank and begin symbols, respectively.
'''

from tools import print_tape, print_transition


class TuringMachine:
	def __init__(self, TM):
		self.BLANK = '_'
		self.BEGIN = '*'
		if self._check(TM):
			self.states = TM['states']
			self.alphabet = TM['alphabet']
			self.aux_alphabet = TM['aux_alphabet']
			self.transitions = TM['transitions']
			self.starter = TM['starter']
			self.final = TM['final']
		else:
			raise(TypeError('The given Turing Machine is misformed.'))


	# Check if the TM is well-formed
	def _check(self, TM):
		if TM['starter'] not in TM['states']:
			return False
		for state in TM['final']:
			if state not in TM['states']:
				return False
		for t in TM['transitions']:
			if t[0] not in TM['states']:
				return False
			for i in [1, 2]:
				if t[i] not in TM['alphabet'] + TM['aux_alphabet'] + [self.BLANK, self.BEGIN]:
					return False
			if t[3] not in ['L', 'R']:
				return False
			if t[4] not in TM['states']:
				return False
		return True


	def _accept_empty_word(self):
		for t in self.transitions:
			if t[0] == self.starter and t[4] in self.final and self.BLANK in [t[1], t[2]]:
				return True
		return False


	def reconize(self, word):
		if word == '':
			return self._accept_empty_word()
		word = self.BEGIN + word + self.BLANK
		return self._run(list(word), 0, self.starter)


	def _run(self, word, index, state):
		print_tape(word)
		if index < 0:
			return False
		if state in self.final:
			return True
		for transition in self.transitions:
			q0, a, A, m, q1 = transition
			if state == q0:
				copy = word.copy()
				i = index
				if a == copy[i]:
					copy[i] = A
					if m == 'R':
						i += 1
					else:
						i -= 1
					print_transition(transition)
					if self._run(copy, i, q1):
						return True
		print('Track failed.')
		return False