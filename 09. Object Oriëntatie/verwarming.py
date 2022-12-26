# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/1745983456

class Verwarming:
    def __init__(self, naam, temperatuur=10.0, minimum = 0.0, maximum = 100.0):
        self.naam = naam
        self.temp = temperatuur
        self.min_temp = minimum
        self.max_temp = maximum

    def __str__(self):
        return "{}: huidige temperatuur: {:.1f}; toegelaten min: {:.1f}; toegelaten max: {:.1f}".format(self.naam, self.temp, self.min_temp, self.max_temp)

    def __repr__(self):
        return "Verwarming('{}', {:.1f}, {:.1f}, {:.1f})".format(self.naam, self.temp, self.min_temp, self.max_temp)

    def wijzig_temperatuur(self, wijziging):
        temp_nieuw = self.temp + wijziging
        if temp_nieuw < self.min_temp:
            temp_nieuw = self.min_temp
        if temp_nieuw > self.max_temp:
            temp_nieuw = self.max_temp
        self.temp = temp_nieuw
    
    def temperatuur(self):
        return round(float(self.temp), 1)
