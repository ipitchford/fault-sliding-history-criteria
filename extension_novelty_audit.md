# Targeted novelty gate: arbitrary-history transfer for finite circular faults

**Audit date:** 28 October 2026.  
**Status:** updated after completion and internal checking of the centre-only historical point-source extension and the conditional Gaussian extension through monotone-pressure, transverse nucleation; manuscript integration follows. This note does not itself amend the manuscript or its academic review.  
**Auditor:** geomorphology/literature subagent.  
**Scope:** prior art and object identity, not certification of the proof.

## 1. Gate decision

**Proceed with the elastic-kernel application, but do not claim the general positivity mechanism as new.** An exact discrete counterpart of the proposed convolution argument is Jurkat's 1954 quotient-sign criterion. Positive resolvents, log-convex Volterra kernels, first-kind inverse kernels, and their nonconvolution generalizations are established subjects. The searches below did not locate a published finite-radius fault theorem equating an all-past centre test with nonnegative slip everywhere under arbitrary injection histories. That is a bounded search result, not proof of originality.

The potentially distinctive contribution is the combination of the exact circular elastic kernel, its age-ratio order, its centre-kernel properties, and a mechanically admissible moving-radius consequence. At the initial gate, nucleation at radius zero and the point-source limit were unresolved. **The team has now completed and independently checked the point-source argument**, recorded in `arbitrary_history_extension.md` and frozen in `target_arbitrary_history.yaml`:

