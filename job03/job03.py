class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


# instanciation de la classe Rectangle
rect = Rectangle(4, 3)
print(f"Le périmètre du rectangle est {rect.perimetre()}")
print(f"La surface du rectangle est {rect.surface()}")

# utilisation des accesseurs et mutateurs
rect.set_longueur(5)
rect.set_largeur(2)
print(f"Le périmètre du rectangle est maintenant {rect.perimetre()}")
print(f"La surface du rectangle est maintenant {rect.surface()}")

# instanciation de la classe Parallelepipede
paral = Parallelepipede(4, 3, 2)
print(f"Le volume du parallélépipède est {paral.volume()}")

# utilisation des accesseurs et mutateurs de la classe Parallelepipede
paral.set_longueur(5)
paral.set_largeur(2)
paral.set_hauteur(3)
print(f"Le volume du parallélépipède est maintenant {paral.volume()}")