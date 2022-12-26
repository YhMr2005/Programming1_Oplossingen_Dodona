# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/172219463
import random

def kaartspel():
    rangen = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    kleuren = ["C", "D", "H", "S"]

    kaarten = []
    for rang in rangen:
        for kleur in kleuren:
            kaarten.append(rang+kleur)
    random.shuffle(kaarten)

    return kaarten