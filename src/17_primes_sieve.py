import math

user_num = math.floor(float(input('Enter a number: ')))
initial = [num for num in range(2, user_num + 1) if num == 2 or num % 2 != 0]
primes = []
for num in initial:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
print(f'There are {len(primes)} prime numbers in {user_num}.')
print(primes)
