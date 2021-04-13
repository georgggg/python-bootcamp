#Print the number of characters in your name

print(len(input("What is your name? ")) )


#Notes:
#len function returns the number of characters in the string in either Python 2 and Python 3
#but be very careful that for non-ascii characters/extended unicode chars in Python 2
#it will return the number of bytes used to represent that string. That is
#it may be that some foreign characters use 2 bytes per character compared 
#to 1 byte for ASCII. Then you can end up with a higher count.
