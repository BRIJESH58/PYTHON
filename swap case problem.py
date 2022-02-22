'''YOU ARE GIVEN A STRING AND YOUR TASJK IS TO SWAP CASES. IN OTHER WORDS, CONVERT ALL LOWERCASE LETTERS TO UPPERCASE LETTERS AND VICE VERSA.
SAMPLE INPUT: HackerRank.com presents "Pythonist 2".
SAMPLE OUTPUT: hACKERrANK.COM PRESENTS "pYTHONIST 2".'''
def SWAP (B):
    OUTPUT = '';
    for PARAGRAPH in B:
        if PARAGRAPH.isupper()==True:
            OUTPUT += (PARAGRAPH.lower())
        else:
            OUTPUT += (PARAGRAPH.upper())
    return OUTPUT

if __name__ == '__main__':
    B = input()
    RESULT = SWAP(B)
    print(RESULT)


