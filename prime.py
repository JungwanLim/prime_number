import math as m

def prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    i = 3
    while i <= int(m.sqrt(n)):
        if n % i == 0:
            return False
        i += 2
    return True

p = [2]
n = 100
count = 1
for x in range(3, n + 1, 2):
    if prime(x):
        p.append(x)
        count += 1
print("count = ", count , p)
p = [1, 2, 354254841917]
for x in p:
    if prime(x):
        print(x, "is prime number.")
    else:
        print(x, "is not prime number.")


print(" \n\n")
def prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(m.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

p = [2]
n = 100
count = 1
for x in range(3, n + 1, 2):
    if prime(x):
        p.append(x)
        count += 1
print("count = ", count , p)
print(prime(354254841917))


print("\n\n")
def prime(n):
    i, p = 3, [2]
    while i <= n:
        j = 3
        while j <= int(m.sqrt(i)):
            if i % j == 0:
                break
            else:
                j += 2
        if int(m.sqrt(i)) < j:
            p.append(i)
        i += 2
    return p
print(prime(100))


print("\n\n")
def prime(n):
    p = [2]
    for i in range(3, n + 1, 2):
        j = 3
        for j in range(3, int(m.sqrt(i)) +  1, 2):
            if i % j == 0:
                break
            else:
                j += 2
        if int(m.sqrt(i)) < j:
            p.append(i)
    return p
print(prime(99))


print("\n\n")
print("Sieve of Eratosthenes")
n = 100
e_sieve = []
for x in range(n + 1):
    if x % 2 != 0:
        e_sieve.append('0')
    else:
        e_sieve.append('1')
    
e_sieve[0] = '1'
e_sieve[1] = '1'
e_sieve[2] = '0'

def prime(n):
    for i in range(3, int(m.sqrt(n)) + 1, 2):
        if e_sieve[i] == '0':
            for j in range(i * i, n + 1, i * 2):
                e_sieve[j] = '1'

prime(n)
for x in range(1, n + 1):
    if e_sieve[x] == '0':
        print(x, end = ' ')
print()


