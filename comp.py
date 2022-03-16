def SUM():
    NUM = 2
    NUM1 = 3
    TOTAL = NUM + NUM1
    print(TOTAL)


SUM: lambda x=5, y=3: print(x + y)
SUM()
SUM(2, 3)
