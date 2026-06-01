##### List Comprehension
'''
Basics Syantax            [expression for item in iterable]

with conditional logic    [expression for item in iterable if condition]

Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]
'''

# intro to python list comprehensions
# >>> nums = [1, 2, 3]
# >>> [i * 2 for i in nums]
# [2, 4, 6]

# where to use
# 1.
nums = [1, 2, 3, 4, 5, 6]
strings = ["intor", "to", "list", "comps"]

# # results = []
# # for i in nums:
# #     i = i * 2
# #     results.append(i)
# # print(results)
# results = [i * 3 for i in nums]
# print(results)

# 2.
# # results = []
# # for i in strings:
# #     i = i.upper()
# #     results.append(i)
# # print(results)

# results = [i.upper() + " hey" for i in strings]
# print(results)

"""
Key features
- returns a list
- always has the for in
"""

# 3.
# def timesFive(num):
#     return num * 5

# # # results = []
# # # for i in nums:
# # #     i = timesFive(i)
# # #     results.append(i)
# # # print('results with function', results)

# # results = [timesFive(i) for i in nums]
# # print('results with function', results)

# results = [timesFive(i) for i in nums if i > 2]
# print('results with function', results)

# 4.
# dicts = [{"name": "John"}, {"name": "Matt"}]

# # results = []
# # for i in dicts:
# #     results.append(i["name"])

# results = [i["name"] for i in dicts]
# print("results", results)

# ----------------dummy-------------
# numbers = [1, 2, 3, 4, 4, 5, 6]

# sqaures = [x**2 for x in numbers]
# cubes = [x**3 for x  in numbers]
# odd_cubes = [x**3 for x in numbers if x % 2 != 0]

# print(sqaures)
# print(cubes)
# print(odd_cubes)

# -----------------------------------

# # list comprehension vs map() function

# a = [1, 2, 3, 4]
# lista = [x*2 for x in a]
# print(lista)

# # map(function, iterable) --> iterables are lists etc.

# a = list(map(lambda x:x*2, a))
# print(a)

# b = [str(x) for x in a]
# print(b)

# c = list(map(str, [1, 2, 3, 4]))
# print(c)

# # filter(function, iterable)

# d = [str(x) for x in a if x > 3]
# print(d)

# e = list(filter(lambda x: int(x) > 1, map(str, [1, 2, 3, 4])))
# print(e)

# def timesTwo(i):
#     return i*2

# f = [timesTwo(x) for x in a]
# print(f)

# ----------------------------------------------------

# # list comprehension vs filter() function

# a = [1, 2, 3, 4, 5]
# b = [i for i in a if i > 4]
# print(b)
# # filter(funtcion, iterable)
# c = list(filter(lambda x:x>3, a))
# print(c)


# def greaterthan4(num):
#     return num>4

# d = [i for i in a if greaterthan4(i)]
# print(d)

# e = list(filter(greaterthan4, a))
# print(e)

# f = list(filter(None, [0, 1, 2, 3]))
# f = list(filter(None, [0, 1, 2, 3, False, True, None, ]))
# print(f)

# ---------------------------------------
# # Nested loops

# pairs = [(i, j) for i in range(3) for j in range(2)]

# print(pairs)

# # Conditional

# even_sum = ["Even" if (x[0] + x[1])%2 == 0 else "Odd" for x in pairs]
# print(even_sum)

# ----------------------------------------------------------------

# # Dictionary comprehensions

# sq = {x:x*x for x in range(6)}
# print(sq)

# # condition

# even = {(k if k%2 ==0 else v):(v if v%2==0 else k) for k,v in sq.items()}
# print(even)

# even_pairs = {k:v for k,v in sq.items() if k%2 == 0 and v%2==0}
# print(even_pairs)

# ------------------------------------------

# # Set comprehension

# nums = [1, 1, 2, 2, 3, 4]

# unique = {x for x in nums}
# print(unique)

# even_unique = {x for x in nums if x % 2 == 0}
# print(even_unique)

# ----------------------------------------------------------------

# # Generator comprehension
# my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
# filtered_list = [x for x in my_list if x % 2 == 0]
# print(filtered_list)

