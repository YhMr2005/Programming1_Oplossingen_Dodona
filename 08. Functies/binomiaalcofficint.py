# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/33489040

def faculteit(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def binomiaal(n,k):
    return int(faculteit(n)/(faculteit(k)*faculteit(n-k)))

