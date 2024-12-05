# # a = "banana"
# #
# # for x in a:
# #     print(x)
# #
# # print("a" in a)
#
# b = "Hello, World!"
# # print(b[2:5])
# # print(b[:5])
# # print(b[1:])
# # print(b[1::2])
#
# # Reverse a string
# # print(b[::-1])
#
# c = ["apple", 'banana', 'cherry']
# # print(c)
#
# # Change items in a specific range
# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # this_list[1:3] = ["blackcurrant", "watermelon"]
# # this_list.extend(c)
# # print(this_list)
#
# # for x in this_list:
# #     print(x)
#
# # for i in range(len(this_list)):
# #     print(this_list[i])
#
# # [print(x) for x in this_list]
#
# # List Comprehension
#
# # newlist = [expression for item in iterable if condition == True]
#
# # Reverses the items in a list
# # this_list.reverse()
# # print(this_list)
#
#
# # Factorial
# # n = int(input("Enter the number "))
# #
# # fact = 1
# #
# # for i in range(1,n+1):
# #     fact = fact * i
# # print(fact)
#
# # Fibonacci
# # n = int(input("Enter how many first fibonacci numbers u would like to see: "))
# # fib1 = 0
# # fib2 = 1
# #
# #
# # if n>= 1:
# #     print(fib1, end=" ")
# # if n >= 2:
# #     print(fib2, end=" ")
# # count = 2
# #
# # while count < n:
# #     fib_next = fib1 + fib2
# #     fib1 = fib2
# #     fib2 = fib_next
# #     print(fib_next, end=" ")
# #
# #     count += 1
#
#
# # Reverse fibonacci search
#
# n = int(input("Enter how many first fibonacci numbers u would like to see: "))
# fib1 = 0
# fib2 = 1
# fib = []
#
#
# if n>= 1:
#     fib.append(fib1)
# if n >= 2:
#    fib.append(fib2)
# count = 2
#
# while count < n:
#     fib_next = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_next
#     fib.append(fib_next)
#
#     count += 1
#
# print(fib[::-1])

str = "Hello this is a string"
this_list = str.split()
for i in this_list:
    print(this_list[::-1])