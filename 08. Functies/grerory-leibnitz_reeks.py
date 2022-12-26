# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/325222513

def gregory_leibnitz(n):
    haakjes = 0
    for i in range(1, n+1):
        haakjes = haakjes + (((-1)**(i+1))/((2*i)-1))
    return 4*haakjes
