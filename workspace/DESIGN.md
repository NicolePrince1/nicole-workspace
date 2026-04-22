---
version: alpha
name: Oviond
description: Agent-readable source of truth for Oviond brand and product design decisions.
colors:
  primary: "#0000FF"
  secondary: "#0A0B5C"
  tertiary: "#5676FF"
  neutral: "#FFFFFF"
  ink: "#000000"
  surface-soft: "#D5E4FF"
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.03em
  h1:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.02em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
  button-secondary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 12px
  card-default:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  chip-accent:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.secondary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    padding: 8px
---

# Oviond DESIGN.md

## Overview

Oviond should feel clean, modern, digital, confident, and commercially credible. The brand should not look like generic B2B office software and it should not drift into noisy startup fluff either.

The emotional target is simple: reporting should feel invisible, dependable, and done. The design language should support that promise by feeling calm, capable, spacious, and sharply intentional.

Use abstract and unspecific imagery more often than literal office scenes. Favor light, open compositions with one clear focal point. Aim for an aesthetic-led feeling of infinite possibility, but keep it grounded in trust, product seriousness, and fast comprehension.

This file is the standing design brief for agent-driven design work across web, product marketing, paid creative, social, sales materials, and supporting UI direction.

## Colors

Oviond uses color with restraint.

- **Primary (#0000FF):** Main digital blue. Use it as the hero accent, key action color, or strongest highlight.
- **Secondary (#0A0B5C):** Deep support blue for depth, structure, and more premium emphasis.
- **Tertiary (#5676FF):** Supportive lighter blue for secondary accents, gradient transitions, and softer emphasis.
- **Neutral (#FFFFFF):** The dominant surface and breathing room. Most layouts should stay white-led.
- **Ink (#000000):** High-contrast text and anchor color.
- **Surface Soft (#D5E4FF):** Light support tone for restrained fills, chips, soft panels, and gentle depth.

Use black, white, and strong digital blue as the foundation. Use the other blues sparingly. Do not flood every design with blue just because the palette exists.

Approved gradient behavior:
- `#0A0B5C -> #0000FF`
- `#0000FF -> #5676FF`
- `#5676FF -> #D5E4FF`

Gradients are a controlled brand device, not wallpaper.

## Typography

The brand logotype uses **Inter Semibold**. For general system and marketing typography, use Inter as the default working family until a more detailed official type system is locked.

Typography should feel clean, precise, and highly legible.

- Headlines should be bold, short, and decisive.
- Body copy should stay simple and readable.
- Labels and UI microcopy should feel crisp, compact, and intentional.
- In image generation, keep text minimal and prefer overlay-safe compositions when possible.

Do not create fussy type systems, over-decorated headings, or low-contrast copy blocks.

## Layout

Layouts should feel spacious, controlled, and calm.

- Use a clear grid and generous whitespace.
- One message per frame whenever possible.
- Build obvious safe zones for headline, proof point, and CTA placement.
- Prefer strong hierarchy over dense explanation.
- In web and product-marketing layouts, let the content breathe instead of stacking floating clutter.

The spacing scale is anchored to a clean 8px rhythm with a 4px micro-step.

## Elevation & Depth

Oviond should communicate depth mostly through tonal contrast, clean panels, restrained gradients, and spacing, not heavy shadow gimmicks.

Use depth to separate layers, not to show off. Cards, panels, and hero blocks should feel polished and digital, not glassy for the sake of trendiness.

Prefer:
- white or near-white surfaces
- subtle blue-tinted support planes
- crisp contrast edges
- minimal shadow use

Avoid muddy gradients, glowing neon effects, and fake-3D chrome nonsense.

## Shapes

Shape language should be modern and slightly sharp.

- Use low-to-moderate corner radius.
- Keep shapes consistent across the same asset.
- Rounded corners should soften, not cartoonify.
- Pills are acceptable for compact metadata or chips, but not as a default for everything.

The visual feel should be engineered and polished, not toy-like.

## Components

Component behavior should reinforce clarity and trust.

- **Primary buttons:** bold blue fill, strong contrast, short labels, obvious click target.
- **Secondary buttons:** white or very light surface with crisp dark text and clear boundary treatment in implementation.
- **Cards:** bright surfaces, disciplined padding, clean structure, no clutter.
- **Chips / tags:** use only where they add scanning value.

In marketing assets, components should never overpower the message. In product UI, they should feel consistent, calm, and easy to parse.

## Do's and Don'ts

- Do keep most compositions light and spacious.
- Do use MAIN BLUE for the single strongest action or emphasis.
- Do favor abstract, product-adjacent, or atmosphere-led visuals over office stock clichés.
- Do optimize for understanding within 2 seconds.
- Do keep one clear focal point.
- Do leave clean overlay zones when copy can be added later.

- Don't rely on meeting-room scenes, smiling-team stock photos, or laptops-on-desks as the default visual language.
- Don't turn every asset into a floating-dashboard collage.
- Don't use too many blues in one frame.
- Don't pack multiple competing messages into one asset.
- Don't trust image models with long or critical text.
- Don't let decorative effects outrun clarity.

When in doubt, choose the cleaner, sharper, more restrained option.