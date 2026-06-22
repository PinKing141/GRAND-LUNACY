"""JSON save/load helpers for the terminal prototype."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .attributes import ATTRIBUTES, AttributeName, AttributeSet
from .characters import Player
from .potential import PotentialSet
from .skills import Skill, Talent, Trait

DEFAULT_SAVE_PATH = Path("grand_lunacy_save.json")


def save_player(player: Player, path: str | Path = DEFAULT_SAVE_PATH) -> Path:
    """Persist a player's hidden state to JSON and return the written path."""
    save_path = Path(path)
    save_path.write_text(json.dumps(_player_to_data(player), indent=2, sort_keys=True), encoding="utf-8")
    return save_path


def load_player(path: str | Path = DEFAULT_SAVE_PATH) -> Player:
    """Load a player previously written by :func:`save_player`."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return _player_from_data(data)


def _player_to_data(player: Player) -> dict[str, Any]:
    return {
        "name": player.name,
        "attrs": {attribute.name.lower(): player.attrs.get(attribute) for attribute in ATTRIBUTES},
        "potential": {
            "ranks": {attribute.name.lower(): player.potential.ranks[attribute] for attribute in ATTRIBUTES},
            "bonus_caps": {attribute.name.lower(): value for attribute, value in (player.potential.bonus_caps or {}).items()},
        },
        "talents": [talent.__dict__ for talent in player.talents],
        "traits": [trait.__dict__ for trait in player.traits],
        "skills": {name: skill.proficiency for name, skill in player.skills.items()},
        "fatigue": player.fatigue,
        "insight": player.insight,
        "bestiary": player.bestiary,
        "encyclopedia": sorted(player.encyclopedia),
    }


def _player_from_data(data: dict[str, Any]) -> Player:
    attrs = data["attrs"]
    potential = data["potential"]
    return Player(
        name=data["name"],
        attrs=AttributeSet(**attrs),
        potential=PotentialSet(
            ranks={AttributeName[key.upper()]: value for key, value in potential["ranks"].items()},
            bonus_caps={AttributeName[key.upper()]: value for key, value in potential.get("bonus_caps", {}).items()},
        ),
        talents=[Talent(**talent) for talent in data.get("talents", [])],
        traits=[Trait(**trait) for trait in data.get("traits", [])],
        skills={name: Skill(name, proficiency) for name, proficiency in data.get("skills", {}).items()},
        fatigue=data.get("fatigue", 0.0),
        insight=data.get("insight", 0.0),
        bestiary=data.get("bestiary", {}),
        encyclopedia=set(data.get("encyclopedia", [])),
    )
