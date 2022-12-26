# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1180618752

def product(t1, t2):
    product = (t1[0]*t2[0] - t1[1]*t2[1], t1[0]*t2[1] + t1[1]*t2[0])
    return product
