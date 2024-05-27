first = int(input('Сравниваем целые числа!\nВведите число: '))
second = int(input('Еще одно: '))
third = int(input('Еще разок: '))
if first == second == third:
    print(3)
elif first == second or third == second or third == first:
    print(2)
elif first != second or third != second or first != third:
    print(0)
