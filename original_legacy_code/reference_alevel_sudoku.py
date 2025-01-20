import random
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from functools import partial


# creates a 9x9 2d array
def createBoardArray():
    board = [[0 for x in range(9)] for y in range(9)]
    # board[0][1] = 2
    return board


# displays the board
def showBoard(board):
    for i in range(9):
        print(board[i], end="\n")
    return


# checks which subsquare a cell is in
def whichSquare(currentRow, currentColumn):
    i = currentRow
    j = currentColumn
    if i < 3:  # top row
        if j < 3:
            return 1
        elif j < 6:
            return 2
        else:
            return 3
    elif i < 6:  # second row
        if j < 3:
            return 4
        elif j < 6:
            return 5
        else:
            return 6
    else:  # third row
        if j < 3:
            return 7
        elif j < 6:
            return 8
        else:
            return 9


# checks if a board is valid
def isValid(board, currentRow, currentColumn):
    currentNumber = board[currentRow][currentColumn]
    repeatCount = -3  # how many times the number is repeated

    # row
    i = currentRow
    for j in range(9):
        if board[i][j] == currentNumber:
            repeatCount += 1

    # column
    j = currentColumn
    for i in range(9):
        if board[i][j] == currentNumber:
            repeatCount += 1

    # square
    square = whichSquare(currentRow, currentColumn)
    print("square" + str(square))
    if square == 1 or square == 2 or square == 3:
        for i in range(3):
            if square == 1:
                for j in range(3):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
                        print("square repeat")
            elif square == 2:
                for j in range(3, 6):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
            else:
                for j in range(6, 9):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
    elif square == 4 or square == 5 or square == 6:
        for i in range(3, 6):
            if square == 4:
                for j in range(3):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
            elif square == 5:
                for j in range(3, 6):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
            else:
                for j in range(6, 9):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
    elif square == 7 or square == 8 or square == 9:
        for i in range(6, 9):
            if square == 7:
                for j in range(3):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
            elif square == 8:
                for j in range(3, 6):
                    if board[i][j] == currentNumber:
                        repeatCount += 1
            else:
                for j in range(6, 9):
                    if board[i][j] == currentNumber:
                        repeatCount += 1

    # did it only appear once?
    print(repeatCount)
    if repeatCount > 0:
        return False
    else:
        return True


# randomises the board
# used in development but not needed for final solution
def scrambleBoard(board):
    for x in range(1000):
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        board[i][j] = random.randint(1, 9)
    return


# prints square
def printSquare(board, square):
    if square == 1:
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=" ")
    if square == 2:
        for i in range(3):
            for j in range(3, 6):
                print(board[i][j], end=" ")
    if square == 4:
        for i in range(3, 6):
            for j in range(3):
                print(board[i][j], end=" ")


# finds coordinates of first cell that contains a 0
def findNextCell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    else:
        return False


# checks if the board has no 0s
def isComplete(board):
    flag = True
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                flag = False
    return flag


# recursive backtracking to try every number
def solveBoard(board):
    if isComplete(board):  # to terminate function if complete
        return board
    else:
        i, j = findNextCell(board)
        print(i, j)
        for tryNum in range(1, 10):  # inputting each number from 1-9
            board[i][j] = tryNum
            if isValid(board, i, j):
                showBoard(board)
                solveBoard(board)
                if isComplete(board):
                    return board
        board[i][j] = 0


# generates a board for the player to play on
def generateBoard():
    board = createBoardArray()
    for i in range(5):  # insert 5 random squares
        number = random.randint(1, 10)
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = number
        print(board)
    try:
        solveBoard(board)
        print("success")
    except:
        print("unsuccessful")
    return board


def difficultyScore(difficulty):  # calculate the score based on hints
    return int(difficulty) * 0.25


def hintScore(hintCount):  # calculate the score based on hints
    if hintCount == 0:
        score = 1
    else:
        score = 0.80 - (hintCount * 0.05)

    if score < 0:
        score = 0

    return score


def timeScore(timeTaken):  # calculate the score based on hints
    score = 1 - (timeTaken / 1800)
    if score < 0:
        score = 0
    return score


# not wokring
def calculateScore1():
    # output = difficultyScore() * hintScore() * timeScore()
    return output


