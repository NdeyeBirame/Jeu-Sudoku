import pygame, sys
from random import*
from numpy import*
from math import*

#---------Resolution d'une grille de sudoku--------------

#cette variable "nombre" saisie par l'utilisateur au clavier reprensente la taille de la grille.
#Mais pour l'interface graphique on fixe sa valeur à 9, elle est donc bénéfique seulement pour générer et résoudre des grilles de taille autre que 9

"""nombre=int(input("Entrez la taille qui doit avoir une racine carrée axacte "))
"""
nombre=9

#pour réaliser l'interface
def premiere_case_vide(grille):
    # Trouver la première case vide dans la grille
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j] == 0:
                return i, j
    return None, None  # S'il n'y a pas de case vide, retourne None


def affectationPossible(grille, valeur, ligne, colonne):
    # Vérifie si le numéro peut être placé dans la case sans violer les règles du Sudoku
    # Vérification de la ligne
    for i in range(len(grille[0])):
        if grille[ligne][i] == valeur:
            return False

    # Vérification de la colonne
    for i in range(len(grille)):
        if grille[i][colonne] == valeur:
            return False

    # Vérification de la sous-grille
    debut_ligne = (ligne // int(sqrt(len(grille)))) * int(sqrt(len(grille)))
    debut_colonne = (colonne // int(sqrt(len(grille)))) * int(sqrt(len(grille)))
    for i in range(int(sqrt(len(grille)))):
        for j in range(int(sqrt(len(grille)))):
            if grille[debut_ligne + i][debut_colonne + j] == valeur:
                return False

    return True
def afficheGrille(grille):   #permet d'afficher un  tableau à deux dimensions
    for i in range(0,len(grille)):
        for j in range(0,len(grille[0])):
            print(grille[i][j],end="  ")
        print()

def resoudre_sudoku(grille):       #trouve une solution d'une grille donnée
    a, b= premiere_case_vide(grille)
    if a is None:
        return True       # La grille est résolue

    for i in range(1, len(grille)+1):
        if affectationPossible(grille, i, a, b):
            grille[a][b] = i

            if resoudre_sudoku(grille):
                return True

            grille[a][b] = 0

    return False  # Aucune solution trouvée

#verifie si une grille donnée est remplie selon les régles de sudoku
def verificationDeLaGrille(tab):
    for i in range(0,len(tab)):
        for j in range(0,len(tab[0])):
            for k in range(0,len(tab[0])):
                if tab[i][k]==tab[i][j] and j!=k:
                    return False
            for k in range(0,len(tab)):
                if tab[k][j]==tab[i][j] and i!=k:
                    return False
            debut_ligne = (i // int(sqrt(len(tab)))) * int(sqrt(len(tab)))
            debut_colonne = (j // int(sqrt(len(tab)))) * int(sqrt(len(tab)))
            for l in range(int(sqrt(len(tab)))):
                for n in range(int(sqrt(len(tab)))):
                    if tab[debut_ligne + l][debut_colonne + n] == tab[i][j] and debut_ligne+l!=i and debut_colonne+n!=j:
                        return False
    return True

#permet de copier une matrice sur une autre sans changer la premiére matrice si on change la deuxiéme
def copier_Matrice(grille1,grille2):
    for i in range(0,len(grille1)):
        for j in range(0,len(grille1[0])):
            grille2[i][j]=grille1[i][j]
def remplir_grille(grille,num):  #on pré-remplie quelques cases d'une grille vide pour générer des grilles différentes
    for i in range(0,num+1):
        a = randint(0, len(grille) - 1)
        b = randint(0, len(grille) - 1)
        while grille[a][b] != 0:
            a = randint(0, len(grille) - 1)
            b = randint(0, len(grille) - 1)
        valeur:int=randint(1,len(grille))
        while affectationPossible(grille,valeur,a,b)==False:
            valeur=randint(1,len(grille))
        grille[a][b]=valeur

def generer_grille(grille,nbCaseCouvert):    #on génére pour le joueur une grille à partir d'une grille solution pour être sûr d'avoir une solution
    for i in range(0,nbCaseCouvert+1):
        a = randint(0, len(grille) - 1)
        b = randint(0, len(grille) - 1)
        while grille[a][b] == 0:
            a = randint(0, len(grille) - 1)
            b = randint(0, len(grille) - 1)
        grille[a][b]=0

#Variables globales pour la résolution
grille=zeros((nombre,nombre),int)
grid=zeros((nombre,nombre),int)


#--------------------Interface graphique-----------------

pygame.init()

# definition des tailles, couleurs et police d ecriture
color_facile = (0, 0, 0)
color_moyen = (0, 0, 0)
color_difficile = (0, 0, 0)
color_diabolique = (0, 0, 0)
taille_ecran_menu = [800 * 0.66, 800 * 0.66]
taille_ecran_menu_difficulte = [800 * 0.66, 800 * 0.66]
taille_ecran_sudoku = [800 * 0.66, 800 * 0.66]
taille_sudoku = [600 * 0.66, 600 * 0.66]
background_color = (200,200,200)
background_color_selection = (0, 58, 58)
taille_police = int(65 * 0.66)
taille_police_titre = int(80 * 0.66)
taille_police_button = int(25 * 0.66)
taille_police_chiffre = int(60 * 0.66)
taille_police_copyright = int(30 * 0.66)
police_ecriture_menu = pygame.font.SysFont('Didot', taille_police)
police_ecriture_copyright = pygame.font.SysFont('Comic sans ms', taille_police_copyright)
police_ecriture_sudoku = pygame.font.SysFont('Comic sans ms', taille_police_titre)
police_ecriture_button = pygame.font.SysFont('Comic sans ms', taille_police_button)
police_ecriture_chiffre = pygame.font.SysFont('Didot', taille_police_chiffre)
violet = (110, 5, 255)
noir = (0, 0, 0)
blanc = (255, 255, 255)
color_jouer = (80, 80, 150, 80)
rouge = (255, 0, 0)
blue = (0, 0, 255)
vert = (0, 255, 0)
rouge_clair = (255, 100, 100)
gris_clair = (200, 200, 200)
jaune_orange = (255, 127, 0)
jaune = (255, 255, 120)
rouge_fonce=(255,0,0)


# definition des differentes classes et de quelques fonctions utiles pour la création de leur définition

class Interface:
    def __init__(self, taille_ecran_menu, police_ecriture_menu, background_color):  # Constructeur de la classe
        self.ecran = pygame.display.set_mode(taille_ecran_menu)
        self.police_ecriture_menu = police_ecriture_menu
        self.background_color = background_color
        self.ecran.fill(background_color)


class Menu(Interface):

    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_jouer,
                 color_quitter):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_jouer = color_jouer
        self.color_quitter = color_quitter
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, noir)
        self.ecran.blit(value, (220 * 0.66, 50 * 0.66))
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, jaune)
        self.ecran.blit(value, (230 * 0.66, 50 * 0.66))

        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu[1] // 2 - 100, 200 * 0.66, 300 * 0.66, 100 * 0.66],0)
        pygame.draw.ellipse(self.ecran, violet, [taille_ecran_menu[1] // 2 - 100, 350 * 0.66, 300 * 0.66, 100 * 0.66],0)
        value = police_ecriture_menu.render(str("Jouer"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 80 * 0.66 - 100, 225 * 0.66))
        value = police_ecriture_menu.render(str("Jouer"), True, self.color_jouer)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 85 * 0.66 - 100, 225 * 0.66 + 3))

        value = police_ecriture_menu.render(str("Quitter"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65 * 0.66 - 100, 375 * 0.66))
        value = police_ecriture_menu.render(str("Quitter"), True, self.color_quitter)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70 * 0.66 - 100, 375 * 0.66 + 3))
        value = police_ecriture_copyright.render(str("Ndeye Birame DIA & Sokhna Laye GADIAGA"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 - 303 * 0.66, taille_ecran_menu[0] - 50))
        value = police_ecriture_copyright.render(str("Ndeye Birame DIA & Sokhna Laye GADIAGA"), True, blue)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 - 300 * 0.66, taille_ecran_menu[0] - 50))
        # rectangle du bouton "Jouer"
        self.rect_jouer = pygame.Rect(taille_ecran_menu[1] // 2 - 100, 200 * 0.66, 300 * 0.66, 100 * 0.66)
        self.rect_quitter = pygame.Rect(taille_ecran_menu[1] // 2 - 100, 350 * 0.66, 300 * 0.66, 100 * 0.66)

    def handle_events(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rect_jouer.collidepoint(event.pos):
                            menu_diff = Menu_difficulte(taille_ecran_menu, police_ecriture_menu,
                                                              police_ecriture_sudoku, background_color, color_facile,
                                                              color_moyen, color_difficile, color_diabolique)
                            menu_diff.handle_events()
                        elif self.rect_quitter.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                pygame.display.flip()


class Menu_difficulte(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_facile,
                 color_moyen, color_difficile, color_diabolique):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_facile = color_facile
        self.color_moyen = color_moyen
        self.color_difficile = color_difficile
        self.color_diabolique = color_diabolique
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, noir)
        self.ecran.blit(value, (220 * 0.66, 50 * 0.66))
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, jaune)
        self.ecran.blit(value, (230 * 0.66, 50 * 0.66))
        pygame.draw.ellipse(self.ecran, violet,[taille_ecran_menu_difficulte[1] / 3.2, 200 * 0.66, 300 * 0.66, 100 * 0.66], 0)
        pygame.draw.ellipse(self.ecran, violet,[taille_ecran_menu_difficulte[1] / 3.2, 350 * 0.66, 300 * 0.66, 100 * 0.66], 0)
        pygame.draw.ellipse(self.ecran, violet,[taille_ecran_menu_difficulte[1] / 3.2, 500 * 0.66, 300 * 0.66, 100 * 0.66], 0)
        pygame.draw.ellipse(self.ecran, violet,[taille_ecran_menu_difficulte[1] / 3.2, 650 * 0.66, 300 * 0.66, 100 * 0.66], 0)

        value = police_ecriture_menu.render(str("Facile"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80 * 0.66, 225 * 0.66))
        value = police_ecriture_menu.render(str("Facile"), True, self.color_facile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85 * 0.66, 225 * 0.66 + 3))

        value = police_ecriture_menu.render(str("Moyen"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80 * 0.66, 375 * 0.66))
        value = police_ecriture_menu.render(str("Moyen"), True, self.color_moyen)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85 * 0.66, 375 * 0.66 + 3))

        value = police_ecriture_menu.render(str("Difficile"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 65 * 0.66, 525 * 0.66))
        value = police_ecriture_menu.render(str("Difficile"), True, self.color_difficile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 70 * 0.66, 525 * 0.66 + 3))

        value = police_ecriture_menu.render(str("Diabolique"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 30 * 0.66, 675 * 0.66))
        value = police_ecriture_menu.render(str("Diabolique"), True, self.color_diabolique)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + +35 * 0.66, 675 * 0.66 + 3))

        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100 * 0.66, taille_ecran_sudoku[1] - 30 * 0.66, 100 * 0.66, 30 * 0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 95 * 0.66, taille_ecran_sudoku[1] - 35 * 0.66))

        self.rect_Facile = pygame.Rect(taille_ecran_menu_difficulte[1] / 3.2, 200 * 0.66, 300 * 0.66, 100 * 0.66)
        self.rect_Moyen = pygame.Rect(taille_ecran_menu_difficulte[1] / 3.2, 350 * 0.66, 300 * 0.66, 100 * 0.66)
        self.rect_Difficile = pygame.Rect(taille_ecran_menu_difficulte[1] / 3.2, 500 * 0.66, 300 * 0.66, 100 * 0.66)
        self.rect_Diabolique=pygame.Rect(taille_ecran_menu_difficulte[1] / 3.2, 650 * 0.66, 300 * 0.66, 100 * 0.66)
        self.rect_Retour=pygame.Rect(taille_ecran_sudoku[0] - 100 * 0.66, taille_ecran_sudoku[1] - 30 * 0.66, 100 * 0.66, 30 * 0.66)




    def handle_events(self):
        running = True
        while running:
            global grille, grid
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rect_Facile.collidepoint(event.pos):
                            remplir_grille(grille,9)
                            resoudre_sudoku(grille)
                            copier_Matrice(grille,grid)
                            generer_grille(grid,46)
                            main()
                        elif self.rect_Moyen.collidepoint(event.pos):
                            remplir_grille(grille, 9)
                            resoudre_sudoku(grille)
                            copier_Matrice(grille, grid)
                            generer_grille(grid, 49)
                            main()
                        elif self.rect_Difficile.collidepoint(event.pos):
                            remplir_grille(grille, 9)
                            resoudre_sudoku(grille)
                            copier_Matrice(grille, grid)
                            generer_grille(grid, 52)
                            main()
                        elif self.rect_Diabolique.collidepoint(event.pos):
                            remplir_grille(grille, 9)
                            resoudre_sudoku(grille)
                            copier_Matrice(grille, grid)
                            generer_grille(grid,55)
                            main()
                        elif self.rect_Retour.collidepoint(event.pos):
                            menu = Menu(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku,
                                        background_color, rouge, blue)
                            menu.handle_events()

                pygame.display.flip()


