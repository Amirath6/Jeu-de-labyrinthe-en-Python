#!/bin/env python3
#-*- coding:utf-8 -*-

import random
# Une fonction afficher qui prend en paramètre une grille, une largeur et un hateur.
# Cette fonction va nous permettre d'afficher une grille rempli de "#"
def afficher(grille, l, h):
	for y in range(h):
		for x in range(l):
			print('#' if grille[x][y] == 1 else ' ', end='')
		print()
		
# Une fonction qui nous permettre de générer la grille 
# Elle nous permettra de construire des grilles et des chemins
def generer(l, h):
	grille = [([0] * h) for c in range(l)]
	n = 2
	for x in range(l):
		for y in range(h):
			if y % 2 == 0:
				grille[x][y] = 1
			elif x % 2 == 0:
				grille[x][y] = 1
			else:
				grille[x][y] = n
				n += 1
	murs = [(x, y) for x in range(l) for y in range(h) if grille[x][y] == 1]
	chemins = {grille[x][y]: [(x, y)] for x in range(l) for y in range(h)
			   if grille[x][y] != 1}
	while len(chemins) > 1:
		im = random.randrange(len(murs))
		xm, ym = murs[im]
		droite = (xm+1, ym)
		gauche = (xm-1, ym)
		haut = (xm, ym+1)
		bas = (xm, ym-1)
		a_verifier = [(droite, gauche), (haut, bas)]
		random.shuffle(a_verifier)
		for (c1x, c1y), (c2x, c2y) in a_verifier:
			if 0 <= c1x < l and 0 <= c1y < h and \
			   0 <= c2x < l and 0 <= c2y < h:
				n1 = grille[c1x][c1y]
				n2 = grille[c2x][c2y]
				if n1 != 1 and n2 != 1 and n1 != n2:
					chemins[n1].append((xm, ym))
					chemins[n1].extend(chemins.pop(n2))
					murs.pop(im)
					for x, y in chemins[n1]:
						grille[x][y] = n1

					break

	for x in range(l):
		for y in range(h):
			if grille[x][y] != 1:
				grille[x][y] = 0
	return grille


#  la condition qui est utilisée pour développer le module pouvant à la fois être exécuté directement. 
if __name__ == '__main__':
	N = 51
	afficher(generer(N, N), N, N)

