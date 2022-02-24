try:
    NAME = input('ENTER YOUR NAME:')
    YEAR_BORN = input('YEAR YOU BORN:')
    AGE = 2022 - int(YEAR_BORN)
except TypeError:
    print('TYPE ERROR OCCURED')
except ValueError:
    print('VALUE ERROR OCCURED')
except ZeroDivisionError:
    print('ZERO DIVISON ERROR OCCURED')
else:
    print('I USUALLY RUN WITH THE TRY BLOCK')
finally:
    print('I ALWAYS RUN.')