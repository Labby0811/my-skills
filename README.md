# my-skills

Personal skills for Claude Code and Codex.

| Plugin | What it does | Claude Code | Codex |
|---|---|---|---|
| `commented-code` | Short docstrings, block comments, descriptive names, units in names. Layered on top of ponytail. | Always active (SessionStart hook) | Always active via `~/.codex/AGENTS.md` |
| `step-by-step-teacher` | Guides hands-on work one verified step at a time; the user implements. | Loaded when the task matches | Loaded when the task matches |

## Setup on a new PC

The repo holds the rules. Each PC needs its own local configuration: Claude
plugins, the Codex skill link and `~/.codex/AGENTS.md` are not synced by Git.
Repeat these steps on every PC.

Requirements: `git`, `python3` (used by the commented-code hook).

### 1. Clone the repo

```bash
git clone https://github.com/Labby0811/my-skills.git ~/Desktop/Giuseppe/my-skills
```

### 2. Claude Code

```bash
claude plugin marketplace add Labby0811/my-skills
claude plugin install commented-code@giuseppe-skills
claude plugin install step-by-step-teacher@giuseppe-skills
```

Restart Claude Code. At startup the context shows `COMMENTED-CODE MODE ACTIVE`.

### 3. Codex

Link the teacher skill, so Codex reads it straight from the repo:

```bash
mkdir -p ~/.codex/skills
ln -s ~/Desktop/Giuseppe/my-skills/plugins/step-by-step-teacher/skills/step-by-step-teacher ~/.codex/skills/step-by-step-teacher
```

Make commented-code always active: write this into `~/.codex/AGENTS.md`
(append it if the file already has content):

```markdown
# Global instructions

When writing or editing code, always follow the rules in
`~/Desktop/Giuseppe/my-skills/plugins/commented-code/skills/commented-code/SKILL.md`.
Read it once at the start of a session. Ponytail is not installed in Codex:
apply the documentation and naming rules, and skip the parts that only describe
how they combine with ponytail.
```

Restart Codex. `step-by-step-teacher` appears in the skill picker.

## Update

Claude Code reads its own copy of the plugins; Codex reads the clone.

```bash
cd ~/Desktop/Giuseppe/my-skills && git pull
claude plugin marketplace update giuseppe-skills
```

Restart both tools to load the new rules.
