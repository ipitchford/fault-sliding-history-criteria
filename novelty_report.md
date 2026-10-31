# Novelty-gate report: centre-first locking under single-peaked injection

**Search date:** 28 October 2026.  
**Research team:** the primary research agent and three delegated agents; this is an internal research audit.  
**Corpus boundary:** public scholarly web searches through both available search engines, accessible publisher text, arXiv, author manuscripts, an EPFL thesis and selected recent primary articles. No subscription citation-index export or author enquiry was performed.  
**Intended units:** a special-kernel inequality; its exact source-admissibility theorem; model-specific consequences; reproducibility artefacts.

**Final scope update.** The initial gate below concerns the single-peaked criterion. Subsequent formula-level gates, fully recorded in extension_novelty_audit.md, also cover the completed point-source and finite-Gaussian historical centre criteria in Appendices A and B. For the point source, the smooth rate has either positive initial value or a positive nondecreasing startup; for the Gaussian source, centre pressure is nondecreasing before transverse first nucleation. In these classes the entire centre history alone is sufficient, including earlier tangential centre-velocity zeros, and radius growth follows automatically. Generic inverse positivity, row normalisation and first-zero arguments are classical. The new targets are target_arbitrary_history.yaml and target_gaussian_startup.yaml. The general pressure-decreasing Gaussian prebirth problem, tangential birth and subsequent pulse evolution remain outside scope.

## 1. Frozen claim and revisions

The narrow target is the circular scalar fault model with zero Poisson ratio, constant friction, zero fracture energy, homogeneous hydraulic properties and uniform positive prestress deficit. The causal injection rate is nonnegative and single-peaked: all positive rate increments precede all negative rate increments. For the exact finite-radius fully sliding branch, the sign of the centre slip rate determines the sign throughout the interior. The centre value is an explicit signed history integral.

The initial point-source target was frozen in `target.yaml` before the detailed proof was assembled. Revision 2 records a fixed Gaussian source extension, the correct nucleation condition and explicit regularity conventions. The separate kernel target is recorded in `target_kernel_order.yaml`. For the Gaussian source, positive rate alone does not imply slip: its centre pressure must exceed the prestress deficit divided by friction.

The time-trajectory conclusion uses piecewise locally Lipschitz rates, with finitely many exceptional times on compact intervals, and nonnegative velocity almost everywhere. The signed-measure kernel inequality is broader but does not by itself assert pointwise differentiability for every BV rate.

### Exclusions

- The initial theorem is single-peaked. The later historical criteria cover the source/startup classes in the final scope update; general Gaussian pressure-decreasing prebirth histories, noncircular rupture, rate-and-state friction and slip weakening remain outside scope.
- A zero centre velocity need not produce a finite locked patch if the zero is tangential. A negative continued trial velocity establishes loss of admissibility.
- The subsequent pulse is outside the result.
- The constant-rate Bessel kernel, circular Abel inversion, volume laws, Laplace single-crossing principle and Abel inversion are established machinery.
- Mathematical no-locking is not a seismic-risk objective.

**Permitted language:** “The exact finite-radius single-peaked criterion was not found in the bounded search described here.”  
**Forbidden language:** “This is the first proof ever”, “the general pulse problem is solved”, “the resulting taper is safe”.

## 2. Normalisation and verified translations

| Original quantity or convention | Canonical version in this work | Translation checked |
|---|---|---|
| Sáez et al. [2025] residual friction | $f$ | Constant-friction upper-bound model; no slip-weakening theorem claimed. |
| Residual background stress change | $\Delta=f\sigma'_0-\tau_0>0$ | Same uniform resistance to rupture growth. |
| Constant-rate pressure scale | $c_pq_0=q_0/(4\pi\alpha S w)$ | Integrating the Gaussian impulse in time gives the standard exponential-integral pressure. |
| Normalised radial crack inversion, Eq. 14 | $\delta=(4/\pi\mu)\int_r^R aF(a)/\sqrt{a^2-r^2}\,da$ | Changed variable from normalised crack radius to dimensional $a$. |
| Zero stress intensity | $F(R,t)=0$ | This cancels the moving-endpoint term when differentiating slip. |
| Viesca [2025] inner slip, Eq. 20 | $u^{-1/2}e^{-r^2/(8\alpha u)}I_0(r^2/(8\alpha u))$ | Differentiate the self-similar constant-rate inner displacement at fixed physical radius. |
| Fixed Gaussian source | Age shift $u\mapsto u+\varepsilon$ | Heat-kernel convolution; the spatial Gaussian is fixed, not a finite-borehole boundary. |

