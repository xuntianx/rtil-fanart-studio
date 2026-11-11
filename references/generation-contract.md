# Generation, Files, and Acceptance

## Compact production brief

Keep a brief in the task output directory; users do not need to fill in a form:

- The user's request and explicit choices of character, format, language, and mood.
- Character anchors and necessary sources, separating canon from this new premise.
- Selected style-reference files and their roles; identify character-reference images separately.
- A title and each panel's action, expression, key prop, speaker, and exact dialogue.
- The final prompt, output file, visual review, and remaining defects.

Preserve a user's original request verbatim when recording provenance. Write the production brief and generated content in English by default.

## Image-tool prompt skeleton

Attach references through the tool's supported parameters and describe their roles by number. Adapt this skeleton to the task rather than mechanically keeping every label.

```text
Use case: Finished fanart comic or illustration.
Reference roles: Images 1 and 2 are rtil visual-style references only. If image 3 is a character sheet, it guides identity only.
New work: <original franchise/characters + the user's premise>.
Character anchors: <appearance, costume, personality, relationships; consistent across panels>.
Visual direction: Reference the supplied linework, color, shadows, expressions, setting, and comic language; create new scenes and compositions.
Format: <aspect ratio, panel count, reading order>; reserve a clean, readable attribution footer.
Storyboard: <each panel's actions, reactions, key props, named speakers, and exact dialogue>.
Text: <verbatim English dialogue, title, signs, and captions; do not invent extra text>.
Exact footer: Creative & style inspiration: @rtil
Attribution treatment: One complete source-credit line, not a forged artist signature. Do not add Patreon branding, original watermarks, or other handles.
Preserve: <character identity and the user's explicit story choices>.
```

Keep dialogue short enough to fit naturally; roughly 3-12 words per speech box is a useful starting point, not a hard limit. Speech-box tails must identify the correct speaker. Explicitly distinguish narration and off-panel speech. Do not inherit another language from reference images or the language used to submit the request. Honor an explicitly requested content language while retaining the English attribution unless the user specifically changes it.

## Footer acceptance

The actual final image must visibly contain `Creative & style inspiration: @rtil`. A prompt, Markdown caption, filename, or metadata entry alone does not satisfy this requirement. Check every page.

Inspect the whole page at a readable scale: correct capitalization and spelling, the ampersand, a colon followed by a space, ASCII `@`, and lowercase `rtil`. The credit must have adequate contrast and safe margins without covering artwork or dialogue. Reserve a separate footer rather than making attribution part of the joke.

If correction is needed, instruct the tool to change only the footer while preserving panels, characters, dialogue, style, and other text. Save a new version and inspect it again; editing can cause drift, so do not promise an unchanged result before checking it.

## User-facing delivery

1. Display the finished image and provide an accessible file link.
2. Supply a concise English title/story introduction and publishable caption, unless the user explicitly requested another language.
3. Include `Creative & style inspiration: [@rtil](https://x.com/rtil)` in the delivery copy.

Keep production materials in the task directory for traceability. Do not dump prompts or implementation details into the default reply. If generation failed or attribution remains incorrect, report the actual status and retain existing results rather than claiming acceptance.
