class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=40):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

eleve1 = Eleve(age=15)
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.affichageAge()

professeur1 = Professeur(matiereEnseignee="Mathématiques", age=40)
professeur1.bonjour()
professeur1.enseigner()