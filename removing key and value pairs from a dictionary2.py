PERSON = {
    'FIRST_NAME' : 'BRIJESH',
    'LAST_NAME' : 'PATEL',
    'AGE': '20',
    'COUNTRY' : 'INDIA',
    'IS_MARRIED' : False,
    'SKILLS' : ['JAVASCRIPT', 'REACT', 'NODE', 'MONGODB', 'PYTHON'],
    'ADDRESS' : {
        'STREET' : 'SPACE STREET',
        'ZIPCODE' : '361004'
    }
}
PERSON.pop('FIRST_NAME')
PERSON.popitem()
del PERSON ['IS_MARRIED']
print(PERSON)