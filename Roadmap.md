# Grand Lunacy — Full Detailed Roadmap

## Split Roadmaps

This full roadmap has also been split into smaller roadmap files:

- [roadmaps/01_foundations.md](roadmaps/01_foundations.md)
- [roadmaps/02_character_systems.md](roadmaps/02_character_systems.md)
- [roadmaps/03_world_systems.md](roadmaps/03_world_systems.md)
- [roadmaps/04_development_plan.md](roadmaps/04_development_plan.md)
- [roadmaps/05_story_direction.md](roadmaps/05_story_direction.md)

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

---

# 3. Phase One — Core Attribute System

## Purpose

Attributes define the raw body, mind, and soul of every living being.

Attributes are not skills. They are natural capability.

A person with high Strength hits harder.

A person with high Intelligence learns complex magic faster.

A person with high Willpower resists fear, pain, curses, and mental attacks.

---

## Core Attributes

| Attribute | Meaning      | Affects                                                 |
| --------- | ------------ | ------------------------------------------------------- |
| STR       | Strength     | Physical damage, lifting, grappling, heavy weapons      |
| AGI       | Agility      | Speed, dodging, reflexes, accuracy, balance             |
| VIT       | Vitality     | Health, stamina, poison resistance, recovery            |
| INT       | Intelligence | Magic theory, learning, crafting, tactics               |
| WIL       | Willpower    | Aura, fear resistance, pain tolerance, curse resistance |
| CHA       | Charisma     | Leadership, persuasion, intimidation, acting            |
| LUK       | Luck         | Rare events, loot, chance, fate interference            |

---

## Hidden Numerical Values

Internally, stats should be decimal-based.

Example:

```text
STR: 7.4
AGI: 11.2
VIT: 8.9
INT: 15.3
WIL: 13.0
CHA: 6.1
LUK: 3.8
```

The decimal system matters because training gives small improvements.

Running might give:

```text
AGI +0.1
VIT +0.05
```

Sword sparring might give:

```text
STR +0.03
AGI +0.02
WIL +0.01
Swordsmanship +0.2%
```

This creates a slow-burn progression system.

---

## Attribute Grades

The player does not see the exact decimal values unless they have special tools or skills.

Use grades instead:

| Grade | Internal Range | Meaning                      |
| ----- | -------------: | ---------------------------- |
| F     |          0–4.9 | Very weak                    |
| E     |          5–9.9 | Normal civilian              |
| D     |        10–19.9 | Trained human                |
| C     |        20–39.9 | Elite human                  |
| B     |        40–79.9 | Superhuman                   |
| A     |       80–159.9 | Legendary                    |
| S     |           160+ | Monster, saint, mythic being |

You can also add plus/minus grades later:

```text
F-
F
F+
E-
E
E+
D-
D
D+
...
S
```

But early prototype should keep it simple.

---

## Player Visibility

At the start, the player may only know their own approximate stats.

Example:

```text
Your Body Assessment

STR: E
AGI: D
VIT: E
INT: D
WIL: C
CHA: E
LUK: ???
```

Luck should often remain hidden.

The player can learn more through:

```text
Medical examination
Magic appraisal
Guild testing
Insight skill
Special artifacts
Academy exams
Combat experience
```

---

# 4. Phase Two — Natural Potential and Soft Caps

## Purpose

Potential determines how far someone can naturally grow.

This is important because **Grand Lunacy** is not just about current power.

A weak child with S-rank potential may become terrifying.

A strong adult with low potential may already be near their limit.

---

## Potential Ranks

Every attribute has a hidden potential rank.

Example:

```text
STR Potential: C
AGI Potential: A
VIT Potential: B
INT Potential: D
WIL Potential: S
CHA Potential: E
LUK Potential: Unknown
```

Potential affects:

```text
Natural attribute cap
Training speed
Chance of awakening related talents
How well the person responds to mentors
How hard limit-breaking becomes
```

---

## Potential to Natural Cap

Example scale:

| Potential | Natural Cap |
| --------- | ----------: |
| F         |           5 |
| E         |          10 |
| D         |          20 |
| C         |          40 |
| B         |          80 |
| A         |         160 |
| S         |         320 |

