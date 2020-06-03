# Transposition Cipher
#
# Based on chapter 7 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    myMessage = '''Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November 1852) was an English mathematician and writer, chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the Analytical Engine. Her notes on the engine include what is recognised as the first algorithm intended to be carried out by a machine. As a result, she is often regarded as the first computer programmer.'''
    myKey = 6

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with a "|" after it in case there are spaces at the end.
    print(ciphertext + '|')

    #Copy the encrypted string to the clipboard
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    
    return ''.join(ciphertext)

#If transpositonEncrypt.py is run call the main() function:
if __name__ == "__main__":
    main()
