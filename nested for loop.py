PERSON = {
    'FIRST_NAME': 'BRIJESH',
    'LAST_NAME': 'PATEL',
    'AGE': 20,
    'COUNTRY': 'INDIA',
    'IS_MARRIED': True,
    'SKILLS': ['JAVASCRIPT', 'REACT', 'NODE', 'MONGODB', 'PYTHON'],
    'ADDRESS': {
        'STREET': 'GOKUL NAGAR',
        'ZIP CODE': 361004
    }
}
for key in PERSON:
    if key == 'SKILLS':
        for SKILL in PERSON['SKILLS']:
            print(SKILL)