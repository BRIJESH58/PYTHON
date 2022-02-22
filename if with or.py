USER = 'JAMES'
ACCESS_LEVEL = 3
if USER == 'ADMIN' or ACCESS_LEVEL >=4:
    print('ACCESS GRANTED!')
else:
    print('ACCESS DENIED!')