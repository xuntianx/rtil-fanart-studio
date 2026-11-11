---
name: rtil-fanart-studio
description: >-
  Create fanart illustrations or short comics featuring familiar anime, game, or other fictional characters in new situations, using rtil visual references and the fixed on-image credit "Creative & style inspiration: @rtil". Use for fanart concepts, character interactions, slice-of-life side stories, and continuing an existing series.
---

# Fanart Studio - rtil Style Reference

Turn "characters I like + a situation I want to see" into finished, shareable artwork. Reference rtil's visual language while preserving the requested characters' identities, and visibly credit that inspiration. Do not automatically redirect the task into personal-photo comics, life predictions, or a four-panel-only template.

## Input and default experience

Accept a natural-language sentence, character or costume references, and previous episodes.

- When the characters and situation are clear, fill in necessary visual details and generate directly. Do not introduce a separate story-approval step.
- When only a character is provided, offer three specific concepts grounded in that character's personality or relationships. If the user asks you to improvise, choose a concept and proceed.
- Ask one necessary question only when ambiguity about character identity, continuity, or relationships would materially change the result.
- Honor explicit choices of format, panel count, language, mood, and plot. **Default to English for titles, dialogue, signs, captions, generation prompts, and delivery copy, even when the request is written in another language.** Follow an explicitly requested output language; keep the fixed English credit unless the user specifically changes it.
- Use a single illustration for one strong moment; use a two-to-four-panel comic when a sequence or dialogue is essential.
- Prefer one to three main characters and one clear situation for an initial concept. These are defaults, not restrictions on a more elaborate user request.

## Characters and story

Establish concise character anchors: original work and continuity, recognizable hair/clothing/props, personality, voice, and relationships. Honor explicit user-provided settings. Verify uncertain or obscure canon using official character pages or other reliable sources. Use user references or verified character images when visual identity needs support.

Separate canon from the new fan-created premise. New occupations, modern settings, future developments, and crossovers are inventions for this artwork, not official events. A creator's own series title does not establish that its characters are original IP.

Choose the approach that fits the request:

- **Themed reinterpretation:** put familiar characters into a holiday, trip, occupation, or everyday situation.
- **Character interaction:** use contrasting personalities, established habits, or relationships to create a small conflict or joke.
- **Side story:** imagine an unseen daily moment, a later chapter, or an alternative possibility.

Make the premise interesting because of these particular characters. Avoid interchangeable plots. For a comic, draft a compact storyboard with each panel's action, expression, key prop, speaker, and exact dialogue. Let the final image deliver the contrast or emotional payoff. A single illustration should also communicate an action or relationship rather than merely display standing characters.

## Visual style: use actual reference images

Read the [style and reference guide](references/style-guide.md). Select and inspect two or three of the five reference images listed in the manifest that best suit the subject. Original posts, dates, purposes, and SHA-256 hashes are in the [source manifest](references/source-manifest.json). These are representative samples, not a claim to cover every period or style in the artist's work.

Use an image-capable generator and submit the chosen images as **visual style references**. Explain that they are neither edit targets nor identity references for the requested characters. Attach separate character references when needed and identify each image's role. Character anchors determine identity; rtil references guide linework, color, lighting, expressions, and comic lettering/layout.

Do not claim to preserve this style by merely requesting "anime style." Do not copy the reference images' characters, dialogue, specific plots, signatures, or Patreon promotions into the new work. Draw on everyday staging, expressions, and composition; mature material elsewhere in the artist's portfolio does not imply a request to sexualize the user's characters.

The public repository includes source records rather than copies of the original artwork. Run `python scripts/fetch_references.py` from the Skill root to download the five references locally; the helper requires Python 3.9+ and only uses its standard library. If Python is unavailable, the agent can download the listed source-image URLs and verify their SHA-256 hashes directly. If a source is unavailable, use a user-supplied reference or report the gap. Never describe a text-only request as having used image references.

## Generation and fixed attribution

Read the [generation and delivery contract](references/generation-contract.md). Prepare character anchors, story, visual direction, layout, exact text, and attribution placement. Prefer the environment's built-in image generator. Deliver actual artwork rather than substituting a prompt or storyboard for the requested image.

In Codex, use the reference-image capability of `image_gen` by default. Inspect local images first, then use the tool's supported reference mechanism. If the host only supports text-to-image generation, explain the missing reference-image capability rather than silently downgrading. Do not depend on a personal credential file, a specific provider model, a fixed local drive, or an unrelated paid service.

**Every final image must contain this entire line:**

> Creative & style inspiration: @rtil

- Put the credit in a clear bottom margin or separate bottom-right area. Use a page footer for comics and include it on every page of a multi-page comic.
- Ensure readable contrast and safe margins. It should remain legible at common mobile viewing sizes without covering faces, dialogue, or the payoff.
- Keep `@rtil` within the complete attribution line. Do not imitate the artist's signature, show only an isolated handle, or label the image "Art by @rtil," "official collaboration," or endorsed by the artist.
- Prefer reserving a dedicated footer during generation and requesting the exact text. If it is wrong, use the current image-editing tool to correct only the attribution region while preserving the artwork. Deterministic footer typesetting is an option only when explicitly permitted by the host; do not assume permission to use otherwise restricted image-processing methods.
- Repeat the same attribution in delivery copy and link to https://x.com/rtil . The credit indicates inspiration, not the artist's participation or authorization.

## Review and bounded correction

Inspect the actual generated page and details as needed:

1. Are the requested characters recognizable, with consistent hair, costumes, props, relationships, and speakers across panels?
2. Is the user's premise visible, is the reading order clear, and does the ending work?
3. Do contours, color, shading, expressions, and speech boxes reflect the selected references? Do not report a subjective resemblance as an objective percentage.
4. Is all visible text accurate and in the intended language, with no omissions, duplicates, or garbling? Is the exact footer `Creative & style inspiration: @rtil` visible and uncropped?

Make targeted edits and save new versions. Default to one initial generation and at most two targeted correction rounds. If problems remain, report them rather than retrying indefinitely or claiming success. Recover an existing result after a download/copy failure rather than paying to regenerate it.

## Delivery and continuation

Deliver the finished image, a short title, and a publishable caption. Display the image and provide its file. Keep the copy natural and concise. Save the storyboard, final prompt, reference selection, and review results in the task output directory, not in the Skill folder.

For requests such as "another episode" or "change the weather, keep everything else," use the previous result as a continuity reference. Preserve character designs, costumes, locations, and established events while changing the requested elements. Continue using the style references and fixed attribution.

## Environment and files

All bundled resources are relative to this file and can move with the Skill to another operating system. The workflow requires a generator that accepts image references and returns actual images, plus local file access. The generation workflow does not require a particular operating system, Node, or an external API key. The optional reference-download helper requires Python 3.9+; manual downloads are also supported. Follow the host's image-generation guidance and tool interface when available.

Use the user's output location or the current task's output directory. Follow repository AGENTS.md rules for temporary files. Keep generated artifacts outside the Skill folder. Do not publish, post, or publicly upload reference originals unless that external action is explicitly requested.
