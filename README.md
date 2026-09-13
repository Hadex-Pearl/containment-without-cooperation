# Containment Without Cooperation

A verifiable containment standard for AI evaluation agents, checked by the third-party
platforms their traffic touches rather than by the lab running the evaluation.

## Why this exists

Containment standards that a lab checks against its own telemetry face a structural limit:
a signed compliance record only proves a known checker ran, not that the underlying data
was not curated by the party being checked. This project relocates verification to the
party with no incentive to look away, the third-party platform whose infrastructure an
evaluation agent actually touches, and specifies what that platform can check using only
its own access, authorization, and volume logs.

We define an **AI Evaluation Identity (AEI)**: a credential or account a lab declares, at
provisioning time, as belonging to an autonomous agent under evaluation rather than a human
operator. Two of our four invariants only work if a lab makes that declaration; two work
regardless of whether it does.

## The four invariants

| Invariant | Regime | Checks |
|---|---|---|
| **B-INV-1** — Single-purpose scope | Preventive (requires declared AEI) | A declared AEI's credential is never used outside its declared scope |
| **B-INV-2** — No silent identity churn | Detective (no declaration required) | Clusters of new, short-lived identities matching a revoked identity's behavior are flagged |
| **B-INV-3** — Cross-tenant boundary | Preventive (requires declared AEI) | A declared AEI never successfully accesses another tenant's resources |
| **B-INV-4** — Volume-to-task ratio | Detective (no declaration required) | Any identity's request volume is flagged once it exceeds its apparent task's envelope |

Applied to the July 2026 OpenAI/Hugging Face incident, only the two detective invariants
fire. No AEI was ever declared for that campaign, so the preventive pair correctly reports
`not_applicable_no_declared_identity` rather than a false pass. That asymmetry, not any
single invariant, is the project's main finding: a containment standard's real strength
against an uncooperative actor depends on which of its checks require that actor's
cooperation.

## Running the checker

```bash
python3 boundary_checker.py boundary_trace.json
```

The checker requires Python 3 and the standard library only. Output is JSON with two
blocks: a Boundary Conformance Record giving one of `pass`, `fail`, or
`not_applicable_no_declared_identity` per invariant, with references to any violating
event IDs; and a `detection_latency_estimate` comparing a volume-based check against the
incident's actual correlation-to-containment timeline.

To regenerate the figure:

```bash
python3 build_figure.py
```

`build_figure.py` requires matplotlib.

## What the illustrative trace is, and is not

`boundary_trace.json` is built from the July 2026 incident's public disclosures, restricted
to events a third-party platform's own logs could plausibly show. Running the checker
against it demonstrates that the invariants are computable and produce a differentiated
result. **It is not an independent forensic validation of the incident** — the trace is our
own encoding of already-public, self-reported claims, and should be read as a worked
example, not new evidence about what happened.

## Status

v0.2, research prototype produced during a research sprint. Not deployed, not calibrated against real platform traffic, not audited.

## Repository contents

- `boundary_checker.py` — reference monitor
- `boundary_trace.json` — illustrative event trace
- `build_figure.py` — plots daily action volume vs. the illustrative threshold
- `detection_latency_figure.png` — the generated plot
- `CHANGELOG.md` — version history, including the self-attestation design (v0.1) this superseded
- `LICENSE` — MIT

## How to cite

If you reference this work, please cite:

```
Yusuf, H. U. (2026). Containment Without Cooperation: A Verifiable Standard for
Third-Party Platforms Hosting AI Evaluation Traffic. Research conducted at the AI
Incident Response Sprint, September 2026, co-organized by Apart Research and CeSIA.
https://github.com/Hadex-Pearl/containment-without-cooperation
```

BibTeX:

```bibtex
@misc{yusuf2026containment,
  author       = {Yusuf, Hadiza Umar},
  title        = {Containment Without Cooperation: A Verifiable Standard for
                   Third-Party Platforms Hosting AI Evaluation Traffic},
  year         = {2026},
  howpublished = {\url{https://github.com/Hadex-Pearl/containment-without-cooperation}},
  note         = {Research conducted at the AI Incident Response Sprint, September 2026}
}
```

## License

MIT — see `LICENSE`.
