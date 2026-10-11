# UseKarma Ecosystem Charter

Status: **proposed initial charter; not adopted**. Human review and explicit adoption are required.

## Purpose and human ownership

The proposed mission is to make agent-assisted systems understandable, corrigible, and governable through explicit intent, falsifiable research, reproducible evidence, bounded implementation, and learning from outcomes.

Humans own purpose, values, acceptable tradeoffs, program priorities, and consequential decisions. Domain subjects retain their own consent and privacy rights. Organization ownership is not permission to access an individual's records. An agent's confidence, successful action, or favorable safety finding cannot create authorization.

## Architectural commitments proposed for adoption

Separate the ownership of intent, experimental knowledge, governance, implementation, and execution. A shared vocabulary should make handoffs inspectable without concentrating privilege or private information in a central agent.

| System | Architectural ownership |
| --- | --- |
| Faraday | Research questions, hypotheses, experiments, evidence lineage, interpretations, and proposed research direction |
| Karma | Evidence governance and decision control: evaluate what evidence supports, preserve blockers and uncertainty, and present bounded continuation findings for human decisions |
| Adage | Infrastructure control architecture: desired state, reusable implementation, discovery, planning, and controlled execution boundaries |
| Adage-Fabric | Event-processing fabric: ingestion, projection, analysis, and observable lineage within defined contracts |
| Aegis | Independent consent-first care-coordination domain and its per-person access boundaries |
| Prudence | Independent financial/business scenario domain, assumptions, alternatives, and decision briefs |
| AWS implementation repositories | Desired configuration, infrastructure implementation and controlled execution paths, and runtime code according to their separate ownership contracts |
| Agent business solution template | Reusable engineering methodology, specifications, quality gates, and readiness review patterns |

These assignments describe intended ownership. [Repositories](REPOSITORIES.md) bounds what has actually been inspected or reported as demonstrated. Karma's governance role does not mean an implemented general-purpose policy engine; Adage's architecture is not itself an executor.

## Research and governance decision boundary

Faraday owns the formulation and assessment of research questions, hypotheses, experimental priorities and proposed next investigations. Karma evaluates evidence, dependencies, permissions and work-continuation conditions within its scoped governance contracts; it reports findings and blockers rather than selecting research truth or authorizing execution. Neither repository independently resolves a dispute over program priorities, acceptance of risk, or consequential action: an authorized human decides. These assignments are proposed responsibilities, not a claim of deployed cross-repository enforcement.

## Scope and non-authority

This charter proposes ecosystem-wide architectural guidance. It cannot authorize execution, expand IAM or data access, supersede consent, relax security controls, or override a target repository's instructions and approval gates. An adopted charter would guide design review; repository changes and operational approvals remain separately scoped.

No merge, queue status, issue label, checksum, simulated approval, or charter statement grants agent dispatch, deployment, financial action, clinical action, device provisioning, or destructive authority. On conflicting instructions or unclear authority, preserve the stricter applicable boundary and seek human resolution. Do not silently migrate contracts or ownership.

## Learning and continuity

Record observations separately from measurements, derived facts, interpretations, hypotheses, decisions, and authorizations. Preserve failed runs, counterexamples, superseded conclusions, and the scope of supporting evidence. Revisions should explain what changed and why rather than make the historical record fit a new theory.

Long-term continuity comes from reviewed Git history and explicit amendment records. This proposal does not promise universal source authentication, automated invalidation, secure distributed consent, or autonomous coordination. Those remain separately reviewed future capabilities.

## Adoption

No adoption has occurred in this proposal. The authorized human must review the final commit, resolve or explicitly defer outstanding decisions, and record the accepted scope and effective version through the [governance process](GOVERNANCE.md). Publication or repository creation alone is not adoption.

**STOP_FOR_HUMAN.**
