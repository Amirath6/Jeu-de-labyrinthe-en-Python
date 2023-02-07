import pygame
class Labyrinthe():
	
	# Définition du constructeur. Il est toujours présent.
	#Les attributs de la classe commencent par self.(+nom) de la variable.
	def __init__(self, largeur, hauteur, grille, fenetre):
		self.largeur = largeur
		self.hauteur = hauteur
		self.grille = grille
		self.fenetre = fenetre
		self.case_vide = pygame.transform.scale(pygame.image.load('cell.jpeg'), (int(self.fenetre.get_width() / self.largeur), int(self.fenetre.get_height() / self.hauteur)))
		self.mur = pygame.transform.scale(pygame.image.load('wall.webp'), (int(self.fenetre.get_width() / self.largeur), int(self.fenetre.get_height() / self.hauteur)))
		self.bille = pygame.transform.scale(pygame.image.load('ball.jpeg'), (int(self.fenetre.get_width() / self.largeur), int(self.fenetre.get_height() / self.hauteur)))
		self.arrivee = pygame.transform.scale(pygame.image.load('arrivee.webp'), (int(self.fenetre.get_width() / self.largeur), int(self.fenetre.get_height() / self.hauteur)))
	# La fonction pour initialiser la position de la bille.
	def initPositionBille(self):
		for y in range(self.hauteur):
			for x in range(self.largeur):
				if self.grille[x][y] == 0:
					self.posX = x
					self.posY = y
					self.grille[x][y] = 2
					return None
	
	# La fonction pour initialiser la position de l'arrivée.				
	def initPositionArrivee(self):
		for y in reversed(range(self.hauteur)):
			for x in reversed(range(self.largeur)):
				if self.grille[x][y] == 0:
					self.posArriveeX = x
					self.posArriveeY = y
					self.grille[x][y] = 3
					return None
	# Finir le jeu si la bille est venu au point d'arrivée				
	def fini(self):
		print(self.posX, self.posY)
		print(self.posArriveeX, self.posArriveeY)
		return self.posX == self.posArriveeX and self.posY == self.posArriveeY
		
						

	#On définit une fonction "afficher console" genre une table étroite destinée à porter des objets décoratifs.
	def afficherConsole(self):
		for y in range(self.hauteur):
			for x in range(self.largeur):
				if self.grille[x][y] == 1:
					print('#', end == ' ')
				elif self.grille[x][y] == 2:
					print('€', end == ' ')
				elif self.grille[x][y] == 3:
					print('$', end == ' ')
				else:
					print(' ', end == ' ')			
				
		print()
		
	# On définit une fonction une fonction "afficher pygame" afin d'associer les images à certaines conditions		
	def afficherPygame(self):
		for y in range(self.hauteur):
			for x in range(self.largeur):
				if self.grille[x][y] == 1:
					#Afficher un mur
					self.fenetre.blit(self.mur, (x*10, y*10))
				elif self.grille[x][y] == 0:
					#Affiche une case vide
					self.fenetre.blit(self.case_vide, (x*10, y*10))
				elif self.grille[x][y] == 2:
					#Afficher la bille
					self.fenetre.blit(self.bille, (x*10, y*10))
				elif self.grille[x][y] == 3:
					# Afficher l'arrivé
					self.fenetre.blit(self.arrivee, (x*10, y*10))	
		pygame.display.flip()
		
	# La fonction pour bouger la bille
	# Fonction pour déplacer la bille vers la droite
	def moveRight(self):
		# Verifier si le cellule existe (donc inférieur à la largeur de la grille ) et si elle est bien vide
		if self.posX+1 < self.largeur and (self.grille[self.posX+1][self.posY] == 0 or self.grille[self.posX+1][self.posY] == 3):
			self.grille[self.posX][self.posY] = 0
			self.grille[self.posX +1][self.posY] = 2
			self.posX = self.posX +1
			
	# Fonction pour déplacer la bille vers la gauche		
	def moveLeft(self):
		# Verifier si le cellule existe (donc supérieur ou égale à 0) et si elle est bien vide
		if self.posX-1 >=0  and (self.grille[self.posX-1][self.posY] == 0 or self.grille[self.posX-1][self.posY] == 3):
			self.grille[self.posX][self.posY] = 0
			self.grille[self.posX - 1][self.posY] = 2
			self.posX = self.posX - 1
			
	# La fonction pour bouger la bille vers le bas		
	def moveDown(self):
		# Verifier si le cellule existe (donc inférieur à la hauteur de la grille ) et si elle est bien vide
		if self.posY+1 < self.hauteur and (self.grille[self.posX][self.posY+1] == 0 or self.grille[self.posX][self.posY+1] == 3):
			self.grille[self.posX][self.posY] = 0
			self.grille[self.posX][self.posY + 1 ] = 2
			self.posY = self.posY + 1
			
	# La fonction pour bouger la bille vers le haut		
	def moveUp(self):
		# Verifier si le cellule existe (donc supérieur ou égale à 0 ) et si elle est bien vide
		if self.posY - 1 >= 0 and (self.grille[self.posX][self.posY-1] == 0 or self.grille[self.posX][self.posY-1] == 3):
			self.grille[self.posX][self.posY] = 0
			self.grille[self.posX][self.posY -1 ] = 2
			self.posY = self.posY - 1
			
	# Déplacement et changement de l'image		
	def update(self):
		self.bougerBille()
