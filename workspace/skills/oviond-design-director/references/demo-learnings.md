# Demo Learnings

Use these notes as the starting operating heuristics for future Oviond design runs.

## Round 1 findings

### 1. The model is better at visual direction than final copy fidelity

Observed in the first website hero demo:
- strong overall composition
- strong brand color restraint
- good premium SaaS feel
- bad in-image copy fidelity (`infile possibility`, other broken words)

Rule:
- do **not** trust image generation for final marketing copy unless the text is extremely short and validated visually
- for serious outputs, prefer either:
  - text-free or text-light image generation
  - or generation with obvious text-safe zones for later overlay/compositing

### 2. Abstract movement works well for Oviond

The strongest directions used:
- abstract blue motion
- flow and transformation
- clean digital ribbons/forms
- spacious white compositions

These align well with the guide’s direction toward abstract, feeling-led imagery and infinite possibility.

Rule:
- prefer abstract flow, transformation, clarity, and light-driven forms over literal workplace scenes

### 3. Messy-to-clear is a promising ad metaphor

The best-performing conceptual ad direction used a left-to-right transition from visual chaos into clean reporting structure.

Rule:
- for pain-point ads, use visual metaphors of:
  - chaos -> clarity
  - friction -> flow
  - clutter -> clean delivery
  - manual mess -> structured reporting

### 4. White-led compositions feel the most on-brand

White-dominant layouts with selective blue emphasis felt closest to the brand guide and most commercially credible.

Rule:
- default to white-led compositions first
- use MAIN BLUE as the high-impact accent, not as full-canvas fill by default

### 5. Avoid over-complex left-side clutter

In one square ad, the left-side abstract chaos was a good idea but became too noisy.

Rule:
- when expressing pain/chaos, keep the complexity controlled
- the metaphor should read instantly, not become messy design for its own sake

## Recommended default workflow after demos

1. Generate **concept-first**
2. Review for brand fit and composition
3. If text quality is weak, regenerate with:
   - less text
   - or explicit text-free design zones
4. Treat final production copy as a separate overlay/compositing step when needed
5. Save good prompts and rejected failure modes back into this skill

## Prompt refinement rules from round 1

When refining after a first pass, try these moves first:
- reduce the amount of in-image text
- specify `leave clear blank space for headline and CTA overlay`
- ask for `text-free` or `headline-free` compositions when the visual is the real goal
- simplify the chaos metaphor if it starts looking like clip-art or generic geometry noise
- push for `premium, restrained, less noisy` when outputs feel too busy

## Reuse note

This file should grow after each meaningful batch of Oviond design work. It is the taste-memory layer for the skill.
