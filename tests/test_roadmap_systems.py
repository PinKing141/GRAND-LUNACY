from grand_lunacy.attributes import AttributeName, AttributeSet, grade
from grand_lunacy.game import create_player
from grand_lunacy.knowledge import analyze, read_encyclopedia
from grand_lunacy.potential import PotentialSet
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
