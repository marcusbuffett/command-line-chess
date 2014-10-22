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
from InputParser import InputParser
import time
import sys

WHITE = True
BLACK = False

playerSide = WHITE
board = Board()
ai = AI(board, BLACK, 2)
board.currentSide = WHITE

#print("What side would you like to play as?")
#chosenSide = input()
#if 'w' in chosenSide.lower() :
    #side = WHITE
#else :
    #side = BLACK

#chosenSide = WHITE

parser = InputParser(board, WHITE)

#while True :
    #move = None
    #playerAI = AI(board, WHITE, 1)
    #if currentSide == playerSide :
        #hasChosenValidMove = False

        #while (not hasChosenValidMove) :
            #moveInput = input("Please input your move : ")
            #if moveInput == 'r' :
                #move = playerAI.getRandomMove()
                #hasChosenValidMove = True
                #continue
            #try :
                #move = parser.moveForShortNotation(moveInput)
                #hasChosenValidMove = True
            #except :
                #print("Invalid input, please enter a valid move in long form notation (ex. d1e2)")
                #continue
    #else :
        #move = ai.getBestMove() 

    #move.notation = parser.notationForMove(move)

    #print("MOVE: " + str(move.notation))
    #board.makeMove(move)
    #currentSide = not currentSide
    #print(board)
    #print(board.getPointAdvantageOfSide(currentSide))
    #print()

moves = 0
while True :
    move = None
    playerAI = AI(board, WHITE, 2)
    if board.currentSide == playerSide :
        move = playerAI.getRandomMove()
    else :
        move = ai.getBestMove() 

    move.notation = parser.notationForMove(move)

    print("MOVE: " + str(move.notation))
    board.makeMove(move)
    moves += 1
    print(board)
    print(board.getPointAdvantageOfSide(board.currentSide))
    if board.isCheckmate() :
        print("MOVES : " + str(moves))
        print("CHECKMATE!")
        break
