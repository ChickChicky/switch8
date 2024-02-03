# Switch 8 Solver

A relative of mine recenty got a small puzzle game. You have a small block of wood with 9 holes in line bored into it, and 8 pegs, half of them are green, the others are yellow. All the pegs of each color are all put on either side of the 'board'. The goal is to switch the positions of all the green pegs with the yellow ones. However, pegs can only be moved towards the side opposite to the one they started from, and they can either move 1 spot, or jump over a single peg.

Of course I really got inspired to make a program to solve it, and it's actually not that complicated !

*(The code really lacks of comments, so I'll add them in a future update.)*

# Quick start

* Install [Python](https://www.python.org/downloads/)
* Run `python3 solver.py` inside the folder where you downloaded the project
* (or double-click the file if it got associated)

You can also modify the two first lines with `board: ... = ...` and `target: ... = ...`. That way, you can change the initial position as well as the target position.