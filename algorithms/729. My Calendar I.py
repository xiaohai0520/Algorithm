class TreeNode():
	def __init__(self, s, e):
		self.s = s
		self.e = e
		self.left = None
		self.right = None

class MyCalendar:

	def __init__(self):
		self.root = None

	def book(self, start: int, end: int) -> bool:
		if not self.root:
			self.root = TreeNode(start, end)
			return True
		else:
			return self.insert(start, end, self.root)

	# try to decide where I can go
	# if my start is greater than or equal to end then go to the right
	# equal is allowed as "end" is not part of the interval

	# if my end is less than or equal to the start then go to the left
	# equal is allowed as "end" is not part of the interval
	def insert(self, s, e, node):
		if s >= node.e: 
			if node.right:
				return self.insert(s, e, node.right)
			else:
				node.right = TreeNode(s, e)
				return True
		elif e <= node.s: 
			if node.left:
				return self.insert(s, e, node.left)
			else:
				node.left = TreeNode(s, e)
				return True
		else:
			return False
