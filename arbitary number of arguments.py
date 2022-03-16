def SUM_ALL_NUMS(*NUMS):
    TOTAL = 0
    for NUM in NUMS:
        if NUM%2!=0:
            TOTAL = TOTAL + NUM
    return TOTAL
print(SUM_ALL_NUMS(2,3,4,1))