This mirrors the attribute grade scale.

A person with **C-rank Strength potential** can naturally reach around **40 STR**, but reaching beyond that requires something abnormal.

---

## Soft Cap Behavior

Growth should slow as the character approaches their natural cap.

Example:

```text
Natural STR Cap: 40
Current STR: 20
Training Gain: Normal

Current STR: 35
Training Gain: Reduced

Current STR: 39
Training Gain: Tiny

Current STR: 40
Training Gain: Blocked
```

This means normal training cannot make everyone endlessly stronger.

---

## Example Formula

A simple growth formula:

```text
actual_gain = base_gain × talent_multiplier × motivation_multiplier × cap_penalty
```

Where:

```text
cap_penalty = 1 - current_stat / natural_cap
```

Example:

```text
Base Gain: 0.10
Current STR: 30
Natural Cap: 40

cap_penalty = 1 - 30/40
cap_penalty = 0.25

actual_gain = 0.10 × 0.25
actual_gain = 0.025
```

So the closer you are to your limit, the slower growth becomes.

---

## Limit Breaking

To surpass natural caps, the player needs rare events.

Examples:

```text
Ancient Body Refinement Ritual
Raises STR and VIT caps.

Near-Death Awakening
Raises WIL cap.

Dragon Blood Infusion
Raises VIT, STR, and mana resistance caps.

Sword Saint Mentorship
Raises Swordsmanship skill cap.

Forbidden Mana Surgery
Raises mana circuit capacity but may cause permanent injury.
```

Limit breaking should feel dangerous, expensive, rare, or story-significant.

---

# 5. Phase Three — Training and Growth

## Purpose

Growth comes from action, not XP.

The player improves by doing things.

---

## Training Types

| Training        | Attributes Improved | Skills Improved            |
| --------------- | ------------------- | -------------------------- |
| Running         | AGI, VIT            | Athletics                  |
| Weight Training | STR, VIT            | Body Control               |
| Meditation      | WIL                 | Mana Control, Aura Control |
| Reading         | INT                 | Scholarship                |
| Sword Sparring  | STR, AGI, WIL       | Swordsmanship              |
| Acting Practice | CHA, WIL            | Acting, Deception          |
| Hunting         | AGI, WIL            | Tracking, Stealth, Archery |
| Magic Study     | INT, WIL            | Magic Theory, Mana Control |
| Public Speaking | CHA, WIL            | Leadership, Persuasion     |

---

## Training Fatigue

Training should not be infinite.

Each action adds fatigue.

```text
Fatigue: 0–100
```

At high fatigue:

```text
Training gains decrease
Injury chance increases
Combat performance drops
Mental stress rises
```

Example:

```text
Fatigue 0–30: Normal
Fatigue 31–60: Slight penalty
Fatigue 61–80: Major penalty
Fatigue 81–100: Injury risk
```

---

## Recovery

Recovery depends on:

```text
Vitality
Food quality
Sleep
Medicine
Healers
Traits
Injuries
Stress
Environment
```

A rich noble recovers faster because they have better food, beds, and doctors.

A poor adventurer recovers slower unless they build connections or earn money.

---

## Training Plateaus

Training should eventually produce messages like:

```text
Your body no longer responds to ordinary running.
You may need harsher terrain, a mentor, better technique, or a breakthrough.
```

This tells the player they hit a soft cap without showing exact numbers.

---

# 6. Phase Four — Talents

## Purpose

Talents are innate gifts or rare awakened abilities.

They determine what someone learns easily, what ceilings they can surpass, and what hidden paths they can access.

Talents are different from skills.

A person can have **Sword Genius** but still be bad at swordsmanship if they never train.

A person can have no talent but still become competent through discipline.

---

## Talent Categories

### Combat Talents

```text
Sword Genius
Spear Genius
Bow Prodigy
Battle Instinct
Perfect Balance
Predator Reflexes
Heavy Weapon Affinity
Duelist’s Eye
```

### Magic Talents

```text
Mana Sensitivity
Mana Vessel
Spell Formation Genius
Elemental Child
Arcane Memory
Ritual Intuition
Curse Affinity
Mana Compression Talent
```

### Social Talents

