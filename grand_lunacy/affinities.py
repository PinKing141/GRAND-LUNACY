"""Natural compatibility ranks for weapons, magic, craft, and social paths."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class AffinityCategory(str, Enum):
    WEAPON = "Weapon"
    MAGIC = "Magic"
    CRAFT = "Craft"
    SOCIAL = "Social"


AFFINITY_MULTIPLIERS: dict[str, float] = {
    "F": 0.65,
    "E": 0.80,
    "D": 0.95,
    "C": 1.0,
    "B": 1.15,
    "A": 1.35,
    "S": 1.65,
}


AFFINITY_FAILURE_RISK: dict[str, float] = {
    "F": 0.30,
    "E": 0.20,
    "D": 0.12,
    "C": 0.08,
    "B": 0.04,
    "A": 0.02,
    "S": 0.005,
}


@dataclass(frozen=True)
class Affinity:
    name: str
    category: AffinityCategory
    rank: str

    @property
    def multiplier(self) -> float:
        return AFFINITY_MULTIPLIERS[self.rank]

    @property
    def failure_risk(self) -> float:
        return AFFINITY_FAILURE_RISK[self.rank]


@dataclass
class AffinitySet:
    affinities: dict[str, Affinity] = field(default_factory=dict)

    def set(self, name: str, category: AffinityCategory, rank: str) -> None:
        self.affinities[name] = Affinity(name, category, rank)

    def get(self, name: str) -> Affinity | None:
        return self.affinities.get(name)

    def multiplier_for(self, name: str) -> float:
        affinity = self.get(name)
        return affinity.multiplier if affinity else 1.0

    def visible(self) -> dict[str, str]:
        return {name: affinity.rank for name, affinity in sorted(self.affinities.items())}
