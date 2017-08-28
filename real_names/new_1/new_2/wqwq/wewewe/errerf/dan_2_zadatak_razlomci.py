class Razlomak(object):
    def __init__(self, brojilac, imenilac):
        self.brojilac = brojilac
        self.imenilac = imenilac

    def __mul__(self, other):
        return Razlomak(self.brojilac * other.brojioc, self.imenilac * other.imenioc)

    def __str__(self):
        return "%d/%d" % (self.brojilac, self.imenilac)

    # self + other
    def __add__(self, other):
        if self.imenilac == other.imenioc:
            return Razlomak(self.brojilac + other.brojioc, self.imenilac)
        else:
            return Razlomak(self.brojilac * other.imenioc + other.brojilac * self.imenilac, self.imenilac * other.imenioc)


r1 = Razlomak(2, 4)
r2 = Razlomak(1, 3)
r3 = Razlomak(1, 2)

print "Sabiranje %s + %s = %s" % (r1, r2, r1 + r2)
print "Sabiranje %s + %s = %s" % (r1, r3, r1 + r3)
print "Mnozenje %s * %s = %s" % (r1, r2, r1 * r2)
