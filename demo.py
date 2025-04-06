from random import *
##from pygame import *

# bonne dim 30x30

def plateau():
    '''fonction qui définit le plateau de jeu (qui évolue
    au fur et à mesure de la partie)'''

    p = [[a]*y] ## 1ère et dernière ligne du plateau
    for i in range(aire):
        p.append(liste())
    p.append([a]*y)

    return p

def liste():
    '''fonction qui définie selon l'aire les lignes principales du plateau'''

    l = [a2]
    for i in range(aire):
        l.append(b)
    l.append(a2)
    return l


def affichage(): ## la liste de listes qui constitue le plateau en paramètre
    '''fonction d'affichage du plateau de jeu'''
    for i in range(y):
        ch = " ".join(p[i])
        print(ch)


def editing(x,y,v): ## paramètres ligne(x) , colonne(y)
    p[x][y] = v


def player_coords(player):
    ''' fonction qui permet de trouver les coordonnées d'un joueur donné'''
    a = 1
    b = 1
    v = "p"+str(player)

    while p[a][b] != v:
        if b < (aire +1):
            b = b+1
        else:
            b = 1
            a = a+1
    else:
        x1 = a ## x c'est la ligne
        y1 = b ## et y la colonne

    return (x1,y1)

def starter(player):
    '''fonction de modification du plateau qui implémente le starter
    d'un joueur donné'''
    v = "p"+str(player)
    x = 1
    if nb_player == 2: # mode duel
        if player == 1:
            y = 1
        else:
            y = aire
    else : # s'il y a plus de 2 joueurs (déconseillé)
        y = round(aire/(nb_player + 1))*player
    editing(x,y,v)


def u(player): ## up
    v = "p"+str(player)
    x,y = player_coords(player)
    if p[x-1][y] != b:
        game_over(player)
    else:
        editing(x,y,vt)
        editing(x-1,y,v)

def d(player): ## down
    v = "p"+str(player)
    x,y = player_coords(player)
    if p[x+1][y] != b:
        game_over(player)
    else:
        editing(x,y,vt)
        editing(x+1,y,v)

def r(player): ## right
    v = "p"+str(player)
    x,y = player_coords(player)
    if p[x][y+1] != b:
        game_over(player)
    else:
        editing(x,y,vt)
        editing(x,y+1,v)

def l(player): ## left
    v = "p"+str(player)
    x,y = player_coords(player)
    if p[x][y-1] != b:
        game_over(player)
    else:
        editing(x,y,vt)
        editing(x,y-1,v)


def game_over(player):
    '''fonction de fin de la partie qui reset également le plateau'''
    global p, score_bot, score_player ## besoin des variables globales pour modifier leur valeur
    print("GAME OVER")
    loser = player
    if loser == 1:
        winner = "Le bot"
        score_bot += 1
    else:
        winner = q2
        score_player += 1
    print(winner, "a gagné.")
    p = plateau() ## le plateau reprend sa valeur initiale, donc vierge



def bot():
    player = 2
    possibilities = []

    if p != comparatif:

        x,y = player_coords(player)

        ## on établie une liste des déplacements possibles
        if p[x-1][y] == b: ## déplacement vers le haut possible
            possibilities.append(0)
        if p[x+1][y] == b: ## déplacement vers le bas possible
            possibilities.append(1)
        if p[x][y+1] == b: ## déplacement vers la droite possible
            possibilities.append(2)
        if p[x][y-1] == b: ## déplacement vers la gauche possible
            possibilities.append(3)

        if len(possibilities) == 0: ## s'il n'y a aucune possibilité de déplacement
            u(player) ## on efectu un déplacement peu importe lequel,
            ## ce qui entraînera un game over
        else:
            a = possibilities[randint(0,len(possibilities)-1)]
            ## on tire un nombre dans la liste de possibilité précédemment définie
            ## chaque nombre tiré équivaut à un déplacement différent
            if a == 0:
                u(player)
            if a == 1:
                d(player)
            if a == 2:
                r(player)
            if a == 3:
                l(player)
        affichage() ## on affiche le tableau


def rules():
    '''cette fonction explique les règles du jeu à l'utilisateur'''
    print("Bonjour, voici le jeu tron. Les règles sont simples, "
    "il faut suivivre plus lontemps que son adversaire (ici un bot). ")
    print("Vous incarnerez le player 1, noté p1 sur la map. "
        "Pour vous déplacer, vous disposerez de 4 commandes:")
    print("z pour un movement vers le haut, s pour un vers le bas,")
    print("d et q pour la droite et la gauche"
    " (aussi connue sous le nom de zqsd). ")
    print("Si vous ne vous rappelez plus des règles. Vous pouvez faire /help"
    "et /ff pour capituler.")
    print('Si vous avez compris, entrer "ok" dans la console de commande'
        " et bon jeu à vous.")
    ok = input("Commande démandée: ").lower()
    while ok != "ok":
        ok = input("Commande démandée: ").lower()


aire = 20 ## dim du plateau (aire de jeu)
y = aire+2 ## borders (taille réelle du plateau)
a = "__" ## horizontal
a2 = " |" ## vertical
b = "  " ## symbole qui marque les cases vides
# "p1" = joueur 1

p = plateau()
comparatif = plateau() ## prend la valeur du plateau vierge, va permettre
## par la suite de pouvoir détecter si la fonction game_over a été utilisé ou
## non (évite aussi des bugs dans certaines fonction comme player_coords)

nb_player = 2 ## nombre total de joueurs

vt = " 3" ## valeur trainé


# Programme principal

for i in range(1,nb_player+1):
    starter(i)

rules()

q2 = input("Comment vous appelez-vous ?")
score_player = 0
score_bot = 0

affichage()
result = ("z","q","s","d","/ff","/help") ## liste des réponses possibles à q

while comparatif != p:
    player = 1
    q = input("Commande (z, q, s, d ou /help ou /ff) :").lower()
    while q not in result:
        q = input("Commande (z, q, s, d ou /help ou /ff) :").lower()
    if q == "z":
        u(player)
    if q == "s":
        d(player)
    if q == "d":
        r(player)
    if q == "q":
        l(player)
    if q == "/help":
        rules()
        affichage()
    if q == "/ff":
        game_over(player)
    bot()
    print("")

print(q2, ":", score_player, "| bot :",score_bot)


## permet de rejouer
q3 = input("Voulez-vous rejouer? (oui/non)").lower()


while q3 != "non":
    if q3 == "oui":

        for i in range(1,nb_player+1):
            starter(i)
        affichage()

        while comparatif != p:
            player = 1
            q = input("Commande (z, q, s, d ou /help ou /ff) :").lower()
            while q not in result:
                q = input("Commande (z, q, s, d ou /help ou /ff) :").lower()
            if q == "z":
                u(player)
            if q == "s":
                d(player)
            if q == "d":
                r(player)
            if q == "q":
                l(player)
            if q == "/help":
                rules()
                affichage()
            if q == "/ff":
                game_over(player)
            bot()
            print("")
        print(q2, ":", score_player, "| bot :",score_bot) ## tableau des scores
    q3 = input("Voulez-vous rejouer? (oui/non)").lower()

print("Fin du jeu.")