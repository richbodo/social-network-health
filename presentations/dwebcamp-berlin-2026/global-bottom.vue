<script setup>
/*
 * Background progression — the "dawn to summer day" rubric.
 *
 * NOTES FOR FUTURE EDITORS (human or LLM) — please keep working in this manner:
 *
 * 1. Everything is keyed to `p` — fractional PROGRESS through the deck
 *    (0 = first slide, 1 = last slide) — NEVER to absolute slide numbers.
 *    Slide count and content will keep changing; the art must not care.
 * 2. The progression must be GRADUAL AND FAIRLY REGULAR: no big leap between
 *    any two adjacent slides. Every visual element gets a ramp window inside
 *    [0, 1] and eases through it; windows overlap so something is always
 *    gently changing. If you add art, give it a window, don't gate it on a
 *    specific slide (the sole exception: the last slide is simply p = 1,
 *    everything fully present).
 * 3. The current schedule:
 *      p 0.00 – 1.00  base wash brightens (darker dawn → bright noon)
 *      p 0.10 – 1.00  yellow glow builds in the upper right
 *      p 0.50 – 0.80  the SUN's disc materializes inside that glow and grows
 *      p 0.66 – 0.98  the sun's comical rays extend out from behind the disc
 *      p 0.58 – 0.80  the grassy hill rises from the bottom edge
 *      p 0.78 – 1.00  sunflowers sprout from the grass, staggered per flower
 * 4. Palette lives in style.css (:root --summer-*); keep new art in it.
 * 5. Verify changes by RENDERING (headless browser screenshots across several
 *    p values), not by curl — transforms and cropping bugs only show visually.
 */
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const nav = useNav()

const p = computed(() => {
  const total = Math.max(2, nav.total.value || 22)
  return Math.min(1, Math.max(0, (nav.currentPage.value - 1) / (total - 1)))
})

const clamp01 = (v) => Math.min(1, Math.max(0, v))
const ramp = (t, a, b) => clamp01((t - a) / (b - a))
const easeOut = (t) => 1 - (1 - t) ** 2
const lerp = (a, b, t) => a + (b - a) * t
const mix = (c1, c2, t) => {
  const h = (c) => [parseInt(c.slice(1, 3), 16), parseInt(c.slice(3, 5), 16), parseInt(c.slice(5, 7), 16)]
  const [r1, g1, b1] = h(c1), [r2, g2, b2] = h(c2)
  return `rgb(${Math.round(lerp(r1, r2, t))}, ${Math.round(lerp(g1, g2, t))}, ${Math.round(lerp(b1, b2, t))})`
}

// base wash: starts a couple shades darker, ends bright summer noon
const bg = computed(() => {
  const t = p.value
  const cream = mix('#f0e8cf', '#fffef8', t)
  const sand = mix('#e9dcb4', '#fdf5e0', t)
  const sky = mix('#cfe3f0', '#ecf8ff', t)
  const glow = t < 0.1 ? 0 : lerp(0.08, 0.7, (t - 0.1) / 0.9)
  const glowSize = lerp(28, 75, t)
  return {
    background: `radial-gradient(ellipse ${glowSize}% ${glowSize * 0.72}% at 86% 4%, rgba(250, 204, 21, ${glow}), transparent 70%),` +
      `linear-gradient(155deg, ${cream} 0%, ${sand} 48%, ${sky} 100%)`,
  }
})

// sun: disc grows inside the glow from the halfway mark; rays follow
const sunP = computed(() => easeOut(ramp(p.value, 0.5, 0.8)))
// fades in quickly at the halfway mark but stays translucent behind slide
// text through the mid-deck, deepening to full strength near the end
const sunOpacity = computed(() => ramp(p.value, 0.5, 0.6) * lerp(0.55, 1, ramp(p.value, 0.5, 0.95)))
const sunScale = computed(() => lerp(0.35, 1, sunP.value))
const rayP = computed(() => easeOut(ramp(p.value, 0.66, 0.98)))
const rayScale = computed(() => lerp(0.55, 1, rayP.value)) // bases stay hidden behind the disc
const rayOpacity = computed(() => ramp(p.value, 0.66, 0.78))

// grass: rises from the bottom edge once the sun is up
const grassP = computed(() => easeOut(ramp(p.value, 0.58, 0.8)))
const grassOffset = computed(() => (1 - grassP.value) * 90)

// sunflowers: staggered sprouting, all fully grown exactly at p = 1
const FLOWERS = [
  { x: 845, top: 70, s: 1.12, w: [0.78, 0.96] },
  { x: 170, top: 92, s: 1.0, w: [0.8, 0.97] },
  { x: 360, top: 118, s: 0.78, w: [0.84, 0.99] },
  { x: 640, top: 138, s: 0.62, w: [0.87, 1.0] },
]
const flowers = computed(() => FLOWERS.map((f) => {
  const g = easeOut(ramp(p.value, f.w[0], f.w[1]))
  return { ...f, grow: g, opacity: clamp01(g * 4) }
}))
</script>

<template>
  <!-- painted wash behind every slide (slide layouts are transparent) -->
  <div class="absolute inset-0 pointer-events-none" :style="bg" />

  <!-- the sun, upper right: appears at the halfway mark, rays extend later -->
  <svg v-if="sunOpacity > 0" class="absolute pointer-events-none" style="top: -4%; right: -3%; width: 34%; height: auto" viewBox="0 0 300 300" aria-hidden="true">
    <g :transform="`translate(150,150) scale(${sunScale})`" :opacity="sunOpacity">
      <g :transform="`scale(${rayScale})`" :opacity="rayOpacity">
        <g v-for="i in 12" :key="i" :transform="`rotate(${i * 30})`">
          <path :d="i % 2 ? 'M -9 -70 L 0 -128 L 9 -70 Z' : 'M -7 -70 L 0 -104 L 7 -70 Z'"
                fill="#f7c948" opacity="0.9" stroke="#ef8a2d" stroke-width="2" stroke-linejoin="round" />
        </g>
      </g>
      <circle r="62" fill="#fde047" stroke="#ef8a2d" stroke-width="4" />
      <circle r="62" fill="url(#sunshine)" />
      <defs>
        <radialGradient id="sunshine" cx="0.38" cy="0.35" r="1">
          <stop offset="0%" stop-color="#fff7c0" />
          <stop offset="100%" stop-color="#fde047" stop-opacity="0" />
        </radialGradient>
      </defs>
    </g>
  </svg>

  <!-- grassy bottom eighth + sunflowers. viewBox maps onto the bottom 40% of
       the slide canvas (preserveAspectRatio=none; the canvas aspect is fixed,
       so nothing distorts or crops). Grass rides up from below; each flower
       grows uniformly from its ground anchor (y=195). -->
  <svg v-if="grassP > 0" class="absolute bottom-0 left-0 w-full pointer-events-none" style="height: 40%" viewBox="0 0 1000 225" preserveAspectRatio="none" aria-hidden="true">
    <defs>
      <linearGradient id="grass" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#7cc35e" />
        <stop offset="100%" stop-color="#4e9e6d" />
      </linearGradient>
    </defs>
    <g :transform="`translate(0 ${grassOffset})`">
      <!-- gentle grassy hill: the bottom eighth of the slide -->
      <path d="M 0 162 Q 250 148 520 158 T 1000 154 L 1000 225 L 0 225 Z" fill="url(#grass)" />
      <!-- a few blades -->
      <g stroke="#3d8a58" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.8">
        <path d="M 120 168 q 4 -16 -2 -26" /><path d="M 132 170 q -2 -12 6 -22" />
        <path d="M 468 164 q 4 -14 -3 -24" /><path d="M 704 160 q -3 -14 5 -24" />
        <path d="M 920 162 q 4 -16 -2 -26" /><path d="M 300 164 q -3 -13 4 -22" />
      </g>
      <!-- sunflowers: stem, leaves, petals, seed head — staggered growth -->
      <g v-for="f in flowers" :key="f.x"
         :transform="`translate(${f.x} 195) scale(${f.grow}) translate(0 -195)`"
         :opacity="f.opacity">
        <path :d="`M 0 195 C -6 ${f.top + 62} 6 ${f.top + 40} 0 ${f.top + 18}`"
              stroke="#3d8a58" :stroke-width="6 * f.s" fill="none" stroke-linecap="round" />
        <path :d="`M 0 ${f.top + 46} q ${-26 * f.s} ${-5 * f.s} ${-30 * f.s} ${-26 * f.s} q ${23 * f.s} ${2 * f.s} ${30 * f.s} ${26 * f.s} Z`" fill="#4e9e6d" />
        <path :d="`M 0 ${f.top + 64} q ${26 * f.s} ${-5 * f.s} ${30 * f.s} ${-26 * f.s} q ${-23 * f.s} ${2 * f.s} ${-30 * f.s} ${26 * f.s} Z`" fill="#4e9e6d" />
        <g :transform="`translate(0 ${f.top}) scale(${f.s})`">
          <g v-for="i in 14" :key="i" :transform="`rotate(${i * (360 / 14)})`">
            <ellipse cx="0" cy="-27" rx="7.5" ry="17" :fill="i % 2 ? '#f7c948' : '#fbbf24'" stroke="#ef8a2d" stroke-width="1.5" />
          </g>
          <circle r="16" fill="#7a4a1f" stroke="#5c3714" stroke-width="2.5" />
          <circle r="16" fill="none" stroke="#9a6633" stroke-width="2" stroke-dasharray="3 4" transform="scale(0.62)" />
        </g>
      </g>
    </g>
  </svg>
</template>
