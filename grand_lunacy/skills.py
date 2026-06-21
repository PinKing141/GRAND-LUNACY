"""Talents, traits, and trainable proficiencies."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Talent:
    name: str
    description: str
    multiplier: float = 1.0


@dataclass(frozen=True)
class Trait:
    name: str
    description: str


@dataclass
class Skill:
    name: str
    proficiency: float = 0.0

    def improve(self, amount: float) -> None:
        self.proficiency = max(0.0, self.proficiency + amount)
