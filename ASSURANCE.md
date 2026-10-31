# Assurance boundary

## What was done

1. **Written proofs** in the manuscript ([output/fault_locking_manuscript.pdf](output/fault_locking_manuscript.pdf); source [manuscript.md](manuscript.md)), with the historical criteria proved in Appendices B and C, the kernel properties in Appendix A and the constants in Appendix D.
2. **Numerical verification.** Ten scripts ([README.md](README.md) table) check the kernel against a 70-digit exact-moment expansion, the age order of Lemma 2 on a grid, two independent kernel implementations (adaptive quadrature and composite Gauss-Legendre), the moving-boundary derivative, the exterior mechanics, the constants and two-term expansion, the taper thresholds, the near-threshold and stepped histories and the counterexamples to stronger statements. Every script uses explicit checks that still run under `python -O`.
3. **Semantic negative controls** inside the scripts must be detected: a wrong 1/R coefficient, a too-small remainder constant, the asymptotic constant 1/2 in place of s*, an understated persistence bound, a perturbed leading-order coefficient, deeper dips, larger steps, the false pairwise radial order and the annular age order.
4. **Internal AI-assisted review.** Round 1: an editor, a methodology, a domain, a perspective and a devil's-advocate reviewer, an outside-model adversarial correctness review, and a clean replay of every original script from a fresh extraction. One revision round with six extensions. Verification: a re-review of every change and two targeted proof audits; the second found no fatal or major defect and its six minor items were corrected by the editor ([FINAL_FIXES.md](FINAL_FIXES.md)). A rating-free summary is in [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md).
5. **Replay.** From a fresh extraction of the frozen archive, `run_checks.py` was rerun (each script with `-I -O -B`) and the regenerated JSON outputs were compared with the retained ones; see [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md). CI reruns the same on Linux.
6. **Citations.** Every reference was copied from its Crossref or DataCite record and rechecked at release ([CITATION_AUDIT.md](CITATION_AUDIT.md)).

## What was not done

- No human specialist or journal peer review, no independent reproduction by an unaffiliated party, no proof-assistant formalisation, no interval-arithmetic certification of the numerical constants or taper roots.
- **Priority is bounded** ([SOURCES.md](SOURCES.md)). The general positivity mechanism for Volterra operators with log-convex kernels is classical and is cited as background; the claimed contribution is its exact application to the circular fault kernel (Lemma 2 and its consequences) and the schedule results.
- **Model class is narrow:** zero Poisson ratio, uniform constant friction, zero fracture energy, homogeneous permeable layer, one-way coupling from pressure to slip. Point-source statements are elastic statements away from the singular centre. Annular sources can violate the centre-first property.
- The results concern the first loss of full sliding only. They say nothing about the later slip pulse, a locked patch's growth, or seismic hazard. The dimensional example uses illustrative parameters, not a calibrated site.
- The editor's last six minor corrections were made without a further review round.
- Agreement between AI reviewers is not independent evidence.
