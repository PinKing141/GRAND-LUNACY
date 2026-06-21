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
