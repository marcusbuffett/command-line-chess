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

board = Board()
ai = AI()
side = WHITE
moves = 30
print(board)

for _ in range(moves) : 
    ai.makeRandomMove(side, board)
    print(board)
    side = not side

#for move in ai.getAllMovesUnfiltered(BLACK) :
    #print(move.piece)
    #print(move.newPos)
#print(board.makeStringRep())

#board = Board()
#ai = AI()

#print(board.makeStringRep())

#side = WHITE
#moves = 10

#timeBefore = time.time()
#for _ in range(moves) : 
    
    #move = ai.getRandomMove(side, board)
    #print(board.pieceAtPosition(move.oldPos))
    #print(move.oldPos)
    #print(move.newPos)
    #board.makeMove(move)
    #print(board.makeStringRep())
    #side = not side

#print('That took ' + str(time.time()-timeBefore))


#times = []
#for _ in range(10) :
    #board = Board()
    #ai = AI()

    #print(board.makeStringRep())

    #side = WHITE
    #moves = 10

    #timeBefore = time.time()

    #for _ in range(moves) : 
        
        #move = ai.getRandomMove(side, board)
        #print(board.pieceAtPosition(move.oldPos))
        #print(move.oldPos)
        #print(move.newPos)
        #board.makeMove(move)
        #print(board.makeStringRep())
        #side = not side
    #times.append(time.time()-timeBefore)

#print('Average time was : ' + str(sum(times)/len(times)))
#4.35

#board = Board()
#ai = AI()

#print(board.makeStringRep())

#side = WHITE
#moves = 1


#for _ in range(moves) : 
    
    #move = ai.getRandomMoveConcurrent(side, board)
    #print(board.pieceAtPosition(move.oldPos))
    #print(move.oldPos)
    #board.makeMove(move)



#100 moves : 54 seconds

#def getEmptyRow() :
    #return [None for _ in range(8)]

#board = Board()
#board.boardArray = []
#board.boardArray.append([Rook(board, BLACK), Knight(board, BLACK), Bishop(board, BLACK), King(board, BLACK), Queen(board, BLACK), Bishop(board, BLACK), Knight(board, BLACK), Rook(board, BLACK)])
##board.boardArray.append([King(board, BLACK), None, None, None, None, None, None, None])
#board.boardArray.append([Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK)])
#blackPawnRow = [Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK), Pawn(board, BLACK)] 
#fourthRow = [Pawn(board, WHITE), None, None, None, None, None, None, None]  

#whitePawnRow = [None, Pawn(board, WHITE), Pawn(board, WHITE), Pawn(board, WHITE), Pawn(board, WHITE), Pawn(board, WHITE), Pawn(board, WHITE), Pawn(board, WHITE)] 
#board.boardArray.append(getEmptyRow())
#board.boardArray.append(getEmptyRow())
#board.boardArray.append(fourthRow)
#board.boardArray.append(getEmptyRow())
#board.boardArray.append(whitePawnRow)
#board.boardArray.append([Rook(board, WHITE), Knight(board, BLACK), Bishop(board, WHITE), King(board, WHITE), Queen(board, WHITE), Bishop(board, WHITE), Knight(board, WHITE), Rook(board, WHITE)])
##board.boardArray.append([King(board, WHITE), None, None, None, None, None, None, None])
#boardFlat = [i for sublist in board.boardArray for i in sublist]


#ai = AI()

#def lenOfBoards() :
    #return len(set([piece.board for piece in [i for sublist in board.boardArray for i in sublist] if piece is not None]))

#side = BLACK
#print(board)
#for _ in range(1) :
    #print(ai.getFirstMove(side, board))
    #board.makeMove(ai.getFirstMove(side, board))
    #print(board)
    #side = not side


#print(board)
#move = ai.getFirstMove(True, board)
#for piece in board.getAllPieces() :
    #print(piece)
#print(board)
#print(move)
#print('hey')
#board.makeMove(move)

#ai = AI()
#board.makeMove(Move(C(1, 1), C(1, 2)))
#print(board)
#print(board.history)
#board.undoLastMove()
#print(board)
#print(board.history)

#times = []
#for _ in range(1) :
    #board = Board()
    #ai = AI()

    ##print(board)

    #side = WHITE
    #moves = 12

    #timeBefore = time.time()

    #for _ in range(moves) : 
        #move = ai.getFirstMove(side, board)
        ##print('Pieces remaining : ' + str(len(list(board.getAllPieces()))))
        ##print(move)
        ##print(board.pieceAtPosition(move.oldPos))
        #print("MOVE CHOSEN : \n" + str(move))
        #print("BOARD : \n" + str(board))
        #print("BOARD HISTORY : \n" + str(board.history))
        #print("\n"*3)

        #board.makeMove(move)
        ##print(board)
        #side = not side
    #times.append(time.time()-timeBefore)

#print('Average time was : ' + str(sum(times)/len(times)))

#playerSide = WHITE
#board = Board()
#ai = AI()
#currentSide = WHITE

#print("What side would you like to play as?")
#chosenSide = input()
#if 'w' in chosenSide.lower() :
    #side = WHITE
#else
    #side = BLACK

#print(board.makeStringRep())

#while True :
    #if currentSide = playerSide :
        #move = 


