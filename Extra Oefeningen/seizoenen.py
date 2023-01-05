# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1800551125

dag = int(input())
maand = input()

if maand in ("april", "mei") \
    or (maand == "maart" and dag >= 21) \
    or (maand == "juni" and dag <= 20):
    seizoen = "lente"

if maand in ("juli", "augustus") \
    or (maand == "juni" and dag >= 21) \
    or (maand == "september" and dag <= 22):
    seizoen = "zomer"

if maand in ("oktober", "november") \
    or (maand == "september" and dag >= 23) \
    or (maand == "december" and dag <= 20):
    seizoen = "herfst"

if maand in ("januari", "februari") \
    or (maand == "december" and dag >= 21) \
    or (maand == "maart" and dag <= 20):
    seizoen = "winter"

print(f"Het is {seizoen} op {dag} {maand}.")