"""Hidden decimal attributes and grade visibility for Grand Lunacy."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable


class AttributeName(str, Enum):
    STRENGTH = "STR"
    AGILITY = "AGI"
    VITALITY = "VIT"
    INTELLIGENCE = "INT"
    WILLPOWER = "WIL"
    CHARISMA = "CHA"
    LUCK = "LUK"


GRADE_THRESHOLDS: tuple[tuple[str, float], ...] = (
    ("S", 160.0),
    ("A", 80.0),
    ("B", 40.0),
    ("C", 20.0),
    ("D", 10.0),
    ("E", 5.0),
    ("F", 0.0),
)


ATTRIBUTES: tuple[AttributeName, ...] = tuple(AttributeName)


def grade(value: float) -> str:
    """Return the simple roadmap grade for a hidden decimal value."""
    for label, threshold in GRADE_THRESHOLDS:
        if value >= threshold:
            return label
    return "F"


@dataclass
class AttributeSet:
    """Engine-facing decimal stat block; UI should usually expose grades only."""

    strength: float
    agility: float
    vitality: float
    intelligence: float
    willpower: float
    charisma: float
    luck: float

    def get(self, attribute: AttributeName) -> float:
        return getattr(self, _FIELD_BY_ATTRIBUTE[attribute])

    def increase(self, attribute: AttributeName, amount: float) -> None:
        field = _FIELD_BY_ATTRIBUTE[attribute]
        setattr(self, field, max(0.0, getattr(self, field) + amount))

    def visible(self, known: Iterable[AttributeName] | None = None, hide_luck: bool = True) -> Dict[str, str]:
        """Return grade visibility, hiding unknown values and usually luck."""
        known_set = set(known or ATTRIBUTES)
        result: Dict[str, str] = {}
        for attribute in ATTRIBUTES:
            if attribute not in known_set or (hide_luck and attribute is AttributeName.LUCK):
                result[attribute.value] = "???"
            else:
                result[attribute.value] = grade(self.get(attribute))
        return result


_FIELD_BY_ATTRIBUTE = {
    AttributeName.STRENGTH: "strength",
    AttributeName.AGILITY: "agility",
    AttributeName.VITALITY: "vitality",
    AttributeName.INTELLIGENCE: "intelligence",
    AttributeName.WILLPOWER: "willpower",
    AttributeName.CHARISMA: "charisma",
    AttributeName.LUCK: "luck",
}
