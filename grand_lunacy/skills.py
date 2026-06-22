"""Talents, traits, and trainable proficiencies."""

from __future__ import annotations

from dataclasses import dataclass


SKILL_RANK_THRESHOLDS: tuple[tuple[str, float], ...] = (
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


@dataclass(frozen=True)
class Talent:
    name: str
    description: str
    multiplier: float = 1.0
    skill_tags: tuple[str, ...] = ()
    discovered: bool = True

    def affects(self, skill_name: str) -> bool:
        lowered = skill_name.lower()
        return any(tag.lower() in lowered for tag in self.skill_tags) or self.name.lower().replace(" genius", "") in lowered


@dataclass(frozen=True)
class Trait:
    name: str
    description: str


@dataclass
class Skill:
    name: str
    proficiency: float = 0.0

    @property
    def rank(self) -> str:
        return skill_rank(self.proficiency)

    def improve(self, amount: float) -> None:
        self.proficiency = min(100.0, max(0.0, self.proficiency + amount))


def skill_rank(proficiency: float) -> str:
    """Return the visible roadmap rank for an internal proficiency percentage."""
    for label, threshold in SKILL_RANK_THRESHOLDS:
        if proficiency >= threshold:
            return label
    return "Untrained"


BASIC_TALENTS: dict[str, Talent] = {
    "Sword Genius": Talent(
        "Sword Genius",
        "Learns sword skills rapidly and notices flaws in enemy sword styles.",
        multiplier=1.8,
        skill_tags=("Sword",),
        discovered=False,
    ),
    "Mana Sensitivity": Talent(
        "Mana Sensitivity",
        "Feels nearby mana and learns mana control faster.",
        multiplier=2.0,
        skill_tags=("Mana", "Aura"),
        discovered=False,
    ),
    "Acting Genius": Talent(
        "Acting Genius",
        "Learns acting and deception quickly enough to survive social danger.",
        multiplier=1.7,
        skill_tags=("Acting", "Deception"),
        discovered=False,
    ),
    "Scholar's Memory": Talent(
        "Scholar's Memory",
        "Retains lore and research patterns with unusual clarity.",
        multiplier=1.5,
        skill_tags=("Scholarship", "Insight"),
        discovered=False,
    ),
}


def discover_talents(talents: list[Talent], skill: Skill) -> tuple[list[Talent], list[str]]:
    """Reveal hidden talents after repeated relevant practice."""
    updated: list[Talent] = []
    messages: list[str] = []
    for talent in talents:
        if not talent.discovered and talent.affects(skill.name) and skill.proficiency >= 5.0:
            updated.append(Talent(talent.name, talent.description, talent.multiplier, talent.skill_tags, True))
            messages.append(f"Talent Discovered: {talent.name}")
        else:
            updated.append(talent)
    return updated, messages
