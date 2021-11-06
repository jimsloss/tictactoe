import os

def displayGrid(squares):

    #system('cls')
     
    print("\n\n         " + squares[1] + " | " + squares[2] + " | " + squares[3])
    print("        ---|---|---")
    print("         " + squares[4] + " | " + squares[5] + " | " + squares[6])
    print("        ---|---|---")
    print("         " + squares[7] + " | " + squares[8] + " | " + squares[9]+"\n")

    
def makeMove(squares):

    message = "\n      Choose a box number between 1 and 9, \n" \
                 "       (top-left to bottom-right):   "
    
    move = input(message)

    while not squares[int(move)] == " ":
            print("\n       Thats not free, try another")
            move = input(message)

    return int(move)

def getPlayer(x):
    player = input(f"\n     Player {x} name: ")
    while not player.isalpha():
        print("\n       incorrect input \n")
        player = input("\n      Player {x} name: ")
    return player

def checkWin(squares):

    t1, t2, t3 = squares[1], squares[2], squares[3]
    m1, m2, m3 = squares[4], squares[5], squares[6]
    b1, b2, b3 = squares[7], squares[8], squares[9]

    win = False

    if ((not t1 == " ") and (t1 == t2) and (t2 == t3)) \
       or ((not m1 == " ") and (m1 == m2) and (m2 == m3)) \
       or ((not b1 == " ") and (b1 == b2) and (b2 == b3)) \
       or ((not t1 == " ") and (t1 == m1) and (m1 == b1)) \
       or ((not t2 == " ") and (t2 == m2) and (m2 == b2)) \
       or ((not t3 == " ") and (t3 == m3) and (m3 == b3)) \
       or ((not t1 == " ") and (t1 == m2) and (m2 == b3)) \
       or ((not t3 == " ") and (t3 == m2) and (m2 == b1)):

        win = True

    return win

class tictactoe():


    print("\n          JIM'S TIC TAC TOE          \n")
    
    #get the players
    player1 = getPlayer("X")
    player2 = getPlayer("Y")
       
    players= {"X": player1, "O": player2}
    score = {player1:0, player2:0}

    player = player1

    finished = False
    
    while not finished:

        #set up the grid content
        squares = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ",7:" ", 8:" ", 9:" "}

        print("\n\t Player \t Name \t\t Score")
        print(f"\t    X \t\t {player1} \t\t   {score[player1]}  ")
        print(f"\t    Y \t\t {player2}  \t\t   {score[player2]}  \n")
        
        print(f"\n\n       {player}'s turn")
        displayGrid(squares)

        for go in range(1,10):
            move = makeMove(squares)
            win = False

            if go % 2 == 0:
                squares[move] = "O" # every even go    
            else:
                squares[move] = "X" # every odd go, 1st, 3rd etc

            win = checkWin(squares)

            if win:
                score[player]+=1 
                player = player.upper()
                displayGrid(squares)
                print(f"\n       !!! {player} WINS !!!")
                break
            
           
            
            if player == player1:
                player = player2
            else:
                player = player1

            print(f"\n\n       {player}'s turn")
            displayGrid(squares)
           
            
        again = input("\n          PLAY AGAIN? (Y/N) :  ")

        again = again.upper()

        while ((again != "Y") and (again != "N")):

            again = input("\n         INVALID INPUT \n PLAY AGAIN? (Y/N) :  ")

        if again == "N":
            print("\n           THANK YOU FOR PLAYING JIM'S TICTACTOE   \n\n")
            finished = True
            

    

   
        
    #    if move in range(1,10):
     #       squares[move] = next(iter(players))
      #  else:
       #     print("\nincorrect entry, game ended\n")
        #    finished = True

    




tictactoe()
