# Transposition Cipher Decryption
#
# Based on chapter 8 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)


import math, pyperclip

def main():
    myMessage = '''AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr.'''
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
