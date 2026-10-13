# Trademark clearance experiment specification

Status: **proposed research; human review pending**. Research date: **2026-10-13 (America/Chicago)**.

## Inputs, authority and baseline

Read `PROJECT_BRIEF.md`, all five `docs/legal/` documents, `GOVERNANCE.md`, `PRINCIPLES.md`, `CHARTER.md`, `ARCHITECTURE.md`, `README.md` and `REPOSITORIES.md` before preparing this experiment. GitHub main base is `ac4ccd92d1ca20536e8752c5d50afaff0c52b9cf` (tree `8152a6558c7fa9809316bdbfba8ef892c64f3f74`); PR #3 is merged by a human. No applicable agent instruction, check script, or CI workflow appears in that base tree; local agent directories are empty. Preserve the charter and historical research. This specification extends the original brief's discovery/verification approach for the user's next research task; it does not adopt policy or change the brand.

Baseline: prior report identified candidates but lacked populated current federal records, registrar metadata for `.com`, and comprehensive marketplace/state coverage. Founder-reported `.dev`/`.ai`/`.io` ownership remains an assertion, not verified title or LLC ownership.

## Research question and falsifiable hypothesis

Question: what evidence raises or reduces the priority for counsel investigation of USEKARMA, USE KARMA, USEKARMA.DEV and KARMA for software/AI engineering, platforms, developer tools and infrastructure services?

Hypothesis: retrieving populated official proceedings/status records and primary marketplace pages will materially improve the candidate risk register over the baseline. A discriminating result is at least one newly verified current official status or a newly observed relevant primary-source use. Failure to obtain them must remain an explicit failed retrieval, never a zero-match claim. Even success cannot establish legal availability.

## Contract and method

- Input scope: four requested word forms plus KARMA-formative and phonetic CARMA leads; all classes initially, then relevance to 9/42 and related channels. Candidate follow-ups must not be described as exhaustive searches.
- Record each finding with evidence ID, URL, retrieval date, source/record date where available, facts, assessment and unresolved questions. Official records outrank aggregator status labels; a docket label is not a merits decision or assignment audit.
- Investigate Illinois state records and scoped other-state/common-law discovery; disclose unsearched jurisdictions. Inspect `.com` homepage, public registry metadata, archive evidence and identity clues without contact or personal-data publication.
- Separate existing source/documented prototypes from actually delivered goods/services and human-confirmed plans. Ask for product/market facts without inventing a launch, customer, intent or first-use date.
- Output: clearance report, risk register and prioritized counsel questions, with this experiment specification and reproducible structural/evidence checks.
- Failure behavior: rate limits, challenge pages, interactive-only interfaces, unavailable records and contradictory statuses remain gaps. No bypass of access controls, paid lookup, bulk state scraping or third-party contact.
- Stop when the bounded primary-source pass and candidate follow-ups yield reviewable evidence or documented endpoint limitations; do not claim a comprehensive professional search.

## Acceptance criteria

| ID | Criterion | Verification |
| --- | --- | --- |
| CLR-01 | All four requested marks assessed individually | Structural check + sequential review |
| CLR-02 | Each candidate status has source/date and verification level | Evidence review; unknown explicitly allowed |
| CLR-03 | Federal/state/common-law and `.com` identity/history covered with gaps | Report review and source manifest |
| CLR-04 | Goods/services and 9/42 relevance distinguished from actual use claims | Product matrix and counsel questions |
| CLR-05 | Risks/questions trace to evidence and unresolved facts | Structural reference check + review |
| CLR-06 | No availability conclusion, legal transaction, brand or charter change | Negative-claim review + changed-path/blob checks |
| CLR-07 | New review PR is open and unmerged | GitHub state and diff verification |

Checks establish structure and tested evidence fields, not legal validity. The agent performs sequential author/source/diff passes; no independent reviewer or counsel opinion is claimed. Exact human approval of a later action remains separate from accepting this research.

## Experiment result and reproducible verification

Hypothesis supported within the bounded scope: official populated queries and 18 candidate status responses improved the earlier evidence, with new technical-market leads and `.com` metadata. This result does not establish trademark availability. The [report](TRADEMARK_CLEARANCE_REPORT.md), [risks](TRADEMARK_CLEARANCE_RISKS.md), [questions](TRADEMARK_COUNSEL_QUESTIONS.md) and [redacted manifest](evidence/trademark-clearance-2026-10-13.json) record findings and failures. Founder product clarification is attributed as E-P01 rather than independently verified commerce.

Run `python3 docs/legal/check_trademark_clearance.py` from the repository. It validates evidence IDs/dates/status provenance, bounded pagination uniqueness/completeness, a positive search control, local links, references and each original base file's Git blob hash. It uses no network and makes no legal assessment. A later intentional base-file change requires a separately scoped verification baseline, not suppression of the mismatch.

This run passed; GitHub final diff and PR-state verification are recorded in the PR description. CLR-01–06 are covered within the explicitly stated scope; CLR-03 does not imply completed state or nationwide common-law searches. CLR-07 is checked after opening the PR. External freshness and legal interpretation remain human/counsel review requirements.
