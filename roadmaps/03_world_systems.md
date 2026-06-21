# 10. Phase Eight — Insight and Hidden Information

## Purpose

Insight is one of the most important systems in the game.

It controls how much the player can understand about people, monsters, items, traps, magic, and social situations.

---

## Without Insight

The player sees:

```text
Unknown Goblin

STR: ???
AGI: ???
VIT: ???
Traits: ???
Weakness: ???
```

---

## With Low Insight

```text
Goblin

STR: F
AGI: ???
VIT: ???
Behavior: Nervous
```

---

## With Moderate Insight

```text
Goblin

STR: F
AGI: D
VIT: F
Behavior: Cowardly
Possible Weakness: Fire
```

---

## With High Insight

```text
Goblin Scout

STR: F+
AGI: D-
VIT: F
Trait: Cowardly
Skill: Crude Dagger Use
Weakness: Bright Light
Threat: Low alone, dangerous in groups
```

---

## With S-Rank Insight

```text
Goblin Scout

STR: 3.4
AGI: 11.7
VIT: 4.2
INT: 2.8
WIL: 2.1
CHA: 1.3
LUK: 2.9

Traits:
Cowardly
Pack-Minded

Skills:
Crude Dagger Use: Beginner
Ambush: Novice

Weakness:
Fire
Bright Light
Isolation

Notes:
Likely to flee if leader dies.
```

---

## Insight Accuracy

Insight should not always be correct.

Accuracy depends on:

```text
Insight skill
Intelligence
Experience with species
Bestiary knowledge
Enemy deception skill
Enemy concealment magic
Stress
Lighting
Distance
Injury
```

A deceptive noble may appear harmless.

A monster may suppress its aura.

A boss may overwhelm your analysis.

Example:

```text
Analysis Failed.

Reason:
Target’s presence is too unstable.
```

Or:

```text
Your assessment may be inaccurate.
```

This keeps mystery alive.

---

# 11. Phase Nine — Bestiary and Knowledge Database

## Purpose

The Bestiary is the player’s growing monster encyclopedia.

It should feel like a living research journal.

---

## How the Bestiary Improves

The player gains information by:

```text
Fighting monsters
Observing monsters
Reading books
Buying encyclopedias
Talking to hunters
Dissecting corpses
Studying tracks
Completing guild reports
Using Insight
Experimenting with weaknesses
```

---

## Bestiary Entry Example

```text
Goblin

Knowledge Level: 42%

Known Attributes:
STR: F
AGI: D
VIT: F

Known Traits:
Cowardly
Pack-Minded

Known Weaknesses:
Fire
Bright Light
Leader death causes panic

Known Variants:
Goblin Scout
Goblin Warrior
Goblin Shaman

Unknown:
Mutation cause
Goblin King behavior
```

---

## Knowledge Levels

| Knowledge % | What Player Knows         |
| ----------: | ------------------------- |
|          0% | Name only or nothing      |
|         10% | Basic appearance          |
|         25% | Rough attributes          |
|         40% | Common behavior           |
|         60% | Weaknesses and variants   |
|         80% | Skills, habitats, tactics |
|        100% | Full species profile      |

---

## Guild Reports

The player can sell information.

Example:

```text
You reported a new Goblin Shaman variant.

Hunter Guild Reputation +8
Gold +40
Bestiary Updated
```

False information should damage reputation.

---

# 12. Phase Ten — Monsters and Species

## Purpose

Monsters should have species baselines instead of levels.

Most monsters of the same species should be similar, unless they are variants, mutants, bosses, ancient individuals, or magically altered.

---

## Species Baseline Example

```text
Species: Goblin

Average Attributes:
STR: F
AGI: D
VIT: F
INT: F
WIL: F
CHA: F
LUK: F

Common Traits:
Cowardly
Pack-Minded
Opportunistic

Common Skills:
Crude Dagger Use
Ambush
Scavenging
```

---

## Variants

Variants are natural differences within a species.

```text
Goblin Scout
Higher AGI
Better Stealth

Goblin Warrior
Higher STR and VIT
Basic weapon training

Goblin Shaman
Higher INT and WIL
Primitive magic

Goblin Chief
Higher CHA and WIL
Leadership trait
```

