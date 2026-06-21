# Grand Lunacy — Full Detailed Roadmap

## 0. Core Identity of the Game

**Grand Lunacy** is a text-based RPG where the player enters a dangerous fantasy/game-like world with no traditional levels.

The main design idea is:

> **Power is not a number the player clearly sees. Power is something the player slowly understands through training, observation, mistakes, research, and survival.**

The world has hidden stats, talents, skills, traits, affinities, species baselines, magic systems, factions, injuries, aging, and legacy. But the player does **not** get perfect information unless they earn it.

This creates the main fantasy:

> “I do not know how strong this enemy is. I have to learn, prepare, adapt, and survive.”

---

# 1. The Non-Negotiable Design Rules

These are the rules that should never be broken.

## Rule 1: No Levels

There are no character levels.

No:

```text
Level 1 Goblin
Level 50 Dragon
Level 99 Hero
```

Instead:

```text
Goblin
Adult Goblin
Goblin Warrior
Goblin Shaman
Goblin Mutant
Goblin King
```

A goblin is weak because its species has weak average stats, not because it is “low level.”

A dragon is terrifying because dragons are naturally superior creatures with enormous physical, magical, and instinctive advantages.

---

## Rule 2: Stats Exist, But Players Usually Cannot See Them

The game engine knows exact stats:

```text
STR: 13.7
AGI: 18.4
VIT: 9.1
INT: 5.3
WIL: 7.2
CHA: 2.1
LUK: 4.0
```

The player normally sees:

```text
STR: ???
AGI: ???
VIT: ???
INT: ???
WIL: ???
CHA: ???
LUK: ???
```

Or after gaining knowledge:

```text
STR: D
AGI: C
VIT: E
INT: F
WIL: E
CHA: F
LUK: ???
```

Exact numbers should be rare.

---

## Rule 3: Knowledge Is Progression

In most RPGs, progression is:

```text
Kill monster → Gain XP → Level up
```

In **Grand Lunacy**, progression is:

```text
Encounter monster → Observe behavior → Survive → Learn pattern → Update bestiary → Prepare better → Fight smarter
```

A player who knows goblins are cowardly, sensitive to fire, and weak alone is stronger than a player who only knows “Goblin: F-rank.”

---

## Rule 4: Birth Matters, But It Is Not Absolute Destiny

Most attributes are determined heavily at birth.

A noble child, a sickly orphan, a beastkin warrior, and a magic-born prodigy will not start equal.

But the game should still allow:

```text
Hard work
Rare opportunities
Mentors
Limit breaks
Dangerous rituals
Magic items
Bloodline awakenings
Near-death experiences
```

to change someone’s future.

The world should feel unfair, but not hopeless.

---

## Rule 5: Luck Is Special

Luck is an attribute, but it is not normally trainable.

You can train Strength.

You can study Intelligence.

You can sharpen Willpower.

But Luck is mostly determined by birth, fate, blessings, curses, bloodline, divine interference, or rare attribute allocation opportunities.

Luck affects:

```text
Rare encounters
Loot quality
Chance meetings
Hidden quest discovery
Survival in uncertain events
Critical accidents
Bad omens
Mutation chances
Blessings and curses
```

Luck should be mysterious.

The player should often wonder:

> “Did I survive because I was skilled, or because I was lucky?”

---

# 2. Main Systems Overview

The full game is built around these major systems:

```text
1. Hidden Attributes
2. Natural Potential and Soft Caps
3. Training and Incremental Growth
4. Talents
5. Affinities
6. Skills and Proficiency
7. Traits and Trait Evolution
8. Insight and Observation
9. Bestiary and Knowledge Database
10. Combat
11. Magic Circuits and Mana
12. Equipment and Item Quality
13. Injuries and Recovery
14. Monster Species and Variants
15. Dynamic NPC Generation
16. Factions and Reputation
17. Procedural Quests
18. Time, Aging, and World Events
19. Permadeath and Legacy
20. Hidden World Lore
```

These systems should not feel separate. They should constantly interact.

Example:

A player with **Mana Sensitivity** and high **Insight** fights a strange goblin. They notice the goblin’s mana flow is abnormal. This updates the bestiary with a possible mutation warning. Later, a Mage Guild scholar pays for that information, increasing faction reputation. The player then unlocks a quest about goblin experiments.

That is the kind of interconnected gameplay **Grand Lunacy** should aim for.
