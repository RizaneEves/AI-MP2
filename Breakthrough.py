import numpy as np
import random
import copy
import time


def getOpponent(player):
    if player == "W":
        return "B"
    else: return "W"


def miniMax(node, depth, heuristic, isMax, player):
    if depth == 0:
        return node, heuristic(getOpponent(player), node)

    if isMax:
        bestVal = -np.inf
        bestChild = []
        for child in getAllPossibleMoves(player, node):
            n, u = miniMax(child, depth - 1, heuristic, False, getOpponent(player))
            if u > bestVal:
                bestVal = u
                bestChild = child

        return bestChild, bestVal

    else:
        bestVal = np.inf
        bestChild = []
        for child in getAllPossibleMoves(player, node):
            n, u = miniMax(child, depth - 1, heuristic, False, getOpponent(player))
            if u < bestVal:
                bestVal = u
                bestChild = child

        return bestChild, bestVal

def alphaBeta(node, depth, heuristic, alpha, beta, isMax, player):
    if depth == 0:
        return node, heuristic(getOpponent(player), node)
    if isMax:
        u = -np.inf
        children = {}
        for child in getAllPossibleMoves(player, node):
            u = max(u, alphaBeta(node, depth - 1, heuristic, alpha, beta, False, getOpponent(player))[1])
            children[u] = child
            alpha = max (alpha, u)
            if beta <= alpha:
                break
        return children[u], u

    else:
        u = np.inf
        children = {}
        for child in getAllPossibleMoves(player, node):
            u = min(u, alphaBeta(node, depth - 1, heuristic, alpha, beta, True, getOpponent(player))[1])
            children[u] = child
            beta = min (beta, u)
            if beta <= alpha:
                break
        return children[u], u

def miniMax3(node, heuristic, player):
    return miniMax(node, 3, heuristic, True, player)[0]

def alphaBeta3(node, heuristic, player):
    return alphaBeta(node, 3, heuristic, -np.inf, np.inf, True, player)[0]

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
        for move in moves:
            b = makeMove(position, move, copy.deepcopy(board))
            allPossibleMoves.append(b)


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
        if((x + 1) < 8):
            if((y - 1) >= 0):
                if(board[x + 1][y - 1] != "B"):
                    moves.append((x + 1, y - 1))
            if((y + 1) < 8):
                if (board[x + 1][y + 1] != "B"):
                    moves.append((x + 1, y + 1))
            if board[x + 1][y] == " ":
                moves.append((x + 1, y))

    elif(board[x][y] == "W"):
        if((x - 1) >= 0):
            if((y - 1) >= 0):
                if (board[x - 1][y - 1] != "W"):
                    moves.append((x - 1, y - 1))
            if((y + 1) < 8):
                if (board[x - 1][y + 1] != "W"):
                    moves.append((x - 1, y + 1))
            if board[x - 1][y] == " ":
                moves.append((x - 1, y))

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



def playGame(searches, heuristics):
    board = createInitialBoard()


    turn = 0
    player = ["W", "B"]
    while(not isGameOver(board)):
        print(turn % 2)
        board = searches[turn % 2](board, heuristics[turn % 2], player[turn % 2])
        print(np.array(board))
        #time.sleep(1)
        turn+=1




print(playGame([miniMax3, alphaBeta3], [off_heur, def_heur]))