from Board import Board
from Pawn import Pawn
from Rook import Rook
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from AI import AI
import time
import sys

WHITE = True
BLACK = False

playerSide = WHITE
board = Board()
ai = AI(board, WHITE, 2)
currentSide = WHITE

#print("What side would you like to play as?")
#chosenSide = input()
#if 'w' in chosenSide.lower() :
    #side = WHITE
#else :
    #side = BLACK

chosenSide = WHITE

print(board)

#while True :
    #move = None
    #if currentSide == playerSide :
        #hasChosenValidMove = False

        #while (not hasChosenValidMove) :
            #moveInput = input("Please input your move : ")
            #if moveInput == 'r' :
                #move = ai.getRandomMove(currentSide, board)
                #hasChosenValidMove = True
                #continue
            #try :
                #move = Move.moveFromHumanCoords(moveInput)
            #except :
                #print("Invalid input, please enter a valid move in long form notation (ex. d1e2)")
                #continue
            #if ai.isValidMove(move, currentSide, board) :
                #hasChosenValidMove = True
    ##if currentSide == playerSide :
       ##move = ai.getRandomMove(currentSide, board) 
        
    #else :
       #move = ai.getBestMove(currentSide, board) 

    #board.makeMove(move)
    #currentSide = not currentSide
    #print(board)
    ##print(board.getPointAdvantageOfSide(currentSide))
    ##print(sys.getsizeof(ai))
    ##print(sys.getsizeof(board))


#side = WHITE
#for _ in range(2000) :
    #board.makeMove(ai.getRandomMove(side))
    ##print(board)
    #side = not side

#print(board)
#print(ai.movesAnalyzed)

