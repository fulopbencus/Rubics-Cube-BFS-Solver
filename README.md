# 2x2x2 Rubik's Cube Breadth-First solver
## About
The Rubics name is intentional.
### Cube
This is an assignment work written in python, representing a 2x2x2 Rubik's cube. It has 6 sides with 24 faces on 8 "cubie".

We imagine the cube based on the cubies. From front to back, up to down and left to right.
We also pair color combinations to the faces of the cubies. (since a cubie has 3 faces on a 2x2x2 cube)
Let's suppose our first cubie, which is the 0th cubie = flu

We determine it's color to rgw. That means from the front, my upper left face is RED. The left side of it is GREEN and the upper face is WHITE.

### Permutation
Permutations are represented as a list of length n-1.  p[i] = j means that p maps i to j. (position)

When operating on a list c (a list of length 24 of colors)

p * c is the rearranged list of colors:

(p * c)[i] = c[p[i]]    for all i

Thus, p[i] is the location of where the color of position it will come from:

p[i] = j means the color at position j moves to position i.

## Requirements
Python3

## License
GPL-2.0-or-later

## Author
Fülöp Bence <fulopbencus@gmail.com>
