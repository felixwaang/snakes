#Making a simple encoder to increase or decrease characters by 13 (rot 13 code).

#After reading all modules from Python you can make it very simply.

import codecs
codecs.encode('this is a test', 'rot_13')

#That works because codecs contains rot_13 code, but I feel this is cheating
#So lets do it via a string

import string
rot_13 = string.maketrans( 
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        
string.translate("Hello reader! Nice decrypting", rot_13)

#I looked back at my rot13 code from C and I was wondering if there was 
#a simpler way to do this, so after reading the python document
#these ways seems to be the best
