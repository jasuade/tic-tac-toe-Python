import random

class game:
#Initialize the board and all variables
  def __init__(self):
    self.board = [[0,0,0],[0,0,0],[0,0,0]]
    self.turn = 0
    self.players = [-1, 1]

#Very ugly way to draw a board in the cmd
  def drawBoard(self):
    print '-------------\n'
    for i in self.board[0]:
      print '|',i,
    print '| \n'
    for i in self.board[1]:
      print '|',i,
    print '| \n'
    for i in self.board[2]:
      print '|',i,
    print '|\n------------- \n'

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
    for idx, elem in enumerate(self.board):
      self.checkLine(elem)
    #Definitely this needs yo be improved
    self.checkLine([self.board[0][0], self.board[1][0], self.board[2][0]])
    self.checkLine([self.board[0][1], self.board[1][1], self.board[2][1]])
    self.checkLine([self.board[0][2], self.board[1][2], self.board[2][2]])
    self.checkLine([self.board[0][0], self.board[1][1], self.board[2][2]])
    self.checkLine([self.board[0][2], self.board[1][1], self.board[2][0]])

  def checkLine(self, line):
    if line.count(1) == 3:
      print 'Player 1 wins the game'
    elif line.count(-1) == 3:
      print 'Player 2 wins the game'



#----------------TEST--------------------------
g1 = game()
#player = random.choice ([0,1])
player = 1
#exit = 0

while (1):
  #if player == 1:
  print "Set position x,y axes",
  move = input()
  if 0 <= move[0] and move[1] < 3:
    g1.drawBoard()
    g1.setMove(move, player)
    g1.checkMatrix()
  else:
    print 'Movement out of board'
  #if playyer == -1 # the machine
      #checkMatrix():
      #move = decideMove():
      #setMove(move, player)
      #player = 1
