# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/387716745

v = float(input())
l = float(input())
rho = float(input())
mu = float(input())

re = (v*l*rho) / mu

if re < 2000:
    stroming = "laminaire stroming"
elif re > 4000:
    stroming = "turbulente stroming"
else:
    stroming = "omslagstroming"

print(f"{re} ({stroming})")