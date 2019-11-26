from pdautomata import PDAutomata
from tools import *

# Exemplos de gramáticas pré-carregadas

# Duplo balanceamento em {a, b}*
G1 = {'V': ['S', 'B'],
	'T': ['a', 'b'],
	'R': [('S', 'aB'), ('S', 'aSB'), ('B', 'b')],
	'S': 'S'}

#  {wwr | w é palavra de {a, b}*}
G2 = {'V': ['S', 'A', 'B'],
	'T': ['a', 'b'],
	'R': [('S', 'a'), ('S', 'b'), ('S', 'aSA'),
		('S', 'bSB'), ('A', 'a'), ('B', 'b')],
	'S': 'S'}

# {wr | w é palavra de {a, b}*}
G3 = {'V': ['S', 'A', 'B'],
	'T': ['a', 'b'],
	'R': [('S', 'a'), ('S', 'b'), ('S', 'aSA'),
		('S', 'bSB'), ('S', 'aA'), ('S', 'bB'),
		('A', 'a'), ('B', 'b')],
	'S': 'S'}

# Balanceamento de parêntesis
G4 = {'V': ['S', 'A'],
	'T': ['x', 'y', '(', ')'],
	'R': [('S', '(SA'), ('S', 'xS'), ('S', 'yS'),
		('S', 'x'), ('S', 'y'), ('S', '(A'), ('S', '(SAS'),
		('S', 'xSS'), ('S', 'ySS'), ('S', '(AS'), ('A', ')')],
	'S': 'S'}

# Para ler uma nova gramática do arquivo, descomente a linha abaixo
G = read_from_file('grammar.in')

auto = PDAutomata(G)
