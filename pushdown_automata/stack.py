class Stack:
	def __init__(self, items = list()):
		self._stack = list()
		self.push(items)

	def length(self):
		return len(self._stack)

	@property
	def items(self):
		return self._stack

	def push(self, item):
		if item not in ['', []]:
			for i in item[::-1]:
				self._stack.append(i)

	def pop(self):
		if self.length() > 0:
			return self._stack.pop()

	def head(self, item):
		if self.empty():
			return False
		return self._stack[-1] == item

	def empty(self):
		return self._stack == []
	
	def __str__(self):
		return str(self._stack)