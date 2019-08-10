import re

def main():
    game = TicTacToe()
    game.start()

class TicTacToe:

    def __init__(self):
        self.defaultVal = " "
        self.board = [[self.defaultVal]*3 for _ in range(3)]
        self.directions = [
            (0, 0, 0, 1),
            (1, 0, 0, 1),
            (2, 0, 0, 1),
            (0, 1, 0, 0),
            (0, 1, 1, 0),
            (0, 1, 2, 0),
            (0, 1, 0, 1),
            (0, 1, 2, -1),
        ]

    def start(self):
        try:
            while True:
                self.doTurn("X")
                self.doTurn("O")
        except Exception as gameOverText:
            print(gameOverText)

    def doTurn(self, player):
        self.show()
        self.getMove(player)
        self.show()

        if self.checkBoard() is not None:
            raise Exception(f"{player}'s win")

    def getMove(self, player):
        while True:
            text = input(f"{player}'s coordinates:").strip()

            try:
                x = int(re.search(r"^\d+", text).group())
                y = int(re.search(r"\d+$", text).group())
            except:
                print("give cordinates in form x,y")
                continue                

            if not 0 <= x <= 2 or not 0 <= y <= 2:
                print("cordinates are from 0 to 2")
                continue

            if self.board[x][y] is not self.defaultVal:
                print("Pick an empty square")
                continue

            self.board[x][y] = player
            return

    def show(self):
        b = self.board
        print("\n"*100)
        print(f" {b[0][0]} | {b[1][0]} | {b[2][0]}")
        print("---+---+---")
        print(f" {b[0][1]} | {b[1][1]} | {b[2][1]}")
        print("---+---+---")
        print(f" {b[0][2]} | {b[1][2]} | {b[2][2]}")

    def checkBoard(self):
        for direction in self.directions:
            if self.check(*direction) is not None:
                return self.check(*direction)
        return None

    def check(self, x, xinc, y, yinc):
        board = self.board
        if (board[x][y] == board[x + xinc][y + yinc] == board[x + xinc*2][y + yinc*2]) and board[x][y] != self.defaultVal:
            return board[x][y]
        return None

if __name__ == '__main__':
    main()