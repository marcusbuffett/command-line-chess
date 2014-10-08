from Board import Board
from Pawn import Pawn
from Coordinate import Coordinate as C
from Move import Move
from Piece import Piece
from AI import AI
import time

WHITE = True
BLACK = False

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

times = []
for _ in range(1) :
    board = Board()
    ai = AI()

    print(board.makeStringRep())

    side = WHITE
    moves = 100

    timeBefore = time.time()



    for _ in range(moves) : 
        move = ai.getRandomMoveConcurrent(side, board)
        print('Pieces remaining : ' + str(len(list(board.getAllPieces()))))
        print(move)
        print(board.pieceAtPosition(move.oldPos))

        board.makeMove(move)
        print(board.makeStringRep())
        side = not side
    times.append(time.time()-timeBefore)

print('Average time was : ' + str(sum(times)/len(times)))

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


