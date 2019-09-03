import re

def validate(pattern, pattern_type):
	if pattern_type == 'name':
		return not re.match('[A-Z][a-z]+ [A-Z][a-z]+$', pattern) == None
	elif pattern_type == 'email':
		return not re.match('[a-z]+@[a-z]+\.br$', pattern) == None
	elif pattern_type == 'password':
		pass
		#return not re.match('([a-z]*([A-Z]|[0-9])+[a-z]*([A-Z]|[0-9])+[a-z]*)$', pattern) == None
		#return not re.match('([a-z]|[A-Z]|[0-9]){8}$', pattern) == None
	elif pattern_type == 'cpf':
		return not re.match('[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', pattern) == None
	elif pattern_type == 'rg':
		return not re.match('[0-9]{6}-[0-9]$', pattern) == None
	elif pattern_type == 'phone':
		return not re.match('\([0-9]{2}\) [0-9]{5}-[0-9]{4}$', pattern) == None
	elif pattern_type == 'phone_':
		return not re.match('\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', pattern) == None
	elif pattern_type == 'cep':
		return not re.match('[0-9]{2}\.[0-9]{3}-[0-9]{3}$', pattern) == None
	elif pattern_type == 'date':
		return not re.match('[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$', pattern) == None
	elif pattern_type == 'float':
		return not re.match('[+-]?[0-9]+([\.,]{1}[0-9]+)*$', pattern) == None
	else:
		raise(Exception('This pattern type is not recognized by this software.'))

# Tests
#print(validate('t', 'name'))