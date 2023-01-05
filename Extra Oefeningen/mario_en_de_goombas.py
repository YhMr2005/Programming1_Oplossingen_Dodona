mario_tot_afgrond = int(input())
goomba_a_tot_afgrond = int(input())
goomba_a_richting = input()
goomba_b_tot_afgrond = int(input())
goomba_b_richting = input()

if goomba_a_richting == "L":
    tijd_goomba_a = 2*mario_tot_afgrond - goomba_a_tot_afgrond
else:
    tijd_goomba_a = goomba_a_tot_afgrond

if goomba_b_richting == "L":
    tijd_goomba_b = 2*mario_tot_afgrond - goomba_b_tot_afgrond
else:
    tijd_goomba_b = goomba_b_tot_afgrond

print(f"Het duurt {max(tijd_goomba_a, tijd_goomba_b)} minuten tot beide Goomba's weg zijn")
