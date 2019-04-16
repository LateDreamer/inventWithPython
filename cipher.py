# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: # Symbol not found in SYMBOLS
            # Just add this symbol without any change
            translated += symbol
        else:
            # Encrypt or decrypt.
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex +=len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))


''' my code

FULL_CIPHER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
CIPHER_LENGTH = len(FULL_CIPHER)

def changedCipherWithKey(key):
    changedCipher = ''
    for i in range(key,CIPHER_LENGTH -1):
        changedCipher += FULL_CIPHER[i]

    for i in range(key):
        changedCipher += FULL_CIPHER[i]

    return changedCipher

def decryptingText(text, changedCipher):
    changedKeyandValue = dict(zip(FULL_CIPHER,changedCipher))
    cipheredText = ''
    for c in text:
        if c in FULL_CIPHER:
            cipheredText += changedKeyandValue[c] 
        else:
            cipheredText += c
    return cipheredText

def encryptingText(text, changedCipher):
    changedKeyandValue = dict(zip(changedCipher,FULL_CIPHER))
    cipheredText = ''
    for c in text:
        if c in FULL_CIPHER:
            cipheredText += changedKeyandValue[c] 
        else:
            cipheredText += c
    return cipheredText





a = changedCipherWithKey(13)
print(a)
text='The sky above the port was the color of television, tuned to a dead channel.'
dec = decryptingText(text,a)
print(dec)
enc = encryptingText(dec,a)
print(enc)
'''