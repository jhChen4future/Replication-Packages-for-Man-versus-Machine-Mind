# Experiment screenshots

This directory was intended to hold Chinese-language screenshot decks for the
main and auxiliary experiments. The current files are **not usable screenshot
documentation**.

## Current artifact status

| File | Size in the repository | Status |
|---|---:|---|
| `Main Experiments Screenshots CN.pptx` | 2 bytes | Empty placeholder; not a valid presentation |
| `Auxiliary Experiments Screenshots CN.pptx` | 2 bytes | Empty placeholder; not a valid presentation |
| `temp` | 2 bytes | Empty placeholder with no documented content |

The placeholders were retained so that their historical names remain visible.
They were not replaced with reconstructed slides because no original screenshot
images or valid decks are present in this repository, and a reconstruction
would not be primary documentation of what participants actually saw.

## Where to inspect the interfaces

The participant-facing HTML templates and static assets are available in:

- [the main experiment program](../Codes/Main_Experiment_GPTcoop_punish_simple_random_seat/)
- [the auxiliary experiment program](../Codes/Auxiliary_Experiment/)

Those source files are the closest available record of the interfaces, but some
Chinese strings in the public snapshot appear to have character-encoding
damage. The checked-in code should therefore be audited before it is used to
reconstruct screenshots.

## Requirements for a future screenshot archive

A complete replacement should be generated from a verified historical
environment and should record:

1. the program commit and oTree version;
2. the session configuration and participant role shown;
3. every instruction, comprehension-check, decision, wait, feedback, and survey
   screen in participant order;
4. both human- and ChatGPT-counterpart identity conditions;
5. the two public-goods result-display conditions;
6. the randomized auxiliary-task order used for the captured session;
7. viewport size, language, date, and model/deployment version; and
8. any known difference between the captured interface and the collected
   experiment.

Until such an archive is available, do not cite the `.pptx` placeholders as
evidence of the experimental procedure.
