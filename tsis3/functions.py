'''1.A recipe you are reading states how many grams you need for the ingredient. 
Unfortunately, your store only sells items in ounces. 
Create a function to convert grams to ounces. ounces = 28.3495231 * grams'''

# def convert(grams):
#     ounces = 28.3495231 * grams
#     return ounces


# grams = int(input())
# a = convert(grams)
# print(a)


'''2.Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)'''

# def Read(F):
#     C = (5 / 9) * (F - 32)
#     return C

# F = int(input())
# print(Read(F))

   

# def solve(numheads , numlegs):
#     countR = (numlegs - (numheads * 2)) / 2
#     countCh = numheads - countR
#     return countR , countCh

# numheads = 35
# numlegs = 94
# a , b = solve(numheads , numlegs)
# print(a , b)


# 4
# def filter_prime(numbers):
#     def is_prime(num):
#         if num <= 1:
#             return False
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#     a = [num for num in numbers if is_prime(num)== True] 
#     return a



# numbers = list(map(int , input().split()))
# prime_numbers = filter_prime(numbers)
# print(prime_numbers)

# 5
# def permutations(string):
#     from itertools import permutations
#     for permutation in permutations(string):
#         print(''.join(permutation))   #''separator.join

# string = input()
# permutations(string)


# 6
# def reverse (sentence):
#     return ' '.join(sentence.split()[::-1]) #The [::-1] slice notation is used to reverse the order of the elements in this list.


# sentence = input()
# print(reverse(sentence))



#7
# def has_33(numbers):
#     n = len(numbers)
#     for i in range(n - 1):
#         if i < n - 1:
#             if(numbers[i] == 3 and numbers[i + 1] == 3):
#                 return True
        
        
#     return False


# a = list(map(int , input().split()))
# b = list()
# b = has_33(a)
# print(b)

# 8
# def spy_games(numbers):
#     my_list = [0, 0, 7]
#     cnt = 0
#     for i in numbers:
#         if i == my_list[cnt]:
#             cnt+=1
#     if cnt == 3:
#         return True
    
#     return False

   


# a = list(map(int , input().split()))
# c = spy_games(a)
# print(c)# 
# 9
# import math
# def Volumne(radius):
#     a = 4/3 * math.pi * (radius ** 3)
#     return a


# radius = int(input())
# print(Volumne(radius))
# 10 
# def unique(my_list):
#     unq_list = []
#     for i in my_list:
#         if i not in unq_list:
#             unq_list.append(i)
#     return unq_list


# a = list(map(int , input().split()))
# a = sorted(a) 
# c = unique(a)
# print(c) 

# 11 
# def Polindrome(str_or):
#     str_rev =str_or[::-1]
#     if str_rev == str_or:
#         return True
#     else:
#         return False


# str_or = input()
# print(Polindrome(str_or))

# 12 
# def histogram(my_list):
#     for i in my_list:
#         for j in range(i):
#             print('*', end='')
#         print()

# a = list(map(int, input().split()))
# histogram(a)
# 13
import random
a = random.randint(1, 20)
cnt = 0
print('Hello! What is your name?')
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print('Take a guess.')
for i in range(1 , 20):
    guess = int(input())
    cnt+=1  
    if guess < a:
        print('Your guess is too low.')   
    if guess > a:
        print('Your guess is too high.')
    if guess == a:
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
        break
# 14
