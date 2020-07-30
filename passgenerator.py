import random

chars = 'abcdefghijklnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

num = int(input('enter number of passwords'))
lenght = int(input('enter lenght of passwords'))

for i in range(num):
    password = ''

    for i in range(lenght):
        password += random.choice(chars)

    print(password)
