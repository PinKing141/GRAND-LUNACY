"""Character models for players and creatures."""

from __future__ import annotations

from dataclasses import dataclass, field

from .attributes import AttributeName, AttributeSet
from .potential import PotentialSet
from .skills import Skill, Talent, Trait


@dataclass
class Character:
    name: str
    attrs: AttributeSet
    potential: PotentialSet
    talents: list[Talent] = field(default_factory=list)
    traits: list[Trait] = field(default_factory=list)
    skills: dict[str, Skill] = field(default_factory=dict)
    fatigue: float = 0.0

    def skill(self, name: str) -> Skill:
        if name not in self.skills:
            self.skills[name] = Skill(name)
        return self.skills[name]

    def talent_multiplier(self, skill_name: str) -> float:
        lowered = skill_name.lower()
        multiplier = 1.0
        for talent in self.talents:
            if talent.discovered and talent.affects(skill_name):
                multiplier = max(multiplier, talent.multiplier)
        return multiplier

    def visible_attributes(self) -> dict[str, str]:
        known = [a for a in AttributeName if a is not AttributeName.LUCK]
        return self.attrs.visible(known=known, hide_luck=True)


@dataclass
class Player(Character):
    insight: float = 0.0
    bestiary: dict[str, int] = field(default_factory=dict)
    encyclopedia: set[str] = field(default_factory=set)
    injuries: dict[str, float] = field(default_factory=dict)

    def record_encounter(self, species_name: str, amount: int = 1) -> None:
        self.bestiary[species_name] = self.bestiary.get(species_name, 0) + amount
