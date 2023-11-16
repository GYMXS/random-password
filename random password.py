import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
characters_password = int(input('Introduce the amount of characters of your password'))
password_content = ''
for i in range(characters_password):
    x = random.randint(0, len(characters) - 1)
    y = characters[x]
    password_content += y
print(password_content)
