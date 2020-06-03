# Transposition Encrypt/Decrypt .txt Files
#
# Based on chapter 10 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'test.txt'
    #Warning: If a file with the outputFilename name already exists, it will be overwritten with this program
    outputFilename = 'test.encrypted.txt'
    myKey = 9638
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'

    #Check if input file exists:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Terminating program... ' % (inputFilename))
        sys.exit()

    #If output file exists, give user a chance to terminate program without overwritting said file:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    #Measure the running time of the encryption/decryption:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % ( myMode.title(), outputFilename))


if __name__ == "__main__":
    main()