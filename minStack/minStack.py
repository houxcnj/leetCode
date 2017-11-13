class MinStack(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []

	def push(self, x):
		"""
		:type x: int
		:rtype: nothing
		"""
		curMin = self.getMin()
		if curMin == None or curMin > x:
			curMin = x
		self.stack.append((x, curMin))

	def pop(self):
		"""
		:rtype: nothing
		"""
		self.stack.pop()

	def top(self):
		"""
		:rtype: int
		"""
		if not self.stack:
			return None
		return self.stack[-1][0]


	def getMin(self):
		"""
		:rtype: int
		"""
		if not self.stack:
			return None
		return self.stack[-1][1]
