class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque:", self.marque)
        print("Annee:", self.annee)
        print("Prix:", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Modele:", self.modele)
        print("Nombre de portes:", self.portes)

    def demarrer(self):
        print("Attention, je roule en voiture !")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Modele:", self.modele)
        print("Nombre de roues:", self.roue)

    def demarrer(self):
        print("Attention, je roule en moto !")


# instanciation de l'objet voiture et appel de la méthode informationsVehicule
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()

# instanciation de l'objet moto et appel de la méthode informationsVehicule
moto = Moto("Yamaha", "1200 VMAX", 1987, 4500)
moto.informationsVehicule()

# démarrage de la voiture et de la moto
voiture.demarrer()
moto.demarrer()