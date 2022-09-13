# Task 30
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# n = input("Insert Number: ")
# d = input("Insert d: ")

# k = len(d.split(".")[1])
# print(n[:n.find(".")+k+1])


# Task 31
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# n = 38
# simpleNums = [2]
# for i in range(3, n, 2):
#     if all(i % j != 0 for j in range(2, i//2)):
#         simpleNums.append(i)                  # ряд простых чисел до N
# resultList = []
# for i in simpleNums:
#     if n % i == 0:
#         resultList.append(i)
# print(resultList)


# Task 32
# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# from random import randint


# n = int(input("Insert count of list: "))
# initList = [0]*n
# for i in range(n):
#     initList[i] = randint(0, 10)
# print(initList)

# resultSet = set(initList)
# print(resultSet)


# Task 33
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# k = 26
# coefficientList = []
# for i in range(k+1):
#     coefficientList.append(random.randint(0, 100))
# print(coefficientList)


# indexes = {                                     # словарь степеней в unicode
#     0: "\u2070",
#     1: "\u00B9",
#     2: "\u00B2",
#     3: "\u00B3",
#     4: "\u2074",
#     5: "\u2075",
#     6: "\u2076",
#     7: "\u2077",
#     8: "\u2078",
#     9: "\u2079",
# }

# # строка для терминала с красивыми степенями
# resultString = ""
# for i in range(k-1):
#     kString = str(k-i)
#     currentPower = ""                           # для создания двузначной степени
#     for j in range(len(kString)):
#         currentPower += indexes[int(kString[j])]
#     resultString += f"{str(coefficientList[i])}x{currentPower} + "
# resultString += f"{str(coefficientList[k-1])}x + "
# resultString += f"{str(coefficientList[k])} = 0"


# # строка для файла (не хочет записывать с красивыми степенями))
# resultStringForFile = ""
# for i in range(k-1):
#     resultStringForFile += f"{coefficientList[i]}x**{k-i} + "
# resultStringForFile += f"{str(coefficientList[k-1])}x + "
# resultStringForFile += f"{str(coefficientList[k])} = 0"


# print(resultString)
# f = open("task33.txt", "w")
# f.write(resultStringForFile)
