from Board import Board
from Pawn import Pawn
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from AI import AI
import time

WHITE = True
BLACK = False

board = Board()
ai = AI()

print(board.makeStringRep())
print(board.checkForKings())
#for move in ai.getAllMovesUnfiltered(BLACK) :
    #print(move.piece)
    #print(move.newPos)
#print(board.makeStringRep())

side = WHITE
moves = 10

timeBefore = time.time()
for _ in range(moves) : 
    
    move = ai.getRandomMove(side, board)
    print(board.pieceAtPosition(move.oldPos))
    print(move.oldPos)
    print(move.newPos)
    board.makeMove(move)
    print(board.makeStringRep())
    side = not side

print('That took ' + str(time.time()-timeBefore))
