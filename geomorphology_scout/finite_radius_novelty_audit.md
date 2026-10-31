# Bounded novelty audit: centre-first locking under unimodal injection

Audit date: 28 October 2026. This report supersedes the finite-radius row marked NOT AUDITED in `fault_novelty_audit.md`. It is an independent, bounded literature audit, not a certificate of historical priority.

## Frozen contribution

The target is the finite circular-fault model in `geology_research/target.yaml`: zero Poisson ratio, spatially constant Coulomb friction, zero fracture energy, constant hydraulic diffusivity, a uniform positive prestress deficit, and a nonnegative injection rate with one increasing stage followed by one decreasing stage. The claim is an exact first-locking test on the fully sliding circular branch. It does not compute the later annular pulse.

For fixed radius R and interior position 0 < r < R, define

`K_R(r,u) = sqrt(4 alpha/u) integral_r^R D(a/sqrt(4 alpha u))/sqrt(a^2-r^2) da`.

The central mathematical assertion is that `K_R(r,u)/K_R(0,u)` is strictly increasing in response age u. Thus, for a signed Stieltjes injection increment dq whose positive part is older than its negative part, nonnegative trial velocity at the centre is equivalent to nonnegative trial velocity throughout the disk. At a nondegenerate zero of the centre velocity, all other interior positions retain positive velocity. Fixed Gaussian source regularisation replaces u by u+epsilon and retains the result.

The exact radius is selected by the zero stress-intensity condition. Its existence is a separate mechanical condition. With a Gaussian source, q(t)>0 does not by itself imply a nonzero disk: the finite centre pressure must exceed the prestress deficit divided by friction. The theorem must be applied after nucleation and on intervals where the full-sliding branch exists.

## Formula-level rewrite checked

The kernel proof in `geology_research/kernel_order_proof.md` was read in full. Its relevant fingerprint is

`S_r = [r^2 + (R^2-r^2) Z^2] (1-T^2)`, with independent uniform Z,T,

and `K_R(r,u) = sqrt(R^2-r^2) E exp[-S_r/(4 alpha u)] / u`.

The centre density is `g_0(s)=arccos(sqrt(s)/R)/(2 R sqrt(s))`, and the off-centre density is an integral proportional to

`integral_max(r^2,s)^(R^2) [sqrt(p-r^2) sqrt(p) sqrt(p-s)]^(-1) dp`.

For each level 0<c<=1, `g_r-c g_0` crosses from negative to positive exactly once. An exponentially tilted first-moment argument proves the transform-ratio monotonicity. The ratio of the densities is not globally increasing; its logarithmic singularity at s=r^2 prevents a direct invocation of monotone likelihood-ratio order. Full radial total positivity is also false, as the supplied short-age expansion proves. These observations help distinguish the actual theorem from a stronger, incorrect generic variation-diminishing assertion.

The proof technique is classical single-crossing/Laplace-transform-ratio machinery. Its application to this kernel, and the resulting exact source test, are the candidate contribution.

## Closest inspected sources and distinctions

