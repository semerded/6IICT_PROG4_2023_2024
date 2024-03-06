import random

class Speler:
    def __init__(self, naam, level, score):
        self.naam  = naam
        self.level = level
        self.score = score

    def level_up(self):
        self.level += 1
        print(f"{self.naam} is level {self.level} geworden.")

    def info(self):
        print(f"{self.naam} (lvl {self.level}): score {self.score}.")

    def verhoog_score(self, punten: 'int'):
        if not isinstance(punten, int):
            print(f"'verhoog_score' vereist int, niet {type(punten)}.")
            return
        self.score += punten

class Spel:
    def __init__(self, naam):
        self.naam = naam
        self.spelers = []

    def speler_toevoegen(self, speler: 'Speler'):
        if not isinstance(speler, Speler):
            print(f"'speler_toevoegen vereist Speler, niet {type(speler)}")
            return
        self.spelers.append(speler)
        print(f"{speler.naam} doet mee aan {self.naam}.")

    def scorebord(self):
        print(f"Huidige scores van spelers in {self.naam}…")
        for speler in self.spelers:
            speler.info()

    def spelen(self):
        levels = [speler.level for speler in self.spelers]
        max_level = max(levels)

        indexen = [index for index, level in enumerate(levels) if level == max_level]
        index = random.choice(indexen)
        speler = self.spelers[index]
        speler.verhoog_score(100)
        print(f"{speler.naam} is gewonnen.")