- Let \(q\in C^1([0,T])\) be nonnegative, and assume either \(q(0)=q_0>0\), or \(q(0)=0\) with \(q\) nondecreasing and immediately positive on an initial interval. Assume the unique positive point-source trial radius exists on \((0,T]\). Then nonnegative velocity everywhere throughout the history is equivalent to **nonnegative centre velocity throughout that same elapsed history**. No restriction is imposed on the number of later source-rate reversals.
- Whenever this historical condition holds, every noncentral interior velocity and the edge-normalised velocity is strictly positive, and \(R'(t)>0\). Radius monotonicity is a conclusion, not a separate test. Earlier tangential centre zeros are covered by the final strict-transfer argument.
- In particular, the first threshold contact is central, and a first loss of forward-slip admissibility is detected by the first negative centre value. This does not make a current nonnegative centre value sufficient after an earlier negative centre interval.
- The age-shift limit and both startup classes are covered. Zero-start point-source histories with arbitrarily early reversals that violate the stated startup assumption remain outside the result.
- A final conditional Gaussian extension has also passed the team's independent audit: if centre pressure is nondecreasing before first nucleation and the crossing is transverse, the whole post-nucleation centre history is sufficient for arbitrary subsequent smooth nonnegative rate histories. Section 11 records its exact normalization and scope. General nonmonotone pre-nucleation centre pressure and tangential nucleation remain unresolved. The original instantaneous Gaussian test remains restricted to single-peaked rates.

This is proof-status information supplied by the root and independent proof auditor, with the exact point-source statement and Sections 5–6 checked against the supplement; this literature audit does not substitute for their mathematical review. The Gaussian theorem and its exact frozen target were also inspected, as recorded in Section 11. A separate finite-volume corollary, valid for both source types without unimodality, is assessed in Section 9 below. The final centre-only strengthening received the bounded follow-up gate in Section 10.

## 2. Formula-first target and identity map

Let the existing manuscript's kernel be

\[
K_R(r,u)=\int_r^R\frac{a}{\sqrt{a^2-r^2}}
\frac{D(a/\sqrt{4\alpha u})}{u\,a/\sqrt{4\alpha u}}\,da,
\qquad 0\le r<R,\quad u>0,
\]

where \(D(z)=e^{-z^2}\int_0^z e^{x^2}\,dx\). The established finite-radius manuscript result is that \(K_R(r,u)/K_R(0,u)\) increases with age \(u\), yielding an instantaneous centre test for unimodal source histories.

The extension uses

\[
K_R(0,u)=2\alpha\int_0^\infty e^{-\alpha u k^2}\operatorname{Si}(kR)\,dk
\]

to obtain complete monotonicity and log-convexity in \(u\). A further auxiliary claim is that

\[
\frac{D(z)}{G(z)}\quad\text{strictly decreases},\qquad
G(z)=\int_0^z\frac{D(x)}x\,dx,
\]

which implies the required radius order for \(\partial_u\log K_R(0,u)\). These were proposed ingredients at the initial gate and have since been proved in the internally checked supplement; proof review remains separate from this literature audit.

The abstract target is the positive factorization

\[
b(t,s)=c(t)a(t,s)+\int_s^t h(t,v)a(v,s)\,dv,\qquad h\ge0,
\quad c(t)=b(t,t)/a(t,t),
\]

under positivity and appropriate regularity of triangular kernels, with

\[
F(t,s)=b(t,s)/a(t,s),\qquad
\ell(t,s)=-\partial_s\log a(t,s),
\]

\(-\partial_sF\ge0\), \(\ell(t,s)\ge\ell(v,s)\) for \(s\le v\le t\), and \(a(s,s)>0\). Differentiation produces a backward Volterra equation with nonnegative inhomogeneity and kernel. For fixed radius this gives the following convolution rule, which was the initial conjecture screened by the gate:

> Positive log-convex \(a\), together with nondecreasing \(b/a\), gives nonnegative causal deconvolution of \(b\) by \(a\), including a possible atom at time zero.

The regularised fault-kernel application sets

\[
a(t,s)=K_{R(t)}(0,t-s+\varepsilon),\qquad
b(t,s)=K_{R(t)}(r,t-s+\varepsilon),
\]

with \(\varepsilon>0\) and \(R(t)>0\) nondecreasing. The output consequence concerns the **entire past centre trace**, not merely the current centre value. This distinction avoids collision with the existing multistage instantaneous-test counterexample.

## 3. Decisive published-method collision

### Jurkat's quotient-sign criterion

**W. B. Jurkat (1954), “Questions of signs in power series,” Proceedings of the American Mathematical Society 5(6), 964–970.**

- AMS DOI: <https://doi.org/10.1090/S0002-9939-1954-0064890-9>.
- JSTOR DOI: <https://doi.org/10.2307/2032565>.
- Original AMS PDF was attempted and returned 403; its original theorem was therefore **not directly inspected**.
- Its precise relevant statement and attribution were directly inspected in the later primary paper below.

**Á. Baricz, J. Vesti and M. Vuorinen (2011), “On Kaluza's sign criterion for reciprocal power series,” Annales Universitatis Mariae Curie-Skłodowska, Sectio A 65(2), 1–16.**

- Publisher record: <https://journals.umcs.pl/a/article/view/3944>.
- Full publisher PDF: <https://journals.umcs.pl/a/article/download/3944/2853>.
- Current publisher DOI: <https://doi.org/10.17951/a.2011.65.2.1-16>.
- The older DOI printed with the publication is 10.2478/v10062-011-0009-2. The publisher page's 2016 upload metadata does not replace the 2011 journal year.
- **Inspected passage:** Theorem 4.4 on printed p. 14 (PDF page 14), together with the immediately preceding explicit attribution to Jurkat and bibliography entry [14]. Theorem 4.1 on p. 13 distinguishes ordinary quotient monotonicity from coefficient positivity. The discussion on pp. 11–12 reports a correction to a different Jurkat statement; it does not invalidate Theorem 4.4.

In mathematical paraphrase, if

\[
f(z)=\sum_{n\ge0}a_nz^n,\qquad
g(z)=\sum_{n\ge0}b_nz^n,
\]

\(b_n>0\), the sequence \(b_n\) is log-convex, and \(a_n/b_n\) is nondecreasing, then every nonconstant coefficient of \(f/g\) is nonnegative. Reversing the ratio monotonicity reverses those coefficient signs. This is the **exact discrete structural analogue** of the proposed fixed-radius transfer.

**Consequence for positioning:** “We discover that log-convex kernels and increasing ratios give positive deconvolution” would overclaim. A suitable description is an elementary continuous Volterra comparison argument, related to the classical Kaluza–Jurkat sign criteria. The audit has not established that Jurkat's original paper explicitly states the continuous or moving-radius version. It should not be cited as though it does.

## 4. Continuous and nonconvolution literature: precise relevance and access limits

| Source | Passage or material actually inspected | Relevance and limit |
|---|---|---|
| **R. K. Miller (1968), “On Volterra integral equations with nonnegative integrable resolvents,” J. Math. Anal. Appl. 22(2), 319–340**, DOI [10.1016/0022-247X(68)90176-5](https://doi.org/10.1016/0022-247X(68)90176-5) | Bibliographic identity checked; relevant theorem read through the explicit attribution in Feng–Li Lemma 2.1, below. Original full text not inspected. | Classical positive-resolvent result for nonnegative, nonincreasing, log-convex kernels. Supports method attribution; not an inspected statement of the exact two-kernel transfer theorem. |
| **G. Gripenberg (1978), “On positive, nonincreasing resolvents of Volterra equations,” J. Differential Equations 30(3), 380–390**, DOI [10.1016/0022-0396(78)90007-4](https://doi.org/10.1016/0022-0396(78)90007-4) | Introduction and Theorems 1–3 in an indexed full-text mirror: <https://paperzz.com/doc/7314003/on-positive--nonincreasing-resolvents-of-volterra>. Bibliographic identity independently checked. | Resolvent \(r+a*r=a\); log-convexity appears as monotonicity of \(a(t)/a(t+T)\). Classical positivity and monotonicity. The mirror is an access aid, not preferred final citation or verification of the original typesetting. |
| **Ph. Clément and J. A. Nohel (1979), “Abstract linear and nonlinear Volterra equations preserving positivity,” SIAM J. Math. Anal. 10(2), 365–388**, DOI [10.1137/0510035](https://doi.org/10.1137/0510035) | Publisher abstract: <https://epubs.siam.org/doi/abs/10.1137/0510035>. | Established positive-solution theory and representation formulas for \(u+a*Au=f\). Abstract alone does not identify an exact collision with the proposed two-kernel factorization. |
| **Ph. Clément and J. A. Nohel (1981), “Asymptotic behavior of solutions of nonlinear Volterra equations with completely positive kernels,” SIAM J. Math. Anal. 12(4), 514–535**, DOI [10.1137/0512045](https://doi.org/10.1137/0512045) | Publisher abstract and metadata: <https://epubs.siam.org/doi/abs/10.1137/0512045>. Theorem 2.2 characterization inspected through the precise reproduction in Feng–Li Lemma 2.2. Original proof not read. | Complete positivity is characterized by a nonnegative, nonincreasing complementary kernel: \(a*(\gamma\delta+c)=1\). This demonstrates that positive first-kind inverse structures are classical, though it is not the exact quotient-ratio claim. |
| **G. Gripenberg (1980), “On the resolvents of nonconvolution Volterra kernels,” Funkcialaj Ekvacioj 23(1), 83–95** | Primary repository OCR PDF, opening pages and Theorems 1–5: <https://da.lib.kobe-u.ac.jp/da/kernel/0100499330/0100499330%20in%20infty%20PDF.pdf>. Repository DOI [10.24546/0100499330](https://doi.org/10.24546/0100499330). | Nonconvolution resolvent existence, regularity, perturbation and integrability machinery. No exact ratio-factorization theorem was identified in the portions inspected. Do not call this a decisive collision. |
| **G. Gripenberg (1980), “On Volterra equations of the first kind,” Integral Equations and Operator Theory 3(4), 473–488**, DOI [10.1007/BF01702311](https://doi.org/10.1007/BF01702311) | Primary publisher abstract and references: <https://link.springer.com/article/10.1007/BF01702311>. | Explicitly studies \(\int_0^t a(t-s)d\beta(s)=1\), regularity of the inverse measure, and a nonconvolution extension. Full text is subscription-only in inspected source. Volume is **3**, despite a secondary bibliography displaying 4. |
| **G. Gripenberg (1982), “Volterra integral operators and logarithmic convexity,” Math. Scand. 50, 209–220**, DOI [10.7146/math.scand.a-11955](https://doi.org/10.7146/math.scand.a-11955) | Indexed primary PDF extracts of the introduction and final proof/reference page. URL <https://www.mscand.dk/article/download/11955/9971/30910> returned 404 when directly opened. | Establishes links between log-convexity and accretivity of inverse Volterra operators, also discussing weighted/nonlinear operators. Strong background collision for any broad novelty claim; exact full theorem not inspected. |
| **G. Gripenberg, S.-O. Londen and O. Staffans (1990), Volterra Integral and Functional Equations**, DOI [10.1017/CBO9780511662805](https://doi.org/10.1017/CBO9780511662805) | Chapter 1 overview/preview and Chapter 20 publisher listing. Preview <https://api.pageplace.de/preview/DT0400.9780511831041_A24404801/preview-9780511831041_A24404801.pdf>. | Overview identifies nonconvolution log-convexity through \(k(v,s)k(t,u)\le k(t,s)k(v,u)\) for \(s\le u\le v\le t\). Full Chapter 20 was not read. Treat as framework, not as a verified theorem identical to the proposed factorization. |
| **Y. Feng and L. Li, “A class of monotonicity-preserving variable-step discretizations for Volterra integral equations,” BIT Numerical Mathematics 64 (2024), article 24**, DOI [10.1007/s10543-024-01027-8](https://doi.org/10.1007/s10543-024-01027-8). The inspected arXiv:2304.06293v4 preprint has the longer title ending “and time fractional ordinary differential equations.” | Primary full preprint: <https://arxiv.org/pdf/2304.06293>. Section 2.1, Lemmas 2.1–2.2, Theorems 2.1–2.2; Section 2.2; Sections 3–4 definitions and initial lemmas. Also inspected publisher metadata, abstract and exposed Appendices A–B: <https://link.springer.com/article/10.1007/s10543-024-01027-8>. Publication date 14 June 2024. | Especially useful accessible source. Preprint Lemma 2.1 credits Miller's log-convexity criterion; Lemma 2.2 credits Clément–Nohel's complementary-kernel characterization. Develops nonuniform discrete triangular-kernel positivity. It does not give the fault kernel or the proposed all-past centre criterion. The main published text was not accessible; lemma numbering here refers to the inspected preprint. |
| **Y. Feng, L. Li, J.-G. Liu and T. Tang (2024), “Some Grönwall inequalities for a class of discretizations of time fractional equations on nonuniform meshes,” SIAM J. Numer. Anal. 62(5), 2196–2221**, DOI [10.1137/24M1631614](https://doi.org/10.1137/24M1631614) | Primary author PDF: <https://sites.math.duke.edu/~jliu/pdf/FLLT_24.pdf>. Introduction pp. 2196–2198, log-convexity discussion near p. 2208, references. | Contemporary evidence that complete monotonicity, log-convexity, resolvent positivity and discrete comparison are established machinery. No geology criterion. |

### Contemporary comparison result screened

**T. M. Baldé, V. Milisic and S. Plunder (2026), “A new comparison principle for discrete Volterra equations with an application to convex sweeping processes with infinite delays,” arXiv:2603.20089v1 (20 March 2026).**

- Abstract: <https://arxiv.org/abs/2603.20089>.
- Full primary PDF: <https://arxiv.org/pdf/2603.20089>.
- Inspected the abstract, assumptions and principal continuous/discrete comparison statements in Section 2.1, and searched the full extract for log-convexity terminology.
- Its displayed equation involves a nonnegative unit memory density and differences \(z(t)-z(t-a)\); its focus is bounds uniform in the discretization step and delayed sweeping processes.
- No exact two-kernel quotient or fault-criterion collision was found in those inspected passages. This is not a claim to have checked every argument in the 34-page paper.

## 5. Exact special-function auxiliary: bounded check

The desired \(D/G\) monotonicity is not the standard assertion that \(D(\sqrt{x})/\sqrt{x}\) is completely monotone. Nor is the proposed sine-integral spectral representation itself the age-ratio order for off-centre points. These identities should remain distinct in the manuscript.

The following primary item was inspected as a plausible Dawson-function predecessor:

**A. J. E. M. Janssen (2021), “Bounds on Dawson's integral occurring in the analysis of a line distribution network for electric vehicles,” Eurandom Preprint Series 2021-014, 14 December 2021.**

- Primary PDF: <https://www.eurandom.tue.nl/wp-content/uploads/2021/12/014-report.pdf>.
- Located through the DLMF bibliography: <https://dlmf.nist.gov/bib/J> and inequalities page <https://dlmf.nist.gov/7.8>.
- Inspected abstract, setup, basic-property section, principal bound statements and ratio discussion; searched the extract for ratio/monotonicity and relevant integral notation.
- The inspected results concern explicit bounds for \(D\), \(e^{z^2}D(z)\), and associated ratios, including a ratio with \(\sqrt{1-e^{-2z^2}}\). No \(D(z)/\int_0^zD(x)/x\,dx\) theorem was located.

A 2026 paper on integral representations of normalized exponential remainders also surfaced, with the standard positive-integral representation of \(D(\sqrt{x})/\sqrt{x}\). It was only screened in primary-source search extracts and is not used as evidence of an exact auxiliary collision. The exact \(D/G\) inequality has not been historically cleared; given the short self-contained proof reported by the team, it should be presented as a supporting lemma without a separate historical novelty claim.

## 6. Geological claim screen

The previous files `literature_audit.md` and `geomorphology_scout/finite_radius_novelty_audit.md` remain the main geological source comparison. The extension does not change the following attribution constraints:

- Sáez, Passelègue and Lecampion (2025), DOI [10.1126/sciadv.adq0662](https://doi.org/10.1126/sciadv.adq0662), explicitly identify unknown source conditions for pulse formation after equation (24), p. 17. Their arbitrary-history formulas remain conditional on crack-like evolution. Primary PDF: <https://francoispasselegue.github.io/FXP-Webpage/alexis2025.pdf>.
- Viesca (2025), DOI [10.1017/jfm.2025.10593](https://doi.org/10.1017/jfm.2025.10593), supplies the constant-rate inner slip profile whose derivative gives the full-plane kernel already used in the manuscript. Primary full text: <https://arxiv.org/html/2401.13828v3>. The extension must not reclassify this kernel as a new discovery.
- Sáez–Lecampion (2023), DOI [10.1098/rspa.2022.0810](https://doi.org/10.1098/rspa.2022.0810), and Jacquey–Viesca (2023), DOI [10.1029/2022GL101228](https://doi.org/10.1029/2022GL101228), already analyse locking/pulses after shut-in in specified protocols. Their source descriptions in the existing audit remain applicable.
- The 2026 experimental successor *Propagation of fluid-driven aseismic slip fronts under upper crustal conditions*, DOI [10.1126/sciadv.aeb0234](https://doi.org/10.1126/sciadv.aeb0234), was re-encountered in the extension search. Primary page: <https://pmc.ncbi.nlm.nih.gov/articles/PMC13344294/>. The previously inspected main text concerns experimental propagation under constant pressure-rate loading, not the arbitrary-history centre test; full-document absence was not established because some follow-up retrieval encountered an access challenge.

Targeted searches using all-past/centre-history, Volterra, Dawson, and locking terminology returned no exact finite-radius transfer or all-past centre criterion. That negative evidence is modest: terminology may differ, unpublished manuscripts cannot be excluded, and abstracts alone do not clear a full paper.

## 7. Exact reproducible query log

These are the literal targeted queries issued in the continued extension audit. Broad historical searches performed in earlier passes are described in the existing audit files rather than reconstructed here. Searches used two engines; the stronger engine was used to verify sparse routine-engine results and to screen recent literature. This is a query log, not a claim that every hit was read.

### Abstract transfer and quotient signs

```text
Jurkat "Questions of signs in power series" 1954 pdf
"Volterra" "log-convex" "quotient" positive
"convolution" "log convex" "b(t)/a(t)"
"positive deconvolution" "log" convex
"Volterra" "logarithmic convexity" "positive" Gripenberg
"Jurkat" "Volterra"
"log-convex" "deconvolution" kernel
"Volterra" "ratio" "logarithmically convex" positive solution
"Volterra" "f(t)/a(t)" nonnegative
"Miller" "log" "resolvent" Volterra 1971
"Jurkat" "integral" signs convolution
"On Volterra equations of the first kind" Gripenberg 1980 pdf
"Volterra" "b/a" "convex"
"Volterra" "ratio" "nonnegative" "log-convex" kernel
"Questions of signs in power series" pdf Jurkat -site:researchgate.net
"Kaluza" "Laplace" "ratio"
"Jurkat" "Laplace transform"
"log-convex" "Volterra" "ratio" positivity
"Volterra" "f/a" "positive"
"Volterra" "ratio" "log convex" -functions -function -density
"nonconvolution" "logconvex"
"On Volterra integral equations with nonnegative integrable resolvents" DOI
"Asymptotic behavior of solutions of nonlinear Volterra equations with completely positive kernels" DOI
"A class of monotonicity-preserving variable-step discretizations" "10.1007"
```

### Geological identity screen

```text
fault slip "centre" "arbitrary" "history" injection
"aseismic" "Volterra" "locking"
"fluid" "slip" "Dawson" "criterion"
```

The first query used a 730-day recency filter, followed by source inspection and the prior audit's broader source set.

### Dawson auxiliary and transform aliases

```text
"Dawson" "integral" "log-convex" monotonicity
"Dawson" "integral" "ratio" "monotonicity" integrated
Dawson integral monotonicity ratio integral G(x)
"Dawson" "geometrically" convex
"Dawson" "completely monotonic" integral
"Janssen" "2021" "Dawson" integral
"Dawson" "integral" "sine integral" log convexity
"Dawson" "integral of" "quotient" monotonic
"Dawson" "F(t)/t" monotonicity
"Dawson" "D(t)/t" monotonicity
```

Several formula-heavy routine-engine queries returned irrelevant results. Those were not counted as substantive clearance; the follow-up stronger-engine search and primary-source reads above carry the assessment.

## 8. Recommended wording and next gate

Following the completed internal proof review, suitable positioning is:

> We use an elementary positive Volterra factorization, related to classical quotient-sign and resolvent-positivity results, to transfer the entire centre history to the slip rate at other radii. The main model-specific steps are the required order properties of the exact circular elastic kernel and their compatibility with the evolving radius.

Avoid claiming a new general positivity theory, complete solution of pulse dynamics, a global instantaneous centre criterion for arbitrary histories, or operational seismic-safety optimisation. The final point-source theorem goes beyond a prescribed positive-radius transfer lemma: it proves radius growth from the whole centre history. It retains the smooth-history, positive-radius and startup assumptions specified in Section 1. The Gaussian historical extension requires its separate pressure-startup and transverse-nucleation conditions in Section 11.

**Final-statement gate:** the exact statement in `target_arbitrary_history.yaml` was inspected after the final strict-transfer proof. The bounded search supports presenting the **centre-only historical point-source theorem**, its automatic radius growth, and the first-centre-threshold consequence as the contribution under consideration, while retaining the classical-method credits above. It does not warrant an unqualified historical-priority claim or a claim to solve subsequent pulse evolution.

## 9. Final structural simplification: finite-volume obstruction

### Exact claim and direct-corollary status

Section 7.1, equation (E20), of `arbitrary_history_extension.md` establishes the following internally checked statement. If a nonnegative integrable rate \(q\in L^1(0,\infty)\) has nucleated a regular fully sliding branch, that branch cannot remain fully sliding for all future time. This applies to the point source and to the Gaussian source, with no unimodality assumption. The Gaussian assertion is conditional on nucleation; a small injection may never initiate slip.

The proof uses only model properties already available before the abstract positive-transfer extension. Continued nonnegative velocity forces a nondecreasing radius through the edge identity. For a fixed \(R_0>0\) below a radius already reached,

\[
\mathcal A p_\varepsilon(R_0,t)
=c_p\int_0^t q(s)J_{R_0}(t-s+\varepsilon)\,ds,
\qquad
J_R(u)=\frac{D(z)}{u z},\quad z=\frac{R}{2\sqrt{\alpha u}}.
\]

Here \(0\le J_{R_0}(u)\le4\alpha/R_0^2\), and \(J_{R_0}(u)\to0\) as \(u\to\infty\). For \(\varepsilon=0\), its finite zero-age limit may be assigned. Dominated convergence against \(q(s)ds\), using the indicator \(s\le t\), gives \(\mathcal A p_\varepsilon(R_0,t)\to0\). Since the pressure average decreases with radius,

\[
0<\frac{\Delta}{f}
=\mathcal A p_\varepsilon(R(t),t)
\le\mathcal A p_\varepsilon(R_0,t)\longrightarrow0,
\]

a contradiction.

**Attribution judgment:** the analytic mechanism is a classical bounded-decaying-kernel convolution limit combined with monotone support and the known zero-stress-intensity equilibrium. The theorem should be labelled an **elementary direct corollary of this model**, with a broader rate-history scope than the finite-protocol examples below. It is not an additional major mathematical novelty and does not depend on claiming a new Volterra theorem. The conclusion is failure of the fully sliding class at some finite time; it does not establish the later pulse geometry, complete fault arrest, cessation of every later reactivation, or any seismic-hazard outcome.

### Closest direct geological precedents inspected

| Source | Inspected passage and relation to this corollary |
|---|---|
| **Sáez and Lecampion (2023), “Post-injection aseismic slip as a mechanism for the delayed triggering of seismicity,” Proceedings of the Royal Society A 479, 20220810**, DOI [10.1098/rspa.2022.0810](https://doi.org/10.1098/rspa.2022.0810) | Already inspected through the author's thesis Chapter 4 in the original audit; the article abstract was rechecked in the bounded follow-up. Constant-rate injection followed by shut-in produces pulses and eventual arrest in their model. This establishes the basic finite-protocol phenomenon, not the displayed arbitrary nonnegative integrable-history proof. Primary author publication record: <https://alexissaezu.github.io/publications/>. Direct arXiv PDF retrieval in this follow-up failed because the file exceeded the tool's size limit; no new full-text inspection is claimed. |
| **Jacquey and Viesca (2023), “Nucleation and arrest of fluid-induced aseismic slip,” Geophysical Research Letters 50, e2022GL101228**, DOI [10.1029/2022GL101228](https://doi.org/10.1029/2022GL101228) | Primary author PDF <https://viesca.github.io/articles/JaVi_Arrest_GRL2023.pdf>, pp. 2–4, equations (1)–(5) and post-injection discussion. A constant-pressure source is deactivated after a finite pressurization phase; pressure redistribution and locking fronts lead to arrest. Different one-dimensional geometry and injection protocol, with transient schedules identified as an extension. Supports credit for known shut-in locking, not an exact collision with arbitrary \(L^1\) source histories in the circular model. |
| **Sáez, Passelègue and Lecampion (2025), “Maximum size and magnitude of injection-induced slow slip events,” Science Advances 11, eadq0662**, DOI [10.1126/sciadv.adq0662](https://doi.org/10.1126/sciadv.adq0662) | Re-inspected full primary PDF <https://francoispasselegue.github.io/FXP-Webpage/alexis2025.pdf>, pp. 7–9 and 17–18: finite-operation volume bounds, post-shut-in pulse/arrest, equations (23)–(28), and the explicit crack-like-history restriction after equation (24). Their finite-volume maximum-size results and specified shut-in treatment are prior art. The exact arbitrary-integrable-rate obstruction was not located in these passages. A maximum-size bound by itself does not imply the present failure-of-full-sliding statement; that inference uses decaying local pressure and irreversible support. |
| **D. I. Garagash (2021), “Fracture mechanics of rate-and-state faults and fluid injection induced slip,” Philosophical Transactions of the Royal Society A 379(2196), 20200129**, DOI [10.1098/rsta.2020.0129](https://doi.org/10.1098/rsta.2020.0129) | Primary author-preprint abstract screened at <https://eartharxiv.org/repository/view/106/> and publication identity/abstract verified at <https://pubmed.ncbi.nlm.nih.gov/33715418/>. Studies one-dimensional rate-and-state fracture approximations and a finite-volume/stopped-injection run-out result. Full text was not inspected in this follow-up; a direct EarthArXiv open returned a robot-check page after search supplied the abstract. This is established finite-volume context, not evidence of an exact circular constant-friction corollary. |
| **Danré et al. (2024), “Control of seismicity migration in earthquake swarms by injected fluid volume and aseismic crack propagation,” Journal of Geophysical Research: Solid Earth 129, e2023JB027276**, DOI [10.1029/2023JB027276](https://doi.org/10.1029/2023JB027276) | Primary publisher discussion of post-injection limitations and Appendix A: <https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2023JB027276>. Explicitly links finite-volume injection in two dimensions to Garagash (2021), and distinguishes its positive-flow-rate crack approximation from post-injection pulses. It helps identify the prior finite-volume literature, without yielding the exact arbitrary-history result here. |

No direct prior statement of the exact both-source, arbitrary nonnegative integrable-history obstruction was found in this small follow-up. This supports calling it a useful extension/direct corollary, not a first-ever finite-volume locking theorem. Broad searching was deliberately not reopened.

### Exact follow-up queries

```text
"aseismic slip" "finite volume" arrest
"fluid" "slip" "finite total" injection arrest
"Sáez" "Lecampion" "volume" "arrest" 2025
"Garagash" "2021" "finite volume" slip
Garagash 2021 "fault" "finite" "injection"
"Fracture mechanics of rate-and-state faults and fluid injection induced slip" pdf
"Garagash" "finite volume injection"
```

One bibliographic follow-up was also run, without reopening the abstract-method gate:

```text
"A class of monotonicity-preserving variable-step discretizations" BIT 64 24 DOI
```

## 10. Final gate: centre history alone, including tangential zeros

### Structural change and object identity

The last proof simplification removes the separate radius-monotonicity hypothesis from the physical point-source conclusion. Sections 5–6 of the revised supplement and the exact target file were inspected. Along an auxiliary nondecreasing radius path, the ratio

\[
\frac{A_\varepsilon(v,s)}{A_\varepsilon(v,d)},\qquad s<d\le v,
\]

is nondecreasing in \(v\), because its logarithm is an integral of the already ordered log-slope. Subtracting two positive-transfer identities therefore supplies a strictly positive lower bound on the transfer mass sampling an initial positive centre interval. The bound survives \(\varepsilon\downarrow0\). This gives strict noncentral and edge positivity even when the centre has touched zero earlier; a first-edge-zero contradiction then makes the actual radius strictly increasing.

This is an elementary strengthening within the same kernel-order and Volterra framework, not a new abstract method or a new mathematical object requiring a fresh broad literature search. The source history remains arbitrary only within the stated smoothness, nonnegativity and startup assumptions. The criterion is a historical source test computable through the pressure-radius relation and centre integral, rather than a pointwise inequality in the current injection rate.

### Narrow source check and attribution judgment

The follow-up used the exact all-history/centre/Volterra aliases below. It found no direct published statement of the final circular point-source criterion. The originating 2025 paper's qualification and open question were re-inspected in the primary author PDF, p. 17 after equation (24): <https://francoispasselegue.github.io/FXP-Webpage/alexis2025.pdf>. Its indexed PMC copy also returned the relevant passage; a later `find` request encountered a browser challenge, so the PDF supplies the reliable inspection record.

The classical strong-positivity mechanism should also be credited. Feng–Li's published Appendix A, equation (A.1) and proof of Theorem 2.1, explicitly uses positive initial history and a first-zero contradiction; that passage was re-inspected at <https://link.springer.com/article/10.1007/s10543-024-01027-8>. It does not contain this fault-kernel criterion or its early-transfer estimate. Jurkat/Kaluza and the continuous-resolvent references in Sections 3–4 remain the methodological comparison.

One recent primary hit was rechecked to resolve a possible terminology collision: **Qifeng Xie, Lei Wang and Qi Li (2026), “Fluid-induced slip on a rate-and-state fault during co- and post-injection: The interplay of fluid pressure diffusion and poroelastic stress,” Deep Underground Science and Engineering**, first published 1 July 2026, DOI [10.1002/dug2.70095](https://doi.org/10.1002/dug2.70095). The publisher's limitations and Section 6 conclusions were inspected at <https://onlinelibrary.wiley.com/doi/full/10.1002/dug2.70095>. Its single-degree-of-freedom spring-slider formulation has no spatial slip profile or evolving crack radius, so it cannot state the present centre-to-edge equivalence. No absence claim for all of its supporting material is made.

**Gate outcome:** no exact predecessor was identified in this deliberately bounded final check. Preserve the prospective contribution as the exact historical criterion and automatic radius growth for this circular constant-friction model. Present strict transfer as the argument that completes the application, while explicitly recognizing classical inverse-positivity and first-zero methods. Do not upgrade this negative search result into proof of priority, and do not extend the conclusion across arbitrary Gaussian pre-nucleation or into post-locking pulse dynamics.

### Exact final follow-up queries

```text
"aseismic slip" "arbitrary" "centre" criterion
"fluid injection" "slip" "history" "necessary and sufficient"
"fault" "slip" "center" "Volterra"
"fluid" "slip" "centre" "locking" "arbitrary"
"fluid-induced" "slip" "central" "criterion"
"aseismic slip" "centre" "history"
"fluid injection" "slip" "arbitrary histories"
"aseismic" "crack" "positive" "Volterra"
```

The first two queries used a 730-day recency filter; the remaining aliases were unrestricted. Results outside the fault/source problem were not counted as evidence of novelty. This final gate adds no new broad research programme and leaves the previously recorded access limitations intact.

## 11. Conditional Gaussian extension: normalization through first nucleation

### Exact formula and remaining startup restriction

The independent proof auditor reports that a fixed physical Gaussian source with age shift \(\varepsilon>0\) also admits a historical centre criterion in the following startup class. Let the nonnegative injection rate be \(C^1\), let \(t_n\) be the first crossing of \(p_\varepsilon(0,t)=\Delta/f\), and require

\[
\partial_t p_\varepsilon(0,t)\ge0\quad (0\le t\le t_n),
\qquad \partial_t p_\varepsilon(0,t_n)>0.
\]

Set \(R(v)=0\) before birth and use the positive trial radius afterwards, on an interval where that radius exists. The same triangular kernel is normalized by its diagonal:

\[
a(v,s)=\frac{K_{R(v)}(0,v-s+\varepsilon)}{K_{R(v)}(0,\varepsilon)},
\qquad
a(v,s)\big|_{R(v)=0}=\frac{\varepsilon}{v-s+\varepsilon}.
\]

The latter expression is the continuous small-radius limit, not a new source model. It has unit diagonal even during pre-nucleation. Its input trace is

\[
H(v)=\int_{[0,v]}a(v,s)\,dq(s)
=\begin{cases}
\varepsilon\,\partial_t p_\varepsilon(0,v)/c_p,&v\le t_n,\\
C_\varepsilon(v)/K_{R(v)}(0,\varepsilon),&v>t_n.
\end{cases}
\]

Here \(C_\varepsilon\) denotes the centre response with the manuscript's positive physical multiplier omitted. The prebirth quantity \(H\) is a mathematical pressure-memory trace; physical slip is zero then. The assumed pressure history makes \(H\) nonnegative before birth and strictly positive on an interval near the transverse crossing. The existing positive-transfer and first-edge-zero arguments then make nonnegative **whole postbirth centre history** equivalent to nonnegative whole-disk velocity throughout that postbirth interval, with strict noncentral and edge positivity and radius growth.

Thus arbitrary later smooth rate changes are allowed. Prebirth rate changes themselves need not be monotone if they preserve the stated monotonicity of centre pressure. A nondecreasing injection rate up to nucleation is a sufficient startup example. General nonmonotone prebirth centre pressure and tangential first nucleation are not covered. The pressure-startup condition must accompany any statement of a Gaussian centre-only criterion.

### Formula-level novelty decision

This normalization multiplies each positive-radius row by a positive scalar and extends that normalized row continuously to zero radius. It leaves the source-time log-slope and relevant kernel-ratio order unchanged. Consequently it stays within the same Volterra/kernel object already screened in Sections 2–4 and the exact geological question screened in Sections 6 and 10. No new abstract positivity theorem, new source kernel or new friction model is being asserted.

The audit therefore does not reopen a broad literature sweep. The bounded source checks support presenting this as a conditional finite-width extension of the historical criterion, with the same classical-method attribution and historical-priority uncertainty. No exact published centre-history criterion under these startup conditions was identified in the source set already inspected. The sufficient role of monotone pressurization itself is established background and should not be claimed as new; the proposed extension is the allowance for arbitrary later rate shape while retaining the historical scalar test.

**Final-statement inspection:** the exact statement in `target_gaussian_startup.yaml` and Theorem G with Sections 2–5 of `gaussian_startup_extension.md` were inspected after the independent proof auditor reported successful algebraic and proof checks. They match the scope recorded above, including the distinction between physical zero slip and the latent prebirth pressure trace. The formula-level gate is complete for this conditional extension. This literature audit records its novelty boundary and does not independently recertify the proof.

It yielded the verified final Feng–Li DOI and shorter published title now recorded in Section 4.
