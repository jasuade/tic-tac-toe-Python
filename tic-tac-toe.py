import random
from time import sleep

class game:
  #Initialize the board and all variables
  def __init__(self):
    self.board = [[0,0,0],[0,0,0],[0,0,0]]
    self.no_exit = True
    self.players = ['X', 'O'] #'X' is the User and 'O' the computer
    self.positionsX = []
    self.positionsO = []

  #Improved way to draw a board in the cmd (v2)
  def drawBoard(self):
    print '-------------\n'
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        print '|', 
        if self.board[i][j] == 1:
          print self.players[0],
        elif self.board[i][j] == -1:
          print self.players[-1],
        elif self.board[i][j] == 0:
          print ' ',
      print '| \n'
    print '------------- \n'

  #Set the move on the board from the different players
  def setMove(self, move, player):
    x = move[0]
    y = move[1]
    if self.board[x][y] != 0:
      print 'Invalid choice: position already held'
      return False
    else:
      self.board[x][y] = player
      self.drawBoard()
      return True

  #Check if there is a line, there is a winner
  def checkMatrix(self):
    for elem in self.board:
      self.checkLine(elem)
    self.checkLine([self.board[0][0], self.board[1][0], self.board[2][0]])
    self.checkLine([self.board[0][1], self.board[1][1], self.board[2][1]])
    self.checkLine([self.board[0][2], self.board[1][2], self.board[2][2]])
    self.checkLine([self.board[0][0], self.board[1][1], self.board[2][2]])
    self.checkLine([self.board[0][2], self.board[1][1], self.board[2][0]])
    if self.boardIsFull():
      print 'End of the game: TIE'
      self.no_exit = False

  def boardIsFull(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == 0:
          return False
    return True

  #Aux function to check full spaces in the board
  def checkLine(self, line):
    p1 = line.count(1) 
    p2 = line.count(-1) 
    if p1 == 3:
      print 'Player 1 wins the game'
      self.no_exit = False
    elif p2 == 3:
      print 'Player 2 wins the game'
      self.no_exit = False
    elif 2 in (p1 , p2):
      return True
    else:
      return False
  
  def clearPositions(self):
    self.positionsX = []
    self.positionsO = []

  def machineMove(self):
    for i in range(len(self.board)):
    #Check positions of 'O' and 'X' in the board
      for j in range(len(self.board[i])):
        if self.board[i][j] == 1:
          self.positionsX.append([i,j])
        elif self.board[i][j] == -1:
          self.positionsO.append([i,j])
    #Could check the O first, and then the X
    #If there is any row with two 'O' --> complete the line || If there is a row with two 'X' --> break the line
    #Check rows
      for i in range(len(self.board)):
        if self.board[i].count(-1) == 2:
          for j in range(len(self.board[i])):
            if self.board[i][j] == 0:
              move = [i,j]
              self.clearPositions()
              return move
        if self.board[i].count(1) == 2:
          for j in range(len(self.board[i])):
            if self.board[i][j] == 0:
              move = [i,j]
              self.clearPositions()
              return move
        #Check columns 
        if self.checkLine([self.board[0][i], self.board[1][i], self.board[2][i]]):
          for j in range(len(self.board[i])):
            if self.board[j][i] == 0:
              move = [j,i]
              self.clearPositions()
              return move
    #Check diagonals
    if self.checkLine([self.board[0][0], self.board[1][1], self.board[2][2]]):
      for j in range(len(self.board)):
        if self.board[j][j] == 0:
          move = [j,j]
          self.clearPositions()
          return move
    if self.checkLine([self.board[0][2], self.board[1][1], self.board[2][0]]):
      for idx, j in enumerate(range(2,-1,-1)):
        if self.board[idx][j] == 0:
          move = [idx,j]
          self.clearPositions()
          return move
    #If there is no line with two symbols then:
    if (len(self.positionsO) == 0) and (len(self.positionsX) == 0):
      x = random.choice([0,1,2])
      y = random.choice([0,1,2])
      move = [x,y]
      self.clearPositions()
      return move
    elif (len(self.positionsO) == 0) and (len(self.positionsX) == 1):
      #'O' in center position
      if self.positionsX[0] == [1,1]:
        x = random.choice([0,2])
        y = random.choice([0,2])
        self.clearPositions()
        return [x,y]
      else:
        #Could be better decision to take in this place
        self.clearPositions()
        return [1,1]
    return self.defaultCase()

  def defaultCase (self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == 0:
          self.clearPositions()
          return [i,j]


def main():
  
  g1 = game()
  g1.drawBoard()
  player = random.choice ([1,-1])

  while g1.no_exit:
    if player == 1 and g1.no_exit:                             # The User
      print "Set position (row,col) from 0 to 2: ",
      move = input()
      if 0 <= move[0] and move[1] < 3:
        if g1.setMove(move, player):
          g1.checkMatrix()
          sleep(1)
          player = -1
      else:
        print 'Movement out of board'
    if player == -1 and g1.no_exit:                             # The Computer
      move = g1.machineMove()
      if move != None:
        if g1.setMove(move, player):
          g1.checkMatrix()
          player = 1
  else:
    print "Play another game? (yes/no)",
    ans = raw_input()
    if ans == 'yes':
      main()
    else:
      quit()


if __name__ == "__main__":
    main()
