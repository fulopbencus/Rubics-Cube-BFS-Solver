# RubicsCube
# Author: Bence Fulop

rgw = flu = 0
gwr = luf = 1
wrg = ufl = 2
rwb = fur = 3
wbr = urf = 4
brw = rfu = 5
ryg = fdl = 6
ygr = dlf = 7
gry = lfd = 8
rby = frd = 9
byr = rdf = 10
yrb = dfr = 11
owg = bul = 12
wgo = ulb = 13
gow = lbu = 14
obw = bru = 15
bwo = rub = 16
wob = ubr = 17
ogy = bld = 18
gyo = ldb = 19
yog = dbl = 20
oyb = bdr = 21
ybo = drb = 22
boy = rbd = 23

def perm_apply(perm, position):
    return tuple([position[i] for i in perm])

def perm_inverse(p):
    n = len(p)
    q = [0]*n
    for i in range(n):
        q[p[i]] = i
    return tuple(q)

def perm_to_string(p):
    s = "("
    for x in p: s = s + "%2d "%x
    s += ")"
    return s

I = (flu, luf, ufl, fur, urf, rfu, fdl, dlf, lfd, frd, rdf, dfr,     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)