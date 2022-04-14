"""
YOU ARE GIVEN A STRING. YOUR TASK IS TO COUNT THE FREQUENCY OF THE STRING AND PRINT THELETTERS IN DESCENDING ORDER PF FREQUENCY.
IF THE FOLLOWING STRING IS GIVEN AS INPUT TO THE PROGRAM: AABBBCCDE
THEN, THE OUTPUT OF THE PROGRAM SHOULD BE:
B 3
A 2
C 2
D 1
E 1
"""
import numpy as np
 
def prCharWithFreq(str) :
     
    n = len(str)
     
    freq = np.zeros(26, dtype = int)

    for i in range(0, n) :
        freq[ord(str[i]) - ord('A')] += 1
                 
    for i in range(0, n) :
         
        if (freq[ord(str[i])- ord('A')] != 0) :
             
            print (str[i], freq[ord(str[i]) - ord('A')],
                                                end = "\n")

            freq[ord(str[i]) - ord('A')] = 0
         
     
if __name__ == "__main__" :
     
    str = "AABBBCCDE";
    prCharWithFreq(str);