class Grid(Interface):

    board=grid
    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None
        self.win = win

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if affectationPossible(self.model, val,row,col):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)
        update_grid(grid,row,col,val)

    def draw(self):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True

class Cube(Interface):
    rows = 9
    cols = 9
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val




# Fonction pour mettre à jour la grille en fonction des entrées de l'utilisateur
def update_grid(tab,ligne, colonne, number):
    tab[ligne][colonne] = number

def redraw_window(win, board):
    win.fill((255,255,255))
    board.draw()

def redraw_window_Resutat1(win,board):
    win.fill((255,255,255))
    fnt = pygame.font.SysFont("arial", 20)
    text = fnt.render("Voici la solution! Malheureusement, vous n'y êtes pas arrivés !",1,rouge_fonce)
    win.blit(text,(150,560))
    board.draw()

def redraw_window_Resutat2(win,board):
    win.fill((255,255,255))
    fnt = pygame.font.SysFont("arial", 20)
    text = fnt.render("C'etait la grille à trouver! Bravo à vous !",1,rouge_fonce)
    win.blit(text,(200,560))
    board.draw()


#une classe simple trés utile pour creer des boutons facilement
class Button:         #permet de creer des boutons
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface,color):
        pygame.draw.rect(surface,color, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, mouse_pos):  #permet de savoir si le bouton est cliqué ou non
        return self.rect.collidepoint(mouse_pos)


