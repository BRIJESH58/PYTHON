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
print(PERSON.get('FIRST_NAME'))
print(PERSON.get('LAST_NAME'))
print(PERSON.get('AGE'))
print(PERSON.get('COUNTRY'))
print(PERSON.get('IS_MARRIED'))
print(PERSON.get('SKILLS'))
print(PERSON.get('ADDRESS')('STREET'))
