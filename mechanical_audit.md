# Independent mechanical and regularity audit

**No theorem-prover verification was performed.** I re-derived the principal mechanical identities, checked the constants against independent exterior singular-integral evaluations, and found no algebraic defect in the finite-radius criterion or its exterior friction argument. The review identified four scope and regularity qualifications. The author incorporated all four, and I inspected the revised statements. No blocking mechanical issue remains within this audit's stated scope.

## Evidence boundary

This is an informal-proof audit using the proof-digest approach, separate from the academic-paper-reviewer assessment. I inspected `manuscript.md`, especially Sections 2--7; the complete `kernel_order_proof.md`; and the relevant definitions in `verify_fault_criterion.py`. I did not rerun the full plotting/numerical pipeline or reassess the entire literature search. I did not modify the manuscript.

The original manuscript hash at initial inspection was `87bc96538f037757db8b9a2aa6dc9c73a563925549371685f3de74f459bcba62`. The manuscript changed while the author addressed the reported issues. The independent numerical log records the exact contemporaneous hash. The final inspected revision, containing all four corrections and the almost-everywhere limiting theorem, had hash `de655646adde1158a4717b1fdfa7546905fc3ed75f8836d89fb755bb06252d2f`. These hashes identify inspected bytes, not a mathematical certificate.

## Findings requiring qualification

1. **No opening is a finite-window assertion. Corrected during review.** A finite Gaussian source does not imply uniformly bounded pressure over all time: constant injection gives `p(0,t)=c_p q_0 log(1+t/epsilon)`. Thus a sufficiently large finite initial normal stress ensures the stated no-opening inequalities on a specified finite interval, not forever. The revised Section 2 states this distinction. Section 7's all-time statements belong to the mathematical forward-slip model.

2. **The Gaussian finite-volume obstruction requires prior nucleation. Corrected during review.** A small finite injection can remain below the slip threshold indefinitely. Once a disk has nucleated, `B_epsilon(t_n)>0`, nonnegative finite-radius centre velocity would imply `B_epsilon' >= 0` thereafter, and the limit `B_epsilon(t) -> 0` yields the contradiction. The revised Section 7 includes this condition.

3. **Past integrability alone does not guarantee a pointwise time derivative. Corrected during review.** For example, let `q=1` up to `t=1`, then `q=1+(t-1)^beta`, with `0<beta<1/2`. At `t=1` the past centre integral is finite and a disk exists, but the new centre-slip increment is proportional to `h^(beta+1/2)`, so its right derivative diverges. The revised definition of a point-source regular time requires a Lipschitz neighbourhood and avoids this case. The Gaussian source has bounded zero-age kernels.

4. **The global trajectory statement must not rely only on the newly defined regular times for unrestricted BV histories. Corrected during review.** A BV history may have no open neighbourhood on which it is Lipschitz, so positivity at such times alone could be vacuous. The revised Section 2 restricts the physical trajectory conclusion to piecewise locally Lipschitz histories with finitely many exceptional times on each compact interval and uses positivity almost everywhere in time. The instantaneous signed-measure kernel inequality remains stated at its broader valid generality. Theorem 3 now defines locally integrable weak velocities for locally BV histories and gives the all-history equivalence almost everywhere, with a causal truncation before using Laplace transforms. These changes address the issue without changing the kernel theorem.

## Claim/check ledger

| Claim | Status | Evidence and limits |
|---|---|---|
| Pressure constant `c_p=1/(4 pi alpha S w)` and Gaussian age shift | Passed algebraic check | Direct convolution of two planar heat kernels; integrating in space gives the injected-volume identity. |
| Dawson Abel-transform identity and factor `4 f c_p/(pi mu)` | Passed algebraic check | Substitution `y=sqrt(1-s^2)` gives the Dawson quotient; the zero-SIF endpoint term cancels. |
| Centre-versus-radius age ordering | Passed independent proof inspection | The density crossing works only at levels `c<=1`, which is sufficient because coupling gives `M_r/M_0<1`. No unsupported global likelihood-ratio order is used. |
| Square-root-cap elastic traction | Passed derivation and finite independent checks | Hankel transform and direct exterior half-Laplacian integral agree in three cases to below `9e-16` absolute error. |
| Abel inversion and exterior friction gap | Passed derivation and finite independent checks | A polynomial loading with an exact `3/2`-power slip profile verifies both traction superposition and the gap formula at three exterior radii. Maximum reported error is below `4e-12`. |
| Expanding support before failure | Passed with added edge step | The revised Section 5 uses the edge limit of velocity and `Rdot=-F_t/F_a`; `F_a<0` and nonnegative velocity imply `Rdot>=0`. |
| Complementarity and uniqueness | Passed conditionally on stated regularity | The energy calculation is correct for absolutely continuous finite-energy trajectories for which the pairings are defined; a natural space is the decaying homogeneous `H^(1/2)` energy space. It is not a post-locking existence proof. |
| Gaussian finite-volume obstruction | Passed after nucleation qualification | The kernel is bounded by `epsilon^(-1/2)` and tends pointwise to zero; dominated convergence against integrable nonnegative `q` proves `B_epsilon -> 0`. |
| Finite-radius error constants | Passed algebraic check | `D(z)<=1/z` gives the tail coefficient `4 alpha`; division by the infinite centre coefficient gives `8 sqrt(alpha)/pi^(3/2)` in the sign certificate. |
| Entire supplied numerical pipeline | Not rerun in this audit | The separate main numerical review covers it. This audit used independently written mechanical quadrature. |
| Formal proof and full novelty assessment | Not assessed here | No proof assistant was used; separate review and novelty records address the other questions. |

