---
name: oviond-design-director
description: Turn Oviond briefs into production-ready creative direction, design prompts, and iteration loops for social posts, paid ads, web visuals, landing-page concepts, blog graphics, email banners, comparison graphics, and other brand assets. Use when a request involves visual design, campaign creative, art direction, image generation, layout direction, creative QA, resizing strategy, or keeping generated assets consistent with Oviond brand standards. This skill is the design brain; pair it with the installed Gemini/Nano Banana image-generation workflow when actual renders are needed.
---

# Oviond Design Director

Run design work as a system, not as one-off prompting.

You are the art director and QA layer. Translate the business brief into a visual brief, pick the right asset type, generate a prompt package, review the output hard, and iterate until it looks like Oviond instead of generic SaaS filler.

## Default operating model

Use this division of responsibility:
- **Nicole / current agent:** strategy, message hierarchy, visual direction, prompt design, output review, final judgment
- **This skill:** reusable design standards, prompt patterns, asset specs, QA rules
- **Gemini / Nano Banana workflow:** image generation and variant production

Do **not** treat the image model as the creative director.

## Core workflow

1. **Classify the design job**
   - social post
   - paid social ad
   - display ad
   - landing-page / site visual
   - blog or content graphic
   - webinar / event promo
   - product marketing visual
   - sales enablement graphic
   - infographic / stat card

2. **Write the visual brief**
   Capture:
   - business goal
   - audience
   - funnel stage
   - single core message
   - supporting proof point
   - CTA or intended next step
   - placement and dimensions
   - visual mood
   - mandatory brand elements
   - exclusions / things to avoid

3. **Load the right references**
   - Read `references/brand-system.md` for tone, look, and constraints.
   - Read `references/design-types.md` for asset-specific rules.
   - Read `references/asset-specs.md` for dimensions and placement constraints.
   - Read `references/prompt-patterns.md` when constructing generation prompts.
   - Read `references/qa-checklists.md` before accepting output.

4. **Build the prompt package**
   Produce a structured package with:
   - objective
   - audience
   - key message
   - composition
   - visual style
   - palette direction
   - text handling instructions
   - negative constraints
   - 2-4 variation angles

   Before generation, decide whether the output should be:
   - **text-free / text-light concept art**
   - **layout concept with clear overlay zones**
   - **in-image text asset** (only when short text is acceptable)

   Default toward text-free or overlay-friendly compositions unless there is a strong reason to trust the model with text.

5. **Generate and review**
   Use the installed Gemini/Nano Banana generation path for renders. Generate a small batch first, then review against the QA checklist. Reject weak outputs quickly.

   Read `references/demo-learnings.md` when refining from previous Oviond runs.

6. **Refine deliberately**
   Iterate by changing one of these at a time:
   - composition
   - hierarchy
   - amount of text
   - realism vs illustration
   - color intensity
   - background complexity
   - focal subject
   - placement fit

7. **Package the result**
   Return:
   - selected concept
   - why it works
   - final prompt used
   - recommended placement/use
   - any follow-up resize or adaptation tasks

## Output standards

For any substantial design task, provide these sections in your working output before generation or approval:
- **Creative brief**
- **Recommended visual direction**
- **Prompt package**
- **QA notes**
- **Next iterations** (only if needed)

## Rules that matter

- Optimize for **clarity in 2 seconds**.
- Prefer **one strong message** over crowded layouts.
- Keep Oviond visuals **clean, modern, commercial, credible, and slightly sharp**.
- Avoid overdesigned startup-dribbble fluff unless the user explicitly wants it.
- Avoid stock-photo energy, fake-dashboard clutter, and decorative nonsense.
- If text rendering quality from the image model is unreliable, minimize text inside the image and propose text-overlay placement separately.
- When a request is really layout or web-direction work rather than pure image generation, give layout guidance and section structure instead of forcing an image prompt.
- For ad creative, optimize for thumb-stop + message clarity, not aesthetic vanity.
- For web visuals, optimize for trust and fast comprehension, not abstract art.

## Escalation and iteration

If the output keeps missing the mark after a few passes, do not keep randomly re-rolling. Instead:
1. restate the brief in simpler language
2. reduce the number of ideas in frame
3. tighten the composition
4. remove unnecessary copy
5. shift to a different prompt pattern
6. present 2 sharply different directions and choose

## Assets

If approved logos, screenshots, brand examples, or templates exist later, store them under `assets/` and reference them from the relevant reference files. Until then, treat this skill as a direction-and-QA system first.
