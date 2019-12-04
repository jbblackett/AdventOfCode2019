#!/usr/bin/env python3


with open("input.txt", "r") as file:
	def crawl_wire():
		loc = [0, 0]

		for move in file.readline().split(","):
			delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]

			for _ in range(int(move[1:])):
				loc[delta[0]] += delta[1]
				yield tuple(loc)

	visited = set(crawl_wire())
	closest = min(abs(loc[0]) + abs(loc[1]) for loc in crawl_wire() if loc in visited)

	print(closest)
