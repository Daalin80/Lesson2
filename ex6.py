list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = float(input("введите число для поиска в списке: "))
if abs(n) in list:
    print("Число найдено")
else:
    print("Число не найдено")

