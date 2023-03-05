# 1 
import math
a = [1,2,3,4,5]
ans = math.prod(a)
print(ans)

2 
word = str(input())
lower_count = sum(map(str.islower, word))
upper_count = sum(map(str.isupper, word))
print(lower_count)
print(upper_count)


3 
word = str(input())
word = word.lower()
rev_word = word[::-1]
if word == rev_word:
    print('Polindrome')
else:
    print('Not Polindrome')

4 
import time
num = int(input())
mil_s = int(input())
time.sleep(mil_s/1000)
sqrt = num ** (0.5)
print(f'Square root of {num} after {mil_s} miliseconds is {sqrt}')
# 5
a = tuple()
a = (1,2,3,4,0)
print(all(a))

