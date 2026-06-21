"""Character models for players and creatures."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field

from .attributes import AttributeName, AttributeSet
from .affinities import AffinitySet
from .potential import PotentialSet
from .skills import BASIC_TALENTS, Skill, Talent, Trait


@dataclass
class Character:
    name: str
    attrs: AttributeSet
    potential: PotentialSet
    talents: list[Talent] = field(default_factory=list)
    traits: list[Trait] = field(default_factory=list)
    skills: dict[str, Skill] = field(default_factory=dict)
    affinities: AffinitySet = field(default_factory=AffinitySet)
    fatigue: float = 0.0

    def skill(self, name: str) -> Skill:
        if name not in self.skills:
            self.skills[name] = Skill(name)
        return self.skills[name]

    def talent_multiplier(self, target: str) -> float:
        multiplier = 1.0
        for talent in self.talents:
            if talent.discovered:
                multiplier = max(multiplier, talent.multiplier_for(target))
        return multiplier

    def affinity_multiplier(self, target: str) -> float:
        return self.affinities.multiplier_for(target)

    def visible_skills(self, exact: bool = False) -> dict[str, str]:
        return {name: skill.visible(exact=exact) for name, skill in sorted(self.skills.items())}

    def visible_talents(self) -> list[str]:
        return [f"{talent.name} ({talent.rarity.value})" for talent in self.talents if talent.discovered]

    def visible_attributes(self) -> dict[str, str]:
        known = [a for a in AttributeName if a is not AttributeName.LUCK]
        return self.attrs.visible(known=known, hide_luck=True)


@dataclass
class Player(Character):
    insight: float = 0.0
    bestiary: dict[str, int] = field(default_factory=dict)
    encyclopedia: set[str] = field(default_factory=set)

    def record_encounter(self, species_name: str, amount: int = 1) -> None:
        self.bestiary[species_name] = self.bestiary.get(species_name, 0) + amount

    def discover_talent(self, talent_name: str) -> str:
        for talent in self.talents:
            if talent.name == talent_name:
                talent.discovered = True
                return f"Talent Discovered: {talent.name}"
        template = deepcopy(BASIC_TALENTS[talent_name])
        template.discovered = True
        self.talents.append(template)
        return f"Talent Discovered: {template.name}"
