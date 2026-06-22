from grand_lunacy.attributes import AttributeName, AttributeSet, grade
from grand_lunacy.game import create_player
from grand_lunacy.knowledge import analyze, read_encyclopedia
from grand_lunacy.potential import PotentialSet
from grand_lunacy.skills import BASIC_TALENTS, Skill, skill_rank
from grand_lunacy.save_load import load_player, save_player
from grand_lunacy.training import train
from grand_lunacy.world import create_world


def test_grade_thresholds_match_roadmap():
    assert grade(4.9) == "F"
    assert grade(5) == "E"
    assert grade(10) == "D"
    assert grade(20) == "C"
    assert grade(40) == "B"
    assert grade(80) == "A"
    assert grade(160) == "S"


def test_luck_is_hidden_by_default():
    attrs = AttributeSet(15, 12, 12, 8, 9, 6, 5)
    visible = attrs.visible(hide_luck=True)
    assert visible["STR"] == "D"
    assert visible["LUK"] == "???"


def test_training_uses_soft_caps_and_fatigue_without_levels():
    player = create_player()
    before = player.attrs.agility
    messages = train(player, "running")
    assert player.attrs.agility > before
    assert player.fatigue > 0
    assert any("AGI improves" in message for message in messages)


def test_soft_cap_blocks_ordinary_growth_at_natural_limit():
    player = create_player()
    player.attrs.strength = player.potential.natural_cap(AttributeName.STRENGTH)
    messages = train(player, "weights")
    assert any("no longer responds" in message for message in messages)


def test_bestiary_knowledge_reveals_more_than_first_encounter():
    player = create_player()
    goblin = create_world()[0]
    unknown = analyze(player, goblin)
    assert unknown["STR"] == "???"
    read_encyclopedia(player, "Goblin")
    studied = analyze(player, goblin)
    assert studied["STR"] == "F"
    assert studied["AGI"] == "D"
    assert studied["LUK"] == "???"


def test_potential_limit_break_raises_cap():
    potential = PotentialSet.from_rank("F")
    original = potential.natural_cap(AttributeName.VITALITY)
    potential.limit_break(AttributeName.VITALITY, 10)
    assert potential.natural_cap(AttributeName.VITALITY) == original + 10


def test_save_load_preserves_player_progress(tmp_path):
    player = create_player()
    train(player, "running")
    read_encyclopedia(player, "Goblin")
    player.record_encounter("Goblin", 2)

    save_path = tmp_path / "save.json"
    save_player(player, save_path)
    loaded = load_player(save_path)

    assert loaded.name == player.name
    assert loaded.attrs.agility == player.attrs.agility
    assert loaded.fatigue == player.fatigue
    assert loaded.bestiary == {"Goblin": 2}
    assert loaded.encyclopedia == {"Goblin"}
    assert loaded.skill("Athletics").proficiency == player.skill("Athletics").proficiency


def test_skill_ranks_match_roadmap_thresholds():
    assert skill_rank(0) == "Untrained"
    assert skill_rank(5) == "Beginner"
    assert skill_rank(15) == "Novice"
    assert skill_rank(30) == "Apprentice"
    assert skill_rank(50) == "Adept"
    assert skill_rank(70) == "Expert"
    assert skill_rank(85) == "Master"
    assert skill_rank(95) == "Grandmaster"
    assert skill_rank(99.5) == "Saint"


def test_relevant_training_discovers_hidden_talent_and_then_multiplies_growth():
    player = create_player()
    player.skills["Swordsmanship"] = Skill("Swordsmanship", 4.9)
    messages = train(player, "sword")
    assert any("Talent Discovered: Sword Genius" in message for message in messages)
    assert any(talent.name == "Sword Genius" and talent.discovered for talent in player.talents)

    before = player.skill("Swordsmanship").proficiency
    train(player, "sword")
    assert player.skill("Swordsmanship").proficiency - before > 0.20


def test_basic_talent_list_contains_roadmap_examples():
    assert {"Sword Genius", "Mana Sensitivity", "Acting Genius"}.issubset(BASIC_TALENTS)


def test_bestiary_entries_track_levels_sources_and_rough_estimates():
    from grand_lunacy.knowledge import bestiary, bestiary_entry, knowledge_level

    player = create_player()
    goblin = create_world()[0]

    assert knowledge_level(player, "Goblin") == "Unknown"
    player.record_encounter("Goblin")
    rough = bestiary_entry(player, goblin.species)
    assert rough.level == "Glimpsed"
    assert rough.encounters == 1
    assert rough.reliability == "rough"
    assert rough.attributes["STR"] == "F"
    assert rough.attributes["AGI"].endswith("~")
    assert rough.attributes["LUK"] == "???"
    assert "Fragmentary" in rough.notes

    read_encyclopedia(player, "Goblin")
    studied = bestiary_entry(player, goblin.species)
    assert studied.level == "Studied"
    assert studied.book_studied is True
    assert studied.attributes["VIT"] == "F"
    assert studied.notes == goblin.species.notes
    assert [entry.species for entry in bestiary(player, create_world())] == ["Goblin"]


def test_fighting_records_bestiary_knowledge_from_combat():
    from grand_lunacy.knowledge import knowledge_level
    from grand_lunacy.combat import fight

    player = create_player()
    goblin = create_world()[0]
    fight(player, goblin)
    assert player.bestiary["Goblin"] == 1
    assert knowledge_level(player, "Goblin") == "Glimpsed"


def test_combat_observe_and_retreat_actions_build_knowledge_without_levels():
    from grand_lunacy.combat import fight

    player = create_player()
    goblin = create_world()[0]

    observed = fight(player, goblin, action="observe", terrain="forest")
    assert observed.victory is False
    assert observed.retreated is False
    assert observed.observations
    assert player.bestiary["Goblin"] == 2
    assert player.insight >= 1.5

    retreated = fight(player, goblin, action="retreat", terrain="forest")
    assert retreated.retreated is True
    assert retreated.injury is None


def test_combat_uses_weaknesses_terrain_injuries_equipment_and_enemy_behavior():
    from grand_lunacy.combat import Equipment, fight

    player = create_player()
    wolf = create_world()[1]

    bad_fight = fight(player, wolf, action="attack", terrain="open", weapon=Equipment("bare hands"), armor=Equipment("plain clothes"))
    assert bad_fight.victory is False
    assert bad_fight.injury is not None
    assert player.injuries

    prepared = create_player()
    read_encyclopedia(prepared, "Wolf")
    good_fight = fight(prepared, wolf, action="attack", terrain="ruins", weapon=Equipment("boar spear", power=8), armor=Equipment("mail", defense=4))
    assert good_fight.victory is True
    assert "Gear, terrain, knowledge" in good_fight.message
