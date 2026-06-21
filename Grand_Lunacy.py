"""
Grand Lunacy - Prototype
A text-based RPG prototype inspired by hidden attributes, talents, traits,
skills, insight, bestiary knowledge, and species-based monsters.

Run:
    python grand_lunacy.py
"""

from dataclasses import dataclass, field
import random

GRADES = [
    ("S", 160),
    ("A", 80),
    ("B", 40),
    ("C", 20),
    ("D", 10),
    ("E", 5),
    ("F", 0),
]

def grade(value: float) -> str:
    for g, threshold in GRADES:
        if value >= threshold:
            return g
    return "F"

@dataclass
class AttributeSet:
    strength: float
    agility: float
    vitality: float
    intelligence: float
    willpower: float
    charisma: float
    luck: float

    def visible(self):
        return {
            "STR": grade(self.strength),
            "AGI": grade(self.agility),
            "VIT": grade(self.vitality),
            "INT": grade(self.intelligence),
            "WIL": grade(self.willpower),
            "CHA": grade(self.charisma),
            "LUK": grade(self.luck),
        }

@dataclass
class Talent:
    name: str
    description: str

@dataclass
class Trait:
    name: str
    description: str

@dataclass
class Skill:
    name: str
    proficiency: float = 0.0

@dataclass
class Species:
    name: str
    baseline: AttributeSet
    notes: str = ""

@dataclass
class Monster:
    species: Species
    mutant: bool = False
    boss: bool = False

    @property
    def attrs(self):
        return self.species.baseline

@dataclass
class Player:
    name: str
    attrs: AttributeSet
    talents: list = field(default_factory=list)
    traits: list = field(default_factory=list)
    skills: dict = field(default_factory=dict)
    insight: float = 0.0
    encyclopedia: set = field(default_factory=set)
    encounter_data: dict = field(default_factory=dict)

    def train_running(self):
        self.attrs.agility += 0.1
        self.attrs.vitality += 0.1

    def analyze(self, monster):
        species = monster.species.name

        if self.insight >= 50:
            return monster.attrs.visible()

        count = self.encounter_data.get(species, 0)

        if species in self.encyclopedia:
            count += 3

        if count <= 0:
            return {"STR": "?", "AGI": "?", "VIT": "?"}
        elif count <= 2:
            return {
                "STR": grade(monster.attrs.strength),
                "AGI": "?",
                "VIT": "?"
            }
        else:
            return {
                "STR": grade(monster.attrs.strength),
                "AGI": grade(monster.attrs.agility),
                "VIT": grade(monster.attrs.vitality)
            }

    def fight(self, monster):
        species = monster.species.name
        self.encounter_data[species] = self.encounter_data.get(species, 0) + 1

        sword = self.skills.get("Swordsmanship", Skill("Swordsmanship"))

        power = self.attrs.strength + sword.proficiency
        enemy = monster.attrs.strength + monster.attrs.vitality

        print(f"\nYou engage a {species}!")

        if power >= enemy:
            print("Victory!")
            sword.proficiency += 0.5
            self.skills["Swordsmanship"] = sword
        else:
            print("Defeat... but you learned something.")
            sword.proficiency += 0.2
            self.skills["Swordsmanship"] = sword

def create_world():
    goblin = Species(
        "Goblin",
        AttributeSet(
            strength=3,
            agility=11,
            vitality=4,
            intelligence=2,
            willpower=2,
            charisma=1,
            luck=2
        ),
        notes="Cowardly pack creature."
    )

    wolf = Species(
        "Wolf",
        AttributeSet(
            strength=12,
            agility=18,
            vitality=10,
            intelligence=3,
            willpower=4,
            charisma=1,
            luck=3
        )
    )

    return [Monster(goblin), Monster(wolf)]

def main():
    player = Player(
        name="Adventurer",
        attrs=AttributeSet(
            strength=15,
            agility=12,
            vitality=12,
            intelligence=8,
            willpower=9,
            charisma=6,
            luck=5
        ),
        talents=[Talent("Sword Genius", "Learns sword skills rapidly.")],
        traits=[Trait("Obsessive", "Improves through repetition.")],
        skills={"Swordsmanship": Skill("Swordsmanship", 5.0)}
    )

    monsters = create_world()

    print("=== GRAND LUNACY ===")

    while True:
        print("\n1. Train Running")
        print("2. Read Monster Encyclopedia (Goblin)")
        print("3. Inspect Monster")
        print("4. Fight Monster")
        print("5. View Character")
        print("0. Quit")

        choice = input("> ")

        if choice == "1":
            player.train_running()
            print("You trained. AGI and VIT increased slightly.")

        elif choice == "2":
            player.encyclopedia.add("Goblin")
            print("Goblin entry learned.")

        elif choice == "3":
            monster = random.choice(monsters)
            print(f"\nTarget: {monster.species.name}")
            print(player.analyze(monster))

        elif choice == "4":
            monster = random.choice(monsters)
            player.fight(monster)

        elif choice == "5":
            print("\nVisible Attribute Grades")
            print(player.attrs.visible())
            print("Skills:")
            for s in player.skills.values():
                print(f" - {s.name}: {s.proficiency:.1f}%")

        elif choice == "0":
            break

if __name__ == "__main__":
    main()
