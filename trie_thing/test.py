class A:
	class B:
		def __init__(self):
			self.test = None

	def __init__(self):
		self.test = self.B()

a = A()