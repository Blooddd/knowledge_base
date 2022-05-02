age = int(input('какой ваш возраст? '))
gender = input('какой у вас пол ? ')

if 18 <= age <= 28 and  gender == "man" or gender == "women":
    print("Кандидат прошел первичную проверку ")
else:
    print("Кандидат не подходит ") 
