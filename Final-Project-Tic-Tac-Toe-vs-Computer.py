EMPTY_SLOT = "-"
X_PLAYER = "X"
O_PLAYER = "0"
TIE = "tie"

#Wining combinations
WIN_COMBINATION_INDICES = [
  # Complete row
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  # Complete column
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  # Complete diagonal
  [0, 4, 8],
  [2, 4, 6]
]

#Initializing the board
def initialize_board():
  board = [EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT,
            EMPTY_SLOT, EMPTY_SLOT, EMPTY_SLOT]
  return board


#Displaying the board
def display_board(board):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


#Valid position as an input
position_list=['1','2','3','4','5','6','7','8','9']



#Check if the input is Valid
def valid_position(position, board):
  valid = False
  if position in position_list and board[int(position)-1]==EMPTY_SLOT:
    position = int(position)
    
    valid = True

  return valid


#Receive input and apply on board
def handle_human_turn(player, board):

  print(f"{player}, it's your turn.")
  position=input('Please pick a position:')

  while not valid_position(position, board):
    position = input('Wrong input, Please try again:')

  board[int(position)-1] = player

  return board
  

#Switch players in each round
def switch_player(current_player):
  
  if current_player == X_PLAYER:
    player = O_PLAYER

  if current_player == O_PLAYER:
    player = X_PLAYER

  return player


#Check winners
def check_for_winner(player,board):
  winner = None
  
  for comb in WIN_COMBINATION_INDICES:

    if board[comb[0]] == board[comb[1]] == board[comb[2]] != EMPTY_SLOT :
      winner = player
    
  if winner == None:

    if '-' not in board:
      winner = TIE
          
  return winner



#Here we make the computer intelligent by implementing three functions 

def handle_ai_turn(player, board):
  
  board , position_taken = next_wining_position(player, board)

  if position_taken == False : 
    board , position_taken = blocking_position(player, board)

    if position_taken == False:
      board = next_other_moves(player, board)

  return board


#With this function the computer will discover the next wining position to make its move

def next_wining_position(player, board):

  position_taken = False

  for i in WIN_COMBINATION_INDICES:

    if board[i[0]] == board[i[1]] == O_PLAYER and board[i[2]] == EMPTY_SLOT:
      board[i[2]] = O_PLAYER
      position_taken = True
      break
      
    elif board[i[0]] == board[i[2]] == O_PLAYER and board[i[1]] == EMPTY_SLOT:
      board[i[1]] = O_PLAYER
      position_taken = True
      break

    elif board[i[1]] == board[i[2]] == O_PLAYER and board[i[0]] == EMPTY_SLOT:
      board[i[0]] = O_PLAYER
      position_taken = True
      break

  return board , position_taken


#With this function the computer will block the next wining move for human

def blocking_position(player, board):

  position_taken = False

  for i in WIN_COMBINATION_INDICES:
    if board[i[0]] == board[i[1]] == X_PLAYER and board[i[2]] == EMPTY_SLOT:
      board[i[2]] = O_PLAYER
      position_taken = True
      break

    elif board[i[0]] == board[i[2]] == X_PLAYER and board[i[1]] == EMPTY_SLOT:
      board[i[1]] = O_PLAYER
      position_taken = True
      break

    elif board[i[1]] == board[i[2]] == X_PLAYER and board[i[0]] == EMPTY_SLOT:
      board[i[0]] = O_PLAYER
      position_taken = True
      break

  return board, position_taken 

#We pre-define the positions for the edges and sides

edge_centre_positions = [0, 2 ,6 ,8,4]
side_positions = [1,3,7,5]

#In case there is no winning or blocking position the computer will choose the edges or the center, if these position are also not available it will choose the sides

def next_other_moves(player, board):

  for i in edge_centre_positions:
    if board[i] == EMPTY_SLOT:
      board[i] = O_PLAYER
      break

  else:
    for i in side_positions:
      if board[i] == EMPTY_SLOT:
        board[i] = O_PLAYER
        break

  return board

#In order to function as human or computer dependent on player's turn

def handle_turn(player, board):

  if player == X_PLAYER:
    board = handle_human_turn(player, board)

  if player == O_PLAYER:
    board = handle_ai_turn(player, board)

  return board


#Define the Game Tic Tac Toe
def tic_tac_toe():
  winner = None
  game_still_going = True
  player = X_PLAYER
    
  board = initialize_board()

  while game_still_going:
   
      # Display board
      display_board(board)

      # Ask the player for a valid position and write it on the board
      
      board = handle_turn(player, board)
      
      # Check if there is a winner already
      winner = check_for_winner(player,board)

      if winner != None:
        game_still_going = False
     
      player = switch_player(player)

     
  print("THE END")
  if winner == TIE:
      print("Tie")
  else:
      print(f"Congratulations {winner}!!")
  display_board(board)


# Start game
tic_tac_toe()


