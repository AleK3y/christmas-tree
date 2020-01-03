#!/usr/bin/python3
from colorama import init, Fore
from random import choice
import os

# Initialize colorama for Windows
if os.name.lower() == "nt":
	init()

def clear():
	os.system("cls") if os.name.lower() == "nt" else os.system("clear")

def sleep(ms):
	import time
	time.sleep(ms/1000)

# Tree ASCII
tree = """
         ╎
       - ● -
         Λ
        / \\
       /\\_ \\
      /   \\_\\
      /\\_ ● \\
     / ● \\__ \\
    /\\_     \\_\\
    /  \\__ ●  \\
   /  ●   \\__  \\
  /\\___   ●  \\__\\
  /    \\___  ●  \\
 /  ●   ●  \\___  \\
/─ˍˍ───ˍ─ˍ───ˍˍ\\__\\
        | |
      |-----|
       \\___/
""".split("\n")[1:-1]		# Filter out the first and the last \n

# List of colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.MAGENTA, Fore.WHITE]		# No black cuz xmas lmao :P

# List of balls positions
balls = []
for i in range(len(tree)):
	for j in range(len(tree[i])):
		if tree[i][j] == "●":
			balls.append([i, j])
del balls[0]		# Remove the start on the top

# List of light that'll change
lights = (
	(4, 8),
	(4, 9),

	(5, 10),
	(5, 11),
	
	(6, 7),
	(6, 8),

	(7, 9),
	(7, 10),
	(7, 11),

	(8, 12),
	(8, 13),

	(8, 5),
	(8, 6),

	(9, 7),
	(9, 8),
	(9, 9),

	(10, 10),
	(10, 11),
	(10, 12),

	(11, 13),
	(11, 14),
	(11, 15),

	(11, 3),
	(11, 4),
	(11, 5),
	(11, 6),

	(12, 7),
	(12, 8),
	(12, 9),
	(12, 10),

	(13, 11),
	(13, 12),
	(13, 13),
	(13, 14),

	(14, 15),
	(14, 16),
	(14, 17),
)

# Make a copy to reset the tree every cycle
originalTree = tree[:]

# Set balls colors before the main loop (no blue: too dark, and no yellow: already in the star)
ballsColors = []
for ball in balls:
	while True:
		currentColor = choice(colors[1:])

		if currentColor not in (Fore.YELLOW, Fore.RED):
			break
	ballsColors.append(currentColor)

# Counter to move the lights
lightOffset = 0
lightBounds = [0, colors.index(Fore.RED)+1]		# Colors array start and end (to skip colors, now using first 4 colors)
starLight = 0
try:
	while True:
		clear()

		# Split strings after the copy of the array [double array bug]
		tree = originalTree[:]
		for i in range(len(tree)):
			tree[i] = list(tree[i])

		# Change lights for the star
		if starLight >= 0 and starLight <= 2:
			tree[0][9] = Fore.YELLOW + tree[0][9] + Fore.RESET
			tree[1][7] = Fore.YELLOW + tree[1][7] + Fore.RESET
			tree[1][11] = Fore.YELLOW + tree[1][11] + Fore.RESET
		elif starLight >= 3 and starLight <= 5:
			tree[1][9] = Fore.YELLOW + tree[1][9] + Fore.RESET

		if starLight == 5:
			starLight = 0
		else:
			starLight += 1

		# Set the already decided colors for balls
		for i in range(len(balls)):
			tree[balls[i][0]][balls[i][1]] = ballsColors[i] + tree[balls[i][0]][balls[i][1]] + Fore.RESET

		# Sequentially color the lights
		for i in range(len(lights)):
			currentColor = colors[lightBounds[0]:lightBounds[1]][(lightOffset+i) % len(colors[lightBounds[0]:lightBounds[1]])]		# Pick an index of colors from chosen bounds based on offset (which goes back to 0 with % after surpassing array's length)
			tree[lights[i][0]][lights[i][1]] = currentColor + tree[lights[i][0]][lights[i][1]] + Fore.RESET

		# Print it
		for i in tree:
			print("\t" + "".join(i))

		lightOffset += 1
		sleep(500)

except KeyboardInterrupt:
	print("\n" + Fore.GREEN + "Merry " + Fore.RED + "Xmas" + Fore.RESET + "!")
