# Oviond first preview review

## Strongest directions

### 1. Product system backbone
Use `oviond-system-seed-preview` as the main visual reference for the first Figma system, with `oviond-blog-cover-preview` as the supporting product-marketing reference.

Why:
- strongest modular UI signal in the batch
- clearer component-family potential
- restrained palette
- feels closer to a reusable reporting system rather than a one-off marketing render

Important caveat:
- this is still not system-grade source of truth by itself
- we should use it as a style and layout seed, then rebuild the real component logic properly in Figma

What to do with it in Figma:
- derive card patterns
- derive spacing rhythm
- define chart card / stat card / table card families
- rebuild typography scale and control states cleanly

What to borrow from `oviond-blog-cover-preview`:
- product-marketing perspective treatment
- elegant layered-report feeling
- blog-cover series territory

### 2. Brand expression layer
Use `oviond-brand-texture-preview` as the secondary direction for abstract brand language.

Why:
- strongest non-generic feeling-led brand territory
- useful for section backgrounds, banners, event covers, abstract support visuals
- gives Oviond a cleaner ownable atmosphere

What to do with it in Figma:
- turn into a reusable background family
- create light / medium / strong intensity variants
- define safe overlay zones for copy

## Weaker directions

### Website hero preview
Good, but too generic to be the main system seed.
Keep only as a reference for depth, shadows, and product-marketing composition.

### Chaos-to-clarity social preview
Useful conceptually, but not strong enough as a base system visual.
Keep as an ad-metaphor exploration, not as the main design language.

## First Figma file structure to build

1. Cover
2. Brand Principles
3. Foundations
   - colors
   - gradients
   - spacing
   - typography
   - imagery rules
4. Components
   - stat cards
   - chart cards
   - table cards
   - UI containers
   - section backgrounds
5. Templates
   - blog covers
   - website hero blocks
   - social square
   - LinkedIn landscape
   - Meta portrait
6. Exploration
   - product-preview concepts
   - abstract brand textures

## Immediate next production move
Build the first Figma system around:
- product-preview UI language from the strongest preview
- abstract brand background language from the texture preview

Do not overfit the system to one generated image. Use them as seeds, then convert the logic into reusable Figma components and template families.
