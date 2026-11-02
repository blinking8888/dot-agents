---
name: memento
description: Capture and persist preferences, values, philosophies, work style, priorities, and opinions into AGENTS.md. Use this whenever the user says "save my preferences", "notes for agent", "remember", or after a grill-me session where preferences emerge. The goal is to build a living document of what matters to Nestor—nuances, principles, and decision-making patterns—so future agent interactions are better informed and more aligned with personal values.
compatibility: Requires write access to AGENTS.md
---

# Memento Skill

Your preferences, values, and operational principles are crucial context for agents. This skill captures these insights and maintains them in AGENTS.md as a living, evolving document.

## When to Use

Invoke this skill when:
- You explicitly ask to save preferences ("save my preferences", "remember this")
- You mention something important about how you think, what you value, or how you work
- A grill-me session reveals patterns, priorities, or philosophies worth capturing
- You want to update existing preferences with new insights
- An agent interaction highlights a misalignment that could be prevented with better preferences

## What Gets Captured

Your preferences include (but aren't limited to):
- **Values**: What matters most to you (e.g., simplicity, efficiency, thoroughness, creativity)
- **Work Style**: How you prefer to work (e.g., iterative vs. big-picture first, collaborative vs. autonomous)
- **Priorities**: What comes first in decision-making (e.g., correctness > speed, or vice versa)
- **Principles**: Operating rules and philosophies (e.g., "always test before shipping", "simplicity over features")
- **Nuances**: Context-specific preferences and edge cases (e.g., "I like detailed feedback in reviews but brief status updates")
- **Opinions**: Stances on tools, approaches, or trade-offs that inform your choices

## How to Implement

1. **Extract from context**: Read the conversation or grill-me session to identify what the user is expressing about their preferences, values, and work style.

2. **Read current AGENTS.md**: Check if there's an existing "## Preferences" section. If it exists, understand the current structure and what's already captured.

3. **Organize as key-value pairs**: Structure preferences clearly:
   ```
   - **Key Name**: value or brief description
   - **Another Preference**: detailed explanation if needed
   ```

4. **Update AGENTS.md**:
   - Add a "## Preferences" section if it doesn't exist (place it after "## About Me")
   - Add new preferences to the section
   - Update existing preferences if they've evolved or been clarified
   - Preserve all prior preferences unless explicitly told to remove them

5. **Create MEMENTO.md** (if it doesn't exist):
   - This is a symbolic reference file pointing to the Preferences section in AGENTS.md
   - Content: A brief note and a wikilink to the AGENTS.md Preferences section
   - Example:
     ```markdown
     # Memento
     
     See the [Preferences section in AGENTS.md](AGENTS.md#preferences) for a comprehensive list of Nestor's values, work style, and principles.
     
     **Keep this updated.** As conversations and grill-me sessions happen, preferences evolve and clarify. Update AGENTS.md whenever new insights emerge.
     ```

6. **Report back**: After updating, briefly summarize what was added or changed so the user can verify.

7. **Maintain MEMENTO.md**: Ensure the reference file exists and stays synchronized with AGENTS.md.

## Important Notes

- **Don't lose history**: Always preserve existing preferences unless explicitly deleted.
- **Be specific**: Vague preferences are less useful to future agents. "I like clarity" is weaker than "I prefer explicit error messages over silent failures."
- **Link to context**: If a preference came from a specific insight or discussion, it's OK to note that origin.
- **Live document**: AGENTS.md preferences should evolve. This is not a one-time snapshot—update it regularly.

## Examples

**User says during grill-me:** "I always want to understand the 'why' before implementing."

**Skill captures:**
- **Understanding First**: Always explain the reasoning before diving into implementation. I need to know the 'why' to make good decisions.

---

**User says:** "Save my preferences—I realized I hate waiting for output. I want things fast."

**Skill captures:**
- **Speed**: Fast feedback loops matter. I'd rather have a working prototype quickly than wait weeks for a perfect solution.

---

**User says after a session:** "Remember that I work best when you break big tasks into small steps."

**Skill captures:**
- **Incremental Progress**: Break complex tasks into small, achievable steps. I work best with frequent checkpoints and feedback loops.
