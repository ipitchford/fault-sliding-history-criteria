# Response to the round-1 review

Revision of 31 October 2026. Section, equation and table numbers refer to the revised `output/fault_locking_manuscript.pdf` (equations are numbered automatically; labels in `manuscript.md` are given where helpful). All items of the merged fix list were addressed. Extensions X1--X5 succeeded; the optional X6 succeeded in a stronger form than asked (a theorem for Gaussian mixtures) together with a counterexample for annular sources. Item A8 succeeded. Two parts were deliberately kept weaker than suggested, with reasons: uniqueness for the point source (A5) and the finite-radius taper threshold, which is given as a checked leading-order approximation rather than a theorem (X2).

## A. Scope and correctness wording

**A1 (title, "locking" language).** Retitled "Scalar history criteria for the first loss of full sliding under variable fluid injection". "Onset of locking" and "locking occurs at the centre" were replaced throughout by "first loss of full sliding" / "first loss … occurs through the centre". Section 2.5 defines full sliding, threshold contact and trial branch; Section 10.2 states that a negative crossing does not prove a locked patch.

**A2 (instantaneous vs trajectory).** Theorem 1 (Section 3.3) is now titled "instantaneous criterion" and stated at a single time. The trajectory statement is the separate Corollary 3.1, which also says that after the first negative margin later evaluations concern only the formal trial branch.

**A3 (weak vs classical derivative).** Section 3.1, "Velocity formula": (15) now *defines* the trial velocity as a signed-measure integral under (14). It is proved to be the classical derivative of the slip at regular times (locally Lipschitz rate for the point source, continuous rate for the Gaussian source), and no classical derivative is claimed for general bounded-variation histories.

**A4 (nondegenerate centre zero).** Replaced by the measure condition (27), $m_+([0,b))+m_-((b,t])>0$, in Theorem 1.

**A5 (uniqueness).** Section 6.2 gives the variational definition (forward-slip solution in a ball $B$: $\delta\in AC([0,t_1];\dot H^{1/2})$, $v\in L^1(0,t_1;\dot H^{1/2})$ in the positive cone, $\chi=\mathfrak T\delta-g$ nonnegative on nonnegative test functions, $\langle\chi,v\rangle=0$ a.e.) and proves uniqueness (Proposition 6.1). Membership of the constructed branch is proved for the Gaussian source. For the point source membership requires absolute convergence of the cap superposition in $\dot H^{1/2}$ near $a=0$, which we did not verify; the paper therefore claims exterior admissibility but not uniqueness for the point source.

**A6 (singular centre for the point source).** Section 3.1 ("Point source at the centre") states that point-source results are elastic statements on $r>0$ with the centre value a finite limit; Section 10.2 states that Gaussian-source results are physically primary and that full Coulomb admissibility is available only for $\varepsilon>0$.

