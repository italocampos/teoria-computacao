class Stack:
	def __init__(self, elements = list()):
		self.stack = list()
		self.stack += elements

	def elements(self):
		return len(self.stack)

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		return self.stack.pop()

	def head(self, element):
		return self.stack[-1] == element

	def pop_if(self, element):
		if self.head(element):
			return self.pop()
	
	def __str__(self):
		return str(self.stack)