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
    
    for i in range(len(p)):  
        for j in range(i, len(p)):  
            sub = int(p[i:j+1])
            #print(sub)
            if is_prime(sub):
                max_prime = max(max_prime, sub)
                #print("bbbbbbbbbb",max_prime)

    return max_prime


n = 241566
print(longest_prime_subset(n))  