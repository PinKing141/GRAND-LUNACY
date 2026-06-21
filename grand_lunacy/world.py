"""Species baselines and default world content."""

from dataclasses import dataclass

from .attributes import AttributeSet
from .characters import Character
from .potential import PotentialSet


@dataclass(frozen=True)
class Species:
    name: str
    baseline: AttributeSet
    potential: PotentialSet
    notes: str = ""


@dataclass
class Monster:
    species: Species
    variant: str = ""

    @property
    def name(self) -> str:
        return f"{self.variant} {self.species.name}".strip()

    def as_character(self) -> Character:
        return Character(self.name, self.species.baseline, self.species.potential)


def create_world() -> list[Monster]:
    goblin = Species(
        "Goblin",
        AttributeSet(3, 11, 4, 2, 2, 1, 2),
        PotentialSet.from_rank("F", agility="D"),
        notes="Cowardly pack creature; weak alone, dangerous when prepared.",
    )
    wolf = Species(
        "Wolf",
        AttributeSet(12, 18, 10, 3, 4, 1, 3),
        PotentialSet.from_rank("D", agility="C"),
        notes="Fast predator with dangerous reflexes.",
    )
    return [Monster(goblin), Monster(wolf)]