#permet d'afficher la solution lorsque le joueur le demande
def afficherSolution():     #permet d'afficher la solution au joueur
    global grille,grid
    copier_Matrice(grille,grid)
    win = pygame.display.set_mode((550, 610))
    pygame.display.set_caption("Sudoku")
    copier_Matrice(grille,grid)
    board = Grid(9, 9, 540, 540, win)
    redraw_window(win, board)
    button = Button(300, 560, 110, 20, "Quitter")
    button1 = Button(150, 560, 110, 20, "Rejouer")
    button.draw(win, gris_clair)
    button1.draw(win,rouge_clair)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.is_clicked(event.pos):
                        pygame.quit()
                        sys.exit()
                    if button1.is_clicked(event.pos):
                        menu_di = Menu_difficulte(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku,
                                                   background_color, color_facile, color_moyen, color_difficile,
                                                   color_diabolique)
                        menu_di.handle_events()

        pygame.display.flip()


def afficheResultat1():    #permet de dire au joueur qu'il a échoué et de lui donner la solution final
    global grille, grid
    copier_Matrice(grille, grid)
    win = pygame.display.set_mode((550, 700))
    pygame.display.set_caption("Sudoku")
    copier_Matrice(grille, grid)
    board = Grid(9, 9, 540, 540, win)
    redraw_window_Resutat1(win,board)
    button = Button(220, 610, 110, 20, "Quitter")
    button.draw(win, blue)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.is_clicked(event.pos):
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()


