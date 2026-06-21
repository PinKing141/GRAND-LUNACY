"""Game assembly and command-line loop."""

from __future__ import annotations

import random

from .attributes import AttributeSet
from .characters import Player
from .combat import fight
from .knowledge import analyze, read_encyclopedia
from .potential import PotentialSet
from .skills import Skill, Talent, Trait
from .training import recover, train
from .world import create_world


def create_player() -> Player:
    return Player(
        name="Adventurer",
        attrs=AttributeSet(15, 12, 12, 8, 9, 6, 5),
        potential=PotentialSet.from_rank("D", agility="C", willpower="C", luck="E"),
        talents=[Talent("Sword Genius", "Learns sword skills rapidly.", multiplier=1.8)],
        traits=[Trait("Obsessive", "Improves through repetition.")],
        skills={"Swordsmanship": Skill("Swordsmanship", 5.0)},
    )


def main() -> None:
    player = create_player()
    monsters = create_world()
    print("=== GRAND LUNACY ===")
    while True:
        print("\n1. Train Running\n2. Sword Sparring\n3. Rest\n4. Read Monster Encyclopedia (Goblin)\n5. Inspect Monster\n6. Fight Monster\n7. View Character\n0. Quit")
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
            for skill in player.skills.values():
                print(f" - {skill.name}: {skill.proficiency:.1f}%")
        elif choice == "0":
            break
