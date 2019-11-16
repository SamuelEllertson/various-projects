#!/usr/bin/env python

from enum import Enum
from itertools import chain

class Color(Enum):
    RED = 1
    BLACK = 2

class GameException(Exception):
    pass

class Piece:
    def __init__(self, color, isKing=False):
        self.color = color
        self.isKing = isKing

    def __repr__(self):
        if self.color == Color.RED:
            return "R" if self.isKing else "r"
        return "B" if self.isKing else "b"

class Board:
    def __init__(self, size=8):
        self.size = size
        self.state = [[None] * size for _ in range(size)]

    def __getitem__(self, key):
        return self.state[key[0]][key[1]]

    def __setitem__(self, key, value):
        self.state[key[0]][key[1]] = value

    def __iter__(self):
        return chain(*self.state)

    def getIndexRow(self):
        output = []
        for i in range(self.size):
            output.append(str(i).center(3))
        return "    " + " ".join(output)

    def getBoarder(self):
        return "   " + "---".join(['+'] * (self.size + 1))

    def getRow(self, index, row):
        output = ['|']
        for piece in row:
            output.append(f" {piece} |" if piece is not None else "   |")
        return str(index).center(3) + "".join(output)

    def __repr__(self):
        output = [self.getIndexRow(), self.getBoarder()]

        for index, row in enumerate(self.state):
            output.append(self.getRow(index, row))
            output.append(self.getBoarder())

        return "\n".join(output)    

class Checkers:
    def __init__(self, size=8):
        self.board = Board(size)
        self.player = Color.RED
        self.initializeBoard()

    def play(self):
        while True:
            self.doTurn()

            if self.gameIsOver():
                self.printWinner()
                break

            self.swapTurn()

    def initializeBoard(self):
        size = self.board.size

        offset = 1
        for row in range(3):
            for col in range(offset, size, 2):
                self.board[row, col] = Piece(color=Color.BLACK)
            offset = (offset + 1) % 2

        offset = size % 2
        for row in range(size - 1, size - 4, -1):
            for col in range(offset, size, 2):
                self.board[row, col] = Piece(color=Color.RED)
            offset = (offset + 1) % 2 

    def clearScreen(self):
        print("\n" * 20)

    def doTurn(self):
        

        while True:
            self.clearScreen()
            print(f"It is {self.player.name}'s turn\n")
            print(self.board)

            turnOver, oldPos, newPos, jumpedPos = self.getMove()

            if turnOver:
                break

            self.board[newPos] = self.board[oldPos]
            self.board[oldPos] = None

            #remove jumped piece
            if jumpedPos is not None:
                self.board[jumpedPos] = None

            #kinging
            if self.player == Color.RED and newPos[0] == 0 or self.player == Color.BLACK and newPos[0] == self.board.size - 1:
                self.board[newPos].isKing = True

    def getMove(self):

        while True:
            try:
                userInput = input("From : To [or done]: ").lower().strip()

                #finish turn
                if userInput in ['done', 'd']:
                    return True, None, None, None

                #quit game
                if userInput in ['quit', 'q']:
                    exit()

                oldPos, newPos = self.convertInput(userInput)

                jumpedPos = self.processMove(oldPos, newPos)

                return False, oldPos, newPos, jumpedPos
            
            except GameException as e:
                print(e)
                continue
            except Exception as e:
                print("invalid input")
                continue

    def processMove(self, oldPos, newPos):

        if len(oldPos) != 2 or self.board[oldPos].color != self.player:
            raise GameException("Must choose piece of your color")

        piece = self.board[oldPos]

        if len(newPos) != 2 or self.board[newPos] is not None:
            raise GameException("Must choose an empty square")

        dx = newPos[1] - oldPos[1]
        dy = newPos[0] - oldPos[0]

        #Check: All moves are square, and at most 2 squares away
        if abs(dx) != abs(dy) or abs(dx) not in [1,2]:
            raise GameException("Illegal Move")

        #Check: non king pieces are moving 'forward'
        if not piece.isKing and (self.player == Color.BLACK and dy < 0 or self.player == Color.RED and dy > 0):
            raise GameException("Illegal Move")

        #Case: Jumping
        if abs(dx) == 2:
            
            jumpedPos = oldPos[0] + dy//2, oldPos[1] + dx//2
            print(dx, dy)
            print(jumpedPos)
            if self.board[jumpedPos] is None or self.board[jumpedPos].color == self.player:
                raise GameException("Must only jump over enemy pieces")

            #All checks passed
            return jumpedPos
        
        #Case: Not jumping -> All checks have been passed -> return None (not jumping)
        return None

    def convertInput(self, userInput):
        return tuple(tuple(int(val.strip()) for val in string.strip().split(",")) for string in userInput.split(":"))

    def gameIsOver(self):
        for piece in self.board:

            if piece is None:
                continue

            if piece.color == self.otherPlayer:
                return False
        return True

    @property
    def otherPlayer(self):
        if self.player == Color.RED:
            return Color.BLACK
        return Color.RED

    def swapTurn(self):
        self.player = self.otherPlayer

    def printWinner(self):
        print(f"{self.player.name} has Won")



def main():
    game = Checkers()
    game.play()

if __name__ == '__main__':
    main()