## 3. Formula fingerprints

The exact finite-radius kernel is

$$
K_R(r,u)=2\sqrt{\alpha/u}\int_r^R
\frac{D(a/(2\sqrt{\alpha u}))}{\sqrt{a^2-r^2}}\,da.
$$

Its positive double-integral normal form is

$$
K_R(r,u)=\frac{\sqrt{R^2-r^2}}u
\int_0^1\int_0^1
\exp\!\left[-\frac{(r^2+(R^2-r^2)x^2)(1-y^2)}{4\alpha u}\right]dx\,dy.
$$

The probability form is the Laplace transform of

$$
S_r=[r^2+(R^2-r^2)Z^2](1-Y^2),
\qquad Z,Y\text{ independent uniform on }[0,1].
$$

The density at the centre is

$$
g_0(s)=\frac{\arccos(\sqrt s/R)}{2R\sqrt s},\quad0<s<R^2.
$$

The off-centre density is

$$
g_r(s)=\frac1{4\sqrt{R^2-r^2}}
\int_{\max(r^2,s)}^{R^2}
\frac{dp}{\sqrt{p-r^2}\sqrt p\sqrt{p-s}}.
$$

The exact moments are

$$
\mathbb E S_r^n=\frac{4^n(n!)^2}{(2n+1)!}
\sum_{j=0}^n\binom nj\frac{r^{2(n-j)}(R^2-r^2)^j}{2j+1}.
$$

At $r=0,R=1$, the first moments after 1 are $2/9$, $8/75$, $16/245$. These elementary beta-product moments are fingerprints, not a proposed new sequence. No finite matrix or rational generating function is involved; matrix hashing and finite spectrum searches are inapplicable.

Three reproducible kernel values for $R=\alpha=1$ are $K_1(0,0.2)=3.94078558171061$, $K_1(0.4,0.2)=3.29207557213647$, and $K_1(0.9,1)=0.377674438903318$. Independent quadrature and exact-moment checks are in the supplied JSON files.

The infinite-radius normal form is the Bessel expression in manuscript Eq. 38. This triggered a mandatory rerun and exposed the Viesca collision.

## 4. Cross-disciplinary aliases

| Area | Aliases searched or assessed |
|---|---|
| Analysis | Abel transform; Dawson integral; hypergeometric ${}_2F_2$; fractional half derivative; mixed boundary elasticity |
| Probability | Product of beta-type variables; Laplace-transform ratio order; single crossing; exponential tilting; positive first-passage mixture |
| Mathematical physics | Penny-shaped crack; circular shear crack; centre locking; crack-to-pulse transition; axisymmetric unloading/contact |
| Optimisation/control | Unimodal input; taper; minimum continuation; no-relocking cone; positive causal transfer |
| Combinatorics | No substantive finite combinatorial object; rational beta moments used only as computational fingerprints |

The proof does not establish total positivity for arbitrary pairs of radii. A stronger radial-ratio assertion was disproved analytically and numerically during the work. Restricting the theorem to comparison with the centre is essential.

## 5. Search log

All queries below were made on 28 October 2026. Both available web engines were used; stronger-source and recent-work checks used the first engine. Title, author and formula searches were followed by source inspection where accessible.