```text
Silver Tongue
Acting Genius
Born Leader
Natural Liar
Noble Presence
Crowd Reader
Emotional Mimicry
```

### Craft Talents

```text
Blacksmith Genius
Alchemy Intuition
Runic Designer
Architectural Mind
Herbalist’s Nose
Perfect Hands
```

### Mental Talents

```text
Perfect Memory
Fast Learner
Strategic Mind
Pattern Recognition
Pain Compartmentalization
Cold Calculation
```

### Rare/Fate Talents

```text
Chosen by Misfortune
Fate Distortion
Heavenly Luck
Cursed Survivor
Worldline Awareness
Forbidden Vessel
```

---

## Talent Rarity

| Rarity    | Meaning                           |
| --------- | --------------------------------- |
| Common    | Noticeable but not world-changing |
| Uncommon  | Strong advantage                  |
| Rare      | Can define a career               |
| Epic      | Marks a prodigy                   |
| Legendary | Known across nations              |
| Mythic    | Changes history                   |

---

## Talent Effects

A talent can affect:

```text
Skill growth speed
Attribute growth speed
Soft cap resistance
Unlock requirements
Insight clarity
Combat instincts
NPC reactions
Rare event access
```

Example:

```text
Sword Genius

Effects:
Swordsmanship growth ×3
Sword-related comprehension improved
Can learn advanced sword techniques earlier
May detect flaws in enemy sword styles
Slightly raises AGI and WIL growth from sword training
```

Example:

```text
Mana Sensitivity

Effects:
Can feel mana nearby
Mana Control growth ×2
Can detect hidden spells with enough Insight
Improves magical research
May notice abnormal monsters before combat
```

Example:

```text
Acting Genius

Effects:
Acting growth ×3
Deception growth ×2
Can imitate accents, emotions, and noble etiquette faster
Improves infiltration quests
Can hide fear, pain, or killing intent better
```

---

## Talent Discovery

The player should not always know their talents immediately.

Discovery methods:

```text
Repeated training
Dangerous situation
Guild examination
Master observation
Magical appraisal
Academy test
Near-death crisis
Hidden bloodline awakening
```

Example:

```text
After surviving the duel, something clicks.

Talent Discovered:
Battle Instinct
```

Or:

```text
The mage examiner stares at you.

"You can see the mana threads, can't you?"

Talent Discovered:
Mana Sensitivity
```

---

## Talent Evolution

Talents should evolve if conditions are met.

Example path:

```text
Sword Genius
→ Blade Prodigy
→ Sword Saint Candidate
→ Sword Saint’s Vessel
```

Another:

```text
Mana Sensitivity
→ Mana Sight
→ Arcane Perception
→ World Thread Vision
```

Evolution should require:

```text
High skill proficiency
Specific life events
Extreme stress
Mentorship
Rare items
Lore discoveries
```

---

# 7. Phase Five — Affinities

## Purpose

Affinities are natural compatibility.

Talent means:

> “You learn this well.”

Affinity means:

> “This suits your nature.”

A person can have a talent for magic but poor fire affinity.

A person can have high sword affinity but no Sword Genius.

---

## Affinity Types

### Weapon Affinities

```text
Sword
Spear
Bow
Dagger
Axe
Greatsword
Rapier
Shield
Unarmed
Staff
```

### Magic Affinities

```text
Fire
Water
Wind
Earth
Lightning
Ice
Shadow
Light
Nature
Blood
Space
Curse
Illusion
Gravity
```

### Craft Affinities

```text
Blacksmithing
Alchemy
Enchanting
Runes
Tailoring
Cooking
Architecture
Medicine
```

### Social Affinities

```text
Leadership
Politics
Commerce
Teaching
Acting
Deception
Diplomacy
Intimidation
```

---

## Affinity Ranks

Use:

```text
F, E, D, C, B, A, S
```

Example:

```text
Sword Affinity: B
Dagger Affinity: D
Fire Affinity: F
Shadow Affinity: A
Politics Affinity: C
Acting Affinity: S
```

---

## Affinity Effects

Affinity affects:

```text
Mana cost
Technique compatibility
Learning comfort
Failure chance
Spell stability
Weapon handling
Emotional resonance
```

