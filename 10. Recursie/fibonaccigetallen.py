# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/546000908

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return(fib(n-2) + fib(n-1))