"""Talents, traits, trainable proficiencies, and rank visibility."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class TalentRarity(str, Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    MYTHIC = "Mythic"


SKILL_RANKS: tuple[tuple[str, float], ...] = (
    ("Saint", 99.5),
    ("Grandmaster", 95.0),
    ("Master", 85.0),
    ("Expert", 70.0),
    ("Adept", 50.0),
    ("Apprentice", 30.0),
    ("Novice", 15.0),
    ("Beginner", 5.0),
    ("Untrained", 0.0),
)


def skill_rank(proficiency: float) -> str:
    for label, threshold in SKILL_RANKS:
        if proficiency >= threshold:
            return label
    return "Untrained"


@dataclass(frozen=True)
class TalentEffect:
    target: str
    multiplier: float = 1.0
    insight_bonus: float = 0.0
    description: str = ""


@dataclass
class Talent:
    name: str
    description: str
    rarity: TalentRarity = TalentRarity.COMMON
    discovered: bool = True
    effects: list[TalentEffect] = field(default_factory=list)
    evolution: str | None = None

    @property
    def multiplier(self) -> float:
        return max((effect.multiplier for effect in self.effects), default=1.0)

    def multiplier_for(self, target: str) -> float:
        target_lower = target.lower()
        matches = [effect.multiplier for effect in self.effects if effect.target.lower() in target_lower or target_lower in effect.target.lower()]
        return max(matches, default=1.0)


@dataclass(frozen=True)
class Trait:
    name: str
    description: str


@dataclass
class Skill:
    name: str
    proficiency: float = 0.0
    style: str | None = None

    def improve(self, amount: float) -> None:
        self.proficiency = min(100.0, max(0.0, self.proficiency + amount))

    @property
    def rank(self) -> str:
        return skill_rank(self.proficiency)

    def visible(self, exact: bool = False) -> str:
        if exact:
            return f"{self.proficiency:.1f}%"
        return self.rank


BASIC_TALENTS: dict[str, Talent] = {
    "Sword Genius": Talent(
        "Sword Genius",
        "Swordsmanship growth is exceptional, and sword flaws are easier to notice.",
        rarity=TalentRarity.RARE,
        discovered=False,
        effects=[TalentEffect("Swordsmanship", 3.0), TalentEffect("Sword Sparring", 1.2)],
        evolution="Blade Prodigy",
    ),
    "Mana Sensitivity": Talent(
        "Mana Sensitivity",
        "Can feel nearby mana and detect abnormal magical flow with enough insight.",
        rarity=TalentRarity.UNCOMMON,
        discovered=False,
        effects=[TalentEffect("Mana Control", 2.0, insight_bonus=5.0), TalentEffect("Magic Theory", 1.2)],
        evolution="Mana Sight",
    ),
    "Acting Genius": Talent(
        "Acting Genius",
        "Learns performance, deception, and emotional imitation unusually quickly.",
        rarity=TalentRarity.RARE,
        discovered=False,
        effects=[TalentEffect("Acting", 3.0), TalentEffect("Deception", 2.0)],
        evolution="Perfect Persona",
    ),
}
