import random
from time import sleep

class game:
#Initialize the board and all variables
  def __init__(self):
    self.board = [[0,0,0],[0,0,0],[0,0,0]]
    self.no_exit = True
    self.players = ['X', 'O'] # 'X' is the User and 'O' the computer
    self.positionsX = []
    self.positionsO = []

#Very ugly improved way to draw a board in the cmd (v2)
  def drawBoard(self):
    print '-------------\n'
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        print '|', 
        if self.board[i][j] != 0:
          print self.board[i][j],
        else:
          print ' ',
      print '| \n'
    print '------------- \n'

#Set the move on the board from the different players
  def setMove(self, move, player):
    x = move[0]
    y = move[1]
    if self.board[x][y] != 0:
      print 'Invalid move: position already held'
      return False
    else:
      self.board[x][y] = self.players[player]
      self.drawBoard()
      return True

#Check if there is a line, there is a winner
  def checkMatrix(self):
    for elem in self.board:
      self.checkLine(elem)
    #Definitely this needs yo be improved
    self.checkLine([self.board[0][0], self.board[1][0], self.board[2][0]])
    self.checkLine([self.board[0][1], self.board[1][1], self.board[2][1]])
    self.checkLine([self.board[0][2], self.board[1][2], self.board[2][2]])
    self.checkLine([self.board[0][0], self.board[1][1], self.board[2][2]])
    self.checkLine([self.board[0][2], self.board[1][1], self.board[2][0]])

  def checkLine(self, line):
    if line.count('X') == 3:
      print 'Player 1 wins the game'
      self.no_exit = False
    elif line.count('O') == 3:
      print 'Player 2 wins the game'
      self.no_exit = False
    return

  def isThereTwo(self, line):
    if line.count('O') == 2:
      return True
    elif line.count('X') == 2:
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
        if self.board[i][j] == 'X':
          self.positionsX.append([i,j])
        elif self.board[i][j] == 'O':
          self.positionsO.append([i,j])
    #If there is any row with two 'O' --> complete the line || If there is a row with two 'X' --> break the line
      for i in range(len(self.board)):
        if self.board[i].count('O') == 2:
          for j in range(len(self.board[i])):
            if self.board[i][j] == 0:
              move = [i,j]
              self.clearPositions()
              return move
        if self.board[i].count('X') == 2:
          for j in range(len(self.board[i])):
            if self.board[i][j] == 0:
              move = [i,j]
              self.clearPositions()
              return move
        #Check columns 
        if self.isThereTwo([self.board[0][i], self.board[1][i], self.board[2][i]]):
          for j in range(len(self.board[i])):
            if self.board[j][i] == 0:
              move = [j,i]
              self.clearPositions()
              return move
    #Check diagonals
    if self.isThereTwo([self.board[0][0], self.board[1][1], self.board[2][2]]):
      for j in range(len(self.board)):
        if self.board[j][j] == 0:
          move = [j,j]
          self.clearPositions()
          return move
    if self.isThereTwo([self.board[0][2], self.board[1][1], self.board[2][0]]):
      for idx, j in enumerate(range(2,-1,-1)):
        if self.board[idx][j] == 0:
          move = [idx,j]
          self.clearPositions()
          return move
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
        #TODO: better decision to take in this place
        self.clearPositions()
        return [1,1]
    return self.defaultCase()

  def defaultCase (self):    
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.board[i][j] == 0:
          self.clearPositions()
          return [i,j]


#----------------TEST--------------------------

def main():
  
  g1 = game()
  g1.drawBoard()
  player = random.choice ([0,1])

  while g1.no_exit:
    if player == 0 and g1.no_exit:                             # The User
      print "Set position x,y axes",
      move = input()
      if 0 <= move[0] and move[1] < 3:
        if g1.setMove(move, player):
          g1.checkMatrix()
          sleep(1)
          player = 1
      else:
        print 'Movement out of board'
    if player == 1 and g1.no_exit:                              # The Computer
      move = g1.machineMove()
      if move != None:
        if g1.setMove(move, player):
          g1.checkMatrix()
          player = 0
  else:
    print "Play another game? (yes/no)",
    ans = raw_input()
    if ans == 'yes':
      main()
    else:
      quit()


if __name__ == "__main__":
    main()
