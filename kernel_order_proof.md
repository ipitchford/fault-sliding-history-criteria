# Centre-minimum ordering for the Dawson–Abel slip-rate kernel

> **Status (31 October 2026).** This supporting note is superseded by the revised manuscript wherever the two differ. Lemma 2 of the manuscript states and proves the same centre-relative age order with renamed symbols ($\bar r$ for $\sqrt{R^2-r^2}$, $\xi$ for the Laplace variable, $X_r$ for the random variable and $\varphi_r$ for the densities). The manuscript additionally proves that the order survives any positive mixture of Gaussian source widths (Proposition 3.3) and reports a numerical counterexample for an annular source (Section 9.4). Equation numbers below are those of this note, not of the manuscript.


Research note prepared 28 October 2026. This is a self-contained mathematical proof for a specified kernel. Its use as a fault-locking theorem is conditional on independently establishing that this kernel represents the velocity on the fully sliding crack branch. No claim about other friction laws or post-locking continuation is made here.

## 1. Frozen theorem statement and exclusions

Let \(R>0\), \(\alpha>0\), and let Dawson's integral be

\[
D(x)=e^{-x^2}\int_0^x e^{z^2}\,dz.
\]

Define, for \(0\le r<R\) and \(u>0\),

\[
K_R(r,u)=\int_r^R \frac{a}{\sqrt{a^2-r^2}}
\frac{D(a/\sqrt{4\alpha u})}{u\,a/\sqrt{4\alpha u}}\,da. \tag{1}
\]

At \(r=0,a=0\), the removable Dawson quotient is interpreted as 1. All integrals in (1) are finite and strictly positive.

**Theorem 1 (centre-minimum ordering).** For every \(0<r<R\), the function

\[
F_r(u):=\frac{K_R(r,u)}{K_R(0,u)} \tag{2}
\]

is strictly increasing for \(u>0\). Equivalently, for every \(0<u_y<u_o\),

\[
\frac{K_R(r,u_o)}{K_R(r,u_y)}
>
\frac{K_R(0,u_o)}{K_R(0,u_y)}. \tag{3}
\]

Thus the ratio of the older response to the younger response has its unique minimum at the centre among \(0\le r<R\).

**Excluded stronger claim.** The left side of (3) need not increase with \(r\). Section 7 gives an analytic obstruction and a numerical example. The theorem orders each interior location relative to the centre, not arbitrary pairs of radii.

## 2. Two integral identities and the probability representation

For \(x\ge0\), substitution \(z=xt\) in Dawson's definition gives

\[
\frac{D(x)}x=\int_0^1e^{-x^2(1-t^2)}\,dt, \tag{4}
\]

with both sides equal to 1 at \(x=0\). Put

\[
L=\sqrt{R^2-r^2},\qquad \lambda=\frac1{4\alpha u}.
\]

The substitution \(y=\sqrt{a^2-r^2}\) has
\(dy=a\,da/\sqrt{a^2-r^2}\). Therefore

\[
K_R(r,u)=\frac1u\int_0^L\int_0^1
e^{-\lambda(r^2+y^2)(1-t^2)}\,dt\,dy.
\]

Let \(Z,T\) be independent uniform random variables on \([0,1]\), and define

\[
S_r=(r^2+L^2 Z^2)(1-T^2),\qquad
M_r(\lambda)=\mathbb E e^{-\lambda S_r}.
\]

Then

\[
K_R(r,u)=\frac L uM_r(\lambda),\qquad
K_R(0,u)=\frac R uM_0(\lambda),\qquad
F_r(u)=\frac LR H_r(\lambda),\quad
H_r=\frac{M_r}{M_0}. \tag{5}
\]

Under this coupling,

\[
S_r-S_0=r^2(1-Z^2)(1-T^2)>0
\quad\text{almost surely if }r>0.
\]

Consequently

\[
0<H_r(\lambda)<1\quad (\lambda>0),\qquad H_r(0)=1. \tag{6}
\]

This coupling alone establishes only the ordinary Laplace-transform comparison. The quotient monotonicity needs the density argument below.

## 3. Exact densities

Set \(P_r=r^2+L^2Z^2\) and \(Q=1-T^2\). Their independent densities are