Example:

A player with **Fire Affinity F** can still learn fire magic, but:

```text
Higher mana cost
Slower spell formation
Higher backlash risk
Weaker output
```

A player with **Shadow Affinity A**:

```text
Lower mana cost
Faster learning
Better stealth magic
More compatible with curses and hidden arts
```

---

# 8. Phase Six — Skills and Proficiency

## Purpose

Skills represent practiced ability.

Attributes are raw stats.

Talents are gifts.

Affinities are compatibility.

Skills are earned.

---

## Skill Examples

### Combat Skills

```text
Swordsmanship
Spear Arts
Archery
Unarmed Combat
Shield Handling
Mounted Combat
Assassination
Battlefield Tactics
```

### Magic Skills

```text
Mana Control
Magic Theory
Fire Magic
Shadow Magic
Healing Magic
Curse Craft
Ritual Magic
Enchanting
```

### Survival Skills

```text
Tracking
Stealth
Foraging
Hunting
Camping
Climbing
Swimming
Navigation
```

### Social Skills

```text
Persuasion
Deception
Acting
Leadership
Negotiation
Etiquette
Intimidation
Seduction
Interrogation
```

### Craft Skills

```text
Blacksmithing
Alchemy
Cooking
Medicine
Tailoring
Carpentry
Runecraft
Engineering
```

---

## Proficiency Percentage

Internally:

```text
Swordsmanship: 37.4%
```

Player sees rank:

```text
Swordsmanship: Apprentice
```

---

## Skill Ranks

| Rank        |    Range |
| ----------- | -------: |
| Untrained   |   0–4.9% |
| Beginner    |  5–14.9% |
| Novice      | 15–29.9% |
| Apprentice  | 30–49.9% |
| Adept       | 50–69.9% |
| Expert      | 70–84.9% |
| Master      | 85–94.9% |
| Grandmaster | 95–99.4% |
| Saint       |   99.5%+ |

Saint rank should be extremely rare.

Not every skill should even have living Saints.

---

## Skill Branching

At higher ranks, skills branch.

Swordsmanship:

```text
Basic Swordsmanship
→ Knight Swordsmanship
→ Duelist Swordsmanship
→ Heavy Blade Style
→ Phantom Step Sword
→ Royal Sword Art
→ Forbidden Blood Sword
```

Magic:

```text
Mana Control
→ Elemental Control
→ Fire Magic
→ Blue Flame Magic
→ Soul Flame Magic
```

Acting:

```text
Acting
→ Court Acting
→ Street Performance
→ Disguise
→ Identity Theft
→ Perfect Persona
```

---

## Style System

For weapons, do not just have generic “Swordsmanship.”

Add styles.

Example:

```text
Iron Wolf Sword Style
Focus: defense, counterattacks, endurance

Moonlit Step Sword Style
Focus: speed, evasion, precision

Royal Execution Sword Style
Focus: heavy decisive attacks

Silent Fang Sword Style
Focus: assassination and weak points
```

A player can learn multiple styles, but each style has its own proficiency.

Example:

```text
Swordsmanship: Adept
Iron Wolf Style: Apprentice
Moonlit Step Style: Beginner
```

---

# 9. Phase Seven — Traits

## Purpose

Traits describe personality, habits, trauma, social behavior, mental tendencies, and life circumstances.

Traits should affect dialogue, training, stress, relationships, combat decisions, and quest options.

---

## Trait Types

### Personality Traits

```text
Cold Hearted
Obsessive
Bossy
Sarcastic
Patient
Arrogant
Humble
Greedy
Disciplined
Reckless
```

### Emotional Traits

```text
Fearful
Brave
Numb
Wrathful
Anxious
Calm Under Pressure
Guilt-Ridden
Vengeful
```

### Social Traits

```text
Young and Bossy
Noble-Bred
Street Rat
Commanding Presence
Awkward Speaker
Charming Smile
Untrustworthy Aura
```

### Trauma Traits

```text
Abandonment Wound
Survivor’s Guilt
Battle Shock
Fear of Fire
Hatred of Nobles
Monster Phobia
```

### Physical Traits

