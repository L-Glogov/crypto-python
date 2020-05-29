# Reverse Cipher
#
# Based on chapter 4 of Cracking Codes with Python by Al Sweigart
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)



message = input("Enter your message:")
secret = ''

i = len(message) - 1 
while i >= 0:
    secret += message[i]
    i -= 1

print(secret) 