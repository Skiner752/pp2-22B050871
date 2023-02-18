# 1 
# def squares(n):
#     for i in range(1 , n+1):
#         yield(i * i)

# n = int(input())
# a = squares(n)
# for num in a:
#     print(num)



# 2
# def even_generator(n):
#     for i in range(0 , n+1):
#         if i != 0:
#             if i % 2 ==0:
#                 yield(i)

# n = int(input())
# even_numbers = list(even_generator(n))
# print(",".join(str(num) for num in even_numbers))

    


# 3
# def divisibility(n):
#     for i in range(0 , n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield(i)


# n = int(input())
# div = divisibility(n)
# for num in div:
#     print(div)


# 4
# def squares(a , b):
#     for i in range(a , b):
#         yield(i * i)

# a = int(input())
# b = int(input()) 
# c = squares(a ,b)
# for num in c:
#     print(num)

# 5
# def reverse(n):
#     for i in range(n)[::-1]:
#         yield(i)


# n = int(input())
# reverse_numbers = reverse(n)
# for num in reverse_numbers:
#     print(num)