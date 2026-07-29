# Main experiment program

This directory is the archived oTree program for the main experiment in
**Strategic De-socialization**. The study compared decisions involving
explicitly identified human and ChatGPT counterparts across several strategic
settings. The public sample reported in the working paper is 84 participants.

This README documents the program as collected. It does not claim that the
current repository can reproduce the historical LLM responses or the reported
numerical results without the original deployment environment and
analysis-ready data.

## Collected session sequence

The active `games` session in `settings.py` uses the following fixed order:

1. `general_instruction`
2. `trust`
3. `Ultimatum`
4. `Repeated_PD` through `Repeated_PD8`
5. `dictator`
6. `punishment_simple`
7. `guess_three_fourth`
8. `bret_simple`
9. `after_survey`

The eight `Repeated_PD` apps are eight separately instantiated indefinitely
repeated Prisoner's Dilemma supergames. Their repeated decisions provide a
denser behavioral record than the one-shot games, but do not create additional
independent participants.

`punishment_simple` is the collected public-goods app despite its historical
name. In the checked-in source it runs for 20 rounds with four players, a
20-point endowment, and a contribution multiplier of 1.6. The
punishment-transfer fields and payoff logic are commented out. The program
changes its result-display treatment after round 10, so this app should not be
described as an active punishment experiment.

## Design map

| Component | Role in the study | Important boundary |
|---|---|---|
| `trust` | Trust and return decisions | One-shot cells are small and exploratory |
| `Ultimatum` | Proposal and response behavior | Small cells; reported proposal difference should not be generalized broadly |
| `Repeated_PD` - `Repeated_PD8` | Indefinitely repeated cooperation | Eight supergames; repeated rounds are nested within participants |
| `dictator` | Allocation without retaliation | Used to separate allocation preferences from strategic enforcement |
| `punishment_simple` | Repeated public-goods contributions and result-display conditions | Punishment code is inactive; fixed location late in the session |
| `guess_three_fourth`, `bret_simple` | Auxiliary cognitive/risk measures | Not the central human-versus-AI outcomes |
| `after_survey` | Demographics and attitudes toward human/ChatGPT players | Self-reports do not independently identify a mechanism |

## Main limitation: fixed task order

The complete task order above was not randomized or counterbalanced.
Rematching opponents does not remove learning, fatigue, carryover, or order
effects across games. More participants under the same sequence would not fix
this design problem; a new study would need a rebuilt counterbalanced or
fully randomized protocol.

## Runtime notes

- oTree: `5.11.1`
- interface language: Simplified Chinese
- currency conversion: 0.25 CNY per point
- participation fee in settings: 10 CNY
- LLM used during collection: ChatGPT-4o-2024-11-20

For a local demonstration:

1. Create and activate an isolated Python environment.
2. Run `pip install -r requirements.txt`.
3. Set a non-public `OTREE_ADMIN_PASSWORD`.
4. Follow the oTree 5 local-server workflow and create the `games` session.

The historical botex/OpenAI orchestration is not pinned by
`requirements.txt`. Model endpoints and default behavior have changed since
collection, so a present-day run is not a behavioral replication.

The checked-in `SECRET_KEY` is only a placeholder and must be replaced for any
deployment. Some participant-facing Chinese strings in this snapshot appear to
have encoding damage and should be audited before use.

## Files and archival boundaries

- `settings.py` defines the active session sequence.
- `requirements.txt` records the oTree dependency.
- `db.sqlite3` contains development or demonstration state, not the complete
  research dataset.
- `yaml_backup.gz` is an application archive, not a documented dataset.
- `_static/` and the app directories contain interface assets and templates.
- `stag-hunt-liu-yi-indefiniteref/` and other apps omitted from the active
  session should be treated as inactive or reference material unless separately
  verified.

No Python, HTML, configuration, database, or image file was changed during the
2026 documentation revision. For interpretation and the decision not to extend
the sample, see the [project README](../../README.md).
