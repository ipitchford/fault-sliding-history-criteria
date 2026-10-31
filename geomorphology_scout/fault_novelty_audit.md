# Bounded novelty audit: fluid-source conditions for crack-like aseismic slip

Search date: 28 October 2026. Audit prepared independently of the main derivation. This is a bounded web/full-text audit, not a priority certificate.

## Frozen candidate and normalisation

The candidate is a criterion for nonnegative slip rate throughout a full-plane, constant-friction, zero-fracture-energy inner problem, under radial linear pressure diffusion and a point source with causal injection-rate history Q. It is NOT a solution of the unrestricted slip-weakening, non-axisymmetric, finite-radius pulse free-boundary problem.

The candidate response kernel is proportional to

`k_r(t) = t^(-1/2) exp[-r^2/(8 alpha t)] I_0[r^2/(8 alpha t)]`.

With Q extended by zero before initiation, the trial slip rate is `v(r,t)=C (k_r*dQ)(t)` for C>0. At r=0 it is proportional to the Riemann–Liouville half derivative of Q (the initial jump must be included). The proposed new statement is the equivalence, over a whole history interval, between nonnegativity at every radius and nonnegativity of the centre history. Candidate consequences include a half-power taper threshold, immediate trial-rate violation after any downward jump, and impossibility of a nonzero finite-total-volume injection remaining globally within the no-relocking cone forever.

Relevant aliases: Abel integral/derivative, Riemann–Liouville half derivative, causal Stieltjes convolution, Riesz potential of the two-dimensional heat kernel, heat Poisson kernel / positive subordination, crack-like versus pulse-like shear rupture, locking-front initiation, transient contact / unloading, monotone displacement under diffusive loading, Basset history kernel, half-line heat Dirichlet-to-Neumann map. Classical fractional calculus and heat-kernel identities must be credited as tools, not claimed as new mathematics.

## Inspected primary corpus

1. Sáez, Passelègue and Lecampion (2025), *Maximum size and magnitude of injection-induced slow slip events*, Science Advances 11, eadq0662, DOI 10.1126/sciadv.adq0662. Full 20-page author PDF inspected: <https://francoispasselegue.github.io/FXP-Webpage/alexis2025.pdf>. Also publicly accessible at <https://pmc.ncbi.nlm.nih.gov/articles/PMC12057678/>. Page 17 explicitly states that necessary and sufficient source conditions for producing a pulse are unknown. Main text gives monotone overpressure as sufficient for crack-like growth and constant source pressure as an example where Q can decrease without creating a pulse. Therefore merely observing that declining Q can preserve crack-like slip is already known.

2. Viesca (2025), *Asymptotic solutions for self-similarly expanding fault slip induced by fluid injection at constant rate*, Journal of Fluid Mechanics 1019, A27, DOI 10.1017/jfm.2025.10593; full accepted preprint <https://arxiv.org/html/2401.13828v3>. Section 3.1, equation (20), gives the leading inner constant-rate slip profile as a combination of exp(-s²/2), I0(s²/2), I1(s²/2) and -4s. Its time derivative at fixed physical radius gives the candidate kernel k_r. The constant-rate kernel and centre coefficient are thus existing results. Equation (21) supplies higher finite-radius corrections. The inspected full text contains no pulse, fractional or arbitrary-injection discussion. Its main scope is constant injection, matched asymptotics and truncation error.

3. Sáez (2023), EPFL thesis 10303, *Three-dimensional fluid-driven frictional ruptures: theory and applications*, DOI 10.5075/epfl-thesis-10303. Full 612,970-character extraction inspected using the public URL <https://infoscience.epfl.ch/server/api/core/bitstreams/93a298b3-3e72-4853-ac41-9f4a324484aa/content>. Relevant sections: 4.4.2–4.4.3 on constant-rate shut-in, and 6.2.5–6.2.6 on arbitrary histories. Section 6.2.5 explicitly retains crack-like propagation as a condition on admissible histories without giving a complete source test. Chapter 4 observes almost immediate centre re-locking after shut-in and studies the subsequent fronts. No Abel/fractional/Dawson occurrences were found in the full extraction. The full text is stored locally as `saez_thesis_full_extract.txt`; mathematical OCR should be checked against PDF images before quoting a formula.

4. Sáez and Lecampion (2023), *Post-injection aseismic slip as a mechanism for the delayed triggering of seismicity*, Proceedings of the Royal Society A 479, 20220810, DOI 10.1098/rspa.2022.0810. Its full content is incorporated in thesis chapter 4. The original publisher/arXiv PDF requests were blocked in the web tool, while chapter 4 was inspected. It establishes pulse propagation/arrest for constant-rate injection followed by abrupt shut-in. This is close physical prior art but does not supply the proposed general source cone.

