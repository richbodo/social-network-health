# PNT Workshop — Slidev deck

Personal Network Toolkit workshop presentation. Slides in `slides.md`; long-form script in
`presentation_long.txt`; voice notes in `talk_voice_notes.txt`. Imported July 2026 from the
standalone `richbodo/pnt-workshop` repo. From the repo root: `just slides pnt-workshop`.

## Running the deck ([Slidev](https://github.com/slidevjs/slidev))

- `bun install` (npm ≤10.x hits a known optional-dependency bug with rolldown's native binding —
  use bun)
- `bun run dev`
- visit <http://localhost:3030>

Needs Node ≥ 20.13 at runtime; `.node-version` pins nodenv to `system` (Homebrew node) since the
nodenv-managed versions on this machine are older.

Edit the [slides.md](./slides.md) to see the changes.

Learn more about Slidev at the [documentation](https://sli.dev/).
