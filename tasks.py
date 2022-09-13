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
