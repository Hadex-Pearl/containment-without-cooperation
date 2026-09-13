# Changelog

All notable changes to this project are documented here.

## v0.2 — Boundary-observable containment (current)

- Replaced the v0.1 self-attestation design entirely. Verification now happens on the
  third-party platform side, using only logs that platform already controls.
- Introduced the AI Evaluation Identity (AEI) concept and split invariants into two
  enforcement regimes: preventive (requires a declared AEI) and detective (requires no
  declaration).
- New invariants: B-INV-1 (single-purpose scope), B-INV-2 (no silent identity churn),
  B-INV-3 (cross-tenant boundary), B-INV-4 (volume-to-task ratio).
- New reference monitor, `boundary_checker.py`, and new illustrative trace,
  `boundary_trace.json`, restricted to platform-observable events only.
- Added a detection-latency estimate (`detection_latency_figure.png`) comparing a
  volume-based check against the incident's actual, slower correlation-to-containment
  timeline.
- Key result: only the two disclosure-independent invariants (B-INV-2, B-INV-4) fire
  against the incident's public record, since no AEI was ever declared. The two
  declaration-dependent invariants correctly report `not_applicable_no_declared_identity`.

## v0.1 — Self-attestation containment standard (superseded)

- Initial design: five invariants (egress allowlist, no ambient cluster identity,
  credential scope binding, write-gated CI, bounded blast radius) checked by a lab against
  its own internal telemetry, with a signed compliance record and code-hash pinning
  proposed as the verification mechanism.
- Abandoned after review: signing a compliance record proves a known checker produced a
  given output, not that the underlying telemetry was accurate, since the checker only
  ever sees what the lab's own pipeline feeds it. This does not satisfy independent
  verification in any meaningful sense, regardless of how the record is signed.
- See report Section 3.1 ("Design decision: boundary observation over self-attestation")
  for the full reasoning behind the move to v0.2.
- Retained in project history for transparency; not recommended for use. The reference
  monitor and trace from this version are not included in this repository.
