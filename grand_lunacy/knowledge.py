"""Insight, observation, and bestiary visibility."""

from .attributes import AttributeName, grade
from .characters import Player
from .world import Monster


OBSERVED_ORDER = (AttributeName.STRENGTH, AttributeName.AGILITY, AttributeName.VITALITY, AttributeName.INTELLIGENCE, AttributeName.WILLPOWER, AttributeName.CHARISMA)


def analyze(player: Player, monster: Monster) -> dict[str, str]:
    species = monster.species.name
    encounters = player.bestiary.get(species, 0)
    if species in player.encyclopedia:
        encounters += 3
    if player.insight >= 50:
        known = OBSERVED_ORDER
    else:
        known = OBSERVED_ORDER[: min(len(OBSERVED_ORDER), encounters)]
    return {attribute.value: grade(monster.species.baseline.get(attribute)) if attribute in known else "???" for attribute in OBSERVED_ORDER} | {"LUK": "???"}


def read_encyclopedia(player: Player, species_name: str) -> str:
    player.encyclopedia.add(species_name)
    return f"You study a rough {species_name} entry. Knowledge, not experience points, is progress."
