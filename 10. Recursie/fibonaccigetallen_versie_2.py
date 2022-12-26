# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1515270930

def fib(n, diepte=0):
    inspringing = 2*" "
    if n == 0:
        print(diepte*inspringing + "fib(0, {})".format(diepte))
        print(diepte*inspringing + "return 0")
        return 0
    if n == 1:
        print(diepte*inspringing + "fib(1, {})".format(diepte))
        print(diepte*inspringing + "return 1")
        return 1
    print(diepte*inspringing + "fib({}, {})".format(n, diepte))
    diepte += 1
    out = fib(n-1, diepte) + fib(n-2, diepte)
    print((diepte-1)*inspringing +"return {}".format(out))
    return(out)
