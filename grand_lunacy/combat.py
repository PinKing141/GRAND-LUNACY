"""Decision-forward no-level combat resolution."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .characters import Player
from .world import Monster


class CombatAction(str, Enum):
    ATTACK = "attack"
    OBSERVE = "observe"
    RETREAT = "retreat"


@dataclass(frozen=True)
class Equipment:
    name: str
    power: float = 0.0
    defense: float = 0.0


@dataclass(frozen=True)
class Terrain:
    name: str
    player_modifier: float = 0.0
    enemy_modifier: float = 0.0
    retreat_modifier: float = 0.0


@dataclass(frozen=True)
class CombatResult:
    victory: bool
    message: str
    retreated: bool = False
    injury: str | None = None
    observations: list[str] = field(default_factory=list)


TERRAINS: dict[str, Terrain] = {
    "open": Terrain("open ground"),
    "forest": Terrain("tangled forest", player_modifier=-0.5, enemy_modifier=0.3, retreat_modifier=1.0),
    "ruins": Terrain("broken ruins", player_modifier=0.2, enemy_modifier=-0.2, retreat_modifier=-0.5),
}

BASIC_WEAPON = Equipment("worn sword", power=1.5)
BASIC_ARMOR = Equipment("padded coat", defense=0.8)
WEAKNESS_BONUS = 2.0


def fight(
    player: Player,
    monster: Monster,
    action: str | CombatAction = CombatAction.ATTACK,
    terrain: str | Terrain = "open",
    weapon: Equipment | None = BASIC_WEAPON,
    armor: Equipment | None = BASIC_ARMOR,
) -> CombatResult:
    """Resolve one simple combat choice against a monster.

    The prototype keeps exact numbers hidden from players, but the resolver now
    models the MVP 5 roadmap pieces: combat choices, observe/retreat actions,
    weaknesses, terrain, injuries, equipment, and enemy behavior.
    """
    enemy = monster.as_character()
    player.record_encounter(monster.species.name)
    selected_action = CombatAction(action)
    selected_terrain = _terrain(terrain)
    observations = _observations(monster)

    if selected_action is CombatAction.OBSERVE:
        player.insight += 1.5
        player.record_encounter(monster.species.name)
        return CombatResult(False, f"You keep distance and study {monster.name}: {' '.join(observations)}", observations=observations)

    if selected_action is CombatAction.RETREAT:
        retreat_score = player.attrs.agility + player.skill("Athletics").proficiency + selected_terrain.retreat_modifier
        pursuit_score = enemy.attrs.agility + _behavior_pressure(monster)
        if retreat_score >= pursuit_score:
            return CombatResult(False, f"You retreat from {monster.name}, choosing survival over pride.", retreated=True, observations=observations)
        injury = _apply_injury(player, "Parting Wound", 6.0 - (armor.defense if armor else 0.0))
        return CombatResult(False, f"You fail to escape {monster.name}. The enemy's behavior turns pursuit into punishment.", retreated=False, injury=injury, observations=observations)

    sword = player.skill("Swordsmanship")
    weapon_power = weapon.power if weapon else 0.0
    armor_defense = armor.defense if armor else 0.0
    weakness_bonus = WEAKNESS_BONUS if monster.species.name in player.encyclopedia else 0.0
    player_power = player.attrs.strength + player.attrs.agility * 0.25 + sword.proficiency + weapon_power + weakness_bonus + selected_terrain.player_modifier
    enemy_power = enemy.attrs.strength + enemy.attrs.vitality + enemy.attrs.agility * 0.15 + _behavior_pressure(monster) + selected_terrain.enemy_modifier
    if player_power >= enemy_power:
        sword.improve(0.5 * player.talent_multiplier("Swordsmanship"))
        return CombatResult(True, f"Victory over {monster.name}. Gear, terrain, knowledge, and preparation mattered more than levels.", observations=observations)
    sword.improve(0.2 * player.talent_multiplier("Swordsmanship"))
    player.insight += 1.0
    injury = _apply_injury(player, "Bruised Ribs", max(1.0, enemy_power - player_power - armor_defense))
    return CombatResult(False, f"Defeat against {monster.name}, but observation sharpens your future odds.", injury=injury, observations=observations)


def _terrain(terrain: str | Terrain) -> Terrain:
    if isinstance(terrain, Terrain):
        return terrain
    return TERRAINS[terrain]


def _behavior_pressure(monster: Monster) -> float:
    if monster.species.name == "Goblin":
        return 0.5
    if monster.species.name == "Wolf":
        return 2.0
    return 1.0


def _observations(monster: Monster) -> list[str]:
    if monster.species.name == "Goblin":
        return ["It feints when cornered.", "Fire and confident pressure can break its nerve."]
    if monster.species.name == "Wolf":
        return ["It circles for hamstrings.", "Open ground favors its speed."]
    return ["Its habits are still unclear."]


def _apply_injury(player: Player, name: str, severity: float) -> str:
    severity = round(max(0.1, severity), 1)
    player.injuries[name] = max(player.injuries.get(name, 0.0), severity)
    player.fatigue = min(100.0, player.fatigue + severity)
    return f"{name} ({severity:.1f})"
