def ggd(a, b):
    
    """
    Berekent de grootste gemene deler van twee natuurlijke getallen a en b.

    >>> ggd(15, 24)
    3
    >>> ggd(252, 105)
    21
    """
    
    # berekening grootste gemene deler op basis van het algoritme van Euclides
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    else:
        return ggd(min(a, b), (max(a, b) - min(a, b)))

def kgv(a, b):
    
    """
    Berekent het kleinste gemene veelvoud van twee natuurlijke getallen a en b.

    >>> kgv(15, 24)
    120
    >>> kgv(252, 105)
    1260
    """
    
    # berekening kleinste gemene veelvoud
    return int((a*b) / ggd(a, b))

def omwentelingen(a, b):
    
    """
    Berekent het kleinste aantal omwentelingen van een tandwiel met a tanden dat 
    tandwielen met a en b tanden terug in hun beginpositie brengt.

    >>> omwentelingen(15, 24)
    8
    >>> omwentelingen(252, 105)
    5
    """
    
    # berekening aantal omwentelingen
    return int(kgv(a, b) / a)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    