---

## Mutants

Mutants break species expectations.

Example:

```text
Mutant Goblin

Expected:
STR: F

Actual:
STR: C

Warning:
Abnormal Individual
```

Mutants can happen because of:

```text
Magic pollution
Bloodline anomaly
Demonic influence
Ancient ruins
Forbidden experiments
Divine curse
Evolution pressure
```

---

## Bosses

Bosses should not just be “more stats.”

They should have:

```text
Unique traits
Unique talents
Unique skills
Special behavior
Environmental advantage
Lore significance
```

Example:

```text
Goblin King

Attributes:
STR: C
AGI: C
VIT: B
INT: D
WIL: C
CHA: B

Traits:
Tyrant
Pack Commander
Cruel Intelligence

Skills:
Crude War Strategy
Commanding Roar
Brutal Club Style

Special:
All nearby goblins gain morale while he lives.
```

---

# 13. Phase Eleven — Combat System

## Purpose

Combat should feel uncertain, dangerous, and information-driven.

The player should not simply compare levels.

They should ask:

```text
What is this enemy?
What do I know?
What terrain am I in?
Am I injured?
Do I have the right weapon?
Can I run?
Can I trick it?
Can I exploit a weakness?
```

---

## Combat Factors

Combat should consider:

```text
Attributes
Skills
Weapon quality
Armor quality
Talents
Traits
Fatigue
Injuries
Morale
Terrain
Weather
Knowledge
Luck
Companions
Ambush state
```

---

## Combat Flow

A text combat encounter could work like this:

```text
A Goblin Scout circles you with a rusted dagger.

1. Attack directly
2. Wait and observe
3. Use fire
4. Intimidate
5. Retreat
```

If the player chooses observe:

```text
You watch its footwork.

Bestiary Updated:
Goblin Scouts favor sudden lunges.
```

If the player uses fire:

```text
The goblin panics.

Weakness Confirmed:
Fire
```

---

## Clash Data

Repeated clashes improve accuracy.

Example:

First encounter:

```text
Goblin Scout
STR: ???
AGI: ???
```

After one fight:

```text
Goblin Scout
STR: F?
AGI: D?
```

After five fights:

```text
Goblin Scout
STR: F
AGI: D
VIT: F
```

After bestiary and insight:

```text
Goblin Scout
STR: F+
AGI: D-
VIT: F
```

---

# 14. Phase Twelve — Magic System

## Purpose

Magic should be deep, dangerous, and partly biological.

Not everyone can become a great mage.

Mana is affected by circuits, sensitivity, intelligence, willpower, affinity, and training.

---

## Magic Core Components

Every character may have:

```text
Mana Capacity
Mana Output
Mana Control
Mana Recovery
Circuit Count
Circuit Quality
Circuit Stability
Mana Sensitivity
Elemental Affinities
```

---

## Mana Circuits

Mana circuits are internal channels that move mana.

Example:

```text
Circuit Count: 7
Circuit Quality: C
Circuit Stability: D
```

A person with many unstable circuits may have high power but dangerous backlash.

A person with few high-quality circuits may have precise control but limited output.

---

## Mana Sensitivity

Mana Sensitivity is a talent.

It allows:

```text
Feeling mana
Seeing spell structure
Detecting hidden enchantments
Sensing magical beasts
Reading aura flow
Discovering abnormal mutations
```

High Mana Sensitivity plus high Insight should be very powerful.

---

## Spellcasting Formula

A spell’s effectiveness can depend on:

```text
INT
WIL
Mana Control skill
Element affinity
Spell proficiency
Circuit quality
Fatigue
Emotional state
```

Example:

```text
Firebolt Power =
INT × Fire Affinity Modifier × Fire Magic Skill × Mana Output
```

But the player should not see this formula directly.

They should see:

```text
Your firebolt forms poorly.
The mana resists you.
```

or:

```text
The flame gathers naturally, almost eagerly.
```

---

## Magic Backlash

Failed magic can cause:

```text
Mana burn
Circuit strain
Temporary blindness
Internal bleeding
Curse contamination
Memory damage
Soul fatigue
```

This makes magic powerful but risky.

