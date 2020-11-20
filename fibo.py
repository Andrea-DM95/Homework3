known_fibo = {0:0, 1:1}
def fibo(n):
    if n not in known_fibo:
        known_fibo[n] = fibo(n-1) + fibo(n-2)
    return known_fibo[n]