def afficheResultat2():    #permet de dire au joueur qu'il a réussi et de lui donner la solution final
    global grille, grid
    copier_Matrice(grille, grid)
    win = pygame.display.set_mode((550, 700))
    pygame.display.set_caption("Sudoku")
    copier_Matrice(grille, grid)
    board = Grid(9, 9, 540, 540, win)
    redraw_window_Resutat2(win,board)
    button = Button(220, 610, 110, 20, "Quitter")
    button.draw(win, gris_clair)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.is_clicked(event.pos):
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()

#Une fonction essentielle; elle permet d'afficher au jouer une grille à resoudre.
#Elle lui permet aussi de jouer et d'obtenir la solution quand il veut.
def main():
    global grid,grille
    win = pygame.display.set_mode((550,610))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)
    key = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.is_finished():
                            print("Game over")

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None
                if button3.is_clicked(pos):
                    pygame.quit()
                    sys.exit()
                if button1.is_clicked(pos):
                    menu_dif = Menu_difficulte(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku,
                                                      background_color, color_facile, color_moyen, color_difficile,
                                                      color_diabolique)
                    menu_dif.handle_events()
                if button2.is_clicked(pos):
                    afficherSolution()
                if button4.is_clicked(pos):
                    afficheGrille(grille)
                    a,b=premiere_case_vide(grid)
                    print()
                    afficheGrille(grid)
                    if a==None:
                        if verificationDeLaGrille(grid):
                            afficheResultat2()
                        else:
                            afficheResultat1()
                    else:
                        print("Remplissez d'abord toutes les cases !")
        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board)
        button1 = Button(0, 560, 65, 20, "Retour")
        button2 = Button(150,560,90,20,"Resoudre")
        button3 = Button(460,560,90,20,"Quitter")
        button4 = Button(300,560,90,20,"Verifier")
        button1.draw(win, blue)
        button2.draw(win, rouge_clair)
        button3.draw(win, violet)
        button4.draw(win,jaune_orange)
        pygame.display.update()


#instanciation de la classe Menu
menu1 = Menu(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, rouge, blue)
menu1.handle_events()






