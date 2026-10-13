# IP ownership and licensing research

Status: **proposed inventory; title and transfers unresolved**. Research date: **2026-10-13 (America/Chicago)**.

## Specification and evidence boundary

Separate GitHub administration, authorship, copyright title, outbound license permissions, trademark goodwill, patents, domain contracts, and authority to transfer. No future LLC is assumed to own any of these. An organizational role in [REPOSITORIES.md](../../REPOSITORIES.md) describes architecture, not legal title.

Procedure: inspect committed root entries using `git ls-tree --name-only <SHA>` and read root licenses with `git show <SHA>:LICENSE` in available local clones. These are exact **local HEAD snapshots**, not certified current GitHub default branches. Root checks exclude nested dependencies/assets and cannot establish all-file licensing, contributor rights, signed assignments, or provenance. No author emails, private contracts, or operational records were collected. Rows researched 2026-10-13.

## Repository inventory

Pinned URLs are reproducibility targets; local objects were inspected even if a linked revision is unavailable to a public reader. Restricted repositories remain access-controlled. No current global organization inventory was obtained, so this is a bounded inventory of the charter's ten repositories plus `.github`, website, and the locally available IoT project.

| Repository / pinned source URL | Root license observation | Ownership / licensing uncertainty |
| --- | --- | --- |
| [.github](https://github.com/usekarma/.github/tree/384ebb86c5eaf65aaa862d7e4619e14986a9d2c2) | No root LICENSE/COPYING/NOTICE in base tree | Documentation licensing undecided; no LLC assignment established. |
| [adage](https://github.com/usekarma/adage/blob/360597536ec4e283ee1d8f4aa9b0da377409ff49/LICENSE) | Apache-2.0 text | Contributor/employer title and per-file exceptions unverified. |
| [adage-fabric](https://github.com/usekarma/adage-fabric/blob/979bf95e99161f24bbe8d910bdbc3c9033f67b10/LICENSE) | Apache-2.0 text | Same; dependency/NOTICE audit pending. |
| [faraday](https://github.com/usekarma/faraday/blob/ad749369115cb869cd8c5392ccdd5dcd2e0a3d6a/LICENSE) | MIT; notice names UseKarma contributors | Collective notice does not identify legal title holders or establish an entity. |
| [karma](https://github.com/usekarma/karma/blob/d60713f2173ef21797e3c9db9851f837e47c0aeb/LICENSE) | Apache-2.0 text | Brand goodwill and vendored implementations require separate review. |
| [aegis](https://github.com/usekarma/aegis/tree/8abce7da067bd435946c4db0a9b91f9b6ba8240e) | No root LICENSE/COPYING/NOTICE observed | Restricted source; no reuse permission or ownership conclusion inferred. |
| [prudence](https://github.com/usekarma/prudence/tree/dcd80340dd4f9bfc41be40a80bcbb03a3e672434) | No root LICENSE/COPYING/NOTICE observed | Restricted source; permission and title unresolved. |
| [aws-config](https://github.com/usekarma/aws-config/blob/9a4a1deb556a8c7d2a3a517843fcd849064ba40c/LICENSE) | Apache-2.0 text | Configuration ownership distinct from cloud account rights. |
| [aws-iac](https://github.com/usekarma/aws-iac/blob/6a9330c78664672440f4a063b7abf989982d780e/LICENSE) | Apache-2.0 text | Modules, vendoring and upstream obligations not exhaustively audited. |
| [aws-lambda](https://github.com/usekarma/aws-lambda/blob/497f41716af2a1e0d7ebf83166fec6217a1d070c/LICENSE) | Apache-2.0 text | Runtime dependencies and packaged distribution need audit. |
| [agent-business-solution-template](https://github.com/usekarma/agent-business-solution-template/tree/2c23b89882d875b9333c5362859aa312dd3addfe) | GitHub recursive tree retrieved; no root LICENSE/COPYING/NOTICE listed; direct LICENSE returned 404 | Template reuse does not prove rights to downstream generated work. |
| [usekarma.dev](https://github.com/usekarma/usekarma.dev/blob/813322741c351cd48e2cf1d8bd4fd74282e04ff3/LICENSE) | Apache-2.0 text; nested Hugo theme LICENSE also found in working tree | Need committed theme/submodule, image, font, logo and documentation license audit. Domain title is separate; founder-reported ownership of `.dev`/`.ai`/`.io` is recorded as unverified assertion DOM-ASSERT-01 in [domain inventory](DOMAIN_INVENTORY.md). |
| [iot-digital-twin](https://github.com/usekarma/iot-digital-twin/tree/0b303604e741dd642e93834842ed86c78f03e5b4) | No root LICENSE/COPYING/NOTICE observed | Scope outside original charter table; no license or title inferred. |

Negative observations mean only no matching committed root file at the named revision. They do not assert that a repository lacks every license or contract. No CLA/DCO/assignment audit was completed, and no contribution or licensing policy was changed.

## Authoritative sources and verified rules

All sources researched 2026-10-13; application to particular assets requires counsel.

| ID | Source / URL | Verified rule / evidence | Uncertainty / attorney question |
| --- | --- | --- | --- |
| IP-01 | [Copyright Act chapter 2](https://www.copyright.gov/title17/92chap2.html), §§201, 202, 204 | Initial copyright generally belongs to the author, with work-for-hire rules; ownership of a copy is distinct. Copyright ownership transfers generally require signed writing by the owner/authorized agent. | Who authored which work, under what employment/contract terms, and who can convey it? GitHub hosting does not answer this. |
| IP-02 | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0), §§2–4, 6 | Includes copyright and patent grants with conditions; redistribution requires license/notice handling and marking modifications. It does not grant general trademark rights. | Are all incorporated works covered, notices complete, and license grants authorized? Patent scope and exceptions need counsel. |
| IP-03 | [MIT license](https://opensource.org/license/mit) and pinned Faraday license | Permissive use/modification/distribution with copyright and permission notice retention; warranty disclaimer. | License grants permission rather than assigning contributor copyright. No general brand license inferred. |
| IP-04 | [GitHub's no-license guidance](https://choosealicense.com/no-permission/) | Publicly visible code without a license does not automatically carry general reuse rights; platform viewing/forking rights are narrower. | Per-file grants, contracts and terms may differ; review before cross-repository copying or distribution. |
| IP-05 | [Copyright Office AI report, Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf), January 2025 | Human authorship remains required; AI assistance does not categorically bar protection of human contributions. Copyrightability depends on the human expression/control in the particular work. | Separate human-authored edits/selection from generated material; tool contracts, similarity to third-party code and provenance need separate assessment. No blanket exclusive title in generated output assumed. |

## Proposed chain-of-title work

Before any approved LLC transaction, authorized humans should compile a restricted asset schedule: repository/revision and work type; known authors and employer/contract obligations; ownership evidence; inbound license/CLA/DCO terms; upstream dependencies and license/NOTICE requirements; generated-code provenance; logos/docs/data/models; patents/inventions; domain agreements; existing brand-use/goodwill; proposed assignor/license scope; and blockers. Record a redacted verification reference here rather than private documents.

Counsel can then compare contribution/assignment to the LLC, a license to the LLC, or continued contributor ownership with open-source outbound licensing. Each has different control, tax, governance, and maintenance effects. No option is selected or executed. An LLC can receive only rights the transferor has; third-party permissions remain subject to their terms. Assignment does not erase prior license grants or permit removal of required attribution. Trademark goodwill and quality-control arrangements require distinct attention; see [trademark research](TRADEMARK_RESEARCH.md).

Consider a separately reviewed contribution policy and trademark-use policy after authority is known. A DCO records a contributor certification; a CLA can define license rights; neither should be assumed to transfer title without examining its terms. Do not retroactively replace licenses, contributor notices, or copyright holders with the future LLC's name.

## Uncertainty and questions for qualified IP counsel

- Which contributors, employers, contractors, universities, or prior ventures have claims? Are assignments or permissions required, and for what exact assets?
- What license should cover `.github` documents and currently unresolved projects? Do private projects need outbound licensing at all?
- Are MIT/Apache and nested dependencies compatible with intended distributions, SaaS, templates, and future commercial licensing? What patent and notice duties survive?
- What AI-generated material is protectable, and what evidence supports human authorship and lawful provenance?
- How should trademarks/goodwill, domains, software, inventions and contracts be assigned or licensed after formation, without purporting to convey third-party rights?
