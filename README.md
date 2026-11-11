# Fanart Studio - rtil Style Reference

An agent Skill that turns **a favorite fictional character + a new situation** into a finished fanart illustration or short comic, with actual visual references and visible attribution.

> Use $rtil-fanart-studio to create a three-panel English comic about Frieren and Fern running a magic shop.

## What it does

- Checks character identity, recognizable details, personality, and relationships.
- Develops themed reinterpretations, character interactions, or slice-of-life side stories.
- Selects relevant rtil visual references for linework, color, expressions, staging, and comic layout.
- Produces an illustration or a short comic, then checks continuity, lettering, and attribution.
- Supports follow-ups such as "another episode" or "change the setting, keep the character designs."

Titles, dialogue, signs, captions, and delivery copy default to English. Users can explicitly request another content language.

Every final image includes this exact credit:

**Creative & style inspiration: @rtil**

## Requirements

- An agent environment that can read Skills and use an image generator with **reference-image input**. Codex with its built-in image generator is the primary workflow.
- Git for the clone instructions below, or GitHub's Download ZIP option.
- Python 3.9+ only for the optional reference downloader; it uses the standard library and requires no API key. An agent can also retrieve and verify references directly from the manifest.

The Skill provides instructions and reference handling, not a standalone image model. Generation availability and costs depend on the host environment.

## Install in Codex

Clone the repository into your personal Skills directory. If the destination already exists, update that checkout rather than cloning over it.

### Windows / PowerShell

```powershell
$skillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$skillsDirectory = Join-Path $skillHome 'skills'
New-Item -ItemType Directory -Force -Path $skillsDirectory | Out-Null
$skillDirectory = Join-Path $skillsDirectory 'rtil-fanart-studio'
git clone https://github.com/xuntianx/rtil-fanart-studio.git "$skillDirectory"
python (Join-Path $skillDirectory 'scripts/fetch_references.py')
```

### macOS / Linux / Git Bash

```bash
skill_home="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$skill_home/skills"
skill_directory="$skill_home/skills/rtil-fanart-studio"
git clone https://github.com/xuntianx/rtil-fanart-studio.git "$skill_directory"
python3 "$skill_directory/scripts/fetch_references.py"
```

For Git Bash on Windows, use `python` if `python3` is not available. If the Skill does not immediately appear, start a new chat or reload the host's Skills list.

## Try it

```text
Use $rtil-fanart-studio. Draw Kakashi working a night shift at a
convenience store as a three-panel comedy. Use English dialogue.
```

```text
Use $rtil-fanart-studio. Create a single illustration of Nami and Robin
running a seaside cafe, with a small visual joke about their roles.
```

```text
Use $rtil-fanart-studio. Continue the previous episode with the same
character designs and shop, but make it a rainy day.
```

The agent should deliver actual artwork, a title, and a caption. A prompt alone is not a finished output.

## Reference images and credit

The public repository contains a [source manifest](references/source-manifest.json), not copies of rtil's original artwork. `scripts/fetch_references.py` retrieves the five listed images into a Git-ignored local folder and checks their SHA-256 hashes. Existing verified files are reused; changed or invalid files are not silently overwritten.

```bash
python3 scripts/fetch_references.py --check
```

Attribution identifies creative and visual inspiration. This is an independent Skill, not an official rtil release or an endorsed collaboration. Reference art and fictional characters remain associated with their respective creators and rights holders. See [ATTRIBUTION.md](ATTRIBUTION.md).

## Files

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Agent instructions and the fixed attribution rule |
| [agents/openai.yaml](agents/openai.yaml) | Codex display metadata and example invocation |
| [references/style-guide.md](references/style-guide.md) | Visual characteristics and reference selection |
| [references/generation-contract.md](references/generation-contract.md) | Prompt structure, output, and acceptance criteria |
| [references/source-manifest.json](references/source-manifest.json) | Original sources, dates, and file hashes |
| [scripts/fetch_references.py](scripts/fetch_references.py) | Optional local reference downloader |

## Validation status

Prepared on 2026-11-11. The underlying workflow was exercised with a real three-panel fan comic using three image references and an on-image credit. English instructions and the English attribution rule were subsequently validated as text/configuration changes; a new English image has not yet been generated as part of that revision.

The downloader and file checks are tested on Windows. macOS/Linux instructions use relative paths and Python's cross-platform standard library, but have not been run on those operating systems. Visual resemblance remains a subjective review rather than a guaranteed match.
