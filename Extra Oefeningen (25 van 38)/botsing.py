# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1301141031

rechthoek1 = {"x1": int(input()), "y1": int(input()), "x2": int(input()), "y2": int(input())}
rechthoek2 = {"x1": int(input()), "y1": int(input()), "x2": int(input()), "y2": int(input())}

# Maak altijd eerste punt linksonder en tweede punt rechtsboven.
if rechthoek1["x2"] < rechthoek1["x1"]:
    rechthoek1["x2"], rechthoek1["x1"] = rechthoek1["x1"], rechthoek1["x2"]
if rechthoek2["x2"] < rechthoek2["x1"]:
    rechthoek2["x2"], rechthoek2["x1"] = rechthoek2["x1"], rechthoek2["x2"]

if rechthoek1["y2"] < rechthoek1["y1"]:
    rechthoek1["y2"], rechthoek1["y1"] = rechthoek1["y1"], rechthoek1["y2"]
if rechthoek2["y2"] < rechthoek2["y1"]:
    rechthoek2["y2"], rechthoek2["y1"] = rechthoek2["y1"], rechthoek2["y2"]

# Main
if rechthoek1['x1'] >= rechthoek2 ['x2'] or rechthoek2['x1'] >= rechthoek1 ['x2']:
    print("geen botsing")
elif rechthoek1['y1'] >= rechthoek2 ['y2'] or rechthoek2['y1'] >= rechthoek1 ['y2']:
    print("geen botsing")
else:
    print("botsing")