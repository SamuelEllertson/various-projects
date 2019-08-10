from collections import defaultdict
from improved_trie_thing import BetterTrie

class Node:

	def __init__(self, value, prime):
		self.value = value
		self.prime = prime
		self.connections = []
		self.signatures = set()

	def connect(self, other):
		self.connections.append(other)

	def getConnection(self, value):
		for node in self.connections:
			if node.value == value:
				return node
		return None

	def addSiganture(self, sig):
		self.signatures.add(sig)

	def signatureExists(self, sig):
		if sig in self.signatures:
			return True
		return False

class Trie:

	def __init__(self):
		self.lookupTable = defaultdict(list)
		self.generator = self.primeGen().__iter__()
		self.containsEmptyString = False

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

		self.createAndConnectNodes(string)
		self.setSignature(string)

	def setSignature(self, string):
		finalIndex = len(string) - 1
		finalChar = string[finalIndex]
		finalNode = self.getNodeAtPosition(finalIndex, finalChar)

		finalNode.addSiganture(self.getSignature(string))

	def getSignature(self, string):
		sig = 1

		for position, char in enumerate(string):
			node = self.getNodeAtPosition(position, char)

			sig *= node.prime

		return sig

	def createAndConnectNodes(self, string):
		for i in range(len(string) - 1):
			headIndex = i
			headChar = string[headIndex]

			tailIndex = i + 1
			tailChar = string[tailIndex]

			headNode = self.getNodeAtPosition(headIndex, headChar)
			tailNode = self.getNodeAtPosition(tailIndex, tailChar)

			headNode.connect(tailNode)		


	def contains(self, string):

		if string == "":
			if self.containsEmptyString:
				return True
			return False

		firstCharacterNodes = self.lookupTable[0]

		node = self.getNodeFromList(firstCharacterNodes, string[0])

		if node is None:
			return False

		sig = node.prime

		for position, char in enumerate(string):

			if position == 0:
				continue

			node = node.getConnection(char)

			if node is None:
				return False

			sig *= node.prime

		return node.signatureExists(sig)

	def getNodeAtPosition(self, position, char):
		nodesAtPosition = self.lookupTable[position]

		node = self.getNodeFromList(nodesAtPosition, char)

		if node is not None:
			return node

		node = Node(char, self.nextPrime())
		self.lookupTable[position].append(node)

		return node

	def getNodeFromList(self, arr, char):
		for node in arr:
			if node.value == char:
				return node
		return None

def r(struct):
	from pympler import asizeof
	return round(asizeof.asizeof(struct) / 1000000, 3)

def test():
	import time
	from pympler import asizeof

	myTrie = Trie()
	betterTrie = BetterTrie()
	theSet = set()

	print(f"Size of trie: {asizeof.asizeof(myTrie)} bytes")
	print(f"Size of betterTrie: {asizeof.asizeof(betterTrie)} bytes")
	print(f"Size of set: {asizeof.asizeof(theSet)} bytes")

	print("\nadding words\n")

	with open("verylongwords.txt", "r", encoding="utf-8") as file:
		ts = time.time()
		
		for line in file:
			break
			myTrie.insert(line.strip())

		te = time.time()
		print(f"trie took {round(te - ts, 3)} s")

	with open("verylongwords.txt", "r", encoding="utf-8") as file:
		ts = time.time()

		for line in file:
			betterTrie.insert(line.strip())

		te = time.time()
		print(f"bettertrie took {round(te - ts, 3)} s")

	with open("verylongwords.txt", "r", encoding="utf-8") as file:
		ts = time.time()

		for line in file:
			theSet.add(line.strip())

		te = time.time()
		print(f"set took {round(te - ts, 3)} s")


	print(f"\nSize of trie: {r(myTrie)} MB")
	print(f"Size of betterTrie: {r(betterTrie)} MB")
	print(f"Size of set: {r(theSet)} MB")

	testStr = "this is a very long string"
	betterTrie.insert(testStr)
	print(betterTrie.getSignature(testStr))

if __name__ == '__main__':
	test()

