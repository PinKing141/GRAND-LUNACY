"""Insight, observation, and bestiary visibility."""

from __future__ import annotations

from dataclasses import dataclass

from .attributes import ATTRIBUTES, AttributeName, grade
from .characters import Player
from .world import Monster, Species


OBSERVED_ORDER = (
    AttributeName.STRENGTH,
    AttributeName.AGILITY,
    AttributeName.VITALITY,
    AttributeName.INTELLIGENCE,
    AttributeName.WILLPOWER,
    AttributeName.CHARISMA,
)
KNOWLEDGE_LEVELS = ("Unknown", "Glimpsed", "Observed", "Studied", "Catalogued", "Expert")


@dataclass(frozen=True)
class BestiaryEntry:
    """Player-facing monster record gated by encounter, book, and insight knowledge."""

    species: str
    level: str
    encounters: int
    book_studied: bool
    attributes: dict[str, str]
    notes: str
    reliability: str


def knowledge_score(player: Player, species_name: str) -> int:
    """Return a compact score combining battle experience, books, and insight."""
    encounters = player.bestiary.get(species_name, 0)
    book_bonus = 2 if species_name in player.encyclopedia else 0
    insight_bonus = int(player.insight // 10)
    return min(5, encounters + book_bonus + insight_bonus)


def knowledge_level(player: Player, species_name: str) -> str:
    """Return the player's current bestiary knowledge tier for a species."""
    return KNOWLEDGE_LEVELS[knowledge_score(player, species_name)]


def analyze(player: Player, monster: Monster) -> dict[str, str]:
    """Return a quick inspection with vague estimates until knowledge improves."""
    entry = bestiary_entry(player, monster.species)
    return entry.attributes


def bestiary_entry(player: Player, species: Species) -> BestiaryEntry:
    """Build the player's currently visible bestiary entry for one species."""
    score = knowledge_score(player, species.name)
    known = set(OBSERVED_ORDER[: min(len(OBSERVED_ORDER), score)])
    if player.insight >= 50:
        known.update(OBSERVED_ORDER)

    attributes = {
        attribute.value: _visible_attribute(species, attribute, score, attribute in known)
        for attribute in ATTRIBUTES
    }
    notes = _visible_notes(species, score, species.name in player.encyclopedia)
    return BestiaryEntry(
        species=species.name,
        level=KNOWLEDGE_LEVELS[score],
        encounters=player.bestiary.get(species.name, 0),
        book_studied=species.name in player.encyclopedia,
        attributes=attributes,
        notes=notes,
        reliability=_reliability(score),
    )


def bestiary(player: Player, monsters: list[Monster]) -> list[BestiaryEntry]:
    """Return deduplicated bestiary entries for all encountered or studied species."""
    species_by_name = {monster.species.name: monster.species for monster in monsters}
    known_names = sorted(set(player.bestiary) | player.encyclopedia)
    return [bestiary_entry(player, species_by_name[name]) for name in known_names if name in species_by_name]


def read_encyclopedia(player: Player, species_name: str) -> str:
    player.encyclopedia.add(species_name)
    return f"You study a rough {species_name} entry. Knowledge, not experience points, is progress."


def _visible_attribute(species: Species, attribute: AttributeName, score: int, precise: bool) -> str:
    if attribute is AttributeName.LUCK:
        return "???"
    if precise:
        return grade(species.baseline.get(attribute))
    if score == 0:
        return "???"
    return _rough_grade(species, attribute)


def _rough_grade(species: Species, attribute: AttributeName) -> str:
    """Return a deterministic but imperfect adjacent-grade estimate."""
    labels = ["F", "E", "D", "C", "B", "A", "S"]
    actual = grade(species.baseline.get(attribute))
    offset = (sum(ord(char) for char in f"{species.name}:{attribute.value}") % 3) - 1
    return labels[max(0, min(len(labels) - 1, labels.index(actual) + offset))] + "~"


def _visible_notes(species: Species, score: int, book_studied: bool) -> str:
    if score >= 3 or book_studied:
        return species.notes
    if score >= 1:
        return "Fragmentary field notes; estimates may be wrong."
    return "No reliable entry yet."


def _reliability(score: int) -> str:
    if score >= 4:
        return "reliable"
    if score >= 2:
        return "partial"
    if score == 1:
        return "rough"
    return "unknown"
