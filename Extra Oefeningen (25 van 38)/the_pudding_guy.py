# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/761303597

aantal = int(input())
kost = float(input())
benodigd_aantal = int(input())
mijlen_per_coupon = int(input())

gespendeerd = aantal * kost
aantal_coupons = aantal // benodigd_aantal
tot_mijlen = aantal_coupons * mijlen_per_coupon

print(f"Phillips spendeerde ${gespendeerd:.2f} voor {tot_mijlen} frequent flyer mijlen.")