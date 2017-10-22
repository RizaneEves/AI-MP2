import numpy as np
import random
import copy

class Node:
    def __init__(self, minOrMax, board,  utlity, children):
        self.minOrMax = minOrMax
        self.board = board
        self.utility = utlity
        self.children = children



def miniMax(board, minOrMax, depth, heuristic):
    if(depth == 0):
        nodes = []
        boardStates = getAllPossibleMoves(minOrMax, copy.deepcopy(board))
        for b in boardStates:
            u = heuristic(minOrMax, b)
            n = Node(minOrMax, b, u, [])
            nodes.append(n)

        return nodes

    if(minOrMax == "W"):
        n = getMaxNode(miniMax(board[:], "B", depth - 1, heuristic))
        nodes = []
        boardStates = getAllPossibleMoves(minOrMax, copy.deepcopy(n.board))
        for b in boardStates:
            u = heuristic(minOrMax, b)
            n = Node(minOrMax, b, u, [])
            nodes.append(n)

        return nodes

    else:
        n = getMinNode(miniMax(board[:], "W", depth - 1, heuristic))
        nodes = []
        boardStates = getAllPossibleMoves(minOrMax, n.board[:])
        for b in boardStates:
            u = heuristic(minOrMax, b)
            n = Node(minOrMax, b, u, [])
            nodes.append(n)

        return nodes




def getMaxNode(nodes):
    maxVal = nodes[0].utility
    maxNode = nodes[0]
    for node in nodes:
        if node.utility > maxVal:
            maxVal = node.utility
            maxNode = node
    return maxNode

def getMinNode(nodes):
    minVal = nodes[0].utility
    minNode = nodes[0]
    for node in nodes:
        if node.utility < minVal:
            minVal = node.utility
            minNode = node
    return minNode

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
        print(moves)
        for move in moves:
            b = makeMove(position, move, copy.deepcopy(board))
            allPossibleMoves.append(b)

    for p in allPossibleMoves:
        print(np.array(p))
    return allPossibleMoves


def createInitialBoard():
    board = [['B'] * 8]
    board.append(['B']*8)
    board.append([' '] * 8)
    board.append([' '] * 8)
    board.append([' '] * 8)
    board.append([' '] * 8)
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

    if(board[x][y] ==  " "):
        return None
    elif(board[x][y] == "B"):
        if((y + 1) < 8):
            if((x - 1) >= 0):
                if(board[x-1][y+1] != "B"):
                    moves.append((x - 1, y + 1))
            if((x + 1) < 8):
                if (board[x + 1][y + 1] != "B"):
                    moves.append((x + 1, y + 1))
            if board[x][y + 1] == " ":
                moves.append((x, y + 1))

    elif(board[x][y] == "W"):
        if((y - 1) >= 0):
            if((x - 1) >= 0):
                if (board[x - 1][y - 1] != "W"):
                    moves.append((x - 1, y - 1))
            if((x + 1) < 8):
                if (board[x + 1][y - 1] != "W"):
                    moves.append((x + 1, y - 1))
            if board[x][y - 1] == " ":
                moves.append((x, y - 1))

    return moves

def makeMove(idx,finidx,board):
    curr = board[idx[0]][idx[1]]
    board[idx[0]][idx[1]] = " "
    board[finidx[0]][finidx[1]] = curr
    return board


def off_heur(player,board):
    if player == 'W':
        return 2.0*(30-len(getPositions(board)[1])) + random.random()
    if player == 'B':
        return 2.0*(30-len(getPositions(board)[0])) + random.random()


def def_heur(player,board):
    if player == 'W':
        return 2.0*len(getPositions(board)[0]) + random.random()
    if player == 'B':
        return 2.0*len(getPositions(board)[1]) + random.random()

board = createInitialBoard()
b2 = makeMove((0,0), (4, 4), board)

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



def playGame():
    board = createInitialBoard()
    nodes = miniMax(board, "W", 2, off_heur)



print(playGame())