## Mechanical derivation in compact form

Let `F=A[g]` decrease through zero at `R`. Integration by parts writes the slip as a positive superposition of square-root caps, with weight `-F'(a)`. The cap has unit normalised interior traction and negative exterior traction `E(a/r)`. Abel inversion gives `g(r)=F(r)-integral_0^r F'(a)E(a/r) da`. Subtracting the actual cap superposition outside the disk leaves `-F(r)+integral_R^r F'(a)E(a/r) da`, whose two terms are positive. Thus the disk solves the exterior inequality as well as the interior equality.

Near the edge, `v(r,t)/sqrt(R^2-r^2)` tends to `4 F_t(R,t)/(pi mu)`. Therefore an everywhere nonnegative trial velocity gives a nondecreasing radius. This prevents the moving support from dropping points that had accumulated positive slip. The resulting time-increasing branch satisfies the irreversible complementarity relations. For two sufficiently regular solutions driven by the same pressure, self-adjointness cancels the common loading and the difference energy has nonpositive derivative; identical initial data therefore give identical trajectories up to the first failure of the branch.

For the point source, the endpoint calculations also use `F'(a)=O(1/a)` near zero, in addition to `F(a)=O(|log a|)`. Both bounds follow directly from boundedness of the rate on compact time intervals. This derivative bound can be made explicit in the text for clarity.

## Reproduction record

Command: `python geology_research/mechanical_audit_checks.py`, from the workspace root. Python 3.12.14; SciPy 1.17.0; exit status 0; internal elapsed time approximately 0.343 seconds. Exact values and the contemporaneous manuscript hash are recorded in `mechanical_audit_checks.json`. The code evaluates the exterior two-dimensional singular integral independently of the manuscript's cap formula and checks an exactly invertible polynomial load. These finite checks support normalisation and implementation; the symbolic sign argument proves the unrestricted inequality.

## Proof-presentation rubric

The following scores concern presentation of the inspected argument, not correctness probability, novelty or publishability. The fifteen informal submetrics retain the proof-digest 1--5 half-point scale.

| Dimension | Three submetrics, in rubric order | Mean |
|---|---|---:|
| Structure | Main outline 4.5; complexity distribution 4.0; dependency clarity 4.5 | 4.33 |
| Signature quality | Natural statements 4.0; hypothesis economy 4.0; useful generality 4.0 | 4.00 |
| Step transparency | Explicit reasoning 4.5; meaningful lemma use 4.5; routine closures controlled 4.5 | 4.50 |
| Reuse | Structural usefulness 4.5; reuse potential 4.0; no decorative lemmas 4.5 | 4.33 |
| Human readability | Proof readability 4.5; consistent mathematical style 4.0; maintainability 4.5 | 4.33 |

Overall presentation mean: **4.30/5**. Section 3 separates the kernel lemma from the signed-history argument effectively. Section 5 now exposes the exterior inequality and the expansion of support rather than assuming them. The revised hypotheses distinguish the broad signed-measure inequality from the more regular physical trajectory statement. The main reusable ingredient is the special kernel ordering; the cap inversion and energy uniqueness are standard tools deployed explicitly.

**Bounded conclusion:** the inspected constants, exterior mechanics and Gaussian finite-volume contradiction are sound with the revised source, nucleation and regularity assumptions. The author resolved all blocking scope issues raised in this audit. A concrete independent sanity check is the exact polynomial example `g(r)=1-r^2`, `R=sqrt(3/2)`, `delta(r)=16(R^2-r^2)_+^(3/2)/(9 pi)`, whose exterior friction gap is strictly positive and agrees with direct nonlocal quadrature.
