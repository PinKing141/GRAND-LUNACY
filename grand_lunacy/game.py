"""Game assembly and command-line loop."""

from __future__ import annotations

import random

from .affinities import AffinityCategory, AffinitySet
from .attributes import AttributeSet
from .characters import Player
from .combat import fight
from .knowledge import analyze, read_encyclopedia
from .potential import PotentialSet
from .skills import Skill, Talent, TalentEffect, TalentRarity, Trait
from .training import recover, train
from .world import create_world


def create_player() -> Player:
    affinities = AffinitySet()
    affinities.set("Swordsmanship", AffinityCategory.WEAPON, "B")
    affinities.set("Sword Sparring", AffinityCategory.WEAPON, "B")
    affinities.set("Mana Control", AffinityCategory.MAGIC, "D")
    affinities.set("Acting", AffinityCategory.SOCIAL, "C")
    return Player(
        name="Adventurer",
        attrs=AttributeSet(15, 12, 12, 8, 9, 6, 5),
        potential=PotentialSet.from_rank("D", agility="C", willpower="C", luck="E"),
        talents=[Talent("Sword Genius", "Learns sword skills rapidly.", rarity=TalentRarity.RARE, discovered=False, effects=[TalentEffect("Swordsmanship", 3.0), TalentEffect("Sword Sparring", 1.2)], evolution="Blade Prodigy")],
        traits=[Trait("Obsessive", "Improves through repetition.")],
        skills={"Swordsmanship": Skill("Swordsmanship", 5.0), "Iron Wolf Style": Skill("Iron Wolf Style", 2.0, style="Sword")},
        affinities=affinities,
    )


def main() -> None:
    player = create_player()
    monsters = create_world()
    print("=== GRAND LUNACY ===")
    while True:
        print("\n1. Train Running\n2. Sword Sparring\n3. Rest\n4. Read Monster Encyclopedia (Goblin)\n5. Inspect Monster\n6. Fight Monster\n7. View Character\n8. Appraise Talents\n0. Quit")
        choice = input("> ")
        if choice == "1":
            print("\n".join(train(player, "running")))
        elif choice == "2":
            print("\n".join(train(player, "sword")))
        elif choice == "3":
            print(recover(player))
        elif choice == "4":
            print(read_encyclopedia(player, "Goblin"))
        elif choice == "5":
            monster = random.choice(monsters)
            print(f"\nTarget: {monster.name}")
            print(analyze(player, monster))
        elif choice == "6":
            print(fight(player, random.choice(monsters)).message)
        elif choice == "7":
            print("\nVisible Attribute Grades")
            print(player.visible_attributes())
            print(f"Fatigue: {player.fatigue:.0f}/100")
            print("Skills:")
            for name, visible in player.visible_skills().items():
                print(f" - {name}: {visible}")
            print("Known Talents:", player.visible_talents() or ["???"])
            print("Affinities:", player.affinities.visible())
        elif choice == "8":
            print(player.discover_talent("Sword Genius"))
        elif choice == "0":
            break