| Query family | Representative exact queries | Inspected consequence |
|---|---|---|
| Original source and gap | `aseismic slip arbitrary injection history pulse criterion`; `"injection" "necessary and sufficient" "pulse"` | Located the explicit gap after Eq. 24 in Sáez et al. 2025. |
| Direct source neighbourhood | `"Sáez" "Lecampion" "Post-injection aseismic slip" 2023`; author publication page | Checked the full 2023 preprint, parallel full thesis chapter and current listed work. |
| First finite-kernel pass | `"aseismic" "Dawson" "flow rate"`; `"slip" "unimodal" "injection"`; `"crack" "pulse" "Abel" "injection"` | No matching source criterion retrieved; negative evidence is weak by itself. |
| Finite-radius aliases | `"penny-shaped" "unimodal" injection locking`; `"fluid-driven" "locking" "centre" "rate" Saez`; `"circular crack" "maximum principle"` | Located surrounding crack/contact terminology, no exact theorem. |
| Transform-method rerun | `"Laplace transform" "ratio" "Yang" "Tian" "2019"`; `"Laplace transform ratio" "single crossing"`; `"axisymmetric" "contact" "single crossing"` | Established general monotonicity methods as prior art. |
| Density/probability rerun | `"Laplace transform ratio" "product" stochastic`; `"arccos" "Laplace" "ratio" "density"`; `"beta" "shifted" "Laplace transform ratio"` | No exact target-kernel order found; beta products themselves are elementary. |
| Special-function rerun | `"Dawson" "Abel" "ratio"`; `"2F2" "1/2" "3/2" "Dawson" monotonicity ratio` | No exact inequality retrieved. |
| Inner-limit collision search | `aseismic fractional derivative`; `aseismic half-order`; Viesca transient/constant-rate searches | Viesca 2025 supplies the constant-rate inner profile and Bessel response. |
| Taper and control aliases | `"injection" "arcsine" taper`; `"arcsin" "injection" "aseismic"`; `"minimum" "continuation" "half derivative"`; `"arcsin" "positive" "Abel" continuation` | No geological predecessor for the exact continuation retrieved; Abel inversion is classical. |
| Current geological evidence | `aseismic fluid injection tapered shut-in centre locking pulse 2026`; exact Ji and Passelègue titles | Inspected 2025 shut-in comparison and 2026 propagation experiments; neither validates or replaces this locking theorem. |

The compact literature comparison and the delegated audit include further exact query strings and source-by-source access boundaries. They are included as separate records to make the search reproducible.

## 6. Verified collisions and distinctions

### 6.1 The explicit gap

Sáez, Passelègue and Lecampion (2025), DOI https://doi.org/10.1126/sciadv.adq0662, full author PDF inspected. The paragraph after Eq. 24 requires crack-like behaviour for the arbitrary-history construction and states that the necessary and sufficient source conditions for a pulse are unknown. The present result resolves a specified single-peaked, first-admissibility subclass; it does not claim the whole broader problem.

### 6.2 Established constant-rate and shut-in results

Sáez and Lecampion (2023), DOI https://doi.org/10.1098/rspa.2022.0810, already establish post-shut-in centre locking and pulse propagation. Their full preprint https://arxiv.org/html/2211.16803v1 and parallel thesis chapter were inspected; Section 4.2 directly documents the complete-shut-in transition. Jacquey and Viesca (2023), DOI https://doi.org/10.1029/2022GL101228, supply a related two-dimensional constant-pressure/shut-in analysis; the full author PDF was inspected. These are collisions for any claim merely announcing post-injection locking.

### 6.3 The Bessel kernel

Viesca (2025), DOI https://doi.org/10.1017/jfm.2025.10593, full preprint https://arxiv.org/html/2401.13828v3 inspected. Differentiating its Eq. 20 self-similar inner slip gives the $e^{-z}I_0(z)/\sqrt u$ response. The response formula is prior art. The arbitrary-history positivity cone and exact finite-radius age order are distinct contribution units.

### 6.4 The proof method

Yang and Tian (2019), DOI https://doi.org/10.1016/j.jmaa.2018.10.034, abstract and arXiv record https://arxiv.org/abs/1803.02513 inspected. General Laplace-transform ratio rules are prior art. The present proof is self-contained and uses a restricted density crossing for levels $0<c\le1$. It does not claim a new general ratio principle or rely on an uninspected theorem from that paper.

## 7. Negative evidence and missingness

