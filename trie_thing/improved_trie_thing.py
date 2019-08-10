from collections import defaultdict

class BetterTrie:

	def __init__(self):
		self.lookupTable = defaultdict(dict)
		self.generator = self.primeGen().__iter__()
		self.containsEmptyString = False
		self.signatures = set()

	def nextPrime(self):
		return self.generator.__next__()
	
	def primeGen(self):
		D = {}
		q = 2

		while True:
			if q not in D:
				yield q
				D[q * q] = [q]
			else:
				for p in D[q]:
					D.setdefault(p + q, []).append(p)
				del D[q]
			q += 1

	def insert(self, string):
		if self.contains(string):
			return

		if string == "":
			self.containsEmptyString = True
			return

		self.signatures.add(self.getSignature(string, createNew=True))

	def getSignature(self, string, createNew=True):
		sig = 1

		try:
			for position, char in enumerate(string):
				sig *= self.getNode(position, char, createNew=createNew)
		except(KeyError):
			return -1

		return sig

	def contains(self, string):

		if string == "":
			return self.containsEmptyString

		return self.getSignature(string, createNew=False) in self.signatures

	def getNode(self, position, char, createNew=True):

		if char in self.lookupTable[position]:
			return self.lookupTable[position][char]

		if not createNew:
			raise KeyError("Node does not exist")

		prime = self.nextPrime()

		self.lookupTable[position][char] = prime

		return prime

trie = BetterTrie()