---

# 15. Phase Thirteen — Equipment and Item Quality

## Purpose

Equipment should feel like part of the world, not just stat sticks.

A sword has:

```text
Material
Craftsmanship
Condition
History
Enchantments
Owner reputation
Hidden flaws
```

---

## Item Quality

| Quality    | Meaning                 |
| ---------- | ----------------------- |
| Trash      | Barely usable           |
| Poor       | Weak, damaged           |
| Common     | Standard                |
| Fine       | Well-made               |
| Excellent  | Professional quality    |
| Masterwork | Crafted by a master     |
| Legendary  | Historically powerful   |
| Mythic     | World-changing artifact |

---

## Weapon Example

```text
Iron Training Sword

Quality: Common
Condition: Worn
Damage Type: Slash
Balance: Average
Durability: 63%
Hidden Property: None
```

---

## Special Weapon Example

```text
Moonsteel Blade

Quality: Legendary
Condition: Perfect
Damage Type: Slash / Mana
Affinity: Shadow
History: Once held by the traitor knight of the old empire.
Hidden Property: Reacts to moonlight.
```

---

## Equipment Knowledge

The player may not know item quality immediately.

Without appraisal:

```text
Old Sword

Quality: ???
Property: ???
```

With appraisal:

```text
Old Sword

Quality: Masterwork
Hidden Enchantment: Blood Memory
Warning: Cursed
```

---

# 16. Phase Fourteen — Injuries and Recovery

## Purpose

Injuries make combat meaningful.

Instead of only losing HP, the player can suffer lasting consequences.

---

## Injury Types

```text
Bruised Ribs
Broken Arm
Sprained Ankle
Deep Cut
Concussion
Mana Burn
Poisoned Blood
Damaged Mana Circuit
Soul Fatigue
Curse Mark
Eye Injury
Internal Bleeding
```

---

## Injury Effects

```text
Broken Arm:
Swordsmanship reduced
Shield use disabled
Training limited

Sprained Ankle:
AGI reduced
Running training blocked
Dodge chance reduced

Mana Burn:
Magic output reduced
Spell failure chance increased

Concussion:
INT reduced
Insight accuracy reduced
Dialogue mistakes more likely
```

---

## Recovery System

Recovery depends on:

```text
VIT
Medicine skill
Healer access
Money
Rest quality
Nutrition
Trait effects
Magic treatment
Injury severity
```

A poor player with a broken arm may need weeks.

A noble with a healer may recover in days.

---

# 17. Phase Fifteen — Dynamic NPC Generation

## Purpose

NPCs should be generated like real people.

They should have:

```text
Birth background
Attributes
Potentials
Talents
Affinities
Traits
Skills
Goals
Fears
Faction ties
Relationships
Secrets
```

---

## NPC Example

```text
Name: Elian Voss
Age: 17
Background: Fallen noble child

Visible:
Polite, quiet, sickly

Hidden:
INT Potential: A
WIL Potential: S
Talent: Curse Affinity
Trait: Resentful
Secret: His family practices forbidden rituals.
```

---

## NPC Growth

NPCs should train and change over time.

A rival should not wait for the player.

Example:

```text
Month 1:
Rival is Apprentice swordsman.

Month 6:
Rival becomes Adept.

Month 12:
Rival joins royal knights.

Month 24:
Rival unlocks Sword Aura.
```

This makes the world feel alive.

---

# 18. Phase Sixteen — Factions and Reputation

## Purpose

Reputation should be separate for each group.

Being loved by commoners may make nobles hate you.

Being respected by assassins may make the church suspicious.

---

## Faction Types

```text
Kingdoms
Noble Houses
Mage Guild
Hunter Guild
Merchant Guild
Church
Criminal Syndicates
Academies
Mercenary Companies
Monster Research Societies
Ancient Cults
```

---

## Reputation Example

```text
Hunter Guild: +45
Mage Guild: +10
Church: -20
House Valemont: -60
Commoners: +35
Criminal Underworld: +5
```

---

## Reputation Effects

Reputation affects:

```text
Quest access
Prices
Mentors
Arrests
Assassination attempts
Marriage offers
Guild ranks
Rumors
Companion recruitment
Political influence
```

