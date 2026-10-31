# Scalar history criteria for the first loss of full sliding under variable fluid injection

**Unrefereed research candidate, version 0.1.0-candidate, 31 October 2026.** DOI [10.5281/zenodo.23838529](https://doi.org/10.5281/zenodo.23838529) (concept DOI 10.5281/zenodo.23838528). Creator: Anonymous. Plain-English summary: <https://evidencepress.org/releases/fault-sliding-history-criteria/>. Internal AI-assisted review only; not peer-reviewed, independently reproduced or formally verified ([STATUS.md](STATUS.md), [ASSURANCE.md](ASSURANCE.md)).

Start here: [AI_INDEX.md](AI_INDEX.md) (map for agents), [CLAIMS.json](CLAIMS.json) (exact claims and scope), [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md) (review objections and responses), [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) (replay record), [CITATION.cff](CITATION.cff). Text, figures and data CC0-1.0; code MIT ([LICENSES.md](LICENSES.md)).

## What this bundle contains

The paper studies the circular, constant-friction, zero-fracture-energy model of fluid-driven aseismic slip with zero Poisson ratio, and asks when an expanding slip crack first stops slipping forward everywhere as the injection rate is reduced. The main results are:

- **Theorem 1.** For rates that rise and then fall, nonnegative slip rate at the injection point (the centre) is equivalent to nonnegative slip rate throughout the disk, at finite radius, for a point source, a Gaussian source and any positive mixture of Gaussian source widths.
- **Theorems A, B and G.** For smooth or stepped rates with many rises and falls, full sliding holds throughout an interval exactly when the centre history has stayed nonnegative throughout it, under stated startup conditions. The crack radius then exists and grows automatically, and full sliding is always lost first at the centre. Point-source downward jumps end full sliding at once.
- **Quantitative consequences.** An abrupt-drop tolerance of roughly the square root of source width over stage duration; a two-term finite-radius criterion with a rigorous remainder; a closed-form bound on the time after shut-in by which full sliding must have ended; the inner-limit linear-taper threshold and the corollary that no linear taper can halve the rate; and an illustrative dimensional example.

The results concern the first loss of full sliding only. They do not describe the later slip pulse or seismic hazard.

## Files

| File | Purpose |
|---|---|
| `output/fault_locking_manuscript.pdf` | The paper, with proofs in Appendices A--D. |
| `manuscript.md`, `refs.bib`, `header.tex`, `build_documents.sh` | Source, bibliography (every entry copied from its Crossref or DataCite record, with DOI) and build script. |
| `crossref/` | The Crossref and DataCite records from which `refs.bib` was copied (publisher abstracts removed before release). |
| `REVISION_RESPONSE.md` | Point-by-point response to the round-1 review and list of new or rewritten proofs. |
| `numerics/fault_locking_results.png`, `.pdf` | Figure 1. |
| `numerics/extension_results.png`, `.pdf` | Figure 2. |
| `kernel_order_proof.md`, `arbitrary_history_extension.md`, `gaussian_startup_extension.md` | Earlier supporting proof notes; the manuscript supersedes them where they differ (each note says how). |
| `mechanical_audit.md`, `novelty_report.md`, `literature_audit.md`, `extension_novelty_audit.md`, `geomorphology_scout/` | Earlier supporting records of the mechanics check and literature searches. |
| `target*.yaml`, `exploratory_transfer_target.yaml` | Earlier frozen target statements. |

## Reproduce the checks

All calculations are synthetic and dimensionless ($\alpha=q_0=1$); velocities omit the positive factor $4fc_p/(\pi\mu)$. Run every check with one command:

```bash
uv run --python 3.12 --with numpy==2.3.5 --with scipy==1.17.0 --with matplotlib==3.10.8 \
    python3 -I -B /absolute/path/to/run_checks.py
```

`run_checks.py` runs each script below with `python -I -O -B` and exits with a nonzero status if any fails. Every script uses explicit checks that still run under `-O`, writes its JSON next to itself (floats rounded to about ten significant figures in the new scripts), and the new scripts include negative controls that must be detected. The full run takes about three minutes on one core.

| Script | Output | What it checks |
|---|---|---|
| `verify_kernel_order.py` | `kernel_order_checks.json` | Kernel against a 70-digit exact-moment expansion; age order of Lemma 2 on a grid; counterexample to the pairwise radial order. |
| `verify_fault_criterion.py` | `numerics/verification_results.json`, Figure 1 | Independent kernel quadratures; moving-boundary derivative; original taper roots; instantaneous multi-stage counterexamples. |
| `mechanical_audit_checks.py` | `mechanical_audit_checks.json` | Cap traction against a real-space fractional Laplacian; exterior complementarity. |
| `reviewer_checks.py` | `reviewer_checks.json` | Exterior mechanics, inner-limit transfer, arcsine continuation, taper threshold. |
| `exploratory_transfer_checks.py` | `exploratory_transfer_checks.json` | Signs of a discrete triangular-kernel transfer along nondecreasing radius paths. |
| `verify_multipeak_example.py` | `numerics/multipeak_example.json` | A smooth three-peak history for both sources. |
| `constants_and_two_term.py` | `constants_and_two_term.json` | Numerically verified bounds $s_*\le0.6424$, $c_D\le0.4115$ (with an explicit floating-point allowance); the two-term expansion and sharpened tail bound; the constant-rate radius map and its asymptotes. Negative controls: wrong $1/R$ coefficient, too-small remainder constant, asymptotic constant $1/2$. |
| `regime_and_taper_checks.py` | `regime_and_taper_checks.json` | Taper roots for $\Theta$ from 0.01 to 10 and two source widths, with refinement and comparison with the adaptive implementation; two-term predictions and rigorous enclosures; finite-radius taper thresholds and the leading-order formula; drop tolerances at realistic widths; the dimensional example; the persistence-time bound. Negative controls: understated persistence bound, perturbed leading-order coefficient. |
| `history_extension_checks.py` | `history_extension_checks.json` | Two-dip history tuned to a tangential centre zero; stepped Gaussian schedule; point-source upward jump; downward-jump asymptotic; Gaussian mixtures, the annular-source counterexample and its time history. Negative controls: deeper dips, larger steps, pairwise radial order, annular age order. |
| `make_extension_figure.py` | Figure 2 | Draws Figure 2 from the two preceding JSON files after checking that they passed. |

`tools/replay_compare.py` reruns `run_checks.py` in a temporary copy and compares every regenerated JSON output with the retained one (relative tolerance $10^{-7}$; CI uses it). `fault_core.py` is the shared Gauss--Legendre kernel module used by the four new scripts. `arbitrary_history_probe.py` is an earlier exploratory search, not part of the checks and not used in any proof.

Recorded environment: Python 3.12, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8 (`requirements.txt`).

## Rebuild the paper

With pandoc (3.x, with citeproc) and a LaTeX installation providing AMS mathematics, `mathtools`, `microtype`, `xurl` and `fancyhdr`:

```bash
bash build_documents.sh
```

This writes `output/fault_locking_manuscript.pdf` and keeps intermediates in `tmp/pdfs/` (not shipped). Regenerate the figures first with `run_checks.py` if needed.

## Limits

The model assumes zero Poisson ratio, uniform constant friction, zero fracture energy, a homogeneous permeable layer and one-way coupling from pressure to slip. Point-source statements are elastic statements away from the singular centre; the Gaussian-source results are the physically primary ones. The historical criteria use the stated startup conditions; Gaussian histories with decreasing centre pressure before nucleation remain open. Annular sources can violate the centre-first property. The dimensional example uses illustrative parameters, not a calibrated site.

## Release records

| File | Purpose |
|---|---|
| `STATUS.md`, `ASSURANCE.md`, `PROVENANCE.md` | Version and status, what was and was not checked, roles and history |
| `CLAIMS.json`, `RESEARCH_GATES.json` | Machine-readable claims and the dated prior-art scrutiny |
| `REVIEW_SUMMARY.md`, `REVISION_RESPONSE.md`, `FINAL_FIXES.md` | Internal review record (rating-free) |
| `REPLAY_RECEIPT.md`, `ENVIRONMENT.txt`, `.github/workflows/replay.yml` | Replay record, environment, CI |
| `CITATION_AUDIT.md`, `SOURCES.md` | Reference checks and sources |
| `CITATION.cff`, `.zenodo.json`, `LICENSE`, `LICENSE-MIT.txt`, `LICENSES.md`, `PUBLIC_DOMAIN.md`, `SHA256SUMS` | Citation, licences and integrity |
