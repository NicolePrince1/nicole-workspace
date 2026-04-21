---
name: openai-image-workflow
description: Use OpenAI image generation for design work that benefits from stronger text rendering, tighter prompt following, conversational multi-turn refinement, or reference-based image editing. Trigger when requests mention ChatGPT Images, gpt-image-2, GPT Image, OpenAI image generation, in-image text, exact layout intent, iterative visual refinement, or using uploaded images as the base for edits.
---

# OpenAI Image Workflow

Use this skill as the model-selection and prompting layer for OpenAI image work.

Do not let the model invent the brief. Start from a real creative brief, then decide whether OpenAI is actually the right render lane.

## Default role in the design stack

Use this split:
- **Oviond design director:** strategy, message hierarchy, brand taste, creative direction, QA
- **This skill:** model routing, prompt structure, edit workflow, OpenAI-specific best practices
- **OpenAI image model:** rendering and iterative visual refinement

If the task is Oviond brand or campaign work, keep the design-director standards in charge. This skill improves execution, not taste.

## When OpenAI is the right lane

Prefer OpenAI image generation when the job needs one or more of these:
- short in-image text that actually needs to survive
- precise prompt adherence with many objects or constraints
- conversational refinement across multiple rounds
- editing from uploaded reference images
- keeping a character, composition, or layout direction coherent across iterations
- transparent-background or composition-controlled marketing assets

## When OpenAI is not the right lane

Do not default to OpenAI for everything.

Use a faster concepting lane when the job is mainly:
- loose ideation
- broad mood exploration
- high-variance thumbnail exploration
- text-free abstract concept generation where speed matters more than precision

Do not trust any image model with final production typography, legal claims, or tiny UI text without hard QA.

## Workflow

1. **Classify the ask**
   - fresh generation
   - edit from an existing image
   - multi-turn refinement
   - text-in-image marketing asset
   - overlay-safe composition for later design finishing

2. **Choose the operating mode**
   - **Generate** when starting from scratch
   - **Edit** when a reference image should be changed, extended, cleaned up, or restyled
   - **Conversational iteration** when the user is clearly refining across rounds

3. **Choose the output style**
   - text-free
   - overlay-safe
   - short validated in-image text

   Default to **overlay-safe** unless short in-image text is strategically important.

4. **Build the prompt in blocks**
   Use this order:
   - objective
   - audience
   - asset type and placement
   - composition and focal point
   - visual style and mood
   - palette and brand constraints
   - text instructions
   - negative constraints
   - output/cropping requirements

5. **Generate small, then tighten**
   Start with 1-2 outputs. Pick the strongest direction, then refine deliberately instead of spraying variants.

6. **Review brutally**
   Reject outputs with:
   - mangled spelling
   - crowded hierarchy
   - awkward anatomy or object artifacts
   - crop risk for the target placement
   - vague focal point
   - generic AI gloss

## Prompting rules that matter

- State the asset type and aspect ratio intent early.
- Be explicit about what must be readable versus what can be added later in layout.
- For text-in-image work, keep copy short and concrete.
- If exact wording matters, repeat the exact phrase once and ask for clean, legible rendering.
- Name clean zones for overlay copy when text will be added later.
- Use negative constraints aggressively to kill stock-photo clichés and decorative sludge.
- Change one major variable at a time during iteration.

## OpenAI-specific tactical advantages

Use OpenAI first when you need:
- better odds of usable short-form text in the image
- tighter adherence to a detailed scene brief
- image editing with a reference already in context
- multi-turn refinement where each iteration should preserve prior decisions

## Current operating caution

OpenAI docs now position `gpt-image-2` as the current API image model tier. If the local runtime/tooling has not exposed it yet, use the newest configured OpenAI image model available and keep the same workflow. The process matters more than the exact model label.

## Read these references when needed

- `references/model-routing.md` for model-choice heuristics and where OpenAI wins
- `references/prompt-recipes.md` for reusable prompt structures by asset type
