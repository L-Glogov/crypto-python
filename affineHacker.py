# The Affine Cipher Hacker
#
# Based on chapter 15 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
       print('Copying hacked message to clipboard:')
       print(hackedMessage)
       pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on macOS and Linux):
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

        if detectEnglish.isEnglish(decryptedText):
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200]) 
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None


if __name__ == "__main__":
    main()