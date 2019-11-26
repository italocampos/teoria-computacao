import string

''' The dictionary G has the form bellow:
G = {'V': ['S', 'B'], # set of variables (a variable must have length = 1)
	'T': ['a', 'b'], # set of terminal symbols (a symbol must have length = 1)
	'R': [('S', 'aB'), ('S', 'aSB'), ('B', 'b')], # set of production rules
	'S': 'S'} # starter symbol
where G is a Context-Free Grammar in Greibach Normal Form
'''

# Check if the grammar G is well-formed
def check_well_formed(G):
	if G['S'] not in G['V']:
		return False
	for rule in G['R']:
		if len(rule[0]) != 1 or rule[0] not in G['V']:
			return False
		for symbol in rule[1]:
			if symbol not in G['V'] + G['T']:
				return False
	return True


# Check if the grammar G is in Greibach Normal Form
def check_gnf(G):
	if check_well_formed(G):
		for rule in G['R']:
			if rule[1][0] in G['T']:
				for symbol in rule[1][1:]:
					if symbol not in G['V']:
						return False
			else:
				return False
	else:
		return False
	return True


# Reads the user input from a file and creates a valid grammar dictionary
def read_from_file(file_name):
	file = open(file_name, 'r')
	text = file.read() # Reads all file in `text`
	text = text.translate({ord(c): None for c in string.whitespace}) # Removes all the spaces characters
	# Separates the grammar into 4 groups
	groups = list()
	temp = text.split('}') # Separates into 4 groups
	for group in temp[:3]:
		groups.append(group[group.find('{')+1:]) # Removes garbage
	groups.append(temp[3].replace(',','').replace(')','')) # Removes garbage
	# Create a dict with the groups V, T, R and S
	G = {'V': groups[0].split(','),
		'T': groups[1].split(','),
		'R': groups[2].split(','),
		'S': groups[3],}
	# Puts the `R` set on the form ('A', 'a'), with A £ V and a £ (V U T)*
	rules = G['R']
	result = list()
	for part in rules:
		l = part.replace('-', '')
		head, body = l.split('>')
		body = body.split('|')
		for alpha in body:
			result.append((head, alpha))
	G['R'] = result
	return G


def debug(level, transition, stack):
	space = '  '
	ident = ''
	for i in range(level):
		ident += space
	print('%sLEVEL: %d. Transition %s' % (ident, level, transition))
	print('%sStack: %s' % (ident, stack))