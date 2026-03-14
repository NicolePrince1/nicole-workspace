# Prompt Patterns

Use these patterns to create consistent generation prompts grounded in the Oviond brand guide. Replace bracketed fields with the task-specific brief.

## Oviond visual principles to carry into prompts

Carry these ideas into most prompts unless the brief clearly overrides them:
- abstract and unspecific imagery
- aesthetic-led, feeling-first direction
- avoid overreliance on office/meeting/computer clichés
- communicate infinite possibility without becoming random or chaotic
- keep the composition light, spacious, and digitally polished
- use white as the base where possible and MAIN BLUE as the key highlight
- use additional blues sparingly

## 1. Brand-led concept prompt

Use when the asset needs strong Oviond identity but flexible execution.

Template:

```text
Create a [asset type] for Oviond, a reporting platform for marketing agencies. Objective: [goal]. Audience: [audience]. Core message: [message]. Visual style: modern, digital, spacious, abstract, and aesthetically driven. Use abstract and unspecific imagery rather than office scenes or literal business clichés. The design should evoke a feeling of infinite possibility while staying commercially credible and clean. Keep the composition light with generous white space, one dominant focal point, and strong hierarchy. Use white as the primary base, MAIN BLUE (#0000FF) as the key accent, and support colors sparingly from #0A0B5C, #5676FF, and #D5E4FF. If gradients are used, keep them simple and drawn from the approved brand transitions. If text appears, keep it minimal and highly legible. Avoid generic stock-photo aesthetics, cluttered pseudo-dashboards, rainbow gradients, decorative overload, or anything that feels like a marketplace template.
```

## 2. Conversion ad prompt

Use for paid social and direct-response creative.

Template:

```text
Design a high-clarity paid social ad for Oviond. Audience: [audience]. Pain point: [pain]. Promise/value proposition: [value prop]. Desired action: [CTA]. Build for fast mobile comprehension with bold hierarchy, simple composition, strong contrast, and a clean CTA zone. Keep the brand feeling modern, digital, spacious, and polished. Use abstract brand-led visual language instead of office stock scenes. Keep the base light and use MAIN BLUE (#0000FF) as the dominant accent. Support colors should be used sparingly. Avoid clutter, tiny UI details, weak focal points, excessive text, and low-contrast layouts.
```

## 3. Web hero visual prompt

Use for landing pages, homepage sections, and product marketing pages.

Template:

```text
Create a website hero visual for Oviond, a client reporting platform for marketing agencies. Support this headline/theme: [headline/theme]. The image should communicate [idea/outcome] through abstract, evocative, brand-feeling visuals rather than literal office or meeting scenes. Style: polished SaaS, modern, clean, trustworthy, spacious, digital. Composition: [composition]. Leave room for surrounding web copy and CTA buttons. Use a mostly light base with selective brand-blue emphasis. Optional gradients should follow approved brand transitions only. Avoid busy compositions, fake-complex dashboards, corporate stock-photo energy, and abstract art that feels disconnected from the product.
```

## 4. Stat card / infographic prompt

Use for data-led content moments.

Template:

```text
Create a clean stat-card style graphic for Oviond centered on this key insight: [stat/insight]. Audience: [audience]. Make the number or key claim the unmistakable focal point. Use a modern, minimal, spacious SaaS design language with disciplined spacing, strong hierarchy, and restrained use of the Oviond brand palette. Keep the background predominantly light and use MAIN BLUE for emphasis. Keep supporting copy minimal. Avoid clutter, over-illustration, tiny labels, and multi-message confusion.
```

## 5. Event / webinar prompt

Use for registrations and promo graphics.

Template:

```text
Design a webinar or event promo graphic for Oviond. Event theme: [theme]. Audience: [audience]. Prioritize a clear headline area, clean event-detail zones, and a polished digital SaaS aesthetic. The composition should feel spacious and brand-led, with restrained color use, strong hierarchy, and minimal clutter. Use the approved blue palette carefully, with white carrying most of the layout. Avoid poster-style chaos, too many decorative elements, and low-legibility typography.
```

## Approved gradient prompt language

When gradients help, use wording like:
- use a clean brand gradient from #0A0B5C to #0000FF
- use a restrained digital gradient from #0000FF to #5676FF
- use a light blue gradient transition from #5676FF to #D5E4FF

Do not stack multiple gradient ideas into one composition unless there is a strong reason.

## Variation angles

When generating variants, change only 1-2 major variables at once. Good variation axes:
- lighter white-led composition vs darker deep-blue-led composition
- more abstract atmospheric direction vs more structured product-adjacent direction
- stronger gradient expression vs flatter minimalist color blocking
- sharper contrast vs softer premium tone
- minimal text vs text-free visual

## Negative constraints bank

Mix in relevant exclusions:
- no office stock-photo scenes
- no meeting-room clichés
- no cluttered floating dashboard cards
- no rainbow palette overload
- no noisy or muddy gradients
- no template-marketplace look
- no decorative nonsense without message value
- no weak contrast on white
- no crowded multi-message layouts

## Text handling modes

Pick one explicitly in the prompt package:
- **Text-free:** no meaningful in-image copy; visual concept only
- **Overlay-safe:** leave obvious clean zones for later headline/subhead/button overlay
- **Short-copy in-image:** only for very short, easy-to-validate text

Default to **Text-free** or **Overlay-safe** for web heroes, ads, and premium brand visuals unless the model has already proven reliable on that exact output type.

## Prompt packaging standard

Before generation, produce:
- **Master prompt**
- **Negative constraints**
- **Variation A/B/C notes**
- **Placement reminder**
- **Chosen text handling mode**