**A7 (Lemma C).** Rewritten as Lemma A.2 (Appendix A.3) in three steps: local expansion, the value of $\Psi''$ at a stationary point (A.4), and the first-zero argument with $z_*=\inf\{z\ge\eta:\Psi'(z)=0\}$. A slip in the old text ($D''/D$) was corrected in passing; the conclusion is unchanged.

**A8 (radius existence).** Succeeded. Proposition 4.1, proved in Appendix B.7: the set of times with a crack radius is relatively open (lower semicontinuity of the centre pressure); while the centre history is nonnegative the radius is nondecreasing and bounded ($R^2\le4\alpha s_*fc_p\mathcal V/\tau_{\rm d}$), so it has a positive limit $R_1$; continuity gives $f\mathcal Ap(R_1,t_R)=\tau_{\rm d}$, strict radial decrease gives $fp(0,t_R)>\tau_{\rm d}$, and openness contradicts maximality. The existence hypothesis was removed from Theorems A and G (their condition (ii) is now stated on the existence interval).

**A9 (Theorem G hypothesis).** The primary hypothesis is now nonnegative latent forcing (30)--(31); nondecreasing injection is listed as a sufficient condition (Section 4, Theorem G).

**A10 (Theorem 3 in the time domain).** Section 7.1: the probability measure $\Lambda_r$ (46) is defined explicitly and $v_\infty(r,\cdot)=\Lambda_r*v_\infty(0,\cdot)$ in $L^1_{\rm loc}$ (47) is proved, with the first-passage interpretation. The inner model is defined as $\Theta\to0$ on a fixed window, with a short convergence argument, and all-time inner statements are flagged as not uniform at fixed $\Theta$.

**A11 (abrupt drops).** Section 5.1 states that equality in the drop tolerance (33) is threshold contact; Section 5.2 gives the one-sided asymptotic (34) for a point-source downward jump, derived from Proposition 7.3, and checks it numerically (Section 9.3).

**A12 (arcsine and taper).** Section 8.1: "bounded below almost everywhere, within the class for which Abel inversion (53) holds". Corollary 8.4 states that $d_\infty$ is strictly inadmissible at every finite radius by (52).

**A13 (Theorem B wording).** Theorem B now reads "within these startup classes".

**A14 (artefact sentence).** The sentence was removed. Section 3.4 and Section 10.2 now state precisely what is known: the result holds for all positive Gaussian mixtures (Proposition 3.3) and fails for annular sources (Section 9.4).

## B. Positioning and literature

**B1.** The model, (8) and (9) are attributed to Sáez, Lecampion, Bhattacharya and Viesca (2022) in Sections 2.2, 2.4 and 10.1; Sáez et al. (2025) is kept for the volume laws and the open question. Section 2.2 and 10.2 state which steps fail for nonzero Poisson ratio (scalar operator, axisymmetry).

**B2.** Section 2.2, (4)--(5): $\Theta$ is identified with the stress-injection parameter $T$ (with $c_pq_0=\Delta p_*$), and the constant-rate map $\lambda(\Theta)$ with both asymptotes is given and proved (Appendix D.1).

**B3.** Added, each copied from its Crossref record (DataCite for the thesis) and checked to resolve: Sáez et al. 2022; Garagash and Germanovich 2012; Bhattacharya and Viesca 2019; Viesca 2021; Sáez and Lecampion 2024; Friedman 1963; Gripenberg 1978; Clément and Nohel 1981; Gripenberg, Londen and Staffans 1990; Alghannam and Juanes 2020; Sneddon 1946; Gorenflo and Vessella 1991. The thesis now carries its DOI 10.5075/epfl-thesis-10303; Jacquey and Viesca carries issue 50(4). The records are in `crossref/` and the bibliography in `refs.bib` (all entries with DOI); the reference list is generated from it.

**B4.** Section 10.1 names the classical positivity theory and the nonconvolution log-convexity condition; Appendix B.2 states that the bracket in (B.3) is exactly that condition and lists the verified kernel hypotheses ((A.2), (A.3), (A.5), (A.6), Lemma 2). Lemma 2 is described as a variation-diminishing argument, and the failure of total positivity of order two is stated after Lemma 2 and in Section 9.4. Novelty is confined as requested in the last paragraph of Section 10.1.

**B5.** Section 10.1, second paragraph (consistency with prior results), and Section 8.1 (insulated half-space and arcsine law as a reinterpretation).

**B6.** Audit language removed from the abstract, Section 1, Section 10 and the references; the "Research record" section was deleted. One sentence of priority caveat remains at the end of Section 10.1.

## C. Readability

**C1.** New abstract (188 words).
**C2.** Section 1: who uses the result (1.1), the result in words with the physical intuition (1.2), contributions with theorem pointers (1.3), roadmap (1.4).
**C3.** Section 1.5, "Main results at a glance".
**C4.** Section 2.6 notation table. Collisions removed: strength excess $\tau_{\rm d}$ (was $\Delta$), Laplacian written $\nabla^2$, jump size $j$; cap traction $\Pi$ vs edge response $E$; $\bar r=\sqrt{R^2-r^2}$, taper duration $L$, operator $\mathfrak T$; friction gap $\chi$ vs transfer kernel $h$; measures $m_\pm$; Laplace variable $\xi$; densities $\varphi_r$; volume $\mathcal V$; auxiliary shift $\eta$, output kernel $\beta$. $\Theta$ and the scalings are introduced in Section 2.2.
**C5.** Single "Scope and limitations" subsection (10.2); repeated caveats removed elsewhere.
**C6.** Section-goal sentences open Sections 2--10; reading guides open Appendices A--D; Appendix B is integrated (no reference to an external note); equations are renumbered automatically; Section 2.5 defines the requested terms.
**C7.** Section 8.5, "What the criterion is for".
**C8.** Section 10: Relation to previous work, Scope and limitations, Implications, Open problems.
**C9.** Author "Anonymous", date 31 October 2026; both figure captions state the nondimensionalisation.

## D. Extensions

**X1 (persistence time) - succeeded.** Proposition 8.2 with proof: two-sided centre-pressure bound (55), nonexistence of a crack after $t_s+fc_p\mathcal V/\tau_{\rm d}-\varepsilon$, existence before $fc_p\mathcal V/\tau_{\rm d}-\varepsilon$, and (with Proposition 4.1) strict loss of full sliding before (56) $=T(1+1/\Theta)-\varepsilon$. A Gaussian tail version is included; for the point source we explain why no tail version holds. Checked in Section 9.2.

**X2 (two-term criterion) - succeeded, with one part as an approximation.** Proposition 7.3 with proof: (50)--(51), with $c_D\le0.4115$ certified (Appendix D.2; grid maximum 0.41133). The constants were re-derived: $K_\infty-K_R=2\alpha/R$ plus a remainder bounded by $16c_D\alpha^2u/(3R^3)$. Table 3 compares the two-term roots with all taper rows and gives rigorous enclosures where the remainder is smaller than the correction ($\Theta\le1$). Agreement is to $10^{-4}$ in time at $\Theta=0.01$ and $5\times10^{-3}$ at $\Theta=0.1$, degrading for $\Theta\ge0.5$; the paper says so. The sharpened uniform certificate (Proposition 7.2) replaces the constant 1 by $s_*\le0.6424$. The finite-radius taper threshold (61) is derived to leading order in Appendix D.3 and checked against directly computed $d_{\max}(\Theta)$ (error $<0.033\Theta$ for $\Theta\le0.1$). It is labelled an approximation because its derivation assumes that the binding time stays at $T+L$ and neglects $O(\Theta)$ terms; we did not prove these steps. The rigorous statement $d_{\max}<d_\infty$ is Corollary 8.4.

**X3 (regimes and realistic numbers) - done.** Table 3 extends to $\Theta=2,5,10$ (Gaussian $\Theta=5,10$: no slip). Table 1 gives drop tolerances at $\varepsilon/T$ down to $10^{-8}$ (about $10^{-3}$ at wellbore scale). Section 8.4 and Table 2 give an illustrative dimensional example (parameters labelled illustrative, no site sources claimed). Corollary 8.4 states that no linear taper can halve the rate.

**X4 (jumps) - succeeded for both sources.** Theorem G allows piecewise-$C^1$ rates with jumps of either sign (right-continuous margins, left limits; Appendix C.2 and C.4). Theorem A allows jumps: downward jumps violate both sides at once (Appendix B.8), and upward jumps are handled by the bound (B.14), which uses $a_jK_{R(t_j)}(0,2\delta_0)>2A_*M\sqrt{T+1}$, together with the observation that the edge response jumps only upward. Checked numerically in Section 9.3.

**X5 (near-threshold tests) - done.** Section 9.3: two-dip point-source history tuned to a tangential centre zero with recovery (noncentral velocities and edge response at the contact listed), stepped Gaussian schedule near its critical step, a point-source upward jump. Section 9.1 states quadrature and root tolerances; refinement changes all Table 3 roots by $<1.5\times10^{-14}$ and the two implementations agree to $3.5\times10^{-11}$.

**X6 (source mixtures) - succeeded, stronger than asked.** Proposition 3.3 proves Theorem 1 for every positive mixture of Gaussian widths (equivalently radial source densities completely monotone in $r^2$). A numerical counterexample shows that annular (difference-of-Gaussians) sources violate the age order and can lose full sliding off-centre first (Section 9.4); this is listed as an open problem (Section 10.4, item 3).

## E. Code and replay

**E1.** All scripts use explicit checks; sibling imports work under `-I`.
**E2.** New scripts `constants_and_two_term.py`, `regime_and_taper_checks.py`, `history_extension_checks.py`, `make_extension_figure.py` and module `fault_core.py`; JSON floats rounded to ten significant figures; each check script has at least two semantic negative controls (listed in README).
**E3.** `run_checks.py` runs every check with `-I -O -B` and exits nonzero on failure. Final run: all ten passed (about 160 s).
**E4.** README rewritten (replay instructions, script list, no ratings). The internal review report and its build files are withheld from the public package; private editorial assessments were also removed from the supporting records.

## New or rewritten proofs (for the proof audit)

| Result | Location | Status |
|---|---|---|
| Velocity formula as definition; classical derivative at regular times | Section 3.1 | rewritten |
| Lemma 2 (centre-relative age order) | Section 3.2 | rewritten (renamed symbols, strictness justified) |
| Theorem 1 with measure condition (27) | Section 3.3 | rewritten |
| Corollary 3.1 (trajectory form) | Section 3.3 | new |
| Proposition 3.3 (Gaussian mixtures) | Section 3.4 | new |
| Theorem A with jumps; downward-jump exclusion; upward-jump bound (B.14) | Section 4; Appendix B.8 | new |
| Theorem G with jumps, latent-forcing hypothesis | Section 4; Appendix C.1--C.4 | rewritten |
| Proposition 4.1 (crack radius persists) | Appendix B.7 | new |
| Abrupt-drop tolerance bound $<\sqrt{\varepsilon/(T+\varepsilon)}$ | Section 5.1 | new (one line) |
| Point-source downward-jump asymptotic (34) | Section 5.2 | new |
| Proposition 6.1 (uniqueness in a variational class) and membership for $\varepsilon>0$ | Section 6.2 | rewritten |
| Theorem 3 in time-domain form (47) | Section 7.1 | rewritten |
| Proposition 7.2 (sharpened uniform bound) | Section 7.2 | new |
| Proposition 7.3 (two-term centre kernel) | Section 7.3 | new |
| One-sided comparison (52) | Section 7.4 | unchanged, restated |
| Arcsine bound in the Abel-inversion class | Section 8.1 | rewritten |
| Proposition 8.2 (persistence-time bound) | Section 8.2 | new |
| Corollary 8.4 (no linear taper halves the rate; strict finite-radius reduction) | Section 8.3 | new |
| Lemma A.2 (expanded), $G(\infty)$, complete monotonicity | Appendix A | rewritten |
| Radius map and asymptotes | Appendix D.1 | new |
| Bounds on $s_*$ and $c_D$, Dawson inequalities (D.1) | Appendix D.2 | new |
| Leading-order taper threshold | Appendix D.3 | new derivation (approximation, not a theorem) |

## Final fixes (after proof audit and re-review)

All items of `FINAL_FIXES_BRIEF.md` were applied. Section, equation and table numbers refer to the final PDF.

| Item | Change and location |
|---|---|
| P1-1 | Corollary 3.1 (Section 3.3) rewritten: positivity is required at every defined time from the start of slip (right-continuous values for the Gaussian source); identification with the physical solution only from startup/nucleation, uniqueness only for Gaussian branches of Theorem G, no point-source uniqueness; Gaussian terminal-drop example and the no-restart caution added. |
| P1-2 | Theorem A (Section 4): downward jumps excluded only for $t_j<T$; two-sided conclusions only for $t_j<T$, left limit at a terminal jump. |
| P1-3 | Theorem B (Section 4) assumes no downward jump in $(0,t_c]$; recovery-zero caveat; first loss stated as first negative crossing or downward jump. B.6 updated. |
| P1-4 | Appendix C.4 split: Lemma C.1 (edge positivity conditional on an existing radius on $(t_n,\tau]$) is used in B.7; Theorem G is then completed with Proposition 4.1. No circularity. |
| P1-5 | Section 3.1: finiteness qualified by (14), with the $q=1-\sqrt{1-s}$ example; Gaussian convergence via the age floor $\varepsilon$; regular-time justification split by source. |
| P1-6 | Theorem 1 stated for $t\ge b$; proof treats $t<b$ and $t=b$ ($u_b=\varepsilon$; point-source atom at $b$ excluded by (14)). |
| P1-7 | Appendix C.1: the kernel extension is continuous; $H$ is càdlàg with $H(v)-H(v^-)$ equal to the jump of $q$. |
| P1-8 | Section 9.4: drop defined by the kernel ratio $\bar K_1(0,u_{\rm o})/\bar K_1(0,u_{\rm y})$; no "exactly". |
| P1-9 | Appendix B.8: $\delta_0\in(0,t_d]$ chosen explicitly. |
| P2-1 | Section 5.2: isolated jump with bounded one-sided derivatives nearby assumed; accumulating-jump caveat added. |
| P2-2 | Proposition 7.3 restricted to positive-radius times satisfying (14), with the combined-kernel-difference form; Proposition 7.2 certificate and the Section 7.1 convergence wording qualified likewise. |
| P2-3 | Section 6.2: membership proved for Theorem G's piecewise-$C^1$, transversely nucleating branches, including the unslipped interval. |
| P2-4 | Appendix D.2 and `constants_and_two_term.py`: explicit floating-point allowance $10^{-13}$ per evaluation (observed error $\le2.2\times10^{-16}$ against an 80-digit series on 2001 points); constants now called numerically verified upper bounds (Propositions 7.2, 7.3 wording updated). |
| P2-5 | Corollary 8.4 (Section 8.3) is explicitly point-source and has a proof of the strict supremum via continuity of $R(T+L;d)$ and of the margin in $d$; Gaussian counterexample for $\varepsilon>T+L$ given with its one-line bound. |
| P2-6 | Appendix D.1 sign of $J_R\,du$ corrected; "Appendix D.4" corrected to D.3. |
| R-1 | "First zero" replaced by "first negative crossing" for loss (Sections 7.3, 8.3, 8.4 Table 2, 8.5, 9.1, 9.2 Table 3, 10.2, 10.3, Figure 1 caption); Section 10.1 no longer says Theorem B proves locking. |
| R-2 | Abstract, Section 1.2, results table (Theorem 1 row, Theorem B/G/Prop 8.2/Cor 8.4 rows), Section 1.3 items 4–6 carry source and startup restrictions. |
| R-3 | Sections 7.1, 8.5 and 10.3 separate the shut-in deadline (Proposition 8.2) from eventual failure of integrable histories. |
| R-4 | Section 9.2: $d_{\max}$ values called finite-window ($t\le50$) estimates; Section 7.3 and Table 3 caption separate the analytic enclosure from the uncertified root search; Section 1.3(5) qualified to $\Theta\lesssim0.1$. |
| R-5 | Section 9.4: the static example is described as failure of the instantaneous centre test; a new time-history check (`history_extension_checks.py`, `annular_trajectory`) shows positive sampled velocities from $t=0.031$ to the drop and an off-centre reversal at the drop while the centre is positive, and reports that the radius equation has two roots earlier, so no full trajectory counterexample is claimed. |
| R-6 | Section 10.1: Viesca (2021) described as constant-pressure, Viesca (2025) as constant-rate; positivity references introduced with "see, for example" (no theorem locators claimed). |
| R-7 | Section 10.1: the "We did not find…" sentence replaced by a direct statement that Appendix B gives a self-contained proof; one priority caveat remains at the end of 10.1. |
| R-8 | "How to use the criterion" paragraph (Section 1.3); Lemma 2's density proof moved to Appendix A.4 with the statement and an "idea of the proof" kept in Section 3.2; Table 2 marks Gaussian versus point-source entries; the Brownian-delay description in Section 1.2 is flagged as inner-limit from its first sentence; wellbore parameters called illustrative where first introduced (Section 5.1). |

**Proofs changed materially in this round:** Corollary 3.1 (statement and proof); Theorem A (terminal-jump scope) and Theorem B (no-downward-jump hypothesis); Appendix C.4 (new Lemma C.1 and reordered proof of Theorem G, removing the circular dependence on Proposition 4.1); Corollary 8.4 (new proof of the strict supremum, point-source scope). Minor proof repairs: Theorem 1 at $t=b$; Section 5.2 isolation hypothesis; Proposition 7.3 integrability scope; C.1 càdlàg statement; B.8 choice of $\delta_0$; D.1 sign; D.2 evaluation allowance.

`run_checks.py` passes all ten scripts after these changes.
