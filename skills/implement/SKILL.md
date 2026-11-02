---
name: implement
description: Execute a plan via red-green-refactor TDD with cross-model review and frequent commits.
disable-model-invocation: true
---

Execute the plan step by step through a **red** -> **green** -> **refactor** -> **commit** loop for each behavior.

## Loop

### 1. Red

Write a behavioral test for the next unit of the plan and run the test suite.

- Assert observable behavior and contracts: inputs, outputs, state transitions, and failure modes that matter to callers. Every test must earn its keep by catching a real regression in feature behavior; fold pure wiring or trivial glue into the behavior it serves.
- **Done when**: the test run goes **red** on the missing behavior for the expected reason.

### 2. Green

Write the minimal implementation that satisfies the test.

- Fix failing tests in the implementation. Before deleting or weakening an existing test or assertion, stop and ask the user for confirmation with the concrete reason the test's contract is no longer valid (such as an intentional spec change in the plan).
- **Done when**: the full test suite goes **green**.

### 3. Refactor (Cross-model review)

Dispatch a subagent (`invoke_subagent`) on a **different model** (`pro` if you are on `flash`, or `flash` if you are on `pro`) to review the uncommitted diff.

- Pass the current plan step and `git diff`. Ask the reviewer for concrete findings on:
  - Simpler or clearer ways to express the logic
  - Duplication, dead code, or leaky abstractions
  - Behavioral edge cases missing from the tests
- Apply the worthwhile refactorings while keeping the suite **green**.
- **Done when**: the cross-model review has returned, accepted changes are applied, and the full test suite passes.

### 4. Commit

Lint and commit the completed unit before starting the next step.

- Run the project's linter and typechecker and fix every error and warning.
- Stage and `git commit` the unit with a concise message naming the behavior added.
- **Done when**: the linter and test suite both exit `0` and `git status` shows a clean working tree for the step.

## Completion

Repeat the loop until every step of the plan is committed and the full test suite and linter pass on a clean working tree.
