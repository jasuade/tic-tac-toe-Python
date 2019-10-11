import random
from time import sleep

class game:
#Initialize the board and all variables
  def __init__(self):
    self.board = [[0,0,0],[0,0,0],[0,0,0]]
    self.exit = 1
    self.turn = 0
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
    else:
      self.board[x][y] = self.players[player]
    self.drawBoard()

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
      self.exit = 0
    elif line.count('O') == 3:
      print 'Player 2 wins the game'
      self.exit = 0
    return

  def sumLine(self, line):
    return line.count('O')


  '''
  Funtion for the computer to decide in wich position locate the symbol 'O'
  TODO: to be impoved
  def machineMove(self):
    # If there is nothing in the central position --> fill the center
    if self.board[1][1] == 0:
      move = [1,1]
      return move
    #If there is any row with two 'O' --> complete the line || If there is a row with two 'X' --> break the line
    for i in range(len(self.board)):
      if self.board[i].count('O') == 2:
        for j in range(len(self.board[i])):
          if self.board[i][j] == 0:
            move = [i,j]
            return move
      if self.board[i].count('X') == 2:
        for j in range(len(self.board[i])):
          if self.board[i][j] == 0:
            move = [i,j]
            return move
      #Otherwise could be a column or diagonal with two symbols 'X'
      #TODO check if there are already two symbols 'O' to complete the line
      #Check columns 
      if self.sumLine([self.board[0][i], self.board[1][i], self.board[2][i]]) == 2:
        print self.sumLine([self.board[i][0], self.board[i][0], self.board[i][0]])
        for j in range(len(self.board[i])):
          if self.board[j][i] == 0:
            move = [j,i]
            return move
      #Check diagonals
      if self.sumLine([self.board[0][0], self.board[1][1], self.board[2][2]]) == 2:
        for j in range(len(self.board[i])):
          if self.board[j][j] == 0:
            move = [j,j]
            return move
      elif self.sumLine([self.board[0][-1], self.board[1][-2], self.board[2][-3]]) == 2:
        for j in range(-1,-3):
          if self.board[i][j] == 0:
            move = [i,j]
            return move
    #Else put the X in somewhere else
    x = random.choice([0,1,2])
    y = random.choice([0,1,2])
    if self.board[x][y] == 0:
      move = [x,y]      
      return move
    # TODO: check if the random is already taken, chose another
    # TODO: If the board is completed --> stalemate/tie
    '''

  def machineMove(self):
    for i in range(len(self.board)):
        for j in range(len(self.board[i])):
          if self.board[i][j] == 'X':
            self.positionsX.append([i,j])
          elif self.board[i][j] == 'O':
            self.positionsO.append([i,j])
    if len(self.positionsO) == 0:
      x = random.choice([0,1,2])
      y = random.choice([0,1,2])
      move = [x,y]
      self.positionsX.append([x,y])
      return move
    elif (len(self.positionsO) == 1) and (len(self.positionsX) == 0):
      #'O' in center position
      if self.positionsO[1] == [1,1]:
        x = random.choice([0,2])
        y = random.choice([0,2])
        self.positionsX.append([x,y])
        return [x,y]
      else:
        self.positionsX.append([1,1])
        return [x,y]
    #elif (len(self.positionsO) == 1) and (len(self.positionsX) == 1):
    #elif (len(self.positionsO) == 2) and (len(self.positionsX) == 1):
    #If there is any row with two 'O' --> complete the line || If there is a row with two 'X' --> break the line
    else:
      for i in range(len(self.board)):
        if self.board[i].count('O') == 2:
          for j in range(len(self.board[i])):
            if self.board[i][j] == 0:
              move = [i,j]
              return move
        if self.board[i].count('X') == 2:
          for j in range(len(self.board[i])):
            if self.board[i][j] == 0:
              move = [i,j]
              return move
        #Check columns 
        if self.sumLine([self.board[0][i], self.board[1][i], self.board[2][i]]) == 2:
          print self.sumLine([self.board[i][0], self.board[i][0], self.board[i][0]])
          for j in range(len(self.board[i])):
            if self.board[j][i] == 0:
              move = [j,i]
              return move
        #Check diagonals
        if self.sumLine([self.board[0][0], self.board[1][1], self.board[2][2]]) == 2:
          for j in range(len(self.board[i])):
            if self.board[j][j] == 0:
              move = [j,j]
              return move
        elif self.sumLine([self.board[0][-1], self.board[1][-2], self.board[2][-3]]) == 2:
          for j in range(-1,-3):
            if self.board[i][j] == 0:
              move = [i,j]
              return move
    return [1,2]

    






#----------------TEST--------------------------
g1 = game()
g1.drawBoard()
#player = random.choice ([0,1])
player = 0


while (g1.exit):
  if player == 0:                             # The User
    print "Set position x,y axes",
    move = input()
    if 0 <= move[0] and move[1] < 3:
      g1.setMove(move, player)
      g1.checkMatrix()
      sleep(2)
      g1.turn += 1
      player = 1
    else:
      print 'Movement out of board'
  if player == 1:                              # The Computer
    move = g1.machineMove()
    print move
    g1.setMove(move, player)
    g1.checkMatrix()
    g1.turn += 1
    player = 0
