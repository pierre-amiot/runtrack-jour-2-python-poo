import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __repr__(self):
        return "{} de {}".format(self.valeur, self.couleur)

class Jeu:
    def __init__(self):
        self.paquet = []
        for valeur in range(2, 11):
            for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
                self.paquet.append(Carte(valeur, couleur))
        for valeur in ["Valet", "Dame", "Roi"]:
            for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
                self.paquet.append(Carte(valeur, couleur))
        for couleur in ["Coeur", "Carreau", "Pique", "Trèfle"]:
            self.paquet.append(Carte("As", couleur))

    def melanger(self):
        random.shuffle(self.paquet)
    
    def donner_carte(self):
        return self.paquet.pop()

    def nouvelle_partie(self):
        self.melanger()
        self.croupier_main = [self.donner_carte(), self.donner_carte()]
        self.joueur_main = [self.donner_carte(), self.donner_carte()]

    def calculer_total(self, main):
        total = 0
        as_count = 0
        for carte in main:
            if isinstance(carte.valeur, int):
                total += carte.valeur
            elif carte.valeur == "As":
                as_count += 1
                total += 11
            else:
                total += 10
        while as_count > 0 and total > 21:
            total -= 10
            as_count -= 1
        return total

    def joueur_tirer_carte(self):
        self.joueur_main.append(self.donner_carte())

    def croupier_jouer(self):
        while self.calculer_total(self.croupier_main) < 17:
            self.croupier_main.append(self.donner_carte())

    def jouer(self):
        self.nouvelle_partie()
        while True:
            print("La main du joueur est :")
            for carte in self.joueur_main:
                print(carte)
            choix = input("Voulez-vous tirer une carte ? (o/n) : ")
            if choix == "o":
                self.joueur_tirer_carte()
                if self.calculer_total(self.joueur_main) > 21:
                    print("La main du joueur est :")
                    for carte in self.joueur_main:
                        print(carte)
                    print("Le joueur a dépassé 21, le croupier gagne.")
                    return
            else:
                break
        self.croupier_jouer()
        joueur_total = self.calculer_total(self.joueur_main)
        croupier_total = self.calculer_total(self.croupier_main)
        print("La main du joueur est :")
        for carte in self.joueur_main:
            print(carte)
        print("La main du croupier est :")
        for carte in self.croupier_main:
            print(carte)
        if croupier_total > 21:
            print("Le croupier a dépassé 21, le joueur gagne.")
        