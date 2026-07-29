# Auxiliary experiment program

This directory is the archived oTree program for the auxiliary experiment in
**Strategic De-socialization**. The study was designed to examine mechanisms
behind human responses to AI counterparts by combining strategic choices with
incentivized beliefs and reported satisfaction. The public sample reported in
the working paper is 35 participants.

The mechanism exercise did not produce reliable structural social-preference
estimates. This program is therefore useful as a record of the attempted design,
not as evidence that stable preference parameters were successfully recovered.

## Collected session structure

The active `games` session contains:

1. `general_instruction`
2. six numbered blocks, each containing one `ug`, one `tg`, and one `pd` task
3. `bret`
4. `after_survey`

Within each numbered block, the three tasks are shuffled when `settings.py` is
loaded. For example, block 1 contains `ug1`, `tg1`, and `pd1` in a random order,
followed by a separately shuffled block 2, and so on through block 6.

This is **partial within-block randomization**. The six block positions remain
fixed, the numbered payoff variants remain attached to those positions, and the
risk/survey tasks remain at the end. The program does not randomly permute all
18 strategic tasks.

## Measurement map

| App family | Intended construct | Recorded material |
|---|---|---|
| `ug1` - `ug6` | Sequential mini Ultimatum Games | Choices by role, beliefs about counterpart choices, outcome satisfaction |
| `tg1` - `tg6` | Sequential mini Trust Games | Choices by role, beliefs, outcome satisfaction |
| `pd1` - `pd6` | Sequential mini Prisoner's Dilemma variants | Conditional choices, beliefs, outcome satisfaction |
| `bret` | Risk preference | Bomb-risk elicitation task |
| `after_survey` | Demographics and human/AI perceptions | Attitudes, perceived traits, prior LLM use |

Belief payments use a quadratic-scoring-rule implementation in the task code.
The design attempted to connect choices, beliefs, and satisfaction to a
Fehr-Schmidt-style social-preference account.

## Why the intended mechanism test is inconclusive

Participants had substantial difficulty understanding and completing the
belief-elicitation task. The resulting structural estimates were noisy,
method-sensitive, and sometimes implausible. With only 35 participants and a
demanding elicitation procedure, the program does not support a strong claim
that the intended social-preference parameters were identified.

A future redesign would need simpler instructions, stronger comprehension
checks, more informative choices, a larger independent sample, and validation
that participants understand the scoring rule before parameter estimation.
Even with those improvements, stable recovery of social-preference parameters
in this setting remains uncertain.

## Runtime notes

- oTree: `5.11.1`
- interface language: Simplified Chinese
- currency conversion: 0.25 CNY per point
- participation fee in settings: 10 CNY
- LLM used during collection: ChatGPT-4.1

For a local demonstration:

1. Create and activate an isolated Python environment.
2. Run `pip install -r requirements.txt`.
3. Set a non-public `OTREE_ADMIN_PASSWORD`.
4. Follow the oTree 5 local-server workflow and create the `games` session.

The current `requirements.txt` does not encapsulate the historical
botex/OpenAI runtime. A present-day model call should not be assumed to reproduce
the collected ChatGPT behavior. The checked-in `SECRET_KEY` is a development
placeholder, and some participant-facing Chinese strings appear to contain
encoding damage; both require review before deployment.

## Files and archival boundaries

- `settings.py` constructs the partially randomized session sequence.
- `requirements.txt` records the oTree dependency.
- `db.sqlite3` contains development or demonstration state, not the complete
  35-participant research dataset.
- `yaml_backup.gz` is an application archive, not a documented analysis file.
- `_static/` and the app directories contain interface assets and templates.
- `lottery/` is present but not included in the active `games` sequence.

No Python, HTML, configuration, database, or image file was changed during the
2026 documentation revision. For the evidence limits and the decision not to
continue collecting data under this design, see the
[project README](../../README.md).