1. **Sáez, Passelègue and Lecampion (2025), Science Advances 11 eadq0662**, DOI [10.1126/sciadv.adq0662](https://doi.org/10.1126/sciadv.adq0662). Full [author PDF](https://francoispasselegue.github.io/FXP-Webpage/alexis2025.pdf) and [PMC text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12057678/) inspected. The source-condition gap is explicit in the paragraph following equation 24. Existing results cover arbitrary histories conditional on continued crack-like propagation, and complete shut-in following constant rate. They do not give the unimodal centre-first test. Nonincreasing flow need not create a pulse is already stated there.

2. **Sáez (2023), EPFL thesis 10303**, DOI [10.5075/epfl-thesis-10303](https://doi.org/10.5075/epfl-thesis-10303). Full public extraction inspected, including chapter 4 on shut-in and chapter 6 on arbitrary injection. [Public bitstream](https://infoscience.epfl.ch/server/api/core/bitstreams/93a298b3-3e72-4853-ac41-9f4a324484aa/content). Chapter 4 incorporates Sáez and Lecampion (2023), PRSA 479 20220810, DOI [10.1098/rspa.2022.0810](https://doi.org/10.1098/rspa.2022.0810). Centre locking after complete shut-in, annular pulses, propagation and arrest are already established. No unimodal theorem or Dawson-ratio criterion was located.

3. **Viesca (2025), JFM 1019 A27**, DOI [10.1017/jfm.2025.10593](https://doi.org/10.1017/jfm.2025.10593), [accepted preprint](https://arxiv.org/html/2401.13828v3). Full text inspected. It supplies the constant-rate inner slip profile, whose time derivative is exactly the full-plane Bessel kernel, and higher finite-radius asymptotic corrections. It does not supply the finite-radius signed-history inequality. Constant-rate kernel formulas must be credited as prior art.

4. **Jacquey and Viesca (2023), GRL 50 e2022GL101228**, DOI [10.1029/2022GL101228](https://doi.org/10.1029/2022GL101228), [full author PDF](https://viesca.github.io/articles/JaVi_Arrest_GRL2023.pdf). Full text inspected. It treats a two-dimensional fault with a constant-pressure source followed by shut-in, numerically calculating locking and arrest. Transient schedules are identified as a future extension. No arbitrary unimodal centre-first theorem was located.

5. **Yang and Tian (2019), JMAA**, DOI [10.1016/j.jmaa.2018.10.034](https://doi.org/10.1016/j.jmaa.2018.10.034), [arXiv:1803.02513](https://arxiv.org/abs/1803.02513). The primary abstract and theorem scope were inspected. General ratio-monotonicity rules for Laplace transforms are established prior art. Their existence limits novelty claims about the method, while no result for the target product distribution or Dawson-Abel kernel was retrieved.

6. **Prasath, Vasan and Govindarajan (2019), JFM 868, 428–460**, DOI [10.1017/jfm.2019.194](https://doi.org/10.1017/jfm.2019.194), [arXiv:1808.08769](https://arxiv.org/abs/1808.08769). Primary abstract and author-uploaded full-text passages were inspected. The half-line heat Dirichlet-to-Neumann map is the classical half derivative; this is background for the full-plane corollary, not a new construction here.

7. **Ji et al. (2025), EPSL 669 119579**, DOI [10.1016/j.epsl.2025.119579](https://doi.org/10.1016/j.epsl.2025.119579), [repository PDF](https://gfzpublic.gfz.de/rest/items/item_5037109_2/component/file_5037124/content). Substantial full-text passages inspected. Laboratory experiments and Pohang modelling compare extraction and tapered shut-in, without the present analytical criterion. This paper also cautions against interpreting suppression of pulse formation as a hazard-minimisation result: sustained injection/tapering can maintain slow slip and pressure buildup, while preferable strategies depend on geological setting and poroelastic effects.

The earlier audit covers Danré et al. (2024), the author's publication list, and contemporary abstracts. Additional 2026 screening found Xie et al., DOI 10.1002/dug2.70095 (rate-and-state/poroelastic simulations); Geng et al., DOI 10.1029/2025GL119289 (cyclic injection/extraction experiments); and Minetto et al., DOI 10.1029/2026GL125281 (pressure-decay/trailing-seismicity correlation). Their inspected abstracts/relevant passages show different models and objectives. Their complete contents were not audited.

## Searches after the finite-radius/probability rewrite

Both configured engines were used. Queries included:

- `"penny-shaped" "unimodal" injection locking`
- `"fluid-driven" "locking" "centre" "rate" Saez`
- `"Dawson" "crack" "slip" injection`
- `"Laplace transform ratio" "single crossing"`
- `"penny-shaped" "unloading" "centre" contact`
- `"Dawson" "slip" "locking"`
- `"crack" "slip" "unimodal" injection`
- `"Dawson" "Abel" "ratio"`
- `"Laplace transform ratio" "product" stochastic`
- `"circular crack" "maximum principle"`
- `"penny-shaped crack" "sign" "monotonic"`
- `"axisymmetric" "contact" "single crossing"`
- `"fault" "locking" "unimodal"`
- `aseismic slip "rate reduction" locking`
- `fault injection "ramp-down" pulse`
- `"injection" "necessary and sufficient" "pulse"`
- `aseismic fluid injection tapered shut-in centre locking pulse 2026`
- `"aseismic" "unimodal"`
- `"aseismic" "ramp-down"`
- `"2F2" "1/2" "3/2" "Dawson" monotonicity ratio`
- `"arccos" "Laplace" "ratio" "density"`
- `"beta" "shifted" "Laplace transform ratio"`

Searches for current successors used recency constraints where appropriate. No person was contacted. No matching theorem was found in the inspected primary corpus, but incomplete indexing, unpublished work and alternate notations remain residual uncertainty. Some highly specific searches returned unrelated material; that is weak negative evidence, not proof of absence.

## Adjudication

| Contribution unit | Status in this bounded audit | Appropriate description |
|---|---|---|
| Abel circular-crack inversion, diffusion convolution, classical single-crossing method | Established machinery | Cite and use, without novelty claims. |
| Constant-rate infinite-radius Bessel kernel | COLLISION | Existing as derivative of Viesca (2025) inner profile. |
| Complete shut-in yields centre locking and an expanding locked region | COLLISION | Established in 2023 work. |
| Exact finite-radius kernel age-ratio inequality relative to the centre | CLEAR TO PROVE within recorded boundary; bounded priority uncertainty | Candidate new special-kernel inequality. |
| One centre test characterises nonnegative velocity for every unimodal rate history | CLEAR TO PROVE within recorded boundary; bounded priority uncertainty | Candidate original source-admissibility theorem in the specified model. |
| Fixed Gaussian source version and finite partial-step threshold | No collision located; bounded uncertainty | Useful exact extension showing the result is not just a point-source singularity. |
| First physical locking follows the scalar test | Requires mechanical validation | Kernel proof alone cannot replace branch existence, exterior yield and moving-boundary checks. |
| Full arbitrary-history/noncircular/rate-and-state open problem | Not resolved | State the unimodal circular constant-friction scope prominently. |

## Assessment note

Quality assessment is outside the scope of this literature record.
