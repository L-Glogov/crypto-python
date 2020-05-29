# Caesar Cipher Hacker
#
# Based on chapter 6 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Loop through all possible keys:
for key in range(len(SYMBOLS)):
    output = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            outputIndex = symbolIndex - key

            #Handles the wraparound:
            if outputIndex < 0:
                outputIndex += len(SYMBOLS)

            #Append the decrypted symbol
            output += SYMBOLS[outputIndex]

        else:
            #Append unsupported symbols
            output += symbol

    #Display all possible decryptions
    print('Key #%s:  %s' % (key, output))
