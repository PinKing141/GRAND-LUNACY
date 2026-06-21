"""Action-based training with fatigue and soft-cap penalties."""

from __future__ import annotations

from dataclasses import dataclass

from .attributes import AttributeName
from .characters import Character


@dataclass(frozen=True)
class TrainingActivity:
    name: str
    attribute_gains: dict[AttributeName, float]
    skill_gains: dict[str, float]
    fatigue: float


TRAINING_ACTIVITIES: dict[str, TrainingActivity] = {
    "running": TrainingActivity("Running", {AttributeName.AGILITY: 0.10, AttributeName.VITALITY: 0.05}, {"Athletics": 0.15}, 8),
    "weights": TrainingActivity("Weight Training", {AttributeName.STRENGTH: 0.10, AttributeName.VITALITY: 0.05}, {"Body Control": 0.12}, 10),
    "meditation": TrainingActivity("Meditation", {AttributeName.WILLPOWER: 0.07}, {"Mana Control": 0.10, "Aura Control": 0.10}, 4),
    "reading": TrainingActivity("Reading", {AttributeName.INTELLIGENCE: 0.08}, {"Scholarship": 0.12}, 3),
    "sword": TrainingActivity("Sword Sparring", {AttributeName.STRENGTH: 0.03, AttributeName.AGILITY: 0.02, AttributeName.WILLPOWER: 0.01}, {"Swordsmanship": 0.20}, 9),
    "acting": TrainingActivity("Acting Practice", {AttributeName.CHARISMA: 0.08, AttributeName.WILLPOWER: 0.02}, {"Acting": 0.12, "Deception": 0.10}, 4),
}


def fatigue_multiplier(fatigue: float) -> float:
    if fatigue <= 30:
        return 1.0
    if fatigue <= 60:
        return 0.75
    if fatigue <= 80:
        return 0.45
    return 0.20


def train(character: Character, activity_key: str) -> list[str]:
    activity = TRAINING_ACTIVITIES[activity_key]
    messages = [f"You perform {activity.name}."]
    fatigue_mod = fatigue_multiplier(character.fatigue)

    for attribute, base_gain in activity.attribute_gains.items():
        current = character.attrs.get(attribute)
        cap_mod = character.potential.cap_penalty(attribute, current)
        actual_gain = base_gain * fatigue_mod * cap_mod
        if actual_gain <= 0.0001:
            messages.append(f"Your {attribute.value} no longer responds to ordinary {activity.name.lower()}.")
        else:
            character.attrs.increase(attribute, actual_gain)
            if cap_mod < 0.15:
                messages.append(f"Your {attribute.value} barely improves; you feel close to a natural wall.")
            else:
                messages.append(f"Your {attribute.value} improves slightly.")

    for skill_name, base_gain in activity.skill_gains.items():
        gain = base_gain * fatigue_mod * character.talent_multiplier(skill_name)
        character.skill(skill_name).improve(gain)
        messages.append(f"{skill_name} proficiency grows through practice.")

    character.fatigue = min(100.0, character.fatigue + activity.fatigue)
    if character.fatigue > 80:
        messages.append("Exhaustion bites deep; further training risks injury.")
    elif character.fatigue > 60:
        messages.append("Fatigue is heavy, and your gains are suffering.")
    return messages


def recover(character: Character) -> str:
    amount = 20.0 + character.attrs.vitality * 0.5
    character.fatigue = max(0.0, character.fatigue - amount)
    return "Rest, food, and time reduce your fatigue."