\[
f_{P_r}(p)=\frac{1}{2L\sqrt{p-r^2}},\quad r^2<p<R^2;
\qquad f_Q(q)=\frac1{2\sqrt{1-q}},\quad0<q<1.
\]

Since \(S_r=P_rQ\), the product-density formula gives, for \(0<s<R^2\),

\[
g_r(s)=\frac1{4L}
\int_{\max\{r^2,s\}}^{R^2}
\frac{dp}{\sqrt{p-r^2}\sqrt p\sqrt{p-s}}. \tag{7}
\]

These are probability densities by the change of variables that produced them. The logarithmic singularity at \(s=r^2\) is integrable. At the centre,

\[
\begin{aligned}
g_0(s)
&=\frac1{4R}\int_s^{R^2}\frac{dp}{p\sqrt{p-s}}\\
&=\frac1{2R\sqrt s}\arctan\sqrt{\frac{R^2-s}{s}}\\
&=\frac{\arccos(\sqrt s/R)}{2R\sqrt s}. \tag{8}
\end{aligned}
\]

In the second line we used \(p=s+y^2\). All density identities hold almost everywhere; the value assigned at the single singular point is irrelevant.

## 4. The required single-crossing property

Fix \(0<r<R\).

On \(0<s<r^2\), the integration range in (7) is fixed. Its integrand increases strictly with \(s\), so \(g_r(s)\) increases strictly. Meanwhile (8) decreases strictly, since both positive factors \(\arccos(\sqrt s/R)\) and \(s^{-1/2}\) decrease strictly. Hence \(g_r/g_0\) increases strictly on this interval.

The endpoint values are

\[
g_r(0+)=\frac{\arctan(L/r)}{2Lr}<\infty,
\qquad g_0(s)\sim\frac\pi{4R\sqrt s}\quad(s\downarrow0),
\]

and \(g_r(s)\to\infty\) as \(s\uparrow r^2\). The last assertion follows, for example, by restricting (7) to \(p\in[r^2,r^2+\varepsilon]\): up to factors bounded above and below by positive constants, the integral is

\[
\int_0^\varepsilon\frac{dx}{\sqrt x\sqrt{x+r^2-s}},
\]

which diverges logarithmically as \(s\uparrow r^2\). Since \(g_0(r^2)\) is finite and positive,

\[
\frac{g_r(s)}{g_0(s)}\longrightarrow0\quad(s\downarrow0),
\qquad
\frac{g_r(s)}{g_0(s)}\longrightarrow\infty\quad(s\uparrow r^2). \tag{9}
\]

For \(r^2<s<R^2\), (7) and (8) have the same integration range. Since

\[
\frac{1}{\sqrt{p-r^2}\sqrt p\sqrt{p-s}}
>
\frac{1}{p\sqrt{p-s}},
\]

we obtain

\[
\frac{g_r(s)}{g_0(s)}>\frac RL>1. \tag{10}
\]

It follows from (9)–(10) that **for every \(0<c\le1\), there is exactly one \(s_c\in(0,r^2)\) such that**

\[
g_r(s)-c\,g_0(s)<0\quad(0<s<s_c),
\qquad
g_r(s)-c\,g_0(s)>0\quad(s_c<s<R^2). \tag{11}
\]

No assertion that \(g_r/g_0\) is globally increasing is needed. In fact it has a singular peak at \(r^2\), which explains why a direct likelihood-ratio-order argument would be too strong.

## 5. Proof of quotient monotonicity and strictness

At a fixed \(\lambda>0\), take \(c=H_r(\lambda)\). By (6), \(0<c<1\), so (11) applies. By the definition of \(c\),

\[
\int_0^{R^2} e^{-\lambda s}[g_r(s)-c g_0(s)]\,ds=0. \tag{12}
\]

All distributions have bounded support, so differentiating their Laplace transforms is justified by dominated convergence. Direct differentiation yields

\[
H_r'(\lambda)
=-\frac1{M_0(\lambda)}
\int_0^{R^2}s e^{-\lambda s}[g_r(s)-c g_0(s)]\,ds.
\]

Subtract \(s_c\) times (12) to obtain

