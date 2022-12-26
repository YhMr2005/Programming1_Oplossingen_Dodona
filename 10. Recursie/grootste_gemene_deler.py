# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/854408577

def ggd(a, b):
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    else:
        return ggd(min(a, b), (max(a, b) % min(a, b)))
