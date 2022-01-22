def IntersecOfSets(ARR1, ARR2, ARR3):
    S1 = set(ARR1)
    S2 = set(ARR2)
    S3 = set(ARR3)
    print('LIST = ',ARR1)
    print('TUPLE = ',ARR2)
    print('DICTIONARY = ',ARR3)
    SET1 = S1.intersection(S2)
    RESULT_SET = set1.intersection(S3)
    FINAL_LIST = set(RESULT_SET)
    print('COMMON OF MEMBERS OF LIST, TUPLE & DICTIONARY =',FINAL_LIST)

    if_name_=='__main__'
    LIST1 = [1, 2, 'ABC', 'xyz']
    TUPLE1 = (80, 50, 'ABC', 'xyz')
    DICTIONARY1 = {300, 900, 'ABC', 'xyz'}
    IntersecOfSets(LIST1, TUPLE1, DICTIONARY1)
