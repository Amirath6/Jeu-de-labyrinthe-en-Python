# Définition de la classe bille qui hérite de la classe pygame.sprite.Sprite
# Chaque sprite est une classe de base pour les objets de jeu visible

import pygame
class Bille():
	
	def __init__(self, x, y):
		
		# Appellation du constructeur de la classe "pygame.sprite.Sprite"
		
		pygame.sprite.Sprite.__init__(self)
		
		# Sprite doit posséder au moins deux attributs 'self.image' et 'self.rect'
		# Self.rect est le rectangle ou il faudra dessiner l'image
		# Documentation de l'object/classe : image de pygame : https://www.pygame.org/docs/ref/image.html
		# Charge l'image et retourne un objet Surface dans la variable 'image'
		# self.image est donc te type Surface
		self.image = pygame.image.load("ball.jpeg")
		
		# Initialisation de self.rect a la taille de self.image 
		# self.image est donc te type Surface
		# Etant de type Surface voici la documentation de l'objet Surface
		# https://www.pygame.org/docs/ref/surface.html
		
		self.rect = self.image.get_rect()
		self.rect = self.rect.move(x, y)
		
		#Attributs specifique aux balls permettants de garder en mémoire leur direction et leur vitesse
		self.dx, self.dy, self.v = 1, 1, 1
		
		# La méthode appelée  pour vérifier que la balle est toujours dans la fenêtre graphique  
	def update(self):
		self.dx, self.dy, self.v = 1, 1, 1
		# Modification du  rectangle d'affichage de la balle en fonction de sa direction (dx, dy) et de sa vitesse.
		self.rect=self.rect.move(self.dx * self.v, self.dy * self.v)
		#self.rect.move = (self.dx * self.v, self.dy * self.v)
		
		#Déplacement de la bille
		
	def deplacement(self):
		#On déplace la bille
		self.rect = self.rect.move(self.dx, self.dy)
			
