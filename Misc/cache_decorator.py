from functools import cache

count_cached = 0
count = 0

@cache
def fibonacci_cached(n):
    global count_cached
    count_cached += 1
    print("count_cached: ", count_cached)

    if n <= 1:
        return n
    else:
        return fibonacci_cached(n-1) + fibonacci_cached(n-2)
    
def fibonacci(n):
    global count
    count += 1
    print("count: ", count)

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_cache_r = fibonacci_cached(8)
print("With cache: ", count_cached, " calls to calculate: ", fib_cache_r)
print(fibonacci(8))
print("With cache: ", count_cached, " calls to calculate: ", fib_cache_r)




# LRU CACHE DECORATOR