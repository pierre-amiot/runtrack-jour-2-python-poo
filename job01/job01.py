class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print("Age:", self.age)
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, age):
        self.age = age
        
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans")
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
        
personne1 = Personne()
eleve1 = Eleve()

eleve1.affichageAge() # J'ai 14 ans
eleve1.bonjour() # Hello

