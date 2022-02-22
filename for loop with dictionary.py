PERSON = {
    'FIRST NAME':'BRIJESH',
    'LAST NAME':'PATEL',
    'AGE':19,
    'COUNTRY':'INDIA',
    'IS_MARRIED':False,
    'SKILLS':['JAVASCRIPT', 'REACT', 'NODE', 'MONGODB', 'PYTHON'],
    'ADDRESS':{
              'STREET':'SHYAM NAGAR',
              'PINCODE':361004
              }
         }
for KEY in PERSON:
    print(KEY)

for KEY, VALUE in PERSON.items():
    print(KEY, VALUE)