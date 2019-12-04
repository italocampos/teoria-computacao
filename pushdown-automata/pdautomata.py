from stack import Stack
from tools import check_gnf, debug

class PDAutomata:
	def __init__(self, G = {'V':[], 'T':[], 'R':[], 'S':''}):
		self.grammar = G
		self._transitions = list()
		self.transitions = G['R']

	@property
	def transitions(self):
		return self._transitions

	@transitions.setter
	def transitions(self, rules):
		for rule in rules:
			self._transitions.append((rule[1][0], rule[0], rule[1][1:]))

	@property
	def grammar(self):
		return self._grammar


	@grammar.setter
	def grammar(self, G):
		if check_gnf(G):
			self._grammar = G
		else:
			raise(Exception('The given grammar is not well-formed or not in Greibach Normal Form.'))

	def reconize(self, word):
		stack = Stack(list(self.grammar['S']))
		return self._run(word, 0, stack)

	def _run(self, word, index, stack):
		if index == len(word):
			return stack.empty()
		symbol = word[index]
		for transition in self.transitions:
			t, V, S = transition 
			if t == symbol and stack.head(V):
				s = Stack(stack.items[::-1])
				s.pop()
				s.push(S)
				debug(index, transition, stack)
				if self._run(word, index + 1, s):
					return True
		return False