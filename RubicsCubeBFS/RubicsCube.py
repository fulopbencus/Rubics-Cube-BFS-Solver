# RubicsCube
# Author: Bence Fulop

"""
Represents a 2x2x2 Rubik's cube
The six sides of the cube: Front(F) Back(B)   Up(U) Down(D)   Left(L) Right(R)

Cubie positions starting
at 0, front to back, up to down, left to right.
Alphabetic names refer the cubies.

Each 8 cubie has three faces, so we have 24 face
positions.

For example:

F or B, in clockwise order (looking from outside).
   0th cubie = FLU
   1st cubie = FUR
   2nd cubie = FDL
   3rd cubie = FRD
   4th cubie = BUL
   5th cubie = BRU
   6th cubie = BLD
   7th cubie = BDR

Permutations:

A permutation p on 0,1,...,n-1 is represented as
a list of length n-1.  p[i] = j
means that p maps i to j.

When operating on a list c (a list of length
24 of colors), then  p * c
is the rearranged list of colors:
   (p * c)[i] = c[p[i]]    for all i
Thus, p[i] is the location of where the color of
position i will come from; p[i] = j means that
the color at position j moves to position i.
"""

# The cube is determined here manually
# START
rgw = flu = 0 # (0-th cubie; front face)
gwr = luf = 1 # (0-th cubie; left face)
wrg = ufl = 2 # (0-th cubie; up face)
rwb = fur = 3 # (1-st cubie and so on...)
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
# END

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

F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, 
     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)    # Front face rotated clockwise.

Fi = perm_inverse(F)                                                # Front face rotated counter-clockwise.

L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr,
     dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)    # Left face rotated clockwise.

Li = perm_inverse(L)                                                # Left face rotated counter-clockwise.

U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr,
     luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)    # Upper face rotated clockwise.

Ui = perm_inverse(U)                                                # Upper face rotated counter-clockwise.

twists = (F, Fi, L, Li, U, Ui)

twists_names = {}
twists_names[F] = 'F'
twists_names[Fi] = 'Fi'
twists_names[L] = 'L'
twists_names[Li] = 'Li'
twists_names[U] = 'U'
twists_names[Ui] = 'Ui'