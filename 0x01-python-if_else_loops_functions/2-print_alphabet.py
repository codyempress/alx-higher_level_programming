#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end="")

# The ord('a') function returns the
#ASCII value of the lowercase letter 'a', which is 97.

#The ord('z') function returns the ASCII 
#value of the lowercase letter 'z', which is 122.

#The range() function generates a sequence 
#of numbers from 97 to 122 (inclusive), representing 
#the ASCII values of the lowercase alphabet.

#The for loop iterates over each 
#ASCII value in the generated sequence.

#The chr(i) function converts each ASCII 
#value back into its corresponding character.

#The print(chr(i), end="") statement prints 
#each character without a newline, due to the end="" argument.

#Since the program only uses one print() statement
#within the loop, it satisfies the requirement 
#of using only one print function with string format.

#Similarly, the program uses only one loop as per the given requirement.
