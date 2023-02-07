import pygame
import random
import generateur 
from labyrinthe3 import Labyrinthe

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
GRAY=(50, 50, 50)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW=(255, 255, 0)

# La fonction pour le texte du menue pour le jeu
def text_format(message, textFont, tailleText, textColor):
	newFont=pygame.font.Font(textFont, tailleText)
	newText=newFont.render(message, 0, textColor)
	return newText					
	# La fonction d'affichage du menue
def afficher_menu(fenetre):
	menu=True
	selected="Facile"
	font = None
	
	FPS = 30
	screen_width = fenetre.get_width()
	screen_height = fenetre.get_height()

	while menu:
		
		# Traitement des évènements
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_UP:
					selected="Facile"
				elif event.key==pygame.K_DOWN:
					selected="Difficile"
				if event.key==pygame.K_RETURN:
					menu = False
					

		# Main Menu Commencement du Jeu
		fenetre.fill(BLUE)
		title=text_format("Bienvenue dans le labyrinthe", font, 80, YELLOW)
		if selected=="Facile":
			text_start=text_format("Facile", font, 75,WHITE)
		else:
			text_start = text_format("Facile", font, 75, BLACK)
		if selected=="Difficile":
			text_quit=text_format("Difficile", font, 75, WHITE)
		else:
			text_quit = text_format("Difficile", font, 75, BLACK)

		title_rect=title.get_rect()
		start_rect=text_start.get_rect()
		quit_rect=text_quit.get_rect()

		# Main Menu Text
		fenetre.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
		fenetre.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
		fenetre.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
		pygame.display.update()
		pygame.time.Clock().tick(FPS)
		pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
		
		# Remplissage de l'écran
	fenetre.fill(BLACK)
	return selected
	
# la condition qui est utilisée pour développer un module pouvant à la fois être exécuté directement mais aussi être importé par un autre module pour apporter ses fonctions
if __name__ == "__main__":
	# Initialisation
	pygame.init()
	pygame.mixer.quit()
	while True:
		#https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
		fenetre = pygame.display.set_mode((800, 600))

			
		#Initialisation du jeu

		difficulte = afficher_menu(fenetre)
		if difficulte == "Facile":
			fenetre = pygame.display.set_mode((111, 111))
			largeur = 11
			hauteur = 11
		else:
			fenetre = pygame.display.set_mode((711,711))
			largeur = 71
			hauteur = 71	
		grille = generateur.generer(largeur, hauteur)
		laby = Labyrinthe(largeur, hauteur, grille, fenetre)
		laby.initPositionBille()
		laby.initPositionArrivee()


		while not laby.fini():
			laby.afficherPygame()
			pygame.time.wait(50)
			#Itération pour la gestion des événements
			for event in pygame.event.get():
				# Verifie si une touche du clavier a été appuyé
				# Si event.type == pygame.KEYDOWN: alors une touche du clavier a été appuyé
				if event.type == pygame.KEYDOWN:
					# Quelle touche a été appuyée,
					# le code de la touche est dans event.key 
					# les differentes valeurs sont dans https://www.pygame.org/docs/ref/key.html#pygame.key
						
					if event.key == pygame.K_RIGHT:
						print('touche RIGHT')
						laby.moveRight()
					if event.key == pygame.K_LEFT:
						laby.moveLeft()
						print('touche LEFT')                                        
					if event.key == pygame.K_UP:
						laby.moveUp()
						print('touche UP')                        
					if event.key == pygame.K_DOWN:
						laby.moveDown()
						print('touche DOWN')
					pygame.display.update()
		
		# Remplissage aléatoire de l'écran	
		fenetre = pygame.display.set_mode((800, 600))
		fenetre.fill(RED)
		text_gagnant = text_format("Vous avez gagné le jeu", None, 100, YELLOW)
		fenetre.blit(text_gagnant, (800/100 - (text_gagnant.get_rect()[2]/1400), 300))
		pygame.display.update()
		pygame.time.wait(5000)
		
		
