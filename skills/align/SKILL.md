---
name: align
description: Align with the agent before execution.
disable-model-invocation: true
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolve dependencies between decisions one by one. For each question, give your recommended answer.

Ask the questions one at a time.

If the codebase can answer a question, explore the codebase instead.

Use the ask_user_question tool.

## Steps

1. **Interview.** Resolve every branch of the design tree. Done when each decision has an answer from the user or an accepted recommendation.
2. **Draft the plan file.** Write it to a md file with a unique filename, or the name the user gives. Use the Plan file sections below. Done when every section is filled or marked "Not applicable" with a reason.
3. **Review with the user.** Show the file. Change it until the user approves. Done when the user says the plan is approved.
4. **Record disagreements.** If the user rejected a recommendation, append it to the project's AGENTS.md under `## IMPORTANT NOTES`.

Do not write implementation code before step 3 is done.

## Plan file

The plan file serves two readers. The user must understand the plan. The agent must know how to build it. Write each section for both.

Sections, in this order:

1. **Goal.** One short paragraph. State what is built and why.
2. **Approach.** The agreed way to implement it. Name the key decisions and the reason for each.
3. **Block diagram.** Show the parts and how they connect. Use a mermaid `flowchart`.
4. **Sequences.** Show the order of calls for each main flow. Use a mermaid `sequenceDiagram`.
5. **Contracts.** Show each API, function signature, message, or data shape that crosses a boundary. Give inputs, outputs, and errors. Write "Not applicable" if none.
6. **Code.** Include code that is available or applicable: existing code to reuse, snippets, or skeletons. Link existing code by path. Write "Not applicable" if none.
7. **Behaviors.** The test source of truth. See below.
8. **Open items.** Questions the user has not answered yet.

### Behaviors

Group behaviors by feature. One group per feature that will be built.

Each group has two lists:

- **Acceptance behaviors.** What the user sees or gets, from outside the system.
- **Unit behaviors.** What one part does alone, with edge cases and errors.

Write each behavior as one sentence: `Given <state>, when <action>, then <result>.` Give each an id (for example `AUTH-A1` for acceptance, `AUTH-U1` for unit). Each behavior must be testable. A test can pass or fail on it.

Every feature in Approach has a group. Every contract has at least one behavior.

## Writing style

Follow ASD-STE100 about 80%. Do not be strict.

- Use short sentences. Aim for 20 words or fewer.
- One idea per sentence.
- Use active voice and simple present tense.
- Use one word for one meaning. Keep the same term for the same thing.
- Use the imperative for instructions.
- Use simple words. Use "use", not "utilize".
- Put the condition before the action.
- Use lists and tables for steps and parameters.
- Break the rules when a rule makes the text harder to read. Technical names are allowed.