# filtered_gen = (x for x in my_list if x%2 != 0)
# print(next(filtered_gen))

# use python shell

# # >>> my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
# # >>> my_list
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # >>> filtered_gen = (x for x in my_list if x%2 != 0)
# # >>> filtered_gen
# # <generator object <genexpr> at 0x00000194AC9B2C20>
# # >>> next(filtered_gen)
# # 1
# # >>> next(filtered_gen)
# # 3
# # >>> next(filtered_gen)
# # 5
# # >>> next(filtered_gen)
# # 7
# # >>> next(filtered_gen)
# # 9
# # >>> next(filtered_gen)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     import platform
# # StopIteration
# # >>> list(filtered_gen)
# # []
# # >>> gen_to_list = list(filtered_gen)
# # >>> gen_to_list
# # []
# # >>> filtered_gen = (x for x in my_list if x%2 != 0)
# # >>> gen_to_list = list(filtered_gen)
# # >>> gen_to_list
# # [1, 3, 5, 7, 9]
# # >>> filtered_gen = (x for x in my_list if x%2 != 0)
# # >>> first = next(filtered_gen)
# # >>> second = next(filtered_gen)
# # >>> first
# # 1
# # >>> second
# # 3
# # >>>

# -----------------------------------------------------------

# Nested comprehensions

# matrix = [
#     [1, 2],
#     [3, 4]
# ]
# # for row in matrix:
# #     for column in row:
# #         print(column)

# flat = [column for row in matrix for column in row]
# print(flat)

# 2d Flatten
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5]
# ]

# flat2 = [x for row in matrix for x in row]
# print(flat2)

# # 3D Flatten

# matrix3 = [
#    [ [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9] ],
#     [[11, 22, 33],
#      [44, 55, 66],
#      [77, 88, 99]]
# ]

# flat3 = [x for layer in matrix3 for row in layer for x in row]
# print(flat3)

# ------------------------------------------------------------------
# # Conditional filtering

# employees = [
#     {"name":"A","salary":50000},
#     {"name":"B","salary":80000}
# ]

# high_pay = [e for e in employees if e['salary'] > 60000]
# print(high_pay)

# --------------------------------------------------------------------
# # Enumerate

# nums = {x*10000:x for x in range(11)}
# print(nums)

# # general

# # for idx, val in enumerate(nums)
# # print(idx, val)
# # [idx:val for idx,val in enumerate(nums)]

# high = [(idx,val) for idx,val in enumerate(nums)]
# print(high)

#  ----------------------------------------------------------------------
# # Zip
# names = ['A', 'B', 'C', 'D', 'D']
# ages = [1, 2, 3, 3, 3]

# pack = set(zip(names, ages))
# print(pack)

# ------------------------------------------------------------------------

# # Lambda functions and sorting

# sqaure = lambda x:x*2

# students = [
#     {'name': "A", "marks":95},
#     {'name': "B", "marks":90},
#     {'name': "C", "marks":94},
#     {'name': "D", "marks":97},
#     {'name': "E", "marks":92},
#     {'name': "F", "marks":98},
#     {'name': "G", "marks":93},
# ]

# students.sort(key=lambda x:x["marks"])
# print(students)

# ----------------------------------------------------
# map, filter, reduce

# map
# comprehension equivalent
# nums = [1, 2, 3, 4, 5]
# print(list(map(lambda x:x*2, nums)))

# filter
# def greator_than(x):
#     return x > 3
# print(list(filter(greator_than, map(lambda x:x*2, nums))))
# print(list(filter(lambda x:x%2 == 0, map(lambda x:x*3, nums))))

# # reduce
# from functools import reduce
# nums = [1, 3, 1, 4, 5]
# ans = reduce(lambda a,b:a*b, nums)
# print(ans)

# --------------------------------------------------------------------
# # Sorting
# nums = [x*x for x in range(0, 10)]

# nums.sort(reverse = True)
# print(nums)

# Any() and All()

print(any([True, False, False, False]))
print(any([False, False, False, False]))
print(any([True, True, True, False]))
print(any([True, True, True, True]))
print(all([True, False, False, False]))
print(all([False, False, False, False]))
print(all([True, True, True, False]))
print(all([True, True, True, True]))