- The search is bounded, not exhaustive. Formula queries may miss alternate notation or unindexed text.
- We did not access subscription citation indexes, search all languages, or inspect every citing article.
- The 2023 journal PDF exceeded one retrieval route's size limit. The full parallel thesis chapter and, in the final audit, the full arXiv HTML preprint were inspected. This resolves the earlier substitute-access limitation for the key shut-in argument, though it is not a line-by-line comparison of journal and preprint versions.
- Some publisher pages returned access errors. Accessible primary alternatives or abstract-only boundaries are recorded rather than treated as full-text inspection.
- The 2026 experimental paper's main text/discussion was inspected by a delegated agent; the primary reviewer independently verified its bibliographic record and abstract. The complete methods were not cleared.
- Current author listings contain forthcoming or under-review work whose full contents were not inspected.
- No field observations, laboratory data or unpublished records validate the new criterion. All new numerical results are synthetic.
- No authors were contacted. A specialist/author enquiry is the most consequential remaining historical-priority check, and was not authorised or performed.

## 8. Outcome by contribution unit

| Unit | Outcome | Confidence / permitted wording |
|---|---|---|
| Diffusion convolution and circular inversion | COLLISION / established machinery | High; cite existing model. |
| Constant-rate Bessel response | COLLISION | High; derived from Viesca's known inner solution. |
| Complete shut-in gives centre locking | COLLISION | High; established in 2023 literature. |
| General transform and Abel methods | COLLISION / classical method | High; no new general method claimed. |
| Exact finite-radius centre-relative age ordering | CLEAR TO PROVE within the boundary; proof completed | Mathematical proof independently checked; historical priority remains bounded uncertainty. |
| Exact single-peaked centre criterion | CLEAR TO PROVE within the boundary; proof completed | Candidate original application; state finite circular model and first-failure scope. |
| Gaussian extension and finite downstep threshold | No collision found | Exact corollary, subject to the same bounded priority uncertainty. |
| Inner-limit all-history cone, arcsine continuation and volume obstruction | No matching geological result found | Derived consequences of classical machinery; do not claim new fractional calculus. |
| Independent numerical/reproducibility artefacts | Completed | They verify implementation and synthetic examples, not field validity. |
| Historical point-source and conditional Gaussian criteria | Proofs completed and internally checked | See Appendices A–B and the final extension audit; no exact predecessor found within its bounded search. |
| General pressure-decreasing Gaussian prebirth, noncircular or rate-dependent pulse problems | Not solved | Explicitly outside scope. |

## 9. Decision

The gate is **CLEAR TO PROVE within the documented search boundary**, and the associated proofs have now been completed and checked internally. The historical-priority statement remains **BOUNDED UNCERTAINTY**. This is sufficient to present a prospective research contribution, not to guarantee novelty.

## 10. Reruns and next decisive checks

The gate was rerun after: (i) the Dawson kernel appeared; (ii) the probability/product-density rewrite; (iii) the Bessel infinite-radius simplification, which revealed a collision; and (iv) the Gaussian age shift and taper corollaries. Any future extension to a new friction law, geometry, source kernel or positive-transfer normal form should trigger another formula-level check.

The next decisive external check is review by a specialist in fluid-driven frictional rupture, with explicit attention to the centre-relative kernel order, prior transient-source calculations and the claimed geological significance. That review could change the originality or significance assessment even if the proof is correct.

## 11. Completed historical extensions

The point-source theorem now covers arbitrary later smooth rate reversals and earlier tangential centre-velocity zeros. A strictly positive amount of the causal transfer samples the initially positive centre history; a first-edge-zero contradiction makes radius growth automatic. The finite-Gaussian theorem uses a unit-diagonal kernel through the zero-radius interval and retains a nonnegative latent pressure history before transverse birth. The exact startup conditions are essential. The finite-volume obstruction was also strengthened to arbitrary nonnegative histories for both source types, conditional on prior nucleation, by an elementary decaying-load contradiction. These additions received their own documented formula-level gate and internal proof audit. The original single-peaked result, including its broader piecewise regularity, remains valid and distinct.
