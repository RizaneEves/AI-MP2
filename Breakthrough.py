import numpy as np

def createInitialBoard():
    board = [[''] * 8] * 8
    board[0:2] = [['B'] * 8] * 2
    board[6:8] = [['W'] * 8] * 2
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





board = createInitialBoard()
makeMove((0,0), (4, 4), board)

print(np.array(board))