Example:

```text
House Valemont Reputation: -60

Effect:
Valemont knights may challenge you.
Valemont merchants refuse service.
Valemont spies track your movement.
```

---

# 19. Phase Seventeen — Procedural Quest System

## Purpose

Quests should emerge from the world, not just be fixed scripts.

A village with missing children, rising monster activity, and a corrupt lord can generate multiple possible quest lines.

---

## Quest Components

A quest should have:

```text
Requester
Location
Problem
Hidden cause
Time limit
Possible solutions
Faction impact
Consequences
Follow-up events
```

---

## Example Quest

```text
Quest:
Missing Children of Greyfen

Surface Problem:
Children have vanished near the forest.

Possible Causes:
Goblin kidnapping
Cult ritual
Noble experiment
Beast migration
False accusation

Possible Solutions:
Track footprints
Question villagers
Interrogate lord
Search forest
Use mana detection
Set trap
Ignore quest
Exploit panic for money
```

---

## Quest Consequences

If solved well:

```text
Village Reputation +30
Hunter Guild +10
Bestiary Updated
```

If ignored:

```text
Children die
Village population decreases
Goblin tribe grows stronger
Future quest becomes harder
```

If solved cruelly:

```text
Village saved
Commoner fear increases
Church suspicion increases
Trait shift toward Cold Hearted
```

---

# 20. Phase Eighteen — Time and Aging

## Purpose

Time should matter.

Every action takes time.

Training, travel, healing, studying, and quests should move the calendar forward.

---

## Time Units

Use:

```text
Morning
Afternoon
Evening
Night
```

or:

```text
Hours
Days
Weeks
Months
Years
```

For a text RPG, start simple:

```text
1 action = part of a day
4 actions = 1 day
30 days = 1 month
12 months = 1 year
```

---

## Aging Effects

As characters age:

Child:

```text
Fast growth
Low strength
High potential discovery
```

Young adult:

```text
Peak training speed
Fast combat growth
```

Middle age:

```text
Stable power
Better mental skills
Slower physical growth
```

Old age:

```text
STR decreases
AGI decreases
VIT decreases
INT may increase
WIL may increase
Skill efficiency remains high
```

---

## World Events

Time causes events:

```text
Wars
Monster migrations
Guild elections
Noble marriages
Plagues
Academy exams
Tournament seasons
Assassinations
Cult awakenings
Ruins opening
```

The player can miss events.

That is good.

It makes the world feel real.

---

# 21. Phase Nineteen — Permadeath and Legacy

## Purpose

Death should matter, but it should not delete all progress.

The world continues.

The player leaves behind a legacy.

---

## What Can Be Inherited

```text
Family name
Money
Property
Weapons
Books
Bestiary data
Faction reputation
Enemies
Allies
Techniques
Curses
Blessings
Bloodline mutations
Political consequences
```

---

## Legacy Example

First character:

```text
Name: Daren
Trait: Obsessive
Founded a monster research guild
Died fighting a mutant troll
```

Second character:

```text
Name: Mira
Relation: Daren’s niece

Inherited:
Partial bestiary
Guild access
Daren’s damaged sword
Family reputation
Troll hatred trait possibility
```

This makes death part of the story instead of just failure.

---

# 22. Phase Twenty — Hidden World Lore

## Purpose

The deepest layer of **Grand Lunacy** should be discovery.

The player starts thinking the world is simple:

```text
Monsters exist.
Magic exists.
Guilds exist.
Nobles rule.
```

But deeper exploration reveals:

```text
The world may be artificial.
The attribute system may have an origin.
Luck may be controlled by something.
Mutations may not be random.
The bestiary may be hiding forbidden species.
Some NPCs may know they are inside a system.
```

---

## Lore Layers

### Surface Lore

```text
Kingdoms
Guilds
Monsters
Magic
Noble houses
```

### Hidden Lore

```text
Ancient civilizations
Forbidden bloodlines
Original magic source
Lost gods
Mana corruption
System fragments
```

### Deep Lore

```text
Why attributes exist
Why Luck behaves differently
Why some people awaken talents
Why monsters mutate
Why the world is called Grand Lunacy
```
