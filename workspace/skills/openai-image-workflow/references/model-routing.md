# Model Routing

Use this file to decide when OpenAI image generation is the best tool for the job.

## Best-fit jobs

### 1. Short text inside the image
Use OpenAI when the asset needs a headline, label, CTA, or short product phrase rendered in-image and it actually needs a chance of being usable.

Still keep the text short. Think:
- 2-6 word headline
- 1 short label
- 1 short CTA

Do not treat it like InDesign. If the asset needs lots of copy, generate an overlay-safe composition and finish the typography outside the model.

### 2. Reference-based editing
Use OpenAI when Chris gives:
- an existing ad to improve
- a blog cover to adapt
- a product screenshot to stylize
- a concept to extend or clean up

OpenAI is especially useful when the job is not "make something random" but "take this thing and move it in a specific direction."

### 3. Iterative refinement with memory
Use OpenAI when the next prompt depends heavily on the last image.

Examples:
- make the same concept cleaner
- keep the composition but change the lighting
- preserve the product card and change the headline zone
- make this look more premium without changing layout structure

### 4. Constraint-heavy marketing art
Use OpenAI when the prompt includes many simultaneous constraints such as:
- exact mood + composition + palette
- multiple objects that must stay distinct
- a clear focal point with whitespace zones
- specific crop or placement demands

## Weak-fit jobs

Use a faster or looser lane first when the goal is:
- 10 rough moods fast
- purely abstract experimentation
- visual wandering without a stable brief
- text-free atmospheric concept hunting

## Practical rule

If the job sounds like **precision, editing, preservation, or legibility**, try OpenAI first.

If the job sounds like **speed, exploration, or broad ideation**, use a faster concepting model first, then move into OpenAI for the keepers.

## Known limitations to design around

- Longer poster-like compositions may crop too tightly.
- Fine-print text can still fail.
- Dense dashboards and tiny UI details can still turn to mush.
- Rendering can take longer, so use it deliberately.

## Safe operating stance

Never approve an output because the prompt was good.
Approve only if the image itself is good.
