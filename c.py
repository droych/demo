def is_prime(n):
    if n==2:
        return True
    if n < 2:
        return False
    for i in range(3, n//2 + 1):
        if n % i == 0:
            return False
    return True

def longest_prime_subset(n):
    p = str(n)
    max_prime = 0
    i = 0
    
    for j in range(len(p)):
        sub = int(p[i:j+1])
        if is_prime(sub):
            max_prime = max(max_prime, sub)
        else:
            i += 1
    
    return max_prime


n = 12241566
print(longest_prime_subset(n))  