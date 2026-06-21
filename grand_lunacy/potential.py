"""Natural potential ranks, soft caps, and limit breaking."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .attributes import ATTRIBUTES, AttributeName


POTENTIAL_CAPS: dict[str, float] = {
    "F": 5.0,
    "E": 10.0,
    "D": 20.0,
    "C": 40.0,
    "B": 80.0,
    "A": 160.0,
    "S": 320.0,
}


@dataclass
class PotentialSet:
    ranks: Dict[AttributeName, str]
    bonus_caps: Dict[AttributeName, float] | None = None

    @classmethod
    def from_rank(cls, default: str, **overrides: str) -> "PotentialSet":
        ranks = {attribute: default for attribute in ATTRIBUTES}
        for key, value in overrides.items():
            ranks[AttributeName[key.upper()]] = value
        return cls(ranks=ranks, bonus_caps={})

    def natural_cap(self, attribute: AttributeName) -> float:
        return POTENTIAL_CAPS[self.ranks[attribute]] + (self.bonus_caps or {}).get(attribute, 0.0)

    def cap_penalty(self, attribute: AttributeName, current_value: float) -> float:
        cap = self.natural_cap(attribute)
        if current_value >= cap:
            return 0.0
        return max(0.0, 1.0 - current_value / cap)

    def limit_break(self, attribute: AttributeName, amount: float) -> None:
        if self.bonus_caps is None:
            self.bonus_caps = {}
        self.bonus_caps[attribute] = self.bonus_caps.get(attribute, 0.0) + amount
