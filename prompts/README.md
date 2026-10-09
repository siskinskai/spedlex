# Prompt templates

SPEDLex was started with an AI model, and we expect most contributions to
use one too. These templates are the project's shared instructions for that
work. They're written to be model-neutral: paste them into Claude, ChatGPT,
Gemini, a local model, or a coding agent.

| Template | Use it to | Who decides |
|---|---|---|
| [add-state.md](add-state.md) | Draft a new state layer from the state's documents | You review the draft before opening a pull request |
| [audit-layer.md](audit-layer.md) | Have a second model (or a fresh chat) check a drafted layer against its documents | You fix what it finds |
| [precheck-review.md](precheck-review.md) | Find each candidate term in its cited document, to speed up a human review | A person with special-education expertise |

Coding agents that work inside the repository (Claude Code, Codex, Copilot,
Cursor and others) also read [AGENTS.md](../AGENTS.md) at the root, which
holds the rules every change must follow.

## Ground rules for model-assisted work

1. **A person is responsible for every contribution.** Whoever opens the
   pull request has checked the work, whatever drafted it.
2. **Say which model helped.** Set `ASSISTED_BY` in the layer module to the
   model's API identifier (e.g. `claude-opus-5-5`), or `"none"`. The build
   copies it onto every source the layer adds, so data users can see and
   filter by it. Name the model in your pull request too.
3. **Give the model the documents.** Don't ask a model to recall a state's
   rules from memory. Attach or paste the documents. Every entry must cite
   one.
4. **Check with a different model or a fresh chat.** Run
   [audit-layer.md](audit-layer.md) before submitting. Drafting and checking
   in the same conversation tends to repeat the same mistakes.
5. **Models don't review.** `sources/reviews.tsv` records human expert
   judgment only.
6. **No student information, ever,** in prompts, documents or outputs. Use
   public state documents only.

## Improving a template

These are meant to get better with use. If a template produced errors you
had to fix, or you found wording that works better with your model:

1. Edit the template and bump its `version` in the header comment.
2. Add the model you tested with to `tested with`.
3. In the pull request, say what went wrong before and what changed after.
   A short before-and-after example (a few entries) is the most convincing
   evidence.

Keep templates model-neutral. If something only helps one model, put it in
a clearly labeled note at the end of the template rather than in the main
instructions. New templates are welcome, for example for Part C, Section
504, or instrument catalogs (see [ROADMAP.md](../docs/ROADMAP.md)).
