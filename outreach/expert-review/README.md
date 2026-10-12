# Asking experts to review a state, by email

Special-education professionals shouldn't have to learn GitHub to help.
`tools/expert_review.py` turns a state's open questions into a plain-text
email. The expert hits Reply and types `Y`, `N` or `?` in brackets. A
maintainer then reads the reply back into the repository.

Nevada is the worked example: [rounds/NV-20261010/email.txt](rounds/NV-20261010/email.txt)
(a sample with the sender fields left in `[BRACKETS]`; it has not been sent).

## Send a request

```bash
python tools/expert_review.py request NV \
    --sender "Your Name" --greeting "Dr. Lee" --reply-to you@example.org
```

Any state with a layer works (`NV`, `Texas`, ...). The command writes a round
folder `rounds/<ST>-<date>/` with:

- `email.txt`: the subject line, then the body. Paste it into a plain-text
  email. Without `--sender`, `--greeting` and `--reply-to`, the email carries
  visible `[BRACKETS]` to fill in by hand.
- `key.json`: what each item id (`A3`, `C12`, ...) means. Keep it; the reply
  reader needs it.

Check the email before you send it. Every number in it comes from the data, but
the choice of expert and the greeting are yours.

## What goes in the email

| Part | Where it comes from in the repo | The expert answers |
|---|---|---|
| Intro, "what SPEDLex is" (what an entry holds, what it is not, and its two uses: privacy tools and AI wording tools), "why experts" | `template.txt`, plus live counts from `data/` | nothing |
| **A. Key questions** | (1) documents dated 3+ years ago (`--stale-years`), (2) concepts the state layer defined whose `note` says *verify*, *may differ*, *ambiguous* or *name from the ... form*, (3) hand-written questions in `extras/<state>.tsv` | Y / N / ? and a comment |
| **B. Same thing, different name?** | every state-tagged `synonym` or `legacy` string on a concept | Y / N / ? |
| **C. Real term?** | every concept with `review.status = candidate` that cites the state | Y / N / ? |
| **D. What are we missing?** | defaults in `template.txt` plus `missing` rows in `extras/<state>.tsv` | free text |

Part A is written to be worth doing alone: the email says so.

## Reuse it for another state

1. Run the command for the new state. Nothing else is required.
2. Optional: add `extras/<state_name>.tsv` (lower case, underscores; see
   `extras/nevada.tsv` for the columns) for judgment calls the data can't
   reveal on its own. Good ones are: "we treat X as another name for Y, is that
   right?", "is this ambiguous acronym really used?", and "which tests or
   diplomas are current?".
3. If Parts B and C run past about 60 lines, pass `--limit 30`.
4. To change the wording for every state, edit `template.txt` (keep the
   `{{PLACEHOLDERS}}` and `@@` lines).

A note written into a layer's `note=` option becomes a Part A question
automatically if it contains one of the cue phrases in `CUES` at the top of
`tools/expert_review.py`. When you draft a layer and you aren't sure of
something, say so in the note ("Verify the current name") and it will be asked.

## Read a reply

Save the reply as plain text (quoted original included; the reader copes with
`>` quoting), then:

```bash
python tools/expert_review.py reply rounds/NV-20261010/key.json some-reply.txt
```

It writes two files next to the reply:

- `*.proposed-reviews.tsv`: rows in `sources/reviews.tsv` format. Only a clean
  **Y** on a Part C item (or a Part A item about a concept) becomes `accept`,
  and only an **N with a comment** on a Part C item becomes `reject`. The
  reviewer column is the person's name and role if they chose credit A or B,
  or `anonymous-<ST>-<hash>` if they chose C or didn't answer. Affiliation is
  never written here: the review log is part of the public dataset.
- `*.followups.md`: everything that needs a person to decide: every N, `?`,
  comment and free-text answer (name pairs to fix, missing terms, outdated
  documents).

**Nothing is applied automatically.** The tool never writes
`sources/reviews.tsv`: a maintainer reads the proposal, appends the rows they
accept, runs `python -m spedlex.build`, and turns the follow-ups into edits to
`sources/states/<state>.py`. A *Yes* on a name pair (Part B) is recorded only by
the lack of a correction; there is no per-string review status yet.

## Credit

The email offers three choices: A (name, role, affiliation), B (name and role)
or C (anonymous). The follow-ups file includes a ready-made `CONTRIBUTORS.md`
row for A and B. A maintainer adds it by hand. Unclear or missing answers are
treated as anonymous.

## Privacy

- Raw replies hold names and email addresses. Keep them out of the repository;
  commit only the proposed rows and any edits they cause.
- The email tells experts not to send student information. If a reply
  contains any, delete it before saving anything.
