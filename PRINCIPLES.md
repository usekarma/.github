# Architectural Principles

Status: **proposed initial charter; not adopted**. Human review and explicit adoption are required.

The principles below are proposed charter commitments, drawing on documented repository practices. They are requirements for design review, not claims of universal technical enforcement.

## Human purpose and bounded agency

Humans determine objectives, values and consequential choices. Agents may prepare scoped research, code, tests, plans and evidence within task authorization and repository controls. Read-only access still requires permission to the source; public visibility or an architectural role does not establish access to private systems. Proposals, test results and continuation findings remain distinct from approval.

## Evidence and explicit uncertainty

Separate observation, measurement, derived fact, interpretation, hypothesis, counterexample, decision and authorization. Record provenance, exact revision/run/target, procedure, assumptions, freshness and limitations. Unknown, conflicting, missing and negative evidence remain visible. Do not convert missing evidence into success or zero. Correlation, predictability, entropy and temporal sequence do not alone establish causality, care, alignment or value.

## Falsifiable research

Define terms operationally when possible. State what would weaken a claim, plausible alternatives, the smallest discriminating experiment, expected evidence, stopping criteria and failure modes before implementation. Explain which decision changes with the answer. Source inspection and synthetic conformance do not substitute for live experiments or independent replication.

## Deterministic quality gates and reproducibility

Use behavior contracts, acceptance/test traceability, negative cases, pinned tools and artifacts, and reproducible procedures where appropriate. Record actual commands, environments, results and unavailable checks. Keep deterministic local checks separate from changing external services such as vulnerability databases. Passing gates establishes only their tested scope; source files and workflow definitions do not prove branch protection, operational safety or production readiness. Verifier and skeptical review must be distinguishable from builder confidence; sequential passes do not imply independent reviewers.

## Dependency-aware invalidation

Record a conclusion's evidence, assumptions, source revisions, scope and freshness dependencies, and an approval's exact artifact, operation, target, issuer, scope, expiry and revocation conditions. Before reuse, check those dependencies under the relevant repository contract.

| Change | Required interpretation |
| --- | --- |
| Supporting source or apparatus revision changes | Reassess applicability; retain old results as historical. Revision change alone does not falsify a claim. |
| Evidence becomes unavailable, contradictory or stale | Mark dependent conclusions insufficient, contested or pending review as justified; do not invent an answer. |
| Assumption changes | Recompute or re-evaluate the scoped conclusion; keep the previous assumptions and result. |
| Artifact, target or approved operation changes | Prior approval does not cover the changed operation; stop and obtain a newly scoped decision. |
| Consent expires or is withdrawn | Deny subsequent reads/sharing under that grant. Record minimal permitted revocation metadata; do not treat withdrawal as evidence that a past observation was false. |

Historical truth, current applicability, consent to use/disclose, and execution authorization are different dimensions. Retaining history is subject to lawful privacy, retention and deletion obligations; do not keep sensitive plaintext merely to preserve lineage. Previously disclosed information cannot be recalled by changing a flag.

Existing pieces include Faraday's freshness rules, artifact binding and Aegis's synthetic current-grant checks. An ecosystem-wide dependency graph or automated propagation is a **future proposal**, not an established capability.

## Consent, privacy and minimum necessity

Require explicit, scoped, revocable sharing permission and fresh checks at each applicable boundary. A family relationship, ownership of infrastructure or previous permission does not grant access. Keep financial and care data separate; default to synthetic fixtures for demonstrations. Review even workflow metadata, aliases and hashes for disclosure risks. Never publish secrets, private domain records, raw plans or sensitive logs in this public repository.

## Institutional knowledge continuity

Maintain durable, version-controlled, reviewable institutional knowledge independently of any particular model, agent session, tool provider or runtime. Link claims to their sources, decisions, revisions and limitations so another authorized contributor can reconstruct why a direction was chosen. Agents may propose corrections and amendments but must not silently redefine the organization's purpose, governing principles, or authority boundaries. Preserve historical rationale subject to privacy, consent, retention and deletion obligations; continuity is not permission to retain or disclose restricted information.

## Learn without rewriting history

Preserve failed attempts and limitations. Add linked corrections and superseding evidence with reasons. Learn from measured outcomes and human corrections without treating them as automatic approval or unbiased labels. New policies and broadened claims require human review; favorable narratives are not verification.
