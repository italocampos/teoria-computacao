import string


def print_transition(transition):
	q0, a, A, m, q1 = transition
	print('%s --> %s: (%s, %s, %s)' % (q0, q1, a, A, m))


def print_tape(tape):
	s = ''
	for w in tape[1: -1]:
		s += w
	print('Tape:', s)