```text
Sickly
Tall Frame
Fragile Bones
Strong Lungs
Scarred Face
One-Eyed
Heavy Sleeper
Light Sleeper
```

### Moral Traits

```text
Merciful
Cruel
Pragmatic
Honorable
Deceitful
Self-Sacrificing
Opportunistic
```

---

## Example Trait Effects

```text
Cold Hearted

Effects:
Fear resistance increased
Guilt gain reduced
Empathy-based dialogue locked more often
Intimidation improved
Companion affection grows slower
```

```text
Obsessive

Effects:
Repeated training gives bonus growth
Stress increases faster when goal is blocked
Harder to abandon quests
Higher chance to discover hidden techniques through repetition
```

```text
Young and Bossy

Effects:
Leadership attempts are more forceful
Older NPCs may dislike you
Timid NPCs may obey faster
Noble children may respect you
Diplomacy becomes harder
Command-based options appear earlier
```

```text
Bossy

Effects:
Leadership growth increased
Persuasion sometimes penalized
Subordinates with weak Willpower comply more easily
Proud allies lose affection faster
```

---

## Trait Evolution

Traits should change through play.

Example:

```text
Cowardly
→ Cautious
→ Survivor
```

Or:

```text
Brave
→ Fearless
→ Reckless Hero
```

Or:

```text
Obsessive
→ Single-Minded
→ Monomaniac
```

Or:

```text
Cold Hearted
→ Emotionally Severed
→ Inhuman Composure
```

Evolution depends on repeated decisions.

If the player constantly chooses ruthless options, traits should reflect that.

---

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

---

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
Natural potentials
Soft caps
Training fatigue
Recovery
Training messages
Attribute growth formulas
```

Player should feel:

> “My character is improving, but not infinitely. I need better methods.”

---

## MVP 3 — Skills and Talents

Add:

```text
Skill proficiency
Skill ranks
Talents
Talent multipliers
Talent discovery
Basic talent list
```

Player should feel:

> “My character is different from other characters.”

---

## MVP 4 — Insight and Bestiary

Add:

```text
Insight skill
Monster knowledge levels
Bestiary entries
Knowledge from fights
Knowledge from books
Inaccurate estimates
```

Player should feel:

> “I am learning the world, not just killing things.”

---

## MVP 5 — Better Combat

Add:

```text
Combat choices
Observe action
Retreat action
Weaknesses
Terrain
Injuries
Basic equipment
Enemy behavior
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

---

# Grand Lunacy — Corrected Story Direction

## Core Game Type

**Grand Lunacy** is now:

```text
Genre:
Dark fantasy / academy / kingdom / demon invasion / hidden-system RPG

Structure:
Linear main story with branching routes

Gameplay:
Text-based choices, training, investigation, combat, relationships, hidden stats

Progression:
No levels. Attributes, skills, talents, traits, insight, reputation, and knowledge.

Ending Style:
Multiple endings based on choices, alliances, failures, corruption, and story flags.
```

The player is not just wandering around forever doing random quests.

The player is inside a story that is moving forward whether they understand it or not.

---

# The Main Story Premise

The world of **Grand Lunacy** is approaching a hidden collapse.

On the surface, the kingdom is dealing with:

```text
Noble politics
Monster activity
Academy rivalries
Guild conflict
Religious tension
Border wars
Strange mutations
Missing villages
Forbidden magic
```

But underneath all of that, several possible world-ending routes are forming.

The player does not know at first which threat is the “true” threat.

That is where the game becomes interesting.

---

# The Major Ending Threats

These are not random. These are major authored story routes.

## 1. The Demon King Rising Ending

This is the classic apocalypse route.

A forgotten Demon King begins returning through:

```text
Demonic cults
Monster mutations
Possessed nobles
Corrupted mana zones
Ancient seals weakening
Demon-blood experiments
```

At first, the player may only see small signs.

Example:

```text
A goblin has abnormal strength.
A village reports black flames.
A priest goes missing.
A noble house starts buying monster corpses.
A dungeon seal cracks.
```

If the player ignores too much, fails key quests, or sides with the wrong people, the Demon King eventually rises.

### Ending Result

```text
Ending: Demon King Ascension

The ancient seal breaks.
The Demon King returns.
The kingdoms collapse one by one.
The player either dies, becomes a demon servant, or survives in a ruined world.
```

This can be a bad ending, but also maybe a secret route if the player intentionally helps it happen.

---

## 2. The Evil Prince Emperor Ending

This one is more political.

There is an **evil prince** who is secretly working with demons.

He is not obviously evil at first.

He might seem like:

```text
A reformer
A strong leader
A victim of court politics
A charming royal
Someone who wants to protect the kingdom
```

But behind the scenes, he is making deals with demons to secure the throne.

He believes:

> “If demons are inevitable, then humanity should survive by kneeling first.”

Or even darker:

> “A controlled hell is better than a chaotic world.”

If he becomes emperor, the world does not end immediately through destruction. It ends through corruption.

### His Route

The player may:

```text
Expose him
Serve him
Be manipulated by him
Become his assassin
Become his general
Become his enemy
Help him take the throne without realizing the truth
```

### Ending Result

```text
Ending: The Demon Emperor

The prince becomes emperor.
The empire unites under demonic contracts.
Humanity survives physically, but loses its freedom.
Demons rule through law, blood contracts, and noble houses.
```

This is a great ending because it is not just “the world explodes.”

It is worse in a political way.

The world continues, but it becomes a prison.

---

## 3. The Player Becomes the Villain Ending

This is important.

The player should not only be able to stop evil.

The player should be able to **become** evil.

Through choices, traits, corruption, reputation, forbidden magic, and cruelty, the player can slowly turn into the villain of the story.

This should not happen from one choice.

It should happen gradually.

Example path:

```text
You kill enemies unnecessarily.
You use forbidden magic.
You sacrifice allies for power.
You manipulate factions.
You accept demonic help.
You silence witnesses.
You become feared by commoners.
The Church marks you.
The Hunter Guild places a bounty.
Former companions leave you.
```

Eventually, the game stops treating you like a hero.

It treats you like a threat.

### Ending Result

```text
Ending: Hunted Monster

The world names you a calamity.
Old allies become enemies.
Heroes, knights, assassins, and saints hunt you down.
You either die, escape into legend, become a demon lord, or destroy the people chasing you.
```

This is one of the strongest routes because it makes the player’s own choices the final boss.

---

## 4. Killed by a Crazy Person Ending

This is actually a very good idea because it makes the world feel dangerous.

Not every ending should be grand.

Sometimes the player should die because they underestimated the wrong person.

This “crazy person” could be:

```text
A failed hero candidate
A jealous academy student
A cursed commoner
A serial killer noble
A demon-touched priest
A broken adventurer
A rejected companion
A mentally unstable genius
```

The player might ignore the signs.

Example:

```text
They keep appearing near crime scenes.
They ask strange questions.
Their Insight reading is unstable.
NPCs mention disappearances.
They become obsessed with the player.
They react badly if humiliated.
```

If the player keeps provoking, ignoring, or trusting them, it can lead to a sudden bad ending.

### Ending Result

```text
Ending: Meaningless Death

You were not killed by a Demon King.
You were not killed by an emperor.
You were killed in an alley by someone the world forgot to fear.
```

This is dark, but it fits **Grand Lunacy** perfectly.

Because in this game, danger is not always obvious.

---

# The Correct Structure: Linear Story With Branches

Instead of a procedural world, use **Acts**.

## Act 1 — Awakening / Arrival

The player enters or begins in the world.

Focus:

```text
Learning attributes
Discovering hidden stats
First monster encounter
First academy/guild/city introduction
First signs of abnormal monsters
Meeting major characters
```

Major story question:

> “What kind of person are you going to become?”

---

## Act 2 — Academy / Guild / Noble Politics

The player begins building their identity.

Possible paths:

```text
Academy student
Guild adventurer
Noble retainer
Mercenary
Mage apprentice
Criminal associate
Church agent
Prince supporter
```

This act introduces the evil prince, rivals, mentors, factions, and early demon signs.

Major story question:

> “Who do you trust?”

---

## Act 3 — First Major Crisis

A major event reveals the world is not normal.

Possible crisis:

```text
Monster wave
Academy attack
Noble assassination
Demon cult ritual
Dungeon break
Village massacre
Mana corruption outbreak
```

This is where the player learns that something bigger is happening.

Major story question:

> “Will you protect people, exploit chaos, or chase power?”

---

## Act 4 — Faction War

The kingdom starts splitting.

Factions begin moving openly.

```text
The prince makes his move.
The Church starts purging suspects.
The Mage Guild hides forbidden research.
Noble houses choose sides.
Demon cults become bolder.
Monster mutations increase.
```

The player’s reputation now matters heavily.

Major story question:

> “Whose side are you really on?”

---

## Act 5 — Revelation

The truth becomes clearer.

The player can discover:

```text
The prince is working with demons.
The Demon King’s seal is weakening.
Certain noble houses knew for years.
Some guilds have been selling monster data.
The Church may have hidden the truth.
The player may have a unique talent/bloodline/system connection.
```

Major story question:

> “Do you reveal the truth, hide it, sell it, or use it?”

---

## Act 6 — Final Route Lock

At this point, the game decides which ending route is active based on choices.

Possible locked routes:

```text
Hero Route
Anti-Hero Route
Prince Route
Demon Route
Villain Route
Tragic Death Route
Neutral Survivor Route
Secret Truth Route
```

Major story question:

> “Can you survive the consequences of who you became?”

---

## Act 7 — Ending

The final act depends on route.

Possible finales:

```text
Fight the Demon King
Stop the prince’s coronation
Serve the prince and crush rebels
Escape the kingdom as a wanted villain
Kill your former companions
Be assassinated by the obsessed madman
Sacrifice yourself to reseal the Demon King
Become ruler yourself
Expose the truth behind the world
```

---

# Major Character Roles

You need a fixed cast.

Not random NPCs.

## 1. The Evil Prince

Role:

```text
Political antagonist
Possible ally
Possible final villain
Possible emperor
```

He should be charming, intelligent, and dangerous.

He should not be cartoon evil.

He believes the world is already doomed, so he chooses the winning side early.

Possible traits:

```text
Charismatic
Cold Hearted
Patient
Noble-Bred
Strategic Mind
Demonic Contract Bearer
```

Possible talents:

```text
Born Leader
Silver Tongue
Contract Magic Affinity
Political Genius
```

---

## 2. The Demon King

Role:

```text
Ancient final threat
Mythic enemy
Possible hidden manipulator
```

The Demon King should not appear immediately.

The player first sees signs of him through:

```text
Mutations
Dreams
Cult activity
Black mana
Monster evolution
Forbidden texts
Corrupted bosses
```

The Demon King should feel like a force of nature.

---

## 3. The Crazy Person / Unstable Killer

Role:

```text
Personal-scale threat
Unexpected bad ending source
Possible rival
Possible companion gone wrong
```

This character should be close enough to the player that their danger feels personal.

They might be introduced as harmless, pathetic, funny, or useful.

Then slowly:

```text
They become obsessed.
They stalk the player.
They kill someone important.
They imitate the player.
They resent the player.
They snap.
```

This character is perfect for a route where the player dies not because of weak stats, but because they ignored social danger.

---

## 4. The Hero Candidate

Role:

```text
Rival
Possible ally
Possible enemy
Possible final hunter if player becomes villain
```

This character is what the player “should” have been.

If the player becomes evil, this person hunts them.

If the player stays good, they may become a companion.

If the player is too weak, this person may finish the main story instead.

That is important.

The world should not wait for the player.

---

## 5. The Mentor

Role:

```text
Teaches systems
Reveals world danger
Can die, betray, or be surpassed
```

The mentor can help explain:

```text
Attributes
Insight
Monster knowledge
Talents
Soft caps
Factions
```

But the mentor should not know everything.

---

## 6. The Demon-Linked Companion

Role:

```text
Moral test
Potential tragedy
Potential romance/friendship
Potential betrayal
```

This character gives emotional weight to the demon conflict.

Maybe they are not evil, but their bloodline or curse links them to demons.

The player can:

```text
Save them
Use them
Kill them
Abandon them
Corrupt them
Be corrupted by them
```

---

# How Multiple Endings Should Work

Use **ending flags**.

The game secretly tracks things like:

```text
Prince Influence
Demon Seal Stability
Player Corruption
Hero Trust
Church Suspicion
Commoner Reputation
Companion Loyalty
Madman Obsession
Forbidden Magic Usage
Demon Contract Status
World Truth Knowledge
```

At the end, the game checks these values.

Example:

```text
If Prince Influence is high
AND Prince Exposed is false
AND Prince Alive is true
→ Evil Prince Emperor Ending
```

Example:

```text
If Demon Seal Stability is low
AND Demon King Vessel survives
→ Demon King Rising Ending
```

Example:

```text
If Player Corruption is high
AND Church Suspicion is high
AND Hero Trust is low
→ Hunted Villain Ending
```

Example:

```text
If Madman Obsession is high
AND Player ignores warning events
AND Player travels alone at night
→ Killed by Madman Ending
```

This is how you make the story feel reactive without making it procedural.

---

# What Should Still Be “Dynamic”

You said you do **not** really want it procedural.

That is fine.

So here is the balance:

## Authored / Fixed

These should be written by you:

```text
Main story
Major characters
Major endings
Main villains
Key battles
Major betrayals
Important locations
Lore reveals
Route choices
Companion arcs
```

## Semi-Dynamic

These can vary but still follow your structure:

```text
Training results
Combat outcomes
Insight discoveries
Reputation changes
Relationship changes
Injury consequences
Bestiary knowledge
NPC reactions
```

## Lightly Random

Only small things should be random:

```text
Minor loot
Travel encounters
Weather
Small rumors
Common monster encounters
Shop inventory variation
```

So **Grand Lunacy is not procedural**.

It is **reactive**.

That is the better word.

---

# Updated Game Description

Use this as the official direction:

```text
Grand Lunacy is a linear-branching dark fantasy text RPG with no traditional levels.

The player progresses through a fixed main story involving demonic resurrection, royal betrayal, forbidden talents, and political collapse.

Instead of level grinding, the player grows through hidden attributes, training, skills, talents, traits, insight, relationships, and knowledge.

The story has multiple endings, including stopping the Demon King, allowing the evil prince to become emperor, becoming a hunted villain, dying tragically to an unstable character, or uncovering the deeper truth behind the world.
```

---

# New Roadmap Priority

Since you want a linear-ish story, the roadmap changes.

## Priority 1: Story Bible

Before coding more systems, define:

```text
Main kingdom
Main city/academy/guild
Main cast
Demon King lore
Evil prince plan
Main timeline
Ending routes
Major story choices
```

---

## Priority 2: Route System

Build flags like:

```text
prince_trust
prince_exposed
demon_seal
player_corruption
hero_trust
madman_obsession
church_suspicion
companion_loyalty
```

These will control endings.

---

## Priority 3: Chapter System

Instead of infinite free roam, make chapters:

```text
Chapter 1: Arrival
Chapter 2: First Blood
Chapter 3: Academy/Guild Entry
Chapter 4: The Black Mana Incident
Chapter 5: The Prince’s Invitation
Chapter 6: Civil Fracture
Chapter 7: Demon Seal
Chapter 8: Coronation or Catastrophe
```

Each chapter has fixed events but flexible outcomes.

---

## Priority 4: Character System

Keep the hidden stat system, but connect it to story.

Example:

High Insight reveals the prince’s lies earlier.

High Charisma lets you sway nobles.

High Willpower lets you resist demon contracts.

High Luck may save you from assassination.

High Intelligence lets you decode forbidden texts.

High Corruption unlocks villain choices.

---

## Priority 5: Endings

Write the endings early.

Not last.

You need to know what the story is building toward.

Start with these:

```text
True Hero Ending
Demon King Rising Ending
Demon Emperor Ending
Hunted Villain Ending
Madman Death Ending
Sacrifice Ending
Coward Survivor Ending
Secret Truth Ending
```

---

# The Best Version of Grand Lunacy

The best version is not:

> “Random fantasy life simulator.”

The best version is:

> “A dark fantasy story where you are trapped inside a dangerous world, and the ending depends on whether you understand the world fast enough — or become one of the things that destroys it.”

That fits your idea way better.