\[
H_r'(\lambda)
=-\frac1{M_0(\lambda)}
\int_0^{R^2}(s-s_c)e^{-\lambda s}[g_r(s)-c g_0(s)]\,ds<0. \tag{13}
\]

The strict inequality holds because the integrand is strictly positive except at one point, on intervals of positive measure on both sides of \(s_c\). Every integral remains finite despite the integrable density singularities.

Finally, \(\lambda=1/(4\alpha u)\) decreases strictly with \(u\), while \(L/R>0\) is constant. Equation (5) proves \(F_r'(u)>0\). This proves Theorem 1.

The same calculation at \(\lambda=0\), with \(c=1\), also shows \(H_r'(0)<0\). As a check, direct moments give

\[
\mathbb E S_r=\frac29(R^2+2r^2),\qquad
H_r'(0)=-(\mathbb E S_r-\mathbb E S_0)=-\frac{4r^2}{9}.
\]

## 6. Endpoints, constants and useful asymptotic checks

### Large response age

Dominated convergence in (4) gives

\[
K_R(r,u)\sim\frac L u,\quad K_R(0,u)\sim\frac R u,
\qquad
F_r(u)\longrightarrow\frac LR\quad(u\to\infty).
\]

More precisely,

\[
F_r(u)=\frac LR\left[1-\frac{r^2}{9\alpha u}+O(u^{-2})\right]. \tag{14}
\]

### Small response age away from the centre

For fixed \(0<r<R\), the standard expansion \(D(x)=1/(2x)+1/(4x^3)+O(x^{-5})\), or an endpoint Laplace expansion in (4), gives

\[
\lim_{u\downarrow0}K_R(r,u)
=2\alpha\int_r^R\frac{da}{a\sqrt{a^2-r^2}}
=\frac{2\alpha}{r}\arccos(r/R). \tag{15}
\]

Writing \(\theta=\arccos(r/R)\), the next term is

\[
K_R(r,u)=\frac{2\alpha\theta}{r}
+\frac{2\alpha^2u}{r^3}(\theta+\sin\theta\cos\theta)
+O(u^2). \tag{16}
\]

The remainder is uniform on any closed subinterval of \((0,R)\), and also on intervals bounded away from 0 when the kernel is divided by \(L\) near the rim.

### Small response age at the centre

The substitution \(x=a/\sqrt{4\alpha u}\) gives

\[
K_R(0,u)=\frac{2\sqrt\alpha}{\sqrt u}
\int_0^{R/\sqrt{4\alpha u}}\frac{D(x)}x\,dx.
\]

By Tonelli and (4),

\[
\int_0^\infty\frac{D(x)}x\,dx
=\frac{\sqrt\pi}{2}\int_0^1\frac{dt}{\sqrt{1-t^2}}
=\frac{\pi^{3/2}}4.
\]

Consequently,

\[
K_R(0,u)\sim\frac{\pi^{3/2}\sqrt\alpha}{2\sqrt u},
\qquad
F_r(u)\sim
\frac{4\sqrt\alpha\,\arccos(r/R)}{\pi^{3/2}r}\sqrt u. \tag{17}
\]

In particular \(F_r(0+)=0\). The two-term centre expansion is

\[
K_R(0,u)=\frac{\pi^{3/2}\sqrt\alpha}{2\sqrt u}
-\frac{2\alpha}{R}+O(u). \tag{18}
\]

### Crack edge

At the exact edge \(r=R\), the integral (1) is zero. Its older/younger ratio is therefore not defined there. The edge limit of that ratio exists. Since

\[
\lim_{r\uparrow R}\frac{K_R(r,u)}{\sqrt{R^2-r^2}}
=\frac1u\frac{D(R/\sqrt{4\alpha u})}{R/\sqrt{4\alpha u}}, \tag{19}
\]

we have

\[
\lim_{r\uparrow R}\frac{K_R(r,u_o)}{K_R(r,u_y)}
=\frac{u_y}{u_o}
\frac{D(x_o)/x_o}{D(x_y)/x_y},
\quad x_j=\frac R{\sqrt{4\alpha u_j}}. \tag{20}
\]

The strict centre-minimum theorem extends to this edge-normalised kernel. One can either take the density limit and repeat the argument, or observe directly that the limiting random variable is \(S_R=R^2(1-T^2)\) with density

\[
g_R(s)=\frac1{2R^2\sqrt{1-s/R^2}}.
\]

Here \(g_R/g_0\) increases strictly from 0 to infinity, so the same proof applies. Indeed, setting \(x=\sqrt s/R\), the ratio is \(x/[\sqrt{1-x^2}\arccos x]\); the numerator increases and the positive denominator decreases on \((0,1)\).

## 7. Why full radial monotonicity is false

For fixed positive \(r\), (16) implies

\[
\frac{K_R(r,u_o)}{K_R(r,u_y)}
=1+c(r)(u_o-u_y)+O(u_o^2+u_y^2),
\qquad
c(r)=\frac\alpha{r^2}
\left[1+\frac{\sin\theta\cos\theta}{\theta}\right]. \tag{21}
\]

Take \(r_1=R/2\), \(r_2=\sqrt3 R/2\). Then

\[
c(r_1)=\frac\alpha{R^2}\left(4+\frac{3\sqrt3}{\pi}\right),
\qquad
c(r_2)=\frac\alpha{R^2}\left(\frac43+\frac{2\sqrt3}{\pi}\right),
\]

so \(c(r_1)>c(r_2)\). With \(u_o=2\varepsilon\), \(u_y=\varepsilon\), (21) proves that the older/younger ratio is larger at \(r_1\) than at \(r_2\) for every sufficiently small \(\varepsilon>0\). This is an analytic counterexample family to global radial monotonicity.

A concrete numerical example uses \(R=\alpha=1\), \(u_o=0.01\), \(u_y=0.001\):

| Radius \(r\) | Older/younger ratio |
|---:|---:|
| 0 | 0.300177711063913 |
| 0.1 | 0.664612044375912 |
| 0.2 | 1.12631636953158 |
| 0.3 | 1.17816821797947 |
| 0.5 | 1.06836853229713 |
| 0.8 | 1.02712985581250 |
| 0.99 | 1.01957057648813 |

These numbers were obtained by removing the Abel singularity with \(y=\sqrt{a^2-r^2}\) and using adaptive quadrature of Dawson's function. Independent high-precision checks are supplied in the accompanying verification script. Numerical data illustrate the analytic theorem and counterexample; the proof does not depend on the numerical values.

## 8. Consequence for a unimodal injection history

This is an abstract signed-measure consequence. Fix \(t>0\), \(R>0\) and a finite signed measure \(\mu\) on \([0,t)\) with a decomposition \(\mu=\mu_+-\mu_-\), where \(\mu_+,\mu_-\) are nonnegative and for some \(b\in[0,t)\),

\[
\operatorname{supp}\mu_+\subset[0,b],\qquad
\operatorname{supp}\mu_-\subset[b,t).
\]

Assume

\[
\int_{[0,t)} K_R(0,t-s)\,d(\mu_++\mu_-)(s)<\infty. \tag{22}
\]

Define

\[
V(r)=\int_{[0,t)}K_R(r,t-s)\,d\mu(s).
\]

For \(0<r<R\), put \(c_r=F_r(t-b)>0\). Older positive increments have \(F_r(t-s)\ge c_r\); younger negative increments have \(F_r(t-s)\le c_r\). Thus

\[
\begin{aligned}
V(r)-c_rV(0)
&=\int_{[0,b]}[F_r(t-s)-c_r]K_R(0,t-s)\,d\mu_+(s)\\
&\quad+\int_{[b,t)}[c_r-F_r(t-s)]K_R(0,t-s)\,d\mu_-(s)
\ge0. \tag{23}
\end{aligned}
\]

The inequality is strict if \(\mu_+([0,b))>0\) or \(\mu_-((b,t))>0\). This condition only requires positive measure away from the splitting time on at least one side. Therefore, if \(V(0)\ge0\), all interior velocities are nonnegative; if \(V(0)=0\) and the strictness condition holds, all \(0<r<R\) have \(V(r)>0\).

For a bounded-variation injection rate \(q\), extended by zero before injection begins, take \(\mu=dq\). A unimodal rate has the required chronological ordering of positive and negative increments. The initial positive jump is included as an atom of \(dq\) at 0. If \(q\) is locally Lipschitz near the observation time and has no atom at \(t\), condition (22) follows from the \(u^{-1/2}\) singularity in (17). More generally, (22) is the exact integrability condition. Bounded variation alone does not guarantee it.

At an instantaneous downward jump at the observation time, the centre's formal rate contains a negative \(u^{-1/2}\) singularity; the finite-rate theorem should be applied at times just after the jump, or the jump treated separately by a one-sided limiting argument. The present note does not call an infinite instantaneous rate an ordinary velocity.

When \(R=R(t)\) is the actual front radius, Theorem 1 can be applied at each fixed \(t\), with that value of \(R\). It does not require \(R\) to be constant as time evolves. However, the derivation of the velocity formula must separately justify any disappearance of \(\dot R(t)\) boundary terms. The mathematical ordering cannot supply that missing mechanical justification.

## 9. Fixed Gaussian source regularisation

Suppose the spatial injection profile is a fixed centred Gaussian with diffusion-age parameter \(\varepsilon>0\). Apart from the positive dimensional normalisation, its pressure impulse response is

\[
G_\varepsilon(r,u)=\frac1{u+\varepsilon}
\exp\left[-\frac{r^2}{4\alpha(u+\varepsilon)}\right],\qquad u\ge0.
\]

This follows directly by convolution of two centred heat-kernel Gaussians: the fixed source Gaussian has age \(\varepsilon\), and diffusion adds age \(u\). Under the same spatial crack transform that gives (1), the velocity response is

\[
K_R^\varepsilon(r,u)=K_R(r,u+\varepsilon).
\]

Theorem 1 therefore applies unchanged after shifting both ages by \(\varepsilon\). The signed-measure result (23) remains valid, replacing \(F_r(u)\) by \(F_r(u+\varepsilon)\). The kernel is now bounded and continuous even at age zero, so any finite signed measure on \([0,t]\) is integrable; an atom at the observation time is allowed. This is an exact result for a fixed Gaussian spatial profile, not a theorem for an arbitrary borehole or arbitrary finite-support source.

One consequence is an exact threshold for an instantaneous partial rate decrease after a constant-rate stage. Let \(q(s)=Q_0\) on \((0,b)\) and \(q(s)=Q_0-\Delta Q\) immediately after \(b\), with \(Q_0>0\), \(0<\Delta Q\le Q_0\). At \(t=b+\), on the same formal crack branch,

\[
V(0)=Q_0K_R(0,b+\varepsilon)-\Delta Q K_R(0,\varepsilon).
\]

Hence the formal branch first violates the nonnegative-velocity condition at this instant precisely when

\[
\frac{\Delta Q}{Q_0}>
\frac{K_R(0,b+\varepsilon)}{K_R(0,\varepsilon)}. \tag{25}
\]

At equality, the centre has zero velocity and every interior \(r>0\) still has positive velocity by strict kernel ordering. The fraction on the right belongs to \((0,1)\): the centre formula in Section 6 is a product of the strictly decreasing factor \(u^{-1/2}\) and an integral with a strictly decreasing upper endpoint, hence \(K_R(0,u)\) decreases strictly. As \(\varepsilon\downarrow0\), the threshold tends to zero. Thus an arbitrarily small downward rate step has a singular instantaneous effect in the point-source idealisation, whereas a fixed Gaussian source has a positive partial-step threshold.

## 10. Formula fingerprint and novelty boundary

The transformed variable is a product of a shifted/scaled \(\mathrm{Beta}(1/2,1)\) variable and an independent \(\mathrm{Beta}(1,1/2)\) variable. Its exact moments are

\[
\mathbb E S_r^n=
\frac{4^n(n!)^2}{(2n+1)!}
\sum_{k=0}^n\binom nk
\frac{r^{2(n-k)}(R^2-r^2)^k}{2k+1}. \tag{26}
\]

For \(R=1,r=0\), the moments begin
\(1,2/9,8/75,16/245,128/2835\), and

\[
M_0(\lambda)={}_2F_2\left(1,\tfrac12;\tfrac32,\tfrac32;-\lambda\right).
\]

For \(R=1\), the polynomial moment factor \(I_n=\mathbb E[r^2+(1-r^2)Z^2]^n\) also obeys the exact recurrence

\[
I_0=1,\qquad I_n=\frac{1+2nr^2I_{n-1}}{2n+1}.
\]

This recurrence and \(\mathbb E(1-T^2)^n/\mathbb E(1-T^2)^{n-1}=2n/(2n+1)\) give an independent high-precision moment-series evaluation of the kernel, used in `verify_kernel_order.py`. The computed 70-digit series values agree with direct Dawson/Abel quadrature to the displayed 13–14 digits.

The exact kernel inequality, product distribution, density in (7), centre density in (8), and the hypergeometric identity are the fingerprints for future searches. No finite matrix is involved, so matrix fingerprints and OEIS eigenvalue searches do not apply; moments are supplied instead.

The abstract method belongs to classical single-crossing and Laplace-transform-ratio-order arguments. A relevant primary source is Z. Yang and J.-F. Tian, *Monotonicity rules for the ratio of two Laplace transforms with applications*, Journal of Mathematical Analysis and Applications (2019), DOI [10.1016/j.jmaa.2018.10.034](https://doi.org/10.1016/j.jmaa.2018.10.034), preprint [arXiv:1803.02513](https://arxiv.org/abs/1803.02513). It is not appropriate to claim invention of the general transform-order principle. This note proves the special kernel order directly, including the density crossing needed for this application.

The geological source is A. Sáez, F. Passelègue and B. Lecampion, *Maximum size and magnitude of injection-induced slow slip events*, Science Advances 11, eadq0662 (7 May 2025), DOI [10.1126/sciadv.adq0662](https://doi.org/10.1126/sciadv.adq0662). The [author-hosted full text](https://francoispasselegue.github.io/FXP-Webpage/alexis2025.pdf) was inspected. The paragraph following its Eq. 24 explicitly identifies the missing source conditions for transition from crack-like to pulse-like behaviour. The kernel theorem addresses the unimodal-history subclass, conditional on the exact crack-velocity derivation. It does not resolve the full arbitrary-history question.

Searches performed 28 October 2026 used the web-search tools' two engines and primary-source pages where available. The following exact queries were run:

- `Dawson function ratio monotonic x Dawson logarithmic derivative`
- `Dawson integral Abel transform total positivity monotonic ratio`
- `"Dawson" "Abel" "fault" locking`
- `"Dawson" "ratio" "Laplace" inequality`
- `"Laplace transform" "single crossing" ratio monotonicity`
- `"arccos" "sqrt" "Laplace transform ratio" beta`
- `"Dawson" "Abel transform" monotonicity`
- `"shifted beta" "Laplace" order`
- `"product" "beta" "Laplace transform ratio order"`
- `"Z^2" "1-T^2" distribution`
- `"Dawson" "locking" slip injection`
- `"arccos" "density" "beta product"`
- `"aseismic" "locking" "Dawson"`
- `"fault" "locking" "centre" "ramp" injection`
- `"Dawson" "arccos" "ratio"`
- `"Laplace transform ratio" "beta" product`
- `"Maximum size and magnitude of injection-induced slow slip events" "pulse"`
- `"injection" "crack-like" "necessary and sufficient" slip`
- `"aseismic" "unimodal" injection`
- `"2/9" "8/75" "16/245"`

The search retrieved transform-order theory and geological locking papers, but did not retrieve inequality (3) or the distribution order proved above. In particular, the general Laplace-ratio method is known, while the exact Dawson–Abel object identity was not found. This is negative evidence within a bounded web-search corpus, not proof of historical priority. The parent thread is auditing the direct geological citation neighbourhood before adjudicating the overall novelty gate.

Current contribution-unit status: mathematical proof complete; general transform method known; specific kernel inequality and application have **bounded novelty uncertainty**. Permitted language is “we prove the following kernel inequality” and “an exact prior statement was not found in the recorded bounded search”. Forbidden language includes “first proof” or “previously unknown” without a stronger priority audit.
