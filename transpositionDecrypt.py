# Transposition Cipher Decryption
#
# Based on chapter 8 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)


import math, pyperclip

def main():
    myMessage = 'Tsme lyaeoh e I pt mitst etsaeshshwn: w! eaaic aei gtlrCrs'
    myKey = 6

    originalMessage = decryptMessage(myKey, myMessage)
    #Print with a "|" after in case there are spaces at the end of the decrypted message
    print(originalMessage + '|')

    pyperclip.copy(originalMessage)


def decryptMessage(key, message):    
    #The number of "columns" in our transposition grid:
    numColumns = int(math.ceil(len(message) / key))
    #The number of "rows" in our transpositon grid:
    numRows = key
    #The number of "shaded boxes" in the last "column" of the grid:
    numShaded = numColumns * numRows - len(message)

    originalMessage = [''] * numColumns

    column = 0
    row = 0

    for symbol in message:
        originalMessage[column] += symbol
        column += 1

        if (column == numColumns) or (column == numColumns - 1 and row >= numRows - numShaded):
            column = 0
            row += 1
    
    return ''.join(originalMessage)

if __name__ == "__main__":
    main()
