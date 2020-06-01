# Transposition Cipher
#
# Based on chapter 7 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    myMessage = 'This is the message that I will encrypt: Cats are awesome!'
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
