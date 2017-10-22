import numpy as np



class Node:
    def __init__(self, minOrMax, board,  utlity, parent):
        self.minOrMax = minOrMax
        self.board = board
        self.utility = utlity
        self.parent = parent



def miniMax(board, minOrMax, depth):
    if(depth == 0):
        boardStates = getAllPossibleMoves(minOrMax, board[:])
        


    if(minOrMax == "W"):
        max(miniMax(board, 0, depth - 1))
    else:
        min(miniMax(board, 1, depth - 1))




def getAllPossibleMoves(player , board):

    allPossibleMoves = []
    positions = getPositions(board)
    playerPositions = []
    if player == "W":
        playerPositions = positions[0]
    else:
        playerPositions = positions[1]

    for position in playerPositions:
        moves = getValidMoves(position, board)
        for move in moves:
            b = makeMove(position, move, board[:])
            allPossibleMoves.append(b)

    return allPossibleMoves


def createInitialBoard():
    board = [['B'] * 8]
    board.append(['B']*8)
    board.append([''] * 8)
    board.append([''] * 8)
    board.append([''] * 8)
    board.append([''] * 8)
    board.append(['W'] * 8)
    board.append(['W'] * 8)
    return board


def getPositions(board):

    blackPositions = []
    whitePositions = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'W':
                whitePositions.append((i,j))
            elif board[i][j] == 'B':
                blackPositions.append((i, j))

    return whitePositions, blackPositions


def getValidMoves(index, board):
    x = index[0]
    y = index[1]

    moves = []

    if(board[x][y] == ""):
        return None
    elif(board[x][y] == "B"):
        moves.append((x - 1, y + 1))
        moves.append((x + 1, y + 1))
        if board[x][y+1] == "":
            moves.append((x, y + 1))
    elif(board[x][y] == "W"):
        moves.append((x - 1, y - 1))
        moves.append((x + 1, y - 1))
        if board[x][y+1] == "":
            moves.append((x, y - 1))

    for move in moves:
        if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
            moves.remove(move)

    return moves

def makeMove(idx,finidx,board):
    curr = board[idx[0]][idx[1]]
    board[idx[0]][idx[1]] = ""
    board[finidx[0]][finidx[1]] = curr
    return board



def isGameOver(board):
    for x  in board[0]:
        if x == "W":
            return True
    for x in board[7]:
        if x == "B":
            return True
    positions = getPositions(board)
    if len(positions[0]) == 0 or len(positions[1]) == 0:
        return True

    return False



