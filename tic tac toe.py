#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionaryin which keys will be the 
location(i.e : top-left,mid-right,etc.)and initialliy it's values will be
 empty space and then after every movewe will change the value 
 according to player's choice of move. '''

theboard ={'7': ' ' , '8': ' ' , '9': ' ',
           '4': ' ' , '5': ' ' , '6': ' ',
           '1': ' ' , '2': ' ' , '3': ' ',}

board_keys = []

for key in theboard:
    board_keys.append(key)

''' We will have to print the updated board after every
 move in the game and thus we will make a function in which we'll define
 the printBoard function so that we can easily print the board 
 everytime by calling this function. '''

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|'+ board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|'+ board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['3'] + '|'+ board['3'])

# Now we'll write the main function which has all the gameplay function.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printboard(theboard)
        print("It's youe turn," + turn + ".Move to which place?")

        move = input()
        if theboard[move] == ' ':
            theboard[move] == turn
            count += 1
        else:
            print("The place is already filled.\nmove to which place?")
            continue

        #now we will check if player X or O has won,for evry move after 5 moves.
        
          