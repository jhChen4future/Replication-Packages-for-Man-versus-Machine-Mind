# Experiment programs

This directory contains the oTree programs used in the two experiments behind
**Strategic De-socialization**. It is a research archive, not a turnkey
replication package: the experimental interfaces are present, but the complete
analysis-ready participant data, analysis pipeline, and a fully pinned LLM
runtime are not.

Read the [repository overview](../README.md) before interpreting results or
reusing the programs. It records the fixed-order problem, task-comprehension
issues, evidence limits, funding constraint, and model-version drift that led to
ending data collection under this design.

## Directory guide

| Directory | Collected protocol | Public sample | Model used during collection | Detailed notes |
|---|---|---:|---|---|
| [`Main_Experiment_GPTcoop_punish_simple_random_seat/`](./Main_Experiment_GPTcoop_punish_simple_random_seat/) | Trust, Ultimatum, eight indefinitely repeated Prisoner's Dilemma supergames, Dictator, Public Goods, risk and survey tasks | 84 | ChatGPT-4o-2024-11-20 | [README](./Main_Experiment_GPTcoop_punish_simple_random_seat/README.md) |
| [`Auxiliary_Experiment/`](./Auxiliary_Experiment/) | Six blocks of sequential mini Ultimatum, Trust, and Prisoner's Dilemma tasks with choices, beliefs, and satisfaction measures | 35 | ChatGPT-4.1 | [README](./Auxiliary_Experiment/README.md) |

The active protocol in each directory is defined by its top-level
`settings.py`. Other app folders may be prototypes, dependencies, copied
references, or inactive alternatives and should not be assumed to have been
part of the collected session.

## Historical software environment

- oTree: `5.11.1`
- botex: `0.1.0` (historical integration version; not the current release)
- interface language: Simplified Chinese
- currency: CNY

Install the Python dependencies inside one experiment directory with
`pip install -r requirements.txt`, then use the standard oTree 5 workflow to
create a local demonstration session. Exact deployment also depends on the
historical botex/OpenAI integration, session labels, and model availability,
which are not fully encapsulated here.

Do not place API keys in this repository. `OTREE_ADMIN_PASSWORD` is read from an
environment variable, and the placeholder development `SECRET_KEY` in the
archived settings is not suitable for a public deployment.

## Design details that filenames do not show

### Main experiment

The game sequence is fixed in `settings.py`. Participants may be rematched
between games, but the games themselves were not fully randomized or
counterbalanced. The `punishment_simple` app name is historical: its active
payoff code implements a 20-round public-goods contribution task, while the
punishment-transfer block is commented out. The task changes how round results
are displayed after round 10. See the experiment-level README for the exact
sequence and interpretation.

### Auxiliary experiment

The auxiliary program randomizes the order of `ug`, `tg`, and `pd` only within
each of six numbered blocks. The block order remains fixed, and the risk and
survey tasks remain at the end. This is partial within-block randomization, not
full randomization of all games.

## Data and reproducibility status

| Artifact | What it is | What it is not |
|---|---|---|
| `db.sqlite3` in each experiment directory | Development or demonstration session state included with the archived program | The complete data for the 119 research participants |
| `yaml_backup.gz` | An oTree application backup/archive | A documented analysis dataset |
| Python and HTML app files | The historical experimental program snapshot | A guarantee that the original LLM behavior can be reproduced today |
| Embedded images and static files | Interface assets | A substitute for a screenshot protocol |

Some Chinese strings in the public code snapshot appear to contain character
encoding damage. Review all participant-facing text before attempting to run or
translate the programs. No source file has been repaired as part of the current
documentation update, so the historical program remains unchanged.

The Stata/Python scripts used for analysis, plotting, and parameter estimation
are not currently organized here as a complete independently reproducible
pipeline. In particular, repeated rounds should not be treated as independent
participants, and the auxiliary structural social-preference estimates should
not be treated as reliable recovered parameters.

## Reuse

No explicit software or data license is currently included in the repository.
Public availability alone should not be interpreted as permission for
unrestricted reuse. Contact the author through the
[project website](https://jhchen4future.github.io/research/strategic-desocialization/)
for questions about replication or reuse.
