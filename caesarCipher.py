# Caesar Cipher
#
# Based on chapter 5 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The message to be encrypted/decrypted:
message = "g0vyvtu7J2sJ7urJgu81qr5JT2qK"

# The encryption key:
key = 13

# Toggle encyrpt/decrypt mode:
mode = 'decrypt' # Set either 'encrypt' or 'decrypt'.

#List of supported symbols:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

output=''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            outputIndex = symbolIndex + key
        elif mode == 'decrypt':
            outputIndex = symbolIndex - key

        #Handles wraparoud if necessary:
        if outputIndex >= len(SYMBOLS):
            outputIndex -= len(SYMBOLS)
        elif outputIndex < 0:
            outputIndex += len(SYMBOLS)

        output += SYMBOLS[outputIndex]
    else:
        #If symbol is not supported, append it as is:
        output += symbol
    
print(output)
pyperclip.copy(output)
