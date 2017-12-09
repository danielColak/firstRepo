def fibonacci(n):
    f1 = 1
    f2 = 0
    f = 1
    clan_Niza = 0
    while clan_Niza < n:
        print "Stigao sam do %d" % f
		changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
changes on testBranch
        f = f1 + f2
        yield f
        f2 = f1
        f1 = f
        clan_Niza = clan_Niza + 1
    return



for i in fibonacci(9):
    print i