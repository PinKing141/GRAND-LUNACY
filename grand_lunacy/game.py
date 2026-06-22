"""Game assembly and command-line loop."""

from __future__ import annotations

import random

from .attributes import AttributeSet
from .characters import Player
from .combat import fight
from .knowledge import analyze, bestiary, read_encyclopedia
from .potential import PotentialSet
from .skills import BASIC_TALENTS, Skill, Trait
from .save_load import DEFAULT_SAVE_PATH, load_player, save_player
from .training import recover, train
from .world import create_world


def create_player() -> Player:
    return Player(
        name="Adventurer",
        attrs=AttributeSet(15, 12, 12, 8, 9, 6, 5),
        potential=PotentialSet.from_rank("D", agility="C", willpower="C", luck="E"),
        talents=[BASIC_TALENTS["Sword Genius"], BASIC_TALENTS["Scholar's Memory"]],
        traits=[Trait("Obsessive", "Improves through repetition.")],
        skills={"Swordsmanship": Skill("Swordsmanship", 5.0)},
    )


def main() -> None:
    if DEFAULT_SAVE_PATH.exists():
        player = load_player(DEFAULT_SAVE_PATH)
    else:
        player = create_player()
    monsters = create_world()
    print("=== GRAND LUNACY ===")
    while True:
        print("\n1. Train Running\n2. Sword Sparring\n3. Rest\n4. Read Monster Encyclopedia (Goblin)\n5. Inspect Monster\n6. Fight Monster\n7. Observe Monster\n8. Retreat Drill\n9. View Character\n10. View Bestiary\n11. Save Game\n0. Save and Quit")
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
            monster = random.choice(monsters)
            result = fight(player, monster, action="observe", terrain="forest")
            print(result.message)
        elif choice == "8":
            monster = random.choice(monsters)
            result = fight(player, monster, action="retreat", terrain="forest")
            print(result.message)
        elif choice == "9":
            print("\nVisible Attribute Grades")
            print(player.visible_attributes())
            print(f"Fatigue: {player.fatigue:.0f}/100")
            if player.injuries:
                print("Injuries:")
                for injury, severity in player.injuries.items():
                    print(f" - {injury}: {severity:.1f}")
            print("Skills:")
            for skill in player.skills.values():
                print(f" - {skill.name}: {skill.rank}")
            print("Known Talents:")
            known_talents = [talent for talent in player.talents if talent.discovered]
            if known_talents:
                for talent in known_talents:
                    print(f" - {talent.name}: {talent.description}")
            else:
                print(" - None discovered")
        elif choice == "10":
            entries = bestiary(player, monsters)
            if not entries:
                print("No bestiary entries yet. Fight, observe, or read first.")
            for entry in entries:
                print(f"\n{entry.species} — {entry.level} ({entry.reliability})")
                print(f"Encounters: {entry.encounters}; Book studied: {entry.book_studied}")
                print(entry.attributes)
                print(entry.notes)
        elif choice == "11":
            print(f"Saved to {save_player(player)}.")
        elif choice == "0":
            print(f"Saved to {save_player(player)}.")
            break
