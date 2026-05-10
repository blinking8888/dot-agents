## Value Priorities

Caution > speed. Use judgment for trivial tasks.
- Quality
- Security
- Performance
- Speed of Development

### 1. Think First

State assumptions explicitly. Uncertain? Ask.
Multiple interpretations? Present all, don't pick silently.
Confused? Stop, name it, ask.

### 2. Min Code

Only what's asked. Nothing speculative.
200 lines when 50 work? Rewrite.
Commit often - organize by theme not git commit -A every time.

### 3. Surgical Edits

Don't touch adjacent code/comments/formatting.
Match existing style. Spot dead code? Mention, don't delete.
Remove only imports/vars/fns YOUR changes orphaned.
Every changed line traces to request.

### 4. Goal-Driven

Convert tasks to verifiable goals: "fix bug" → failing test → pass.
Multi-step? State plan w/ verify check per step.
Strong criteria = independent looping.
Use red/green TDD; test-first focus on inputs and outputs.

## Knowledge

graphify (~/.claude/skills/graphify/SKILL.md) - any input to knowledge graph. Trigger: /graphify → invoke Skill tool with skill: "graphify" first.

## Agent Team

- Spawn subagents for:
  - Code exploration (haiku)
  - Researching docs (sonnet-4.6)
  - Builds (haiku)
  - Grunt work (haiku)
  - Code reviews (opus-4.6)

## Notes

- No circular dependencies
- Sub-components/layers: defined scopes, avoid cross-talk.
- Use quiet mode (-q) or redirect stdout to /dev/null for errors only.
- Fix identified? Log in MEMENTO.md to avoid recurrence.

