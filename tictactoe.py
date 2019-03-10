# Tic-Tac-Toe

import random

def drawBoard(board):
    # 넘겨받은 보드를 그리는 함수
    # 보드는 10개의 문자열로 이루어진 리스트이며 편의상 0번째는 사용 안 함
    print(board[7]+ '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4]+ '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1]+ '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # 플레이어가 O,X 중 원하는 문자를 고르게 하고
    # 플레이어가 첫번째, 컴퓨터가 두번째인 플레이어ㅗ 문자 리스트를 반환
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # 리스트의 첫번째는 플레이어, 두 번째는 컴퓨터
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # 어느 플레이어가 먼저 할지 랜덤으로 정함
    if random.randint(0,1) == 0:
        return 'computer'
    else: 
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # board와 플레이어 문자가 주어지면 이겼는지 판정함
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or # 상단 가로방향
    (bo[4]==le and bo[5]==le and bo[6]==le) or # 중앙 가로방향
    (bo[1]==le and bo[2]==le and bo[3]==le) or # 하단 가로방향
    (bo[7]==le and bo[4]==le and bo[1]==le) or # 좌측 세로방향
    (bo[8]==le and bo[5]==le and bo[2]==le) or # 중앙 세로방향
    (bo[9]==le and bo[6]==le and bo[3]==le) or # 우측 세로방향
    (bo[7]==le and bo[5]==le and bo[3]==le) or # 대각선
    (bo[9]==le and bo[5]==le and bo[1]==le)) # 대각선

def getBoardCopy(board):
    # 보드의 카피본을 생성해 반환
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # 선택한 곳이 비어있으면 True 반환
    return board[move] == ' '

def getPlayerMove(board):
    # 플레이어가 움직일 곳을 선택하게 함
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move) 

def chooseRandomMoveFromList(board, movesList):
    # 주어진 보드의 리스트로부터 이동 가능한 곳을 하나 반환
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
     # 보드와 컴퓨터의 문자가 주어지면 이동할 곳을 골라 리턴함
    if computerLetter == 'X':
         playerLetter = 'O'
    else:
        playerLetter = 'X'

    # 이 게임의 인공지능 알고리듬 부분
    # 1.먼저 다음 턴에 이길 수 있는지를 판정
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # 2.만약 플레이어가 다음에 이길 수 있다면 그것을 저지
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # 3.코너 부분이 남아 있다면 그것부터 차지
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move

    # 4.센터가 비어 있다면 차지
    if isSpaceFree(board, 5):
        return 5

    # 5.옆선도 차지
    return chooseRandomMoveFromList(board, [2,4,6,8])


def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True


print('Welcome to Tic-Tac-Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.' )
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break