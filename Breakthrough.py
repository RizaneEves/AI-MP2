import numpy as np

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

def off_heur(player,board):
    if player == 'W':
        return 2.0*(30-len(getPositions(board)[1])) + random()
    if player == 'B':
        return 2.0*(30-len(getPositions(board)[0])) + random()
    
def def_heur(player,board):
    if player == 'W':
        return 2.0*len(getPositions(board)[0]) + random()
    if player == 'B':
        return 2.0*len(getPositions(board)[1]) + random()

board = createInitialBoard()
b2 = makeMove((0,0), (4, 4), board)

print(np.array(b2))