def setBoard():
    board = [[0, 0, 5, 4, 0, 0, 0, 0, 0],
             [0, 3, 0, 0, 0, 5, 0, 7, 6],
             [0, 0, 0, 0, 0, 0, 0, 2, 0],
             [7, 0, 0, 8, 0, 0, 0, 6, 1],
             [0, 0, 0, 0, 0, 0, 2, 0, 0],
             [0, 1, 0, 0, 0, 0, 4, 0, 0],
             [0, 7, 0, 0, 0, 4, 0, 5, 3],
             [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [8, 0, 0, 0, 9, 0, 0, 0, 0]]
    return board


def initGameWindow(board):
    gamewindow = Sudoku_Main(board)
    gamewindow.show()


class mainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.resize(600, 600)
        self.mainbuttons()
        #self.setStyleSheet(open('styleSheet.css').read()) STYLE SHEET !!!!!
        self.show()

    def mainbuttons(self):
        # logo
        self.imagelabel = QtWidgets.QLabel(self)
        self.imagelabel.setPixmap(
            QtGui.QPixmap("logo.png").scaled(600, 600, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.imagelabel.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.imagelabel.move(0, -250)

        # play
        self.playButton = QPushButton('Play', self)
        self.playButton.setToolTip('Opens the Game Window')
        # button.setGeometry(left,top,width,height)
        self.playButton.setGeometry(50, 150, 500, 50)
        self.playButton.clicked.connect(self.play_clicked)
        self.playButton.setObjectName('playButton')
        # settings
        self.settingsButton = QPushButton('Settings', self)
        self.settingsButton.setToolTip('Opens the Settings Window')
        self.settingsButton.setGeometry(50, 200, 500, 50)
        self.settingsButton.clicked.connect(self.settings_clicked)
        self.settingsButton.setObjectName('settingsButton')

        # creatorTag
        self.creatorTag = QLabel('Rohan Shergill', self)
        self.creatorTag.setGeometry(400, 450, 200, 200)
        self.creatorTag.setObjectName('creatorTag')

    def play_clicked(self):
        print("pressed")

    def settings_clicked(self):
        print("settings pressed")


class Sudoku_Main(QtWidgets.QMainWindow):
    def __init__(self, board):
        super().__init__()
        self.timervalue = 0
        self.board = board
        self.background = QtWidgets.QLabel(self)
        self.background.setPixmap(
            QtGui.QPixmap("board.png").scaled(900, 900, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.background.setGeometry(QtCore.QRect(0, 0, 900, 900))
        self.setStyleSheet(
            "background-color: rgba(0,0,0,0%); color:white;font-size:40px;")  # add to external file if able to
        self.grid_labels = [[0 for x in range(9)] for y in range(9)]
        self.size_properties()
        self.difficulty = 2  # set difficulty
        # self.image_grid()
        self.labels_present()
        self.buttons(board)

        self.updateBoard(board)
        self.highlightedElement = QtWidgets.QPushButton(self)

        self.selectedElementI = 0
        self.selectedElementJ = 0

        # self.highlightElement(0,0)

        self.show()

    def buttons(self, board):
        self.autoSolveButton = QtWidgets.QPushButton(self)
        self.autoSolveButton.setText("Auto-Solve")
        self.autoSolveButton.clicked.connect(partial(self.autoSolve, board))
        self.autoSolveButton.setGeometry(900, 0, 500, 100)

        self.checkAnswer = QtWidgets.QPushButton(self)
        self.checkAnswer.setText("Check Answer")
        self.checkAnswer.clicked.connect(partial(self.checkAnswerFunc, board))
        self.checkAnswer.setGeometry(900, 100, 500, 100)

        self.newgame = QtWidgets.QPushButton(self)
        self.newgame.setText("New Game")
        self.newgame.clicked.connect(self.autoSolve)
        self.newgame.setGeometry(900, 200, 500, 100)

        self.giveHint = QtWidgets.QPushButton(self)
        self.giveHint.setText("Give Hint")
        self.giveHint.clicked.connect(self.hints)
        self.giveHint.setGeometry(900, 300, 500, 100)
        return

    def newGame(self):
        return

    def hints(self):
        return

    def autoSolve(self, board):
        print("autoSolve ran")
        self.updateBoard(solveBoard(board))

        return

    def getDifficulty(self, board):
        return self.difficulty

    # function which is triggered when "Check Answer" button is clicked
    def checkAnswerFunc(self, board):
        flag = True
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    flag = False
        if flag:  # all squares are filled
            flag = True
            for i in range(9):
                for j in range(9):
                    if not isValid(self.board, i, j):
                        flag = False
            if flag:  # correctly completed board
                QMessageBox.about(self, "Sudoku", "Congratulations! Your board is correct.")

                # sequence of events when board is correct
                print("Score:")
                print(self.calculateScore(1, 3, 640))

            else:  # incorrectly completed board
                QMessageBox.about(self, "Sudoku", "Unfortunately your board contains some errors.")
        else:  # not all squares are filled
            QMessageBox.about(self, "Sudoku",
                              "This board is not solvable.")  # Not all squares are completed on this board!
        return

    def keyPressEvent(self, event):
        print(event.text())

        if event.text().isnumeric():
            self.updateNumber(event.text())

        return

    # if event.text().isnumeric() and event.text() != "0" or event.text() == "-": can be entered above to allow no 0s and -s

    def updateNumber(self, newNumber):
        self.grid_labels[self.selectedElementI][self.selectedElementJ].setText(newNumber)
        self.highlightElement(self.selectedElementI, self.selectedElementJ)
        self.board[self.selectedElementI][self.selectedElementJ] = int(newNumber)
        return

    def size_properties(self):
        self.width = 900
        self.length = 900
        self.setMaximumSize(1500, 900)
        self.setMinimumSize(1500, 900)
        self.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.setWindowTitle("Sudoku")

    def image_grid(self):
        self.imagelabel = QtWidgets.QLabel(self)
        self.imagelabel.setPixmap(
            QtGui.QPixmap("download.png").scaled(self.width, self.length, QtCore.Qt.KeepAspectRatio,
                                                 QtCore.Qt.SmoothTransformation))
        self.imagelabel.setGeometry(QtCore.QRect(0, 0, self.width, self.length))

    def labels_present(self):
        for i in range(9):
            for j in range(9):
                buttonName = str(i) + str(j)
                self.grid_labels[i][j] = QtWidgets.QPushButton(self)
                self.grid_labels[i][j].setGeometry(QtCore.QRect(100 * j, 100 * i, 100, 100))
                self.grid_labels[i][j].setText("0")
                self.grid_labels[i][j].clicked.connect(partial(self.highlightElement, i, j))

    def numberClicked(self, whichButton):
        print(whichButton)
        return

    def buttonPressed(self):
        print(clicked)
        return

    def updatenum(self, i, j, string):
        self.grid_labels[i][j].setText(string)
        return

    def updateBoard(self, board):
        for i in range(9):
            for j in range(9):
                self.updatenum(i, j, str(board[i][j]))
        return

    def highlightElement(self, i, j):
        self.unhighlightElement()
        self.setSelectedElement(i, j)
        contents = self.grid_labels[i][j].text()
        self.highlightedElement = QtWidgets.QPushButton(self)
        self.highlightedElement.setGeometry(j * 100, i * 100, 100, 100)
        self.highlightedElement.setText(contents)
        self.highlightedElement.setStyleSheet("background-color: rgba(0,0,0); color:white;font-size:40px;")
        self.highlightedElement.show()
        return

    def unhighlightElement(self):
        self.highlightedElement.hide()
        return

    def setSelectedElement(self, i, j):
        self.selectedElementI = i
        self.selectedElementJ = j
        return

    # calculates game score based on stastics of the game
    def calculateScore(self, difficulty, hintCount, timeTaken):
        score = difficultyScore(difficulty) + hintScore(hintCount) + timeScore(timeTaken)
        score = score * 1000/3
        return score


def main():  # row col
    board = createBoardArray()
    showBoard(board)
    print(difficultyScore(4))
    print(hintScore(60))
    print(timeScore(4000))
    board = setBoard()
    Sudoku_Application = QtWidgets.QApplication(sys.argv)

    menuwindow = mainMenu()
    gamewindow = Sudoku_Main(board)
    gamewindow.show()
    menuwindow.show()
    sys.exit(Sudoku_Application.exec_())

    return


if __name__ == '__main__':
    main()
