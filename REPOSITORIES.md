# Repository Responsibilities and Evidence

Status: **proposed initial charter; not adopted**. Human review and explicit adoption are required.

## Assessment scope

Reviewed on October 11, 2026. The table pins the ten requested GitHub `main` revisions; README blobs were re-fetched at those commits and matched the reviewed content. Related contracts and authority documents were also inspected. This is source/document inspection, not a new execution of repository tests or a live deployment audit. Reported demonstrations remain attributed reports, not independent replication.

The role assignments are proposed charter ownership. Existing source and contracts support parts of them, with the following limits. No private domain records were accessed or copied. Only architectural descriptions are summarized for this public proposal.

| Repository and pinned source | Responsibility | Inspected/documented capability | Limits |
| --- | --- | --- | --- |
| [adage](https://github.com/usekarma/adage/blob/3033eff9bd8ae42664ef16d4e3558c806f3cc0e0/README.md) (`3033eff9bd8a`) | Infrastructure control architecture | Configuration/SSM/Terraform model and architectural guides; README also describes evolving agent workflow. | No complete cost reconciliation proof; older PR-status prose needs refresh against implementation sources. |
| [adage-fabric](https://github.com/usekarma/adage-fabric/blob/c0a2349a7d36de4dccbd1dbff9fba58d6b07bd92/README.md) (`c0a2349a7d36`) | Event-processing fabric | Compose services, raw → parsed → facts → views SQL, fixtures, snapshot/test tooling. | Source and documented commands do not establish current live transport, lossless decision evidence, or general production readiness. |
| [faraday](https://github.com/usekarma/faraday/blob/131de8b97dd75576eab051b4a4b4a3819944f244/README.md) (`131de8b97dd7`) | Research and experimental knowledge | Typed registries, hypotheses/experiments, evidence records, freshness workflow and deterministic validation commands. | Research direction and work-package proposals do not authorize downstream execution; snapshots are revision-scoped. |
| [karma](https://github.com/usekarma/karma/blob/d4438bd0fddb472409303a1d00fd61d756b80f7d/README.md) (`d4438bd0fddb`) | Governance and decision control | Normalizer/SQL/contracts and bounded offline steward coordination; governance role is documented in Faraday registry. | Graph handlers include mocks/TODOs; prediction/action paths remain placeholders. No verified general executor or deployed policy engine. |
| [aegis](https://github.com/usekarma/aegis/blob/8abce7da067bd435946c4db0a9b91f9b6ba8240e/README.md) (`8abce7da067b`) | Independent consent-first care domain | Offline synthetic care briefs and current-grant consent/withdrawal model; documentation reports bounded negative checks. | No real clinical facts, secure distributed consent service, medical-record connector, scheduling or action executor. Restricted repository. |
| [prudence](https://github.com/usekarma/prudence/blob/dcd80340dd4f9bfc41be40a80bcbb03a3e672434/README.md) (`dcd80340dd4f`) | Independent financial/business domain | Offline deterministic synthetic cash-flow/runway and compensation scenarios with assumptions and human review records. | No real account data, tax/legal validation, financial connector or executor; scenario arithmetic is not a real-world forecast. Restricted repository. |
| [aws-config](https://github.com/usekarma/aws-config/blob/76d9554ffda4ec0f39bb0c2ec0ef1de54bbc96b6/README.md) (`76d9554ffda4`) | Desired state and environment bindings | Schemas, validation, configuration publication tools, preflight/guards and Lambda declarations. | SSM publishing is consequential; committed configuration is not approval. Unresolved artifact/principal inputs remain blocked. |
| [aws-iac](https://github.com/usekarma/aws-iac/blob/9b3797dee7ed7bfdad63e9baf4407c6daec61863/README.md) (`9b3797dee7ed`) | Infrastructure implementation and controlled execution paths | Terraform/Terragrunt modules, validation/planning, preflight, evidence/postflight and human-only saved-plan paths are documented. | Some component directories are documentation-only or blocked prototypes. Local/mock gates do not establish live readiness; agents cannot self-authorize execution. |
| [aws-lambda](https://github.com/usekarma/aws-lambda/blob/497f41716af2a1e0d7ebf83166fec6217a1d070c/README.md) (`497f41716af2`) | Application runtimes, tests and packaging | IoT ingestion validation, injectable adapters, conditional sequence writes, tests and reproducible ZIP packaging source. | README states no live AWS integration; identity depends on trusted infrastructure injection. No certificate, history, liveness scheduling or TwinMaker integration. |
| [agent-business-solution-template](https://github.com/usekarma/agent-business-solution-template/blob/2c23b89882d875b9333c5362859aa312dd3addfe/README.md) (`2c23b89882d8`) | Reusable engineering methodology | Executable specifications, behavioral checks, pinned tools/CI actions and readiness gates. | Starter intentionally fails production readiness. Workflow presence does not establish branch protection or a release decision. |

## Contract and authority sources

- [faraday: AGENTS.md](https://github.com/usekarma/faraday/blob/131de8b97dd75576eab051b4a4b4a3819944f244/AGENTS.md).
- [faraday: registry/ecosystem.json](https://github.com/usekarma/faraday/blob/131de8b97dd75576eab051b4a4b4a3819944f244/registry/ecosystem.json).
- [karma: docs/faraday-work-intake.md](https://github.com/usekarma/karma/blob/d4438bd0fddb472409303a1d00fd61d756b80f7d/docs/faraday-work-intake.md).
- [karma: coordination/README.md](https://github.com/usekarma/karma/blob/d4438bd0fddb472409303a1d00fd61d756b80f7d/coordination/README.md).
- [aws-iac: docs/lambda-artifact-contract.md](https://github.com/usekarma/aws-iac/blob/9b3797dee7ed7bfdad63e9baf4407c6daec61863/docs/lambda-artifact-contract.md).
- [agent-business-solution-template: AGENTS.md](https://github.com/usekarma/agent-business-solution-template/blob/2c23b89882d875b9333c5362859aa312dd3addfe/AGENTS.md).
- [prudence: specs/karma-work.md](https://github.com/usekarma/prudence/blob/dcd80340dd4f9bfc41be40a80bcbb03a3e672434/specs/karma-work.md) — restricted source; access is not granted by this link.
- [aegis: docs/governance-proof.md](https://github.com/usekarma/aegis/blob/8abce7da067bd435946c4db0a9b91f9b6ba8240e/docs/governance-proof.md) — restricted source; access is not granted by this link.

## Established practices versus proposed capabilities

Documented existing practices include repository-local human approval boundaries, separation of AWS ownership, source-linked research records, synthetic-only steward metadata, and deterministic verification procedures. They are not uniformly enforced across every ecosystem path.

The steward governance-proof documentation reports an offline synthetic cross-repository demonstration with stale/revoked input rejection and tested privacy boundaries. Fixture identities and reviewer registries are not authenticated real-world people; in-memory revocation is not durable distributed consent. The demo preserves an externally supplied active slot rather than querying the actual Faraday registry. No autonomous dispatch is demonstrated.

The local Faraday/Fabric/Karma work reviewed earlier in this session also contained test-only offline evidence handoff. It is not established as a GitHub `main` capability in this snapshot: the Fabric `offline_evidence/README.md` lookup returned not-found. That difference is a source-applicability limitation, not proof the work never existed. This charter does not publish local uncommitted receipts.

Automatic cross-repository invalidation, authenticated approval/consent services, live metadata sharing, production evidence handoff, and autonomous orchestration remain future proposals. Private steward prototypes are independent domains, not modules that central governance can inspect without permission.

## Architectural ambiguities and freshness

Adage and Karma README text describes infrastructure PR safeguards as under review, while the inspected AWS default-branch documentation describes implemented gates and contracts. Preserve the discrepancy rather than infer current maturity from the older summaries. This review did not certify each gate or update those repositories.

Karma combines event-intelligence source with a governance role and a limited steward contract. The division between research-program choices in Faraday and continuation findings in Karma needs explicit human confirmation; both remain subordinate to human authority. Event processing in Karma and Fabric overlaps; adapters and interface ownership need separately scoped review rather than an assumed consolidation.

Neither the proposed intake lifecycle nor synthetic metadata snapshots establish a canonical authenticated active-task service. Contract harmonization, dependency-invalidation semantics, and operational evidence collection are unresolved. Refresh pinned sources before making new current-capability claims; do not silently rewrite this historical assessment.
