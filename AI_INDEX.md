# Agent navigation

## Identity

- Release slug: `fault-sliding-history-criteria`. Version `0.1.0-candidate`, tag `v0.1.0-candidate`. DOI 10.5281/zenodo.23838529; concept DOI 10.5281/zenodo.23838528.
- Repository: https://github.com/ipitchford/fault-sliding-history-criteria. Release page: https://evidencepress.org/releases/fault-sliding-history-criteria/
- Scholarly creator: Anonymous. Status: unrefereed candidate ([STATUS.md](STATUS.md)).
- Manuscript: [PDF](output/fault_locking_manuscript.pdf) (39 pages) and its Markdown source [manuscript.md](manuscript.md) with [refs.bib](refs.bib), [header.tex](header.tex), [build_documents.sh](build_documents.sh).
- Machine-readable claims: [CLAIMS.json](CLAIMS.json). Human overview: [README.md](README.md).
- Assurance limits: [ASSURANCE.md](ASSURANCE.md). Review record: [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md), [FINAL_FIXES.md](FINAL_FIXES.md).
- Prior art and sources: [RESEARCH_GATES.json](RESEARCH_GATES.json), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md), [literature_audit.md](literature_audit.md), [novelty_report.md](novelty_report.md), [extension_novelty_audit.md](extension_novelty_audit.md). Provenance: [PROVENANCE.md](PROVENANCE.md).
- Citation: [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json). Licences: [LICENSES.md](LICENSES.md).

## Scientific map

Object: the circular, constant-friction, zero-fracture-energy, zero-Poisson-ratio model of fluid-driven aseismic slip (Sáez, Lecampion, Bhattacharya and Viesca 2022) with a point or Gaussian pressure source and injection rate q(t). Question: when is "full sliding" (nonnegative slip rate everywhere in the expanding crack) first lost? Answer: the centre margin C(t), the slip rate at the injection point, decides it.

- Section 2: model, stress-injection parameter Theta, radius equation (8), definitions (full sliding, centre margin, threshold contact, trial branch).
- Lemma 2 (Section 3.2, Appendix A.4): centre-relative age order of the Dawson-function kernel K_R(r,u)/K_R(0,u).
- Theorem 1 and Corollary 3.1 (Section 3.3): instantaneous criterion for rise-then-fall rates; Proposition 3.3: Gaussian mixtures.
- Theorems A, B, G and Proposition 4.1 (Section 4; Appendices B, C): historical criteria for piecewise-C^1 and stepped rates under startup conditions; radius existence; centre-first loss.
- Section 5: abrupt-drop tolerance (26), Table 1; point-source downward jump (27).
- Section 6: exterior friction inequality; Proposition 6.1 uniqueness in a variational class (Gaussian source).
- Section 7: Theorem 3 (inner limit, first-passage subordination), Propositions 7.2 and 7.3 (finite-radius bounds, two-term criterion), Appendix D (constants s*, c_D).
- Section 8: arcsine continuation, Proposition 8.2 (shut-in deadline), Corollary 8.4 (point source: no linear taper halves the rate), formula (54) (approximation), dimensional example (illustrative).
- Section 9: numerical verification and counterexamples (pairwise radial order false; instantaneous test insufficient for general histories; annular source).
- Section 10: relation to previous work, scope and limitations, open problems.

## Evidence and replay

- Runner: [run_checks.py](run_checks.py) (each script with `-I -O -B`; nonzero exit on failure). Comparer: [tools/replay_compare.py](tools/replay_compare.py) (temporary copy; regenerated JSON vs retained). Environment: [requirements.txt](requirements.txt), [ENVIRONMENT.txt](ENVIRONMENT.txt). CI: [.github/workflows/replay.yml](.github/workflows/replay.yml). Record: [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md). Integrity: [SHA256SUMS](SHA256SUMS).
- Check scripts and outputs: [verify_kernel_order.py](verify_kernel_order.py) -> [kernel_order_checks.json](kernel_order_checks.json); [verify_fault_criterion.py](verify_fault_criterion.py) -> [numerics/verification_results.json](numerics/verification_results.json) and Figure 1; [mechanical_audit_checks.py](mechanical_audit_checks.py) -> [mechanical_audit_checks.json](mechanical_audit_checks.json); [reviewer_checks.py](reviewer_checks.py) -> [reviewer_checks.json](reviewer_checks.json); [exploratory_transfer_checks.py](exploratory_transfer_checks.py) -> [exploratory_transfer_checks.json](exploratory_transfer_checks.json); [verify_multipeak_example.py](verify_multipeak_example.py) -> [numerics/multipeak_example.json](numerics/multipeak_example.json); [constants_and_two_term.py](constants_and_two_term.py) -> [constants_and_two_term.json](constants_and_two_term.json); [regime_and_taper_checks.py](regime_and_taper_checks.py) -> [regime_and_taper_checks.json](regime_and_taper_checks.json); [history_extension_checks.py](history_extension_checks.py) -> [history_extension_checks.json](history_extension_checks.json); [make_extension_figure.py](make_extension_figure.py) -> Figure 2. Shared module: [fault_core.py](fault_core.py).
- Semantic negative controls are inside the last three check scripts (wrong 1/R coefficient, too-small remainder constant, constant 1/2 for s*, understated persistence bound, perturbed taper coefficient, deeper dips, larger steps, pairwise radial order, annular age order); each must be detected.
- Development notes (superseded by the manuscript where they differ): [kernel_order_proof.md](kernel_order_proof.md), [arbitrary_history_extension.md](arbitrary_history_extension.md), [gaussian_startup_extension.md](gaussian_startup_extension.md), [mechanical_audit.md](mechanical_audit.md), frozen targets `target*.yaml`. [arbitrary_history_probe.py](arbitrary_history_probe.py) is exploratory and not used in any proof.

## Trust boundary

All review was internal and AI-assisted. There was no peer review, no independent reproduction and no formal verification. Numerical checks test formulas, signs and examples on grids; they do not prove the theorems. The constants s* and c_D are numerically verified, not interval-certified; taper thresholds are finite-window estimates; formula (54) is an approximation. Priority holds only within bounded searches; the Volterra positivity mechanism is classical. Results concern the first loss of full sliding in a narrow model class, not the later slip pulse or seismic hazard.
