import re

def validate(sentence, mask):
	if mask == 'name':
		return re.match('[A-Z][a-z]+ [A-Z][a-z]+$', sentence) != None
	elif mask == 'email':
		return re.match('[a-z]+@[a-z]+\.br$', sentence) != None
	elif mask == 'password':
		return re.match('[A-Za-z0-9]*([A-Z]{1}[A-Za-z0-9]*[0-9]{1}[A-Za-z0-9]*|[0-9]{1}[A-Za-z0-9]*[A-Z]{1}[A-Za-z0-9]*)$', sentence) != None and re.match('(.){8}$', sentence) != None
	elif mask == 'cpf':
		return re.match('[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$', sentence) != None
	elif mask == 'rg':
		return re.match('[0-9]{6}-[0-9]$', sentence) != None
	elif mask == 'phone':
		return re.match('\([0-9]{2}\) [0-9]{5}-[0-9]{4}$', sentence) != None
	elif mask == 'phone_':
		return re.match('\([0-9]{2}\)[0-9]{5}-[0-9]{4}$', sentence) != None
	elif mask == 'cep':
		return re.match('[0-9]{2}\.[0-9]{3}-[0-9]{3}$', sentence) != None
	elif mask == 'date':
		return re.match('[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}$', sentence) != None
	elif mask == 'float':
		return re.match('[+-]?[0-9]+([.,]{1}[0-9]+)*$', sentence) != None
	else:
		raise(Exception('This sentence type is recognized by this software.'))


# Tests
def serialize_tests(mask, sentence_list):
	for sentence in sentence_list:
		if validate(sentence, mask):
			print(sentence, ': OK')
		else:
			print(sentence, ': REJECTED')

# Nomes
serialize_tests('name',
	['Alan Turing', 'Noam Chomsky', 'Italo Campos', 'JUSCELINO KUBITSCHEK', '', 'jANIO qUADROS', 'R3ginaldo S4nt0s'])

# Emails
serialize_tests('email',
	['alanturing@uk.br', 'noam.homsky@homsky.br', 'italo@ufpa.br', 'KUBITSCHEK@gmail.com', '', '@janio@quadros.br', 'r santos@ufpa.br'])

# Senhas
serialize_tests('password',
	['518R2r5e', 'F1234567A', '1234567T', 'ropsSoq0', 'S3nh@123', '1qQ', ' ', 'iw2_3', 'E312 ks8'])

# CPF
serialize_tests('cpf',
	['123.456.789-00', '123.asd.456-78', '12345678900', '123.456.789_05', '756.7732.54-58', '000 456 782 52', ' 456.159.753-46'])

# RG
serialize_tests('rg',
	['875467-2', 'RSFHJO-3', '458716-G', '84 579.9', '854912-5', '845579.3', '3-89545-2'])

# Telefones
serialize_tests('phone',
	['91 99363-1167', '(91) 993631167', '(91) 99363-1167', '91) 9982-1576', '91993421577', '(9I) 99413-1415', '(11) 52534-1167', '3ABC'])

# CEP
serialize_tests('cep',
	['66.645-225', '66.821-110', '66425-115', '25.123-IIO', '12455730', ' 66.452-190', '190'])

# Datas
serialize_tests('date',
	['31/08/2019 20:14:55', '03/7/1956 00:12', '14/03/1995 02-15-20', '13/jun/2000, 14h20', '16/09/1993 14:45:35', '12/12/12 12:12:12', '1/1/99 22:32:1'])

# Float
serialize_tests('float',
	['2.', '0,', '+,02', '+-45.1', '3,5', '3.5', '-5.2', '+12.1265', '5', '+13154.45a'])

