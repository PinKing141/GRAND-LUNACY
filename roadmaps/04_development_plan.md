# 23. Development Roadmap

Now, in actual build order.

## MVP 1 — Playable Skeleton

Goal: Make the game playable in terminal.

Build:

- [x] Character creation
- [x] Hidden attributes
- [x] Visible grade system
- [x] Basic training
- [x] Basic monsters
- [x] Basic combat
- [x] Basic inspection
- [x] Save/load

Player should be able to:

- [x] Create character
- [x] Train
- [x] Inspect monster
- [x] Fight monster
- [x] Gain encounter data
- [x] View rough character sheet
- [x] Quit and reload

---

## MVP 2 — Growth System

Add:

```text
[x] Natural potentials
[x] Soft caps
[x] Training fatigue
[x] Recovery
[x] Training messages
[x] Attribute growth formulas
```

Player should feel:

> “My character is improving, but not infinitely. I need better methods.”

---

## MVP 3 — Skills and Talents

Add:

```text
[x] Skill proficiency
[x] Skill ranks
[x] Talents
[x] Talent multipliers
[x] Talent discovery
[x] Basic talent list
```

Player should feel:

> “My character is different from other characters.”

---

## MVP 4 — Insight and Bestiary

Add:

```text
[x] Insight skill
[x] Monster knowledge levels
[x] Bestiary entries
[x] Knowledge from fights
[x] Knowledge from books
[x] Inaccurate estimates
```

Player should feel:

> “I am learning the world, not just killing things.”

---

## MVP 5 — Better Combat

Add:

```text
[x] Combat choices
[x] Observe action
[x] Retreat action
[x] Weaknesses
[x] Terrain
[x] Injuries
[x] Basic equipment
[x] Enemy behavior
```

Player should feel:

> “Combat is a decision, not a stat check.”

---

## MVP 6 — Magic and Affinity

Add:

```text
Mana circuits
Mana sensitivity
Element affinities
Mana control skill
Basic spells
Magic backlash
Spell learning
```

Player should feel:

> “Magic is powerful, but my body and talent determine how safely I can use it.”

---

## MVP 7 — NPCs and Factions

Add:

```text
NPC generation
NPC traits
NPC talents
Guilds
Reputation
Faction quests
Mentors
Merchants
```

Player should feel:

> “The world has people with their own power, motives, and growth.”

---

## MVP 8 — Procedural Quests

Add:

```text
Village quests
Monster quests
Investigation quests
Faction quests
Consequences
Time limits
Quest failure
```

Player should feel:

> “My choices affect the world.”

---

## MVP 9 — Time, Aging, and Legacy

Add:

```text
Calendar
Aging
Long-term NPC growth
Permadeath
Inheritance
Family reputation
Legacy save data
```

Player should feel:

> “This is bigger than one character.”

---

## MVP 10 — Full Grand Lunacy Alpha

Add:

```text
Hidden lore
Bosses
Mutants
Advanced bestiary
Advanced traits
Advanced equipment
Rare events
Multiple regions
Major faction conflicts
World events
```

Player should feel:

> “This is a living world full of secrets.”

---

# 24. Suggested Code Structure

For the Python version, eventually split the game into files like this:

```text
grand_lunacy/
│
├── main.py
├── game.py
├── save_system.py
│
├── core/
│   ├── attributes.py
│   ├── grades.py
│   ├── character.py
│   ├── time.py
│
├── systems/
│   ├── training.py
│   ├── combat.py
│   ├── insight.py
│   ├── bestiary.py
│   ├── magic.py
│   ├── injury.py
│   ├── reputation.py
│   ├── quests.py
│
├── data/
│   ├── species.json
│   ├── talents.json
│   ├── traits.json
│   ├── skills.json
│   ├── items.json
│   ├── factions.json
│
├── world/
│   ├── locations.py
│   ├── factions.py
│   ├── npc_generator.py
│   ├── events.py
│
└── ui/
    ├── menus.py
    ├── text_display.py
```

Do not keep everything in one file once the prototype grows.

The current prototype is fine as a starting point, but the full game needs structure.

---

# 25. Final Game Loop

The final player loop should look like this:

```text
Wake up
↓
Choose how to spend time
↓
Train, study, work, travel, investigate, rest, or quest
↓
Encounter people, monsters, events, or opportunities
↓
Make decisions with incomplete information
↓
Gain knowledge, injuries, skills, reputation, or trauma
↓
World updates
↓
Time passes
↓
Character changes
↓
Eventually die, retire, ascend, disappear, or leave legacy
↓
World continues
```

That is the heart of **Grand Lunacy**.

The game should not ask:

> “What level are you?”

It should ask:

> “What do you know?”
> “What have you survived?”
> “What are you naturally gifted at?”
> “What have you sacrificed?”
> “Who remembers your name after you die?”

Yes — that changes the design in a **better** direction.

So **Grand Lunacy should not be a procedural sandbox first**.

It should be:

> **A linear-ish dark fantasy text RPG with a fixed main story, hidden stat systems, branching routes, and multiple endings based on what the player learns, who they side with, who survives, and what major threats are allowed to grow.**

So the world can still feel alive, but the **main story is authored**, not random.
