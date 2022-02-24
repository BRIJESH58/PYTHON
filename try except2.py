try:
    NAME = input('ENTER YOUR NAME:')
    YEAR_BORN = input('YEAR YOU WERE BORN:')
    AGE = 2022 - YEAR_BORN
    print('YOU ARE {NAME}. AND YOUR AGE IS {AGE}.')
except:
    print('SOMETHING WENT WRONG')