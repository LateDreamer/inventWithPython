import random
HANGMAN_PICS=['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''','''
  +---+
  O   |
 /|   |
      |
     ===''','''
  +---+
  O   |
 /|\  |
      |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

words = words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    # 넘겨받은 문자열 딕셔너리로부터 임의의 단어 선택
    # 먼저 딕셔너리로부터 임의의 키를 선택
    wordKey = random.choice(list(wordDict.keys()))

    # 다음으로 해당 키의 리스트로부터 임의의 단어 선택
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letter
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        # show the secret word with spaces in between each letter.
        print(letter, end= ' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter player entered. This function makes sure the
    # player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again;
    # otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = 'X'
while difficulty not in ['E', 'M', 'H']:
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord., secretSet  = getRandomWord(words)
gameIsDone = False

while True:
    print("The secret word is in the set: " + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters+correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times ans lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + 
                str(len(missedLetters)) + ' missed guesses and ' + 
                str(len(correctLetters)) + ' correct guesses, the word was "' +
                 secretWord + '"')
            gameIsDone = True

        # Ask the player if they want to play again
        # (but only if the game is done).

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break