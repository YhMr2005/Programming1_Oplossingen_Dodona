from math import sqrt, atan, pi

def pool_coordinaten(x, y):
    r = sqrt(x**2 + y**2)

    # Zorg ervoor dat theta tussen 0 en 360°, dus geen negatieve waarde
    if x == 0:
        if y >= 0:
            theta = pi/2
        else:
            theta = 3*(pi/2)
    elif x > 0:
        if y >= 0:
            theta = atan(y/x)
        else:
            theta = atan(y/x) + 2*pi
    elif x < 0:
        theta = atan(y/x) + pi
        
    return r, theta

def sector_van_hoek(hoek):
    '''
    Ik heb niet de omzetting naar beta gedaan zoals in de opgave voorgesteld wordt,
    maar ik heb direct de sector berekent met de hoek theta.
    '''
    hoek_omgedraaid = 2*pi - hoek # Draait hoek om in wijzerzin (theta is in tegenwijzerzin)
    sector = round(hoek_omgedraaid / (pi/10)) + 6
    if sector > 20:
        sector -= 20
    return sector

def bereken_score(sector, straal):
    if straal <= (12.7/2):
        score = 50
    elif straal <= (31.8/2):
        score = 25
    elif straal <= (214/2 - 9.6):
        score = sector
    elif straal <= (214/2):
        score = sector * 3
    elif straal <= (340/2 - 9.6):
        score = sector
    elif straal <= (340/2):
        score = sector * 2
    else:
        score = 0
    
    return score

def main():
    carth_x = float(input())
    carth_y = float(input())
    pool_r, pool_theta = pool_coordinaten(carth_x, carth_y)
    sector_index = sector_van_hoek(pool_theta)
    score = bereken_score(sector_index, pool_r)
    print(score)

main()