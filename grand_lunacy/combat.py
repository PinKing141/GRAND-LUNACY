"""Simple no-level combat resolution."""

from dataclasses import dataclass

from .characters import Player
from .world import Monster


@dataclass(frozen=True)
class CombatResult:
    victory: bool
    message: str


def fight(player: Player, monster: Monster) -> CombatResult:
    enemy = monster.as_character()
    player.record_encounter(monster.species.name)
    sword = player.skill("Swordsmanship")
    player_power = player.attrs.strength + player.attrs.agility * 0.25 + sword.proficiency
    enemy_power = enemy.attrs.strength + enemy.attrs.vitality + enemy.attrs.agility * 0.15
    if player_power >= enemy_power:
        sword.improve(0.5 * player.talent_multiplier("Swordsmanship"))
        return CombatResult(True, f"Victory over {monster.name}. Your preparation mattered more than levels.")
    sword.improve(0.2 * player.talent_multiplier("Swordsmanship"))
    player.insight += 1.0
    return CombatResult(False, f"Defeat against {monster.name}, but observation sharpens your future odds.")