5. Danré et al. (2024), *Control of Seismicity Migration in Earthquake Swarms by Injected Fluid Volume and Aseismic Crack Propagation*, JGR Solid Earth, DOI 10.1029/2023JB027276. Inspected relevant full-text passages on variable injection and pulse relevance. It relates crack advance to volume and discusses linear/ramped histories. No half-derivative source criterion was located.

## Contemporary coverage

The author's live publication list <https://alexissaezu.github.io/publications/> was inspected. It includes the 2025 target, a 2027-labelled forthcoming numerical solver (DOI 10.1016/j.cma.2026.119348), and four 2026 under-review manuscripts. One concerns runaway ruptures during reservoir operations and one hydraulic-fracturing-induced earthquakes. Their unpublished full contents were not available. These entries cannot be treated as negative evidence. A 2026 SSA abstract by Sáez et al., on spatiotemporal migration patterns, concerns a coupled pressure/slip migration model and does not announce the candidate criterion.

Recent searches also located 2026 papers on rate-and-state nucleation, gouge stability and hydraulic memory. Their titles/abstracts concern different frictional/dynamic models; this limited screening does not exclude an unindexed overlap.

## Query families actually run

- Exact target title and DOI, including recency-constrained searches for 2025–2026 successors.
- `aseismic Abel injection`; `fault half derivative injection slip`; `fluid slip fractional derivative pulse`; `aseismic half-order`.
- `injection slip Dawson`; `aseismic Bessel flow rate`; `fault slip injection Bessel function`; `aseismic I0 injection`; `aseismic Bessel critically stressed`.
- `aseismic slip decreasing injection rate pulse`; `slip pulse variable injection`; `frictional Abel diffusion`; `pressure Abel Coulomb fault`; `fault Riemann-Liouville slip`.
- `aseismic ramp-down`; `fault slip decreasing rate injection`; `fluid-driven pulse variable 2025 2026`; `injection half-order derivative`.
- Exact Viesca 2025 title, arXiv identity and formulas; full-text searches for pulse, fractional, arbitrary injection and Dawson.
- Exact Sáez thesis title and DOI; full-text searches for Abel, fractional, Dawson, arbitrary injection, pulse, Bessel and convolution.

Both configured search engines were used across separate calls. The stronger engine was used for the decisive primary-source and recent-work searches. No author was contacted.

## Adjudication by contribution unit

| Unit | Outcome | Permitted claim |
|---|---|---|
| Constant-rate inner slip and time-derivative kernel | COLLISION | Obtain from / independently rederive the leading inner solution of Viesca (2025). |
| Abrupt complete shut-in produces locking and a pulse | COLLISION | Established by Sáez–Lecampion (2023); may be recovered as a benchmark. |
| Decreasing Q can remain crack-like | COLLISION | Explicitly acknowledged in Sáez et al. (2025). |
| Whole-history all-radius sign criterion via D^(1/2)Q | CLEAR TO PROVE within recorded boundary, with bounded priority uncertainty | No matching statement was found in the inspected fault-slip corpus and formula-level searches. State precise full-plane scope. |
| Downward partial jump criterion / sharp smooth taper threshold | BOUNDED UNCERTAINTY | Candidate consequences of the proposed theorem; no source was found in this search, but the fractional calculus itself is classical. |
| Finite-volume no-relocking obstruction / minimal admissible continuation | BOUNDED UNCERTAINTY | Potentially useful geological consequences; require complete proof and a fresh targeted search once their final formulas are frozen. |
| Finite-radius necessary-and-sufficient source criterion | NOT AUDITED | Exact final statement and formula were not supplied to this auditor. Do not extend full-plane priority status to it. |
| Full unrestricted 2025 open problem | NOT RESOLVED BY THIS CANDIDATE ALONE | Finite-radius moving boundaries, finite source radius, nonzero Poisson ratio and more general friction remain separate issues. |

## Remaining checks and language limits

A failure to find a matching statement does not establish historical priority. The strongest defensible language is that the work resolves the source-admissibility question for a precisely defined limiting model and supplies further finite-radius tests if independently proved. Do not say that all injection-driven pulse dynamics have been solved. Distinguish loss of admissibility of a crack-like trial from existence, shape and propagation of the ensuing physical pulse.

The key mathematical mechanism is a positive heat-kernel/subordination representation. That representation may be classical under another name. The paper should present the novelty as its exact consequence for this geological model and, if supported, new source-design and impossibility theorems.
