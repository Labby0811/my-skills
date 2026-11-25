"""Inject the commented-code rules into the session or subagent context.

Reads the hook event from stdin and prints the SKILL.md body as
additionalContext, so the rules are always active without loading the skill.
"""
import json
import sys
from pathlib import Path

SKILL_PATH = Path(__file__).resolve().parent.parent / "skills" / "commented-code" / "SKILL.md"


def strip_frontmatter(markdown_text):
    """Remove the leading YAML frontmatter block from a markdown file.

    Args:
        markdown_text: Full file content.

    Returns:
        The content after the closing '---' line, or the input if no frontmatter.
    """
    if not markdown_text.startswith("---"):
        return markdown_text
    # Split into: empty, frontmatter, body
    parts = markdown_text.split("---", 2)
    return parts[2].lstrip() if len(parts) == 3 else markdown_text


def main():
    """Print the hook JSON that adds the rules to the context."""
    # Hook input tells which event fired; default to SessionStart if missing
    try:
        hook_event_name = json.load(sys.stdin).get("hook_event_name", "SessionStart")
    except (json.JSONDecodeError, ValueError):
        hook_event_name = "SessionStart"

    rules_text = strip_frontmatter(SKILL_PATH.read_text(encoding="utf-8"))
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": hook_event_name,
            "additionalContext": "COMMENTED-CODE MODE ACTIVE\n\n" + rules_text,
        }
    }))


if __name__ == "__main__":
    main()
