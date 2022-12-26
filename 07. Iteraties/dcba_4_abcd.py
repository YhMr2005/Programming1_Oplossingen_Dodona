# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/128911221

for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if int(str(i)+str(j)+str(k)+str(l))==4*int(str(l)+str(k)+str(j)+str(i)):
                    print(str(i)+str(j)+str(k)+str(l), "= 4 *", str(l)+str(k)+str(j)+str(i))
