number_system = input("Enter a number system [Binary, Octal, Decimal, Hexadecimal]: ")
number_system = number_system.lower()
num = ''.join(input("Enter number: ").split(' ')).strip()

hex_dict = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}
hex_to_bi = {
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def binaryToDecimal(num):
    sum = 0
    size = len(num)
    for index in range(size):
        sum += (int(num[size - index - 1]) * (2 ** index))
    return str(sum)


def binaryToHexadecimal(num):
    sum = ''

    while len(num) % 4 != 0:
        num = ''.join(('0', num))

    num_list = []
    for i in range(0, len(num), 4):
        num_list.append(num[i:i + 4])

    count = 0
    for n in num_list:
        if count == 0 and n != '0000':
            count += 1

        if count != 0:
            sum += hex_dict[binaryToDecimal(n)]
    return sum


def binaryToOctal(num):
    sum = ''

    while len(num) % 3 != 0:
        num = ''.join(('0', num))

    num_list = []
    for i in range(0, len(num), 3):
        num_list.append(num[i:i + 3])

    count = 0
    for n in num_list:
        if count == 0 and n != '000':
            count += 1

        if count != 0:
            sum += binaryToDecimal(n)

    return sum


def decimalToBinary(num):
    num = int(num)
    remainder_list = []

    if num == 0:
        return '0'
    while num != 0:
        remainder_list.append(str(num % 2))
        num = num // 2

    remainder_list = remainder_list[::-1]
    return ''.join(remainder_list)


def octalToBinary(num):
    sum = ''
    for n in num:
        toAdd = decimalToBinary(n)
        while len(toAdd) % 3 != 0:
            toAdd = ''.join(('0', toAdd))
        sum += toAdd
    while sum.startswith('0'):
        sum = sum[1:]
    return sum


def hexadecimalToBinary(num):
    sum = ''
    toAdd = ''
    for n in num:
        if n in hex_to_bi.keys():
            toAdd = hex_to_bi[n]
        else:
            toAdd = decimalToBinary(n)
            while len(toAdd) % 3 != 0:
                toAdd = ''.join(('0', toAdd))
        sum += toAdd
    while sum.startswith('0'):
        sum = sum[1:]
    return sum


if number_system == 'binary':
    print(f'Bin number: {num}')
    print(f'Decimal form: {binaryToDecimal(num)}')
    print(f'Octal form: {binaryToOctal(num)}')
    print(f'Hexadecimal form: {binaryToHexadecimal(num)}')

elif number_system == 'octal':
    print(f'Octal number: {num}')
    bin = octalToBinary(num)
    print(f'Binary form: {bin}')
    print(f'Decimal form: {binaryToDecimal(bin)}')
    print(f'Hexadecimal form: {binaryToHexadecimal(bin)}')

elif number_system == 'decimal':
    print(f'Decimal number: {num}')
    bin = decimalToBinary(num)
    print(f'Binary form: {bin}')
    print(f'Octal form: {binaryToOctal(bin)}')
    print(f'Hexadecimal form: {binaryToHexadecimal(bin)}')

elif number_system == 'hexadecimal':
    print(f'Hexadecimal number: {num}')
    bin = hexadecimalToBinary(num)
    print(f'Binary form: {bin}')
    print(f'Decimal form: {binaryToDecimal(bin)}')
    print(f'Octal form: {binaryToOctal(bin)}')
else:
    print("Invalid number system, try again."