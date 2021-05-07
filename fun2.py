# Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел

num = set()

for i in range(5):
    try:
        num1 = int(input("Введите число: "))
        num.add(num1)
        if num1 == 0:
            print("Введите натуральное число")
        if num1 < 0:
            print("Без минусов братан")
    except ValueError:
        print("Введите число")

print("Самое маленькое число: ", min(num))

