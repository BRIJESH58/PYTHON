try:
    NAME = input('ENTER YOUR NAME:')
    YEAR_BORN = input('YEAR YOU BORN:')
    AGE = 2022 - int(YEAR_BORN)
    print({NAME}, {AGE})
except Exception as e:
    print(e)