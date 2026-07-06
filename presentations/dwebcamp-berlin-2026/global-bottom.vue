<script setup>
import { computed } from 'vue'
import { useNav } from '@slidev/client'

const nav = useNav()

// 0 on the first slide → 1 on the last: drives the dawn-to-full-summer progression
const p = computed(() => {
  const total = Math.max(2, nav.total.value || 22)
  return Math.min(1, Math.max(0, (nav.currentPage.value - 1) / (total - 1)))
})
const isLast = computed(() => nav.currentPage.value >= (nav.total.value || 22))

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
  // the yellow glow in the upper right: absent early, building steadily
  const glow = t < 0.1 ? 0 : lerp(0.08, 0.7, (t - 0.1) / 0.9)
  const glowSize = lerp(28, 75, t)
  return {
    background: `radial-gradient(ellipse ${glowSize}% ${glowSize * 0.72}% at 86% 4%, rgba(250, 204, 21, ${glow}), transparent 70%),` +
      `linear-gradient(155deg, ${cream} 0%, ${sand} 48%, ${sky} 100%)`,
  }
})
</script>

<template>
  <!-- painted wash behind every slide (slide layouts are transparent) -->
  <div class="absolute inset-0 pointer-events-none" :style="bg" />

  <!-- the last slide: full comical summer — sun with rays, grass, sunflowers -->
  <template v-if="isLast">
    <!-- sun with rays, upper right -->
    <svg class="absolute pointer-events-none" style="top: -4%; right: -3%; width: 34%; height: auto" viewBox="0 0 300 300" aria-hidden="true">
      <g transform="translate(150,150)">
        <g v-for="i in 12" :key="i" :transform="`rotate(${i * 30})`">
          <path :d="i % 2 ? 'M -9 -70 L 0 -128 L 9 -70 Z' : 'M -7 -70 L 0 -104 L 7 -70 Z'"
                fill="#f7c948" opacity="0.9" stroke="#ef8a2d" stroke-width="2" stroke-linejoin="round" />
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

    <!-- grassy bottom eighth with sunflowers of various heights.
         viewBox maps 1:1 onto the bottom 40% of the slide canvas
         (preserveAspectRatio=none; the slide canvas has a fixed aspect,
         so nothing distorts and nothing crops) -->
    <svg class="absolute bottom-0 left-0 w-full pointer-events-none" style="height: 40%" viewBox="0 0 1000 225" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <linearGradient id="grass" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#7cc35e" />
          <stop offset="100%" stop-color="#4e9e6d" />
        </linearGradient>
      </defs>
      <!-- gentle grassy hill: the bottom eighth of the slide -->
      <path d="M 0 162 Q 250 148 520 158 T 1000 154 L 1000 225 L 0 225 Z" fill="url(#grass)" />
      <!-- a few blades -->
      <g stroke="#3d8a58" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.8">
        <path d="M 120 168 q 4 -16 -2 -26" /><path d="M 132 170 q -2 -12 6 -22" />
        <path d="M 468 164 q 4 -14 -3 -24" /><path d="M 704 160 q -3 -14 5 -24" />
        <path d="M 920 162 q 4 -16 -2 -26" /><path d="M 300 164 q -3 -13 4 -22" />
      </g>
      <!-- sunflowers: stem, leaves, petals, seed head — various heights -->
      <g v-for="f in [
        { x: 170, top: 92, s: 1.0 },
        { x: 360, top: 118, s: 0.78 },
        { x: 845, top: 70, s: 1.12 },
        { x: 640, top: 138, s: 0.62 },
      ]" :key="f.x" :transform="`translate(${f.x} 0)`">
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
    </svg>
  </template>
</template>
