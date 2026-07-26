# Strategic De-socialization

### Experimental Evidence on Human Interaction with Large Language Models

This project asks a simple question with an increasingly complicated answer:
**when does an LLM remain a social counterpart, and when do people instead treat
it as a predictable strategic object?**

Across linked laboratory experiments, participants interacted with either human
or ChatGPT counterparts in allocation, trust, bargaining, repeated cooperation,
and public-goods settings. The evidence does not support a single, uniform
anti-AI bias. Instead, behavior appears to depend on the strategic environment:
people can treat AI and human counterparts similarly when retaliation is absent,
yet become less reciprocal or more willing to exploit AI when its behavior is
perceived as reliably cooperative.

The repository retains its original URL and the earlier project name, *Man versus
Machine Mind*, so that existing links continue to work. **Strategic
De-socialization** is the project's current public-facing title.

[Read the working paper](./Paper/Writing_sample_latest.pdf) ·
[View the project page](https://jhchen4future.github.io/research/strategic-desocialization/) ·
[Browse the experiment programs](./Codes/)

## Project in brief

| | |
|---|---|
| **Research setting** | Human decisions involving human or explicitly identified ChatGPT counterparts |
| **Main experiment** | Trust Game, Ultimatum Game, indefinitely repeated Prisoner's Dilemma, Dictator Game, Public Goods Game, and a risk task |
| **Auxiliary experiment** | Sequential Prisoner's Dilemma, mini Trust Game, and mini Ultimatum Game, with choices, incentivized beliefs, and reported satisfaction |
| **Participants** | 84 in the main experiment and 35 in the auxiliary experiment |
| **Collection period** | December 2024-April 2025 |
| **Location** | Neuromanagement Laboratory, Zhejiang University |
| **LLM implementations** | `ChatGPT-4o-2024-11-20` in the main experiment and `ChatGPT-4.1` in the auxiliary experiment |

### Core argument

The working paper describes **strategic de-socialization** as a shift from
reciprocal, socially contingent interaction toward simpler, more instrumental
behavior when a person believes an AI counterpart is predictable and unlikely to
punish exploitation. The claim is not that people always dislike or exploit AI.
It is that the social meaning of the counterpart can weaken when strategic
leverage changes.

## Important research status and known limitations

> [!IMPORTANT]
> **Data collection is complete, and this experimental design will not be
> extended with additional participants.** This decision reflects the combined
> cost of repairing the design, task-comprehension problems, uncertain model
> identification, and limited remaining funding. It should not be read as a
> claim that the existing sample provides definitive causal or population-level
> estimates.

1. **The main experiment has a fixed-order problem.** Participants were
   rematched before each game, but the games themselves followed a fixed
   sequence rather than being fully randomized or counterbalanced. Learning,
   fatigue, carryover, and order-reversal effects therefore cannot be cleanly
   separated from game-specific treatment effects. A rigorous correction would
   require rebuilding and rerunning the study with randomized or
   counterbalanced game orders. Recruiting more participants under the existing
   sequence would not repair this limitation, while a full redesign would be
   costly.

2. **The intended social-preference model was too demanding for the observed
   task comprehension.** The auxiliary experiment was designed to explain
   behavior using choices, elicited beliefs, reported satisfaction, and a
   Fehr-Schmidt-style social-preference model. In practice, many participants
   had difficulty with the belief-elicitation task and its quadratic scoring
   rule. The resulting structural estimates were noisy, unstable across
   methods, and sometimes implausible. The paper therefore does not use them as
   a basis for firm conclusions. A future study would need simpler instructions,
   stronger comprehension checks, and substantially more informative choices;
   even then, the literature suggests that convincing recovery of stable
   social-preference parameters in a setting like this is difficult and
   uncertain.

3. **The remaining budget could not support a sufficiently powered redesign.**
   The experiment was supported by an SRTP provincial undergraduate innovation
   research grant of RMB 10,000 and approximately RMB 2,000 in additional
   support from the supervisor. After necessary participant payments, OpenAI API
   use, and other operating costs, the remaining funds were not enough to recruit
   the sample required for a conventionally powered rerun. Given the design
   issues above, continuing to recruit under the same protocol would not have
   been a responsible use of the remaining resources.

4. **The strength of evidence differs across games.** The one-shot Trust and
   Ultimatum Game cells are small and do not meet conventional power
   expectations, so their estimates should be treated as exploratory even when
   a reported comparison is statistically significant. The indefinitely
   repeated Prisoner's Dilemma provides a much denser behavioral record through
   eight separately rematched supergames. Those trajectories reveal recurring
   strategy patterns that differed from the project's initial expectations but
   shared common features across participants. They can inform a descriptive
   account of behavior; repeated rounds, however, do not turn a small number of
   independent participants into a large independent sample.

5. **AI capability changed faster than the original design assumed.** The
   project began from the expectation that human bias toward AI would change
   more slowly than model capability over horizons such as three, five, or ten
   years. The intuition was that identity-based reactions are partly formed
   through long-run socialization, social interaction, and cultural
   representations of AI, including films such as *The Terminator*, and would
   not change merely because a model became incrementally more capable. That
   premise made one or two frontier models seem like a reasonable experimental
   snapshot. From the "DeepSeek moment" to rapidly deployed agentic systems,
   however, AI capability has begun to alter everyday experience rather than
   only perceived model quality. A study using only one or two
   state-of-the-art-at-the-time models may therefore conflate stable human bias
   with model-specific capability and moment-specific expectations. Future work
   should compare multiple models, capability levels, identities, and time
   snapshots.

## What the current data suggest

These results are reported to describe the existing data, subject to the notice
above.

| Setting | Descriptive result | Interpretation in the working paper |
|---|---|---|
| **Trust and Dictator Games** | No statistically significant mean difference was detected between decisions involving human and AI counterparts. | The data do not support a simple, across-the-board aversion to AI in low-enforcement settings. A null result is not evidence that the full choice distributions are identical. |
| **Ultimatum Game** | Human proposers offered AI responders 7.85 of 20 tokens on average, compared with 9.25 to human responders (`p = .006`). | Participants may have expected AI to be less willing to reject and punish an unequal offer. The small cell sizes make this an exploratory result. |
| **Indefinitely repeated Prisoner's Dilemma** | Human cooperation rates were similar with AI and human partners, but Tit-for-Tat behavior was less common and non-contingent play more common against AI. | Similar aggregate cooperation can conceal a shift away from reciprocal strategy. |
| **Public Goods Game** | Mean human contributions were 9.85 in all-human groups, 5.85 with one AI member, and 2.22 with two AI members. | Stable AI contributions may invite strategic free-riding rather than reciprocal cooperation. |
| **Auxiliary mechanism measures** | Participants expected AI partners to cooperate more often, while the structural social-preference estimates were not reliable. | Beliefs about predictable AI cooperation are consistent with strategic adaptation, but the intended parameter model did not successfully explain the data. |

The narrow conclusion is therefore not that AI benevolence universally reduces
human cooperation. The current evidence is consistent with the possibility that
**predictable benevolence changes the strategy people use**, especially when
exploitation is difficult for the AI counterpart to punish.

## Repository contents

```text
.
├── Paper/
│   ├── Writing_sample_latest.pdf
│   └── ReadME.md
├── Codes/
│   ├── Main_Experiment_GPTcoop_punish_simple_random_seat/
│   ├── Auxiliary_Experiment/
│   └── ReadME.md
└── Screenshots/
```

- [`Paper/Writing_sample_latest.pdf`](./Paper/Writing_sample_latest.pdf) is the
  current working-paper manuscript. Its title page retains the earlier title,
  *Humans versus Machine Mind: Bias and Strategic Adaptation in Human
  Interactions with AI*.
- [`Codes/Main_Experiment_GPTcoop_punish_simple_random_seat/`](./Codes/Main_Experiment_GPTcoop_punish_simple_random_seat/)
  contains the oTree programs used for the main experiment.
- [`Codes/Auxiliary_Experiment/`](./Codes/Auxiliary_Experiment/) contains the
  choice, belief-elicitation, and satisfaction tasks used in the auxiliary
  experiment.
- [`Codes/ReadME.md`](./Codes/ReadME.md) records the historical software
  environment and code notes.
- The checked-in SQLite files contain development or demonstration session
  state, not the complete analysis-ready dataset for the 119 participants.
- The current `.pptx` files under `Screenshots/` are empty placeholders and
  should not be treated as usable experimental documentation.
- The Stata and Python analysis pipeline is not yet presented here as a
  complete, independently reproducible package.

## Technical notes

- The experiment programs target **oTree 5.11.1**.
- The real-time ChatGPT integration used **botex 0.1.0**, which is not the
  current botex release.
- The LLM was presented as an independent "ChatGPT player" rather than as a
  delegate or assistant. Apart from technical instructions needed to read and
  respond to the experimental interface, no additional persona was imposed.
- The main experiment used the official OpenAI API. Credentials are not and
  should never be stored in this repository.
- Model endpoints, default parameters, and API behavior may have changed since
  data collection. Exact behavioral reproduction therefore cannot be assumed
  from the code alone.

## Manuscript status and citation

This is a working paper and has not been presented here as a journal
publication. The manuscript used an AEA Word template for formatting
convenience only; that does not imply submission to or endorsement by an AEA
journal.

Suggested working-paper citation:

> Chen, Jinghao. "Strategic De-socialization: Experimental Evidence on Human
> Interaction with Large Language Models." Working paper.

## Funding and contact

This research was supported by an SRTP provincial undergraduate innovation
research project and supplementary support from the supervisor. For questions,
corrections, or suggestions, please use the contact information on
[Jinghao Chen's personal website](https://jhchen4future.github.io/).
