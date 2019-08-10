
class HashTable:

	def __init__(self, size=10):
		self.table = [[] for i in range(size)]
		self.numItems = 0
		self.maxLoad = 1.5
		self.increaseFactor = 2

	def get(self, key):
		outerIndex = self.getIndex(key)
		innerIndex = self.findTupleInnerIndex(key)

		if innerIndex is None:
			raise KeyError("Can not get key/item pair that does not exist")

		return self.table[outerIndex][innerIndex][1]

	def set(self, key, value):
		if self.keyExists(key):
			self.overrideKey(key, value)
			return

		if self.needsRehash():
			self.rehash()

		index = self.getIndex(key)

		self.table[index].append((key, value))
		self.numItems += 1

	def remove(self, key):
		if not self.keyExists(key):
			raise KeyError("Can not remove key/item pair that does not exist")

		outerIndex = self.getIndex(key)
		innerIndex = self.findTupleInnerIndex(key)

		self.table[outerIndex].pop(innerIndex)
		self.numItems -= 1

	def keyExists(self, key):
		if self.findTupleInnerIndex(key) is None:
			return False
		return True

	def findTupleInnerIndex(self, key):
		outerIndex = self.getIndex(key)

		for innerIndex, (tempKey, tempVal) in enumerate(self.table[outerIndex]):
			if tempKey == key:
				return innerIndex

		return None

	def getIndex(self, key):
		return hash(key) % len(self.table)

	def needsRehash(self):
		if self.getLoadFactor() > self.maxLoad:
			return True

		return False

	def rehash(self):
		newSize = len(self.table) * self.increaseFactor

		newTable = HashTable(newSize)

		for arr in self.table:
			for key, value in arr:
				newTable.set(key, value)

		self.table = newTable.table

	def getLoadFactor(self):
		return self.numItems / len(self.table)
	
	def overrideKey(self, key, value):
		outerIndex = self.getIndex(key)
		innerIndex = self.findTupleInnerIndex(key)

		self.table[outerIndex][innerIndex] = (key, value)

	def keys(self):
		return self.__iter__()

	def values(self):
		for arr in self.table:
			for key, value in arr:
				yield value

	def items(self):
		for arr in self.table:
			for key, value in arr:
				yield key, value

	def __str__(self):
		size = len(self.table)
		loadFactor = self.getLoadFactor()

		return f'<HashTable, size={size}, numItems={self.numItems}, loadFactor={loadFactor}>'
	
	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.set(key, value)

	def __delitem__(self, key):
		self.remove(key)

	def __contains__(self, key):
		return self.keyExists(key)

	def __iter__(self):
		for arr in self.table:
			for key, value in arr:
				yield key
