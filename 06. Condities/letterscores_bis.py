# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/721367095

# numerieke score inlezen
numerieke_score = int(input())

# letterscore bepalen
if numerieke_score >= 60 and numerieke_score < 70:
    letterscore = 'D'
elif numerieke_score >= 70 and numerieke_score < 80:
    letterscore = 'C'
elif numerieke_score >= 80 and numerieke_score < 90:
    letterscore = 'B'
elif numerieke_score >= 90:
    letterscore = 'A'
else:
    letterscore = 'F'

# letterscore uitschrijven
print(letterscore)

