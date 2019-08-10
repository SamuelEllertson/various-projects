
class Hangman:

	def __init__(self):
		self.word = ""
		self.letterList = []
		self.guessedSet = set()
		self.wrongCount = 0
		self.guessList = []
		self.maxWrongGuesses = 10

	def play(self):
		
		self.initializeGame()
		self.clearScreen()

		while True:
			
			self.displayState()

			letter = self.getGuess()

			if letter in self.guessedSet:
				self.clearScreen()
				print("You already guessed that letter\n")
				continue

			self.guessedSet.add(letter)

			if letter not in self.letterList:
				self.wrongCount += 1
				self.clearScreen()
				print("That letter is not in the word\n")

				if self.tooManyGuesses():
					self.displayLose()
					exit()

				continue

			self.addToGuessList(letter)
			self.clearScreen()

			if self.wordIsSolved():
				self.displayWin()
				exit()

	def initializeGame(self):
		self.word = self.getWord()
		self.letterList = list(self.word)
		self.guessList = [None] * len(self.word)
		
	def clearScreen(self):
		for i in range(25):
			print("\n\n\n\n")

	def displayState(self):
		print("Wrong guesses: " + str(self.wrongCount) + ", only " + str(self.maxWrongGuesses - self.wrongCount) + " remaining")

		print("Guessed Letters: " + "".join(sorted(list(self.guessedSet))))

		string = ""
		for char in self.guessList:
			if char is None:
				string += "_"
			else:
				string += char

		print("word: " + string + "\n")

	def getGuess(self):
		while True:
			guess = input("Guess a Letter (or type exit): ").strip().upper()
			if guess == "exit":
				exit()
			if len(guess) != 1:
				self.clearScreen()
				print("only enter one letter\n")
				continue
			if not guess.isalpha():
				self.clearScreen()
				print("only enter a-z letters\n")
				continue
			return guess

	def getWord(self):
		while True:
			word = input("Enter a Word: ").strip()

			if not word.isalpha():
				print("only enter a-z words, no spaces or punctuation")
				continue

			return word.upper()

	def tooManyGuesses(self):
		if self.wrongCount > self.maxWrongGuesses:
			return True
		return False

	def addToGuessList(self, letter):
		for index, char in enumerate(self.letterList):
			if char == letter:
				self.guessList[index] = letter

	def displayLose(self):
		print("You Lose.\n")
		input("Press any key to exit.")

	def displayWin(self):
		print("You Win.\n")
		input("Press any key to exit.")

	def wordIsSolved(self):
		for val in self.guessList:
			if val is None:
				return False
		return True

if __name__ == '__main__':
	game = Hangman()
	game.play()