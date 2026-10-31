---
title: "Scalar history criteria for the first loss of full sliding under variable fluid injection"
author: "Anonymous"
date: "31 October 2026. Version 0.1.0-candidate, DOI [10.5281/zenodo.23838529](https://doi.org/10.5281/zenodo.23838529)"
---

## Abstract

Fluid injected into a fault can drive slow, aseismic slip that spreads as an expanding crack. When the injection rate is reduced, part of the fault eventually stops slipping forward. We ask when this first happens, in the standard circular model with constant friction, zero fracture energy and zero Poisson ratio. We show that one scalar quantity, the slip-rate history at the injection point, decides the question. For a point source or a Gaussian source and any injection rate that rises and then falls, the whole slipping disk moves forward exactly when the injection point does. For piecewise-smooth rates with any number of rises, falls and steps, the same holds over an interval exactly when the injection-point history has stayed nonnegative throughout it, provided injection starts with a nondecreasing phase (for a Gaussian source: the centre pressure must not fall before slip starts, and slip must start transversely). Under these conditions full sliding is lost first at the injection point. We give explicit consequences: a finite-radius correction to the classical half-derivative test, a closed-form bound on the time after shut-in by which full sliding must have ended, and, for a point source, the result that no linear taper can halve the rate without loss of full sliding. The results concern the first loss of full sliding only; they do not describe the later slip pulse or seismic hazard.

## 1. Introduction

### 1.1 Who needs this result and why

Injection of fluid into a fault raises pore pressure, lowers frictional strength and can trigger slow, aseismic slip. While injection continues at a steady or increasing rate, the slipping region in the simplest models behaves as an expanding crack: every point inside it slips forward. When the rate is reduced, or injection stops, the pressure near the well falls first, and somewhere inside the crack the frictional stress balance can no longer be maintained with forward slip. From that moment the slip region is no longer a simple crack; slip continues as a pulse around a locked interior [@saez2023; @jacquey2023]. Rupture-size laws written for crack-like behaviour [@saez2025] hold only until that moment.

Three groups need to know when and where this first happens. Numerical modellers need an exact benchmark for codes that must resolve the birth of a back front under stepped, cyclic or tapered injection protocols. Analysts who use crack-like volume laws need to know how long those laws remain valid for a given schedule. Those who design injection schedules need to know which rate reductions are compatible with continued forward slip in the model, and which are not.

### 1.2 The result in words

In the circular model, checking full sliding normally requires the whole slip-rate field inside the crack. We show that, for a point source or a Gaussian source, it is enough to watch a single scalar history: the slip rate at the injection point (the centre of the crack). If the injection rate first rises and then falls, the crack is sliding forward everywhere at a given instant exactly when the centre is. For general piecewise-smooth or stepped rates that start with a nondecreasing phase (Theorems A and G give the precise startup conditions, including transverse nucleation for a Gaussian source), the crack has slid forward everywhere throughout an interval since the start exactly when the centre has done so. Under these conditions the first point to stop is always the centre. For annular sources this can fail (Section 9.4).

The physical reason is the memory of the pressure field. A recent rate decrement is felt strongly near the source and only weakly and later farther out, while old increments have spread over the whole crack. In the infinite-radius (critically stressed) limit this can be made exact: the slip rate at radius $r$ responds to the same injection history as the centre, but with every rate change delayed by a random diffusive travel time, namely the first time a one-dimensional diffusion with the fault's diffusivity covers a random distance $r\sin\theta$, with $\theta$ uniform on $(0,\pi/2)$ (Section 7.1). A delayed average of a function that has stayed nonnegative stays nonnegative. At finite radius no such clean probabilistic picture is available; the proof instead compares how fast responses to old and young rate changes decay with age at each radius and at the centre.

### 1.3 Contributions

1. **Instantaneous criterion (Theorem 1, Section 3).** For any injection rate that rises and then falls, nonnegative centre slip rate is equivalent to nonnegative slip rate throughout the disk, at finite radius, for a point source, a Gaussian source and any positive mixture of Gaussian source widths (Proposition 3.3). The proof rests on a centre-relative age order for a Dawson-function kernel (Lemma 2). The same order fails for an annular source (Section 9.4).
2. **Historical criteria (Theorems A, B and G, Section 4).** For smooth or stepped rates with arbitrarily many rises and falls, nonnegativity of the whole centre history is equivalent to full sliding. Radius growth and existence of the crack radius follow automatically (Proposition 4.1). For a point source, rate jumps upward are allowed and any downward jump ends full sliding at once; for a Gaussian source, jumps of both signs are allowed.
3. **Abrupt drops (Section 5).** An exact tolerance for a sudden rate drop with a Gaussian source, and its size at realistic source widths: roughly $\sqrt{\varepsilon/T}$, about $10^{-3}$ at wellbore scale.
4. **Mechanical admissibility (Section 6).** The constructed crack satisfies the friction inequality outside the disk; for a Gaussian source it is, in a stated variational class, the unique forward-slip solution up to first failure.
5. **Finite-radius quantification (Section 7).** A sharpened uniform error bound, and a two-term finite-radius criterion with a rigorous remainder (Proposition 7.3) that reproduces the numerically computed thresholds in the critically stressed regime ($\Theta\lesssim0.1$).
6. **Consequences for schedules (Section 8).** The arcsine minimum continuation in the infinite-radius limit; an explicit time after shut-in by which full sliding must have ended (Proposition 8.2); for a point source, the linear-taper threshold and the corollary that no linear taper can halve the rate; a leading-order finite-radius taper threshold; and a dimensional worked example.

**How to use the criterion.** (1) Check that the source and history fall in one of the classes of Section 1.5. (2) At each time, solve the radius equation \eqref{eq:radius}. (3) Evaluate the centre margin \eqref{eq:centremargin} along the history. (4) A zero of the margin is only a threshold contact; full sliding is lost at the first time the margin becomes negative (for a point source, also at any downward rate jump).

### 1.4 Roadmap

Section 2 states the model, the dimensionless parameters and the notation. Section 3 proves the instantaneous criterion. Section 4 states the historical criteria; their proofs are in Appendices B and C, and the kernel properties they use are in Appendix A. Section 5 treats abrupt rate drops. Section 6 closes the mechanics outside the disk. Section 7 treats the infinite-radius limit and finite-radius corrections, with proofs in Appendix D. Section 8 draws the consequences for injection schedules. Section 9 reports the numerical verification. Section 10 relates the results to previous work and lists open problems.

### 1.5 Main results at a glance

| Result | Radius | Source | History class | Startup condition | Conclusion |
|-----------|--------|------------|---------------|----------------|--------------------|
| Theorem 1 | finite | point, Gaussian, Gaussian mixture | rises then falls (single-peaked) | none | centre velocity $\ge0$ $\Leftrightarrow$ all velocities $\ge0$, at each instant |
| Theorem A | finite | point | piecewise $C^1$; downward jumps end full sliding | positive initial rate or nondecreasing start | whole centre history $\ge0$ $\Leftrightarrow$ full sliding; radius grows |
| Theorem B | finite | point | as Theorem A, no downward jump before the contact | as Theorem A | first loss of full sliding is at the centre |
| Theorem G | finite | Gaussian | piecewise $C^1$, jumps of both signs | nonnegative latent forcing before slip starts; transverse nucleation | as Theorems A and B |
| Proposition 4.1 | finite | point, Gaussian | as A or G | as A or G | crack radius exists while centre history $\ge0$ |
| Theorem 3 | infinite | point | bounded variation | none | centre history $\ge0$ $\Leftrightarrow$ full sliding |
| Proposition 7.3 | finite | point, Gaussian | bounded variation | none | two-term centre margin with rigorous remainder |
| Proposition 8.2 | finite | point, Gaussian | integrable, zero after shut-in $t_s$ | as Theorem A or G | no crack after $t_s+f c_p\mathcal V/\tau_{\rm d}-\varepsilon$; full sliding lost before |
| Corollary 8.4 | infinite and finite | point | linear taper | constant first stage | admissible depth $<\tfrac12$; strictly smaller at finite radius |

## 2. Model, parameters and notation

*This section fixes the model, introduces the dimensionless stress-injection parameter, and defines the terms used in the statements.*

### 2.1 Pressure diffusion

The fault is a homogeneous, planar, permeable layer of width $w>0$ and storage coefficient $S>0$, with hydraulic diffusivity $\alpha>0$. The host rock has shear modulus $\mu>0$; friction is constant with coefficient $f>0$. The initial shear stress is $\tau_0$ and the initial effective normal stress is $\sigma'_0$. Put

\begin{equation}
\tau_{\rm d}=f\sigma'_0-\tau_0>0,
\qquad c_p=\frac{1}{4\pi\alpha S w}.
\label{eq:constants}
\end{equation}

We call $\tau_{\rm d}$ the *strength excess*. Let $q(t)\ge0$ be the volume injection rate, extended by zero to $t<0$. A parameter $\varepsilon\ge0$ fixes the source width. The pressure above its initial value is

\begin{equation}
p_\varepsilon(r,t)=c_p\int_0^t
\frac{q(s)}{t-s+\varepsilon}
\exp\!\left[-\frac{r^2}{4\alpha(t-s+\varepsilon)}\right]ds.
\label{eq:pressure}
\end{equation}

For $\varepsilon=0$ this is the standard point-source solution. For $\varepsilon>0$ it solves the diffusion equation with the fixed, normalised Gaussian source density

\begin{equation}
\rho_\varepsilon(r)=\frac{1}{4\pi\alpha\varepsilon}e^{-r^2/(4\alpha\varepsilon)},
\label{eq:gaussian}
\end{equation}

whose e-folding radius is $2\sqrt{\alpha\varepsilon}$. The Gaussian source is a specified regularisation, not an exact wellbore boundary condition. Both sources conserve volume: $Sw\int_{\mathbb R^2}p_\varepsilon\,dx=\int_0^tq(s)\,ds=:\mathcal V(t)$.

### 2.2 Elastic model and the dimensionless parameters

The elastic model has zero Poisson ratio, unidirectional slip with axisymmetric magnitude, and zero fracture energy. Under these assumptions the shear traction produced by slip $\delta$ is $\mathfrak T\delta$, where $\mathfrak T=(\mu/2)(-\nabla^2)^{1/2}$ acts in the fault plane. This is the circular model of Sáez, Lecampion, Bhattacharya and Viesca [-@saez2022], used for volume laws in @saez2025. For nonzero Poisson ratio the rupture is no longer circular [@saez2022], and the scalar operator $\mathfrak T$ is no longer available; our proofs use both facts.

The single dimensionless group of a constant-rate stage at rate $q_0$ is

\begin{equation}
\Theta=\frac{\tau_{\rm d}}{f c_p q_0}=\frac{f\sigma'_0-\tau_0}{f\,\Delta p_*},
\qquad \Delta p_*=c_pq_0=\frac{q_0}{4\pi\alpha Sw}.
\label{eq:Theta}
\end{equation}

This is the stress-injection parameter, denoted $T$ in @saez2022 and, in its plane-strain form, in @bhattacharya2019. Small $\Theta$ is the *critically stressed* regime and large $\Theta$ the *marginally pressurised* regime. For constant-rate point-source injection the crack radius is $R(t)=2\lambda\sqrt{\alpha t}$, where (Appendix D.1)

\begin{equation}
\Theta=2\int_\lambda^\infty\frac{D(z)}{z^2}\,dz,
\qquad
\lambda\sim\frac{1}{\sqrt{2\Theta}}\ (\Theta\to0),
\qquad
\lambda\sim\tfrac12e^{(2-\gamma_{\rm E}-\Theta)/2}\ (\Theta\to\infty),
\label{eq:lambdamap}
\end{equation}

with $D$ Dawson's integral \eqref{eq:dawson} and $\gamma_{\rm E}$ Euler's constant. For example, $\Theta=0.1,1,10$ give $\lambda=2.305,0.723,0.00686$. In the numerical examples we scale time by the first injection stage $T$, rates by $q_0$, and lengths by $\sqrt{\alpha T}$.

### 2.3 Histories

On each finite interval the rate $q$ is right-continuous with bounded variation. Its increment measure $dq$ includes the initial atom $q(0)\delta_0$. We call $q$ *single-peaked* if a time $b$ separates its increases from its decreases:

\begin{equation}
dq=m_+-m_-,\qquad
\operatorname{supp}m_+\subset[0,b],\qquad
\operatorname{supp}m_-\subset[b,\infty),
\label{eq:singlepeak}
\end{equation}

with $m_\pm$ nonnegative measures; plateaux are allowed. A *regular time* is a time $t>0$ at which a positive crack radius exists and near which $q$ is locally Lipschitz (point source) or continuous (Gaussian source).

### 2.4 The circular crack branch

For a radial function $\phi$ define the Abel average

\begin{equation}
\mathcal A\phi(a)=\int_0^1\phi(as)\frac{s\,ds}{\sqrt{1-s^2}},
\label{eq:abel}
\end{equation}

which maps a constant to itself. Set $g(r,t)=fp_\varepsilon(r,t)-\tau_{\rm d}$ and $F(a,t)=\mathcal Ag(\cdot,t)(a)$. The *crack radius* is the positive solution of the zero-stress-intensity condition

\begin{equation}
F(R(t),t)=0,
\qquad\text{equivalently}\qquad
f\mathcal Ap_\varepsilon(R(t),t)=\tau_{\rm d}.
\label{eq:radius}
\end{equation}

For a nonzero history the pressure strictly decreases with radius, so its Abel average does too and tends to zero at infinity. Hence a positive root exists, and is unique, exactly when $fp_\varepsilon(0,t)>\tau_{\rm d}$ (an infinite centre value allowed). Before a Gaussian source has *nucleated* slip, $fp_\varepsilon(0,t)\le\tau_{\rm d}$ and the fault is unslipped. The circular inversion [@saez2022; @sneddon1946] gives the slip

\begin{equation}
\delta(r,t)=\frac4{\pi\mu}\int_r^{R(t)}\frac{aF(a,t)}{\sqrt{a^2-r^2}}\,da,
\qquad 0\le r<R(t),
\label{eq:slip}
\end{equation}

and $\delta=0$ outside. Since $F$ decreases in $a$ and vanishes at $R$, this slip is positive inside the disk. We call the field \eqref{eq:slip}, with its time derivative, the *trial branch* (or circular branch). It is the physical solution only while its slip rate is nonnegative everywhere; once that fails, later values of \eqref{eq:slip} are a formal continuation only.

### 2.5 Terms used in the statements

- *Full sliding* at time $t$: the trial slip rate is nonnegative at every point of the disk. A *fully sliding branch* on an interval is a trial branch with full sliding at every time of the interval.
- *Centre margin* $\mathcal C_\varepsilon(t)$: the centre slip rate divided by the positive factor $4fc_p/(\pi\mu)$, equation \eqref{eq:centremargin}.
- *Edge-normalised velocity*: the limit of $v(r,t)/\sqrt{R^2-r^2}$ as $r\uparrow R$; it is proportional to the front speed $R'(t)$ (equation \eqref{eq:edge}).
- *Threshold contact*: a time at which the centre margin is zero. It does not by itself imply a locked patch.
- *Abel half derivative*: $\mathcal Hq(t)=\int_{[0,t)}(t-s)^{-1/2}\,dq(s)$, which is $\sqrt\pi$ times the Riemann--Liouville half derivative of $q$.
- *Positive causal transfer*: a representation of one causal response as a nonnegative combination of the present and past values of another (equations \eqref{eq:B9} and \eqref{eq:C7}).

### 2.6 Notation

| Symbol | Meaning |
|------------------|----------------------------------------|
| $\alpha$, $\mu$, $f$ | hydraulic diffusivity, shear modulus, friction coefficient |
| $\tau_{\rm d}=f\sigma'_0-\tau_0$ | strength excess |
| $c_p$, $\Delta p_*=c_pq_0$ | pressure constant, characteristic pressure |
| $\Theta$ | stress-injection parameter \eqref{eq:Theta} |
| $\lambda=R/(2\sqrt{\alpha t})$ | radius relative to the diffusion length |
| $q$, $dq$, $\mathcal V$ | injection rate, its increment measure, injected volume |
| $\varepsilon$, $\rho_\varepsilon$ | Gaussian source width (a time), source density |
| $p_\varepsilon$, $g$, $F$ | pressure, frictional load $fp_\varepsilon-\tau_{\rm d}$, its Abel average |
| $R(t)$ | crack radius \eqref{eq:radius} |
| $\delta$, $v$ | slip and slip rate |
| $D$, $G$ | Dawson's integral, $G(z)=\int_0^zD(x)\,dx/x$ |
| $K_R(r,u)$, $K_\infty$ | velocity kernel at radius $r$ and response age $u$ |
| $J_R(u)$ | edge kernel |
| $A_*=\pi^{3/2}\sqrt\alpha/2$ | constant with $K_\infty(0,u)=A_*u^{-1/2}$ |
| $\mathcal C_\varepsilon(t)$, $V(r,t)$, $E(t)$ | centre margin, normalised velocity, edge response |
| $\mathcal Hq$ | Abel half derivative |
| $\mathfrak T$, $\chi$ | elastic traction operator, friction gap $\mathfrak T\delta-g$ |
| $\Pi$ | normalised exterior traction of a square-root cap |
| $T$, $L$, $d$ | first-stage duration, taper duration, taper depth |
| $s_*$, $c_D$ | constants $\sup xD(x)$ and $\sup x^3\lvert D(x)-1/(2x)\rvert$ |

## 3. The instantaneous criterion

*This section proves that, for rates that rise and then fall, the sign of the centre slip rate decides the sign everywhere in the disk.*

### 3.1 The velocity kernel

Let Dawson's integral be

\begin{equation}
D(z)=e^{-z^2}\int_0^ze^{y^2}\,dy.
\label{eq:dawson}
\end{equation}

For $0\le r<R$ and $u>0$ define the positive kernel

\begin{equation}
K_R(r,u)=\int_r^R\frac{a}{\sqrt{a^2-r^2}}\,
\frac{D(a/\sqrt{4\alpha u})}{u\,a/\sqrt{4\alpha u}}\,da .
\label{eq:kernel}
\end{equation}

The Dawson quotient $D(z)/z$ equals one at zero. At the centre,

\begin{equation}
K_R(0,u)=2\sqrt{\frac\alpha u}\;G\!\left(\frac R{2\sqrt{\alpha u}}\right),
\qquad G(z)=\int_0^z\frac{D(x)}x\,dx,
\qquad G(\infty)=\frac{\pi^{3/2}}4 .
\label{eq:centrekernel}
\end{equation}

The value $G(\infty)$ is proved in Appendix A.1. Define the *centre margin* and the normalised velocity

\begin{equation}
\mathcal C_\varepsilon(t)=\int_{[0,t]}K_{R(t)}(0,t-s+\varepsilon)\,dq(s),
\qquad
V(r,t)=\int_{[0,t]}K_{R(t)}(r,t-s+\varepsilon)\,dq(s).
\label{eq:centremargin}
\end{equation}

The closed interval gives right-continuous values at Gaussian-source jump times; for continuous rates it is immaterial. For a Gaussian source the age floor $\varepsilon$ makes every kernel bounded, so the integrals converge at every time. For the point source they can diverge even where $q$ is continuous: for $q(s)=1-\sqrt{1-s}$ on $[0,1)$ and $q=1$ afterwards, the centre integral diverges logarithmically at $t=1$. Point-source statements are therefore made only at times where condition \eqref{eq:integrable} below holds.

**Velocity formula.** If

\begin{equation}
\int_{[0,t]}K_{R(t)}(0,t-s+\varepsilon)\,|dq|(s)<\infty,
\label{eq:integrable}
\end{equation}

the integrals \eqref{eq:centremargin} converge absolutely, and $V(r,t)\to\mathcal C_\varepsilon(t)$ as $r\to0$. We *define* the trial velocity as

\begin{equation}
v(r,t)=\frac{4fc_p}{\pi\mu}\,V(r,t).
\label{eq:velocity}
\end{equation}

At a regular time this is the classical time derivative of the slip \eqref{eq:slip}, as follows. Condition \eqref{eq:integrable} holds there: for the point source because $K_R(0,u)\le A_*u^{-1/2}$ is integrable against the bounded density of $dq$ near $t$, and for the Gaussian source because the kernels are bounded by $K_R(0,\varepsilon)$. Causal integration by parts in \eqref{eq:pressure} gives, for $r>0$,

\begin{equation}
\partial_tp_\varepsilon(r,t)=c_p\int_{[0,t]}\frac{e^{-r^2/[4\alpha(t-s+\varepsilon)]}}{t-s+\varepsilon}\,dq(s),
\label{eq:pressurerate}
\end{equation}

which is continuous near $t$. The identity

\begin{equation}
\int_0^1e^{-z^2s^2}\frac{s\,ds}{\sqrt{1-s^2}}=\frac{D(z)}z
\label{eq:abeldawson}
\end{equation}

(substitute $y=\sqrt{1-s^2}$) computes its Abel average, so $F_t$ is continuous near $(a,t)$ for $0<a\le R$, the logarithmic singularity of the point-source pressure rate at $r=0$ being integrable. Since $F_a(R,t)<0$, the implicit function theorem makes $R$ differentiable at $t$. Differentiating \eqref{eq:slip}, the moving-endpoint term vanishes because $F(R(t),t)=0$, and substitution of \eqref{eq:pressurerate}--\eqref{eq:abeldawson} gives \eqref{eq:velocity}. Neither the front speed nor the slip field enters the result. For general bounded-variation histories we use \eqref{eq:velocity} as the definition of the trial velocity and claim no classical derivative.

**Point source at the centre.** During active point-source injection the centre pressure is infinite, so the Coulomb law has no literal meaning at $r=0$. All point-source statements are elastic statements about $r>0$; the centre value $\mathcal C_0(t)$ is the finite limit of $V(r,t)$ as $r\to0$. Full Coulomb admissibility, including finite pressure everywhere, is available only for $\varepsilon>0$ (Section 10.2).

### 3.2 The kernel-ordering lemma

**Lemma 2 (centre-relative age order).** For each fixed $R,\alpha>0$ and $0<r<R$, the ratio

\begin{equation}
u\longmapsto\frac{K_R(r,u)}{K_R(0,u)}
\quad\text{is strictly increasing on }(0,\infty).
\label{eq:lemma2}
\end{equation}

Equivalently, for older age $u_{\rm o}$ and younger age $u_{\rm y}<u_{\rm o}$,
$K_R(r,u_{\rm o})/K_R(r,u_{\rm y})>K_R(0,u_{\rm o})/K_R(0,u_{\rm y})$: relative to the centre, every other radius gives more weight to old increments. The lemma compares each radius with the centre only. The stronger statement that $K_R(r,u_{\rm o})/K_R(r,u_{\rm y})$ increases with $r$ is false (Section 9.4): the kernel family is not totally positive of order two in $(r,u)$, yet the centre is extremal.

*Idea of the proof* (details in Appendix A.4). The kernel is a Laplace transform, $K_R(r,u)=(\bar r/u)\,\mathbb E\,e^{-X_r/(4\alpha u)}$ with $\bar r=\sqrt{R^2-r^2}$, of a random variable $X_r$ that can be coupled so that $X_r>X_0$. Old increments correspond to small Laplace variables, where the larger values of $X_r$ are penalised less; the claim reduces to a single sign change of the difference of the two densities, which is checked directly.

The argument is a variation-diminishing (single-crossing) argument in the sense of total positivity, applied with the crossing level restricted to $c\le1$, which the coupling \eqref{eq:coupling} guarantees; transform-ratio rules of this kind are classical [@yang2019].

### 3.3 Theorem 1

**Theorem 1 (instantaneous criterion).** Let $q$ be single-peaked with peak time $b$, let $t>0$ be a time at which a positive crack radius $R(t)$ exists and \eqref{eq:integrable} holds, and let $\varepsilon\ge0$. Then

$$
V(r,t)\ge0\quad\text{for all }0\le r<R(t)
\qquad\Longleftrightarrow\qquad
\mathcal C_\varepsilon(t)\ge0 .
$$

More precisely, for $t\ge b$ put $u_b=t-b+\varepsilon$; then for every $0<r<R(t)$

\begin{equation}
V(r,t)\ \ge\ \frac{K_{R(t)}(r,u_b)}{K_{R(t)}(0,u_b)}\;\mathcal C_\varepsilon(t),
\label{eq:theorem1bound}
\end{equation}

with strict inequality whenever

\begin{equation}
m_+([0,b))+m_-((b,t])>0,
\label{eq:strictness}
\end{equation}

that is, whenever some increase or some decrease occurs at a time different from $b$. In that case a zero centre margin leaves every other interior point with strictly positive velocity, and the edge-normalised velocity is strictly positive too (by Lemma A.2, equation \eqref{eq:A7}, in place of Lemma 2).

*Proof.* For $t<b$ all increments in $[0,t]$ are nonnegative and the result is immediate. For $t\ge b$, write $u=t-s+\varepsilon$. Increases have ages $u\ge u_b$ and decreases have ages $u\le u_b$. (At $t=b$ a decrease can only be an atom at $b$, of age $u_b=\varepsilon$; for the point source such an atom would violate \eqref{eq:integrable}, so it does not occur; for $\varepsilon=0$ and $t=b$ the ratio in \eqref{eq:theorem1bound} is evaluated at $u_b=0^+$, where it equals its limit $0$ for $r>0$, and the bound is then the trivial statement $V\ge0$ already given by the nonnegative increments.) By Lemma 2,

\begin{equation}
\begin{aligned}
V(r,t)
&=\int\frac{K_R(r,u)}{K_R(0,u)}K_R(0,u)\,dm_+-\int\frac{K_R(r,u)}{K_R(0,u)}K_R(0,u)\,dm_-\\
&\ge\frac{K_R(r,u_b)}{K_R(0,u_b)}\left(\int K_R(0,u)\,dm_+-\int K_R(0,u)\,dm_-\right),
\end{aligned}
\label{eq:separation}
\end{equation}

with $R=R(t)$. The inequality is strict if either measure charges ages different from $u_b$, which is \eqref{eq:strictness}. Necessity follows by taking $r=0$. $\square$

**Corollary 3.1 (trajectory form).** Let $q$ be single-peaked and piecewise locally Lipschitz (point source) or piecewise continuous (Gaussian source), with finitely many exceptional times on compact intervals. Let $t_0$ be the start of slip ($t_0=0$ for the point source, the nucleation time for the Gaussian source), and suppose the crack radius exists on $(t_0,t_2]$. If $\mathcal C_\varepsilon(s)\ge0$ at every time $s\in(t_0,t_2]$ where it is defined (right-continuous values \eqref{eq:centremargin} for the Gaussian source; every time satisfying \eqref{eq:integrable} for the point source), then $V(r,s)\ge0$ for all $0\le r<R(s)$ at each such time, and $R$ is nondecreasing on $(t_0,t_2]$. The trial branch is then a forward-slip trajectory from the start of slip; for a Gaussian source satisfying the full hypotheses of Theorem G (piecewise-$C^1$ rate, latent-forcing and transverse-nucleation conditions) it is the unique solution in the class of Section 6.2. For the point source we claim admissibility, not uniqueness.

Two cautions. Positivity only almost everywhere does not suffice: for a Gaussian source with $q=1$ before $T$ and $q=0$ from $T$ on, the margin is positive before $T$ but $\mathcal C_\varepsilon(T)=K_R(0,T+\varepsilon)-K_R(0,\varepsilon)<0$. And positivity on a later subinterval alone does not identify the physical solution, because earlier backward motion of the trial branch cannot be undone; after the first negative margin, later evaluations of \eqref{eq:centremargin} describe only the formal trial branch.

*Proof.* Every truncation of a single-peaked history is single-peaked, so Theorem 1 applies at each such time. The separation argument with \eqref{eq:A7} gives a nonnegative edge response, so by \eqref{eq:edge} the right derivative of the continuous function $R$ is nonnegative at all but finitely many times, and $R$ is nondecreasing. Section 6.1 gives admissibility outside the disk and Proposition 6.1 gives uniqueness in the stated Gaussian case. $\square$

**Remark 3.2 (why this is not obvious).** The pressure rate \eqref{eq:pressurerate} has a trivially ordered kernel: $e^{-r^2/(4\alpha u)}$ increases with age at every $r$, so a pressure-rate version of Theorem 1 is immediate. The slip rate is different because the elastic inversion averages the pressure rate over all radii between $r$ and $R$, and that averaging destroys total positivity. Lemma 2 shows that the centre nevertheless remains extremal.

### 3.4 Sources that are mixtures of Gaussian widths

Let $\omega$ be a probability measure on $[0,\infty)$ and consider the source density $\rho_\omega=\int\rho_\varepsilon\,\omega(d\varepsilon)$, where $\rho_0$ denotes a point source. Apart from a possible point-source component $\omega(\{0\})$, the normalised integrable densities of this form are, by Bernstein's theorem, exactly the radial densities in the plane that are completely monotone functions of $r^2$, for example $(1+r^2/a^2)^{-k}$ with $k>1$. By linearity the pressure is $\int p_\varepsilon\,\omega(d\varepsilon)$ and the velocity kernel is

\begin{equation}
\bar K_R(r,u)=\int K_R(r,u+\varepsilon)\,\omega(d\varepsilon).
\label{eq:mixturekernel}
\end{equation}

**Proposition 3.3 (Gaussian mixtures).** For every $0<r<R$, $u\mapsto\bar K_R(r,u)/\bar K_R(0,u)$ is strictly increasing on $(0,\infty)$. Consequently Theorem 1, with $K$ replaced by $\bar K$, holds for every such source.

*Proof.* Fix $0<u_1<u_2$. Let $\pi_u(d\varepsilon)\propto K_R(0,u+\varepsilon)\,\omega(d\varepsilon)$, a probability measure, and $\Phi(u)=K_R(r,u)/K_R(0,u)$. Then

$$
\frac{\bar K_R(r,u)}{\bar K_R(0,u)}=\int\Phi(u+\varepsilon)\,\pi_u(d\varepsilon).
$$

The density $d\pi_{u_2}/d\pi_{u_1}$ is proportional to $K_R(0,u_2+\varepsilon)/K_R(0,u_1+\varepsilon)=\exp\int_{u_1}^{u_2}\ell_R(y+\varepsilon)\,dy$, where $\ell_R=\partial_u\log K_R(0,\cdot)$ is nondecreasing (Appendix A, equation \eqref{eq:A4}). So the density is nondecreasing in $\varepsilon$, and $\pi_{u_2}$ dominates $\pi_{u_1}$ in the likelihood-ratio order, hence in the usual stochastic order. Since $\varepsilon\mapsto\Phi(u_1+\varepsilon)$ is nondecreasing (Lemma 2),

$$
\int\Phi(u_2+\varepsilon)\,\pi_{u_2}(d\varepsilon)
>\int\Phi(u_1+\varepsilon)\,\pi_{u_2}(d\varepsilon)
\ge\int\Phi(u_1+\varepsilon)\,\pi_{u_1}(d\varepsilon),
$$

the first inequality being strict by Lemma 2. The proof of Theorem 1 uses only this monotonicity. $\square$

The conclusion does not extend to all nonnegative source profiles. A difference of two Gaussians with a central deficit, a crude model of injection along a wellbore wall, violates the age order, and Section 9.4 gives an explicit instantaneous counterexample in which the centre margin is zero while a ring has negative velocity.

## 4. Historical criteria for rates with many rises and falls

*This section states the criteria for general histories: full sliding holds throughout an interval exactly when the centre margin has stayed nonnegative throughout it. Proofs are in Appendices B and C.*

A positive centre margin at one instant does not certify full sliding for general histories (Section 9.4): after an earlier negative interval, the centre can recover while a ring is already moving backwards. The correct test is historical. In this section a rate is *piecewise $C^1$* on $[0,T]$ if there are finitely many times $0=\tau_0<\tau_1<\dots<\tau_N\le T$ such that $q$ is continuously differentiable on each $[\tau_k,\tau_{k+1})$, with bounded one-sided derivatives; $q$ may jump at the $\tau_k$. Write $\mathcal J$ for the set of jump times after zero.

**Theorem A (point source).** Let $\varepsilon=0$, let $q\ge0$ be piecewise $C^1$ on $[0,T]$, and assume one of the startup conditions

1. $q(0)>0$; or
2. $q(0)=0$ and, for some $t_{\rm start}>0$, $q$ is continuous, nondecreasing and positive on $(0,t_{\rm start}]$.

Then the following are equivalent:

(i) the crack radius exists for every $t\in(0,T]$, and $V(r,t)\ge0$ for all $0\le r<R(t)$ and all $t\in(0,T]\setminus\mathcal J$;

(ii) $\mathcal C_0(t)\ge0$ for every $t\in(0,T]\setminus\mathcal J$ such that the crack radius exists throughout $(0,t]$.

When they hold, $q$ has no downward jump at any time $t_j<T$ (a jump exactly at the final time $T$ is not tested by (i) or (ii)); at every $t\in(0,T]\setminus\mathcal J$ each noncentral velocity and the edge-normalised velocity is strictly positive; at a jump time $t_j<T$ the same holds for both one-sided limits, and at a jump at $T$ for the left limit; and the radius is continuous and strictly increasing. Earlier zeros of the centre margin are allowed.

**Theorem B (first loss is central).** Under the startup conditions of Theorem A, let $t_c$ be the first time at which the centre margin vanishes, if one exists, and assume that $q$ has no downward jump in $(0,t_c]$. (If a downward jump occurs first, full sliding is lost at that jump, at the centre, by Section 5.2; the margin need not pass through zero, and a later zero may be a recovery after a negative interval.) Before $t_c$ every interior velocity and the edge-normalised velocity is strictly positive; at $t_c$ every noncentral and the edge-normalised velocity is still strictly positive. The same holds at any later centre zero that is preceded by a nonnegative centre history. Thus, within these startup classes, the first loss of full sliding, at the first negative crossing of the centre margin or at a downward jump, always occurs through the centre.

For a Gaussian source, the fault is unslipped before nucleation, and the physical centre slip rate carries no information about the injection history in that interval. The proof instead uses the rate of change of the centre pressure before slip, which we call the *latent forcing*:

\begin{equation}
H_{\rm pre}(v)=\frac{\varepsilon}{c_p}\,\partial_t^+p_\varepsilon(0,v)
=\varepsilon\int_{[0,v]}\frac{dq(s)}{v-s+\varepsilon},
\qquad 0\le v\le t_n,
\label{eq:latent}
\end{equation}

where $\partial_t^+$ is the right derivative and $t_n$ is the first nucleation time, $fp_\varepsilon(0,t_n)=\tau_{\rm d}$.

**Theorem G (Gaussian source).** Let $\varepsilon>0$, let $q\ge0$ be piecewise $C^1$ on $[0,T]$ with jumps of either sign, and suppose nucleation occurs at some $t_n<T$ with

\begin{equation}
H_{\rm pre}(v)\ge0\quad(0\le v\le t_n),\qquad H_{\rm pre}(t_n)>0.
\label{eq:startupG}
\end{equation}

Then the following are equivalent:

(i) the crack radius exists for every $t\in(t_n,T]$, and $V(r,t)\ge0$ for all $0\le r<R(t)$, both for the right-continuous values \eqref{eq:centremargin} and for their left limits;

(ii) $\mathcal C_\varepsilon(t)\ge0$ for every $t\in(t_n,T]$ such that the crack radius exists throughout $(t_n,t]$.

When they hold, every noncentral velocity and the edge-normalised velocity is strictly positive (both one-sided values at jump times), and the radius is continuous and strictly increasing. A rate that is nondecreasing on $[0,t_n]$ satisfies \eqref{eq:startupG}; the second condition says that nucleation is transverse. Later rate reversals and jumps are unrestricted.

The hypothesis \eqref{eq:startupG} cannot simply be dropped from the proof: if the latent forcing is negative before nucleation, the positive transfer of Appendix C receives a negative contribution that the post-nucleation centre history does not record. Whether the conclusion nevertheless holds for such histories is open (Section 10.4).

**Proposition 4.1 (the crack radius persists).** In Theorems A and G the existence of the crack radius is not an extra assumption: if the centre margin is nonnegative wherever the radius has existed since the start (respectively since nucleation), then the radius exists on the whole interval. Proof: Appendix B.7.

For a single-peaked smooth history Theorem A reduces to the trajectory form of Theorem 1. For the point source, a downward jump at a time when the crack exists makes the centre margin tend to $-\infty$ immediately afterwards (Section 5.2), so both sides of the equivalence in Theorem A fail at once; only upward jumps survive the criterion.

## 5. Abrupt rate drops

*This section quantifies how large a sudden rate reduction can be before full sliding is lost, and shows that the answer depends strongly on the source width.*

### 5.1 Gaussian source

Suppose $q=q_0>0$ until time $T$ and then drops to $q_1=q_0-j\ge0$, with $j>0$, and that slip has nucleated before $T$. The pressure and the radius are continuous at $T$, and the right-continuous centre margin just after the drop is

\begin{equation}
\mathcal C_\varepsilon(T)=q_0K_R(0,T+\varepsilon)-jK_R(0,\varepsilon),\qquad R=R(T).
\label{eq:dropmargin}
\end{equation}

Full sliding is lost at the drop exactly when

\begin{equation}
\frac{j}{q_0}>\frac{K_R(0,T+\varepsilon)}{K_R(0,\varepsilon)}
=\sqrt{\frac{\varepsilon}{T+\varepsilon}}\;
\frac{G\bigl(R/[2\sqrt{\alpha(T+\varepsilon)}]\bigr)}{G\bigl(R/[2\sqrt{\alpha\varepsilon}]\bigr)} .
\label{eq:droptolerance}
\end{equation}

Equality is a threshold contact, not a failure: the centre velocity is then zero while, by \eqref{eq:strictness}, every other interior point and the front are strictly positive. Because $G$ increases, the tolerance is strictly smaller than $\sqrt{\varepsilon/(T+\varepsilon)}$. It concerns the instant after the drop only; a schedule of several drops has a smaller, history-dependent tolerance (Section 9.3).

At realistic source widths the tolerance is tiny. Identifying the Gaussian e-folding radius $2\sqrt{\alpha\varepsilon}$ with a wellbore radius $a_w$ gives $\varepsilon=a_w^2/(4\alpha)$. With the illustrative values $a_w=0.1$ m and $\alpha$ between $10^{-2}$ and $1$ m$^2$/s, $\varepsilon$ is between $2.5\times10^{-3}$ and $0.25$ s, so $\varepsilon/T$ is about $10^{-8}$ to $10^{-5}$ for stages of hours to days. Table 1 gives \eqref{eq:droptolerance} after a constant-rate stage.

: Largest abrupt relative drop $j/q_0$ compatible with full sliding, after a constant-rate stage of duration $T$ (Gaussian source). A dash means slip has not nucleated by $T$.

| $\varepsilon/T$ | $\Theta=0.1$ | $\Theta=1$ | $\Theta=10$ |
|---:|---:|---:|---:|
| $2\times10^{-2}$ | $1.20\times10^{-1}$ | $6.95\times10^{-2}$ | -- |
| $10^{-4}$ | $8.39\times10^{-3}$ | $4.68\times10^{-3}$ | -- |
| $10^{-6}$ | $8.38\times10^{-4}$ | $4.66\times10^{-4}$ | $5.18\times10^{-6}$ |
| $10^{-8}$ | $8.38\times10^{-5}$ | $4.66\times10^{-5}$ | $4.96\times10^{-7}$ |

So at wellbore scale almost any abrupt reduction, of more than about a tenth of a per cent, ends full sliding at once. The finite source changes the threshold qualitatively, from zero to positive, but not by much quantitatively.

### 5.2 Point source

For the point source the centre kernel is singular at zero age. By Proposition 7.3, $K_R(0,u)=A_*u^{-1/2}-2\alpha/R+O(u)$ as $u\downarrow0$. Suppose $q$ has an isolated downward jump of size $j$ at $T$ and is otherwise $C^1$ with bounded one-sided derivatives on a neighbourhood of $T$, as in the piecewise-$C^1$ class of Section 4. Then the remaining history contributes a bounded amount to the centre margin near $T$, and the radius is continuous, so

\begin{equation}
v(0,t)\sim-\frac{4fc_p}{\pi\mu}\,j\,\frac{A_*}{\sqrt{t-T}}\qquad(t\downarrow T).
\label{eq:pointjump}
\end{equation}

The centre velocity has no finite value just after the jump; it tends to $-\infty$. The isolation hypothesis matters: for a merely bounded-variation rate, upward jumps accumulating just after $T$ can make the margin positive along a sequence of times. Every downward point-source jump therefore ends full sliding immediately, consistent with the immediate locking at the injection point after shut-in found by Sáez and Lecampion [-@saez2023]. The numerical check in Section 9.3 confirms \eqref{eq:pointjump} to $3\times10^{-5}$ relative error at $t-T=10^{-10}$.

## 6. Mechanical admissibility outside the disk

*This section verifies that the trial branch satisfies the friction inequality outside the disk and identifies the class in which it is the unique forward-slip solution.*

### 6.1 Exterior friction inequality

Forward-slip complementarity requires, at each time,

\begin{equation}
v\ge0,\qquad \chi=\mathfrak T\delta-g\ge0,\qquad v\,\chi=0,
\label{eq:complementarity}
\end{equation}

where $\chi$ is the friction gap. Inside the disk, \eqref{eq:slip} gives $\mathfrak T\delta=g$. Since $F(R)=0$, integration by parts gives

\begin{equation}
\delta(r)=-\frac4{\pi\mu}\int_r^R F_a(a)\sqrt{a^2-r^2}\,da\ \ge0,
\label{eq:capsum}
\end{equation}

a superposition of square-root caps $\psi_a(r)=\sqrt{a^2-r^2}_+$ with nonnegative weights. The radial Fourier--Bessel transform

\begin{equation}
\int_0^a r\sqrt{a^2-r^2}\,J_0(kr)\,dr=\frac{\sin(ak)-ak\cos(ak)}{k^3},
\label{eq:hankel}
\end{equation}

multiplication by $k$ and the elementary Bessel sine and cosine integrals give $(-\nabla^2)^{1/2}\psi_a=\pi/2$ inside the cap and $\arcsin(a/r)-a/\sqrt{r^2-a^2}$ outside. Hence the normalised traction of a cap is one inside and, for $r>a$,

\begin{equation}
\frac4{\pi\mu}\mathfrak T\psi_a(r)=\Pi(a/r),\qquad
\Pi(x)=\frac2\pi\left[\arcsin x-\frac{x}{\sqrt{1-x^2}}\right]<0,
\label{eq:captraction}
\end{equation}

the sign following from $\theta<\tan\theta$. The Abel average \eqref{eq:abel} has the inverse

\begin{equation}
g(r)=\frac2\pi\int_0^r\frac{F(a)+aF_a(a)}{\sqrt{r^2-a^2}}\,da
=F(r)-\int_0^rF_a(a)\,\Pi(a/r)\,da,
\label{eq:abelinverse}
\end{equation}

the second form by integration by parts with $\partial_a\arcsin(a/r)=(r^2-a^2)^{-1/2}$. For the point source with bounded rate, $F(a)=O(|\log a|)$, $F_a(a)=O(1/a)$ and $\Pi(a/r)=O(a^3)$, so the integrals converge. For $r>R$, \eqref{eq:capsum}--\eqref{eq:abelinverse} give

\begin{equation}
\chi(r)=\mathfrak T\delta(r)-g(r)=-F(r)+\int_R^rF_a(a)\,\Pi(a/r)\,da>0,
\label{eq:exterior}
\end{equation}

since $F(r)<0$, $F_a<0$ and $\Pi<0$. The exterior is below its slip threshold. If in addition $\tau_0\ge0$ and the pressure stays below $\sigma'_0$ (no opening), the exterior shear stress is nonnegative because $\mathfrak T\delta<0$ outside a nonnegative compactly supported slip, which gives the two-sided Coulomb inequality.

The support cannot shrink while the velocity is nonnegative. The edge limit of the time derivative of \eqref{eq:slip} and differentiation of \eqref{eq:radius} give

\begin{equation}
\lim_{r\uparrow R}\frac{v(r,t)}{\sqrt{R^2-r^2}}=\frac4{\pi\mu}F_t(R,t),
\qquad
R'(t)=-\frac{F_t(R,t)}{F_a(R,t)},\qquad F_a<0,
\label{eq:edge}
\end{equation}

so the front speed and the edge-normalised velocity have the same sign. In terms of the *edge response* $E(t)=\int_{[0,t]}J_{R(t)}(t-s+\varepsilon)\,dq(s)$, with the edge kernel

\begin{equation}
J_R(u)=\lim_{r\uparrow R}\frac{K_R(r,u)}{\sqrt{R^2-r^2}}=\frac{D(z)}{uz},\qquad z=\frac R{2\sqrt{\alpha u}},
\label{eq:edgekernel}
\end{equation}

one has $F_t(R,t)=fc_pE(t)$.

### 6.2 Uniqueness in a variational class

Fix a ball $B\subset\mathbb R^2$. Call $(\delta,\chi)$ a *forward-slip solution in $B$* on $[0,t_1]$ if

1. $\delta\in AC([0,t_1];\dot H^{1/2}(\mathbb R^2))$, $\delta(t)$ is supported in $\bar B$, and $\delta(0)=0$;
2. $v=\dot\delta\in L^1(0,t_1;\dot H^{1/2})$ satisfies $v(t)\ge0$ almost everywhere in space, for almost every $t$;
3. $\chi(t)=\mathfrak T\delta(t)-g(t)$, where $\mathfrak T\delta(t)\in\dot H^{-1/2}$ and $g\in L^\infty(0,t_1;L^{4/3}(B))$, is nonnegative in the sense $\langle\chi(t),\phi\rangle\ge0$ for every nonnegative $\phi\in\dot H^{1/2}$ supported in $\bar B$;
4. $\langle\chi(t),v(t)\rangle=0$ for almost every $t$.

Here $\langle\chi,\phi\rangle=\langle\mathfrak T\delta,\phi\rangle-\int_Bg\phi\,dx$; the integral is finite because $\dot H^{1/2}(\mathbb R^2)$ embeds in $L^4$.

**Proposition 6.1.** Two forward-slip solutions in $B$ with the same load $g$ coincide.

*Proof.* Let $\bar\delta=\delta_1-\delta_2$. Then $\mathfrak T\bar\delta=\chi_1-\chi_2$, and $\langle\mathfrak T\bar\delta,\bar\delta\rangle=(\mu/2)\|\bar\delta\|^2_{\dot H^{1/2}}$ up to the normalisation of the norm. For an absolutely continuous function with values in a Hilbert space, the squared norm is absolutely continuous with derivative $2(\bar\delta,\dot{\bar\delta})$. Hence, for almost every $t$,

\begin{equation}
\frac12\frac{d}{dt}\langle\mathfrak T\bar\delta,\bar\delta\rangle
=\langle\chi_1-\chi_2,v_1-v_2\rangle
=-\langle\chi_1,v_2\rangle-\langle\chi_2,v_1\rangle\le0,
\label{eq:energy}
\end{equation}

using items 3 and 4. The energy starts at zero and is nonnegative, so it vanishes and $\delta_1=\delta_2$. $\square$

We prove membership for the Gaussian-source branches of Theorem G: piecewise-$C^1$ rates satisfying \eqref{eq:startupG}, with transverse nucleation, on an interval where the velocity is nonnegative, including the unslipped interval $[0,t_n]$ on which $\delta=0$; $B$ is the final disk. Indeed $\delta(t)=(4/\pi\mu)\int_0^{R(t)}(-F_a(a,t))\psi_a\,da$ by \eqref{eq:capsum}; the map $a\mapsto\psi_a$ is continuous into $\dot H^{1/2}$ with $\|\psi_a\|_{\dot H^{1/2}}=a^{3/2}\|\psi_1\|_{\dot H^{1/2}}$; for $\varepsilon>0$ the weight $-F_a$ and its time derivative are continuous in $(a,t)$ between jump times; and $R$ is continuous with $R'$ integrable; near nucleation $R\propto(t-t_n)^{1/2}$ by \eqref{eq:C11} and $-F_a=O(a)$, so $\|\dot\delta\|_{\dot H^{1/2}}$ stays bounded. Hence $\delta$ is piecewise $C^1$ and absolutely continuous into $\dot H^{1/2}$. Item 4 holds because $\chi=0$ on the disk and $v$ vanishes outside it. For the point source the same construction applies if the $a$-integrals converge absolutely in $\dot H^{1/2}$ near $a=0$; we do not verify this here, so for the point source we claim exterior admissibility, but not uniqueness.

Proposition 6.1 identifies the branch only up to first failure. It is not an existence theorem for the subsequent slip pulse, and it presupposes constant friction, one-way coupling from pressure to slip, and no healing.

## 7. The infinite-radius limit and finite-radius corrections

*This section treats the critically stressed limit, in which the criterion becomes a half-derivative test for arbitrary histories, and quantifies how far a finite radius moves the answer.*

### 7.1 The inner limit

Extending the integral \eqref{eq:kernel} to infinity and using \eqref{eq:dawsonintegral} gives

\begin{equation}
K_\infty(r,u)=\frac{A_*}{\sqrt u}\,e^{-r^2/(8\alpha u)}I_0\!\left(\frac{r^2}{8\alpha u}\right),\qquad A_*=\frac{\pi^{3/2}\sqrt\alpha}2,
\label{eq:bessel}
\end{equation}

consistent with differentiation of the known constant-rate inner solution [@viesca2025]. In particular the point-source centre velocity in this limit is

\begin{equation}
v_\infty(0,t)=\frac{4fc_p}{\pi\mu}\,A_*\,\mathcal Hq(t),
\qquad
\mathcal Hq(t)=\int_{[0,t)}\frac{dq(s)}{\sqrt{t-s}} .
\label{eq:halfderivative}
\end{equation}

The *inner model* is the limit $\Theta\to0$ on a fixed observation window $[t_0,t_1]$ with $t_0>0$. For fixed $q$, not identically zero before $t_0$, and any $a>0$, the Abel-averaged pressure is bounded below by a positive constant on $[t_0,t_1]\times\{a\}$; so once $\Theta$ is small enough the crack radius exceeds $a$ throughout the window, and by Proposition 7.2 the difference between finite-radius and inner velocities, which is the absolutely convergent integral of a bounded kernel difference, tends to zero uniformly on the window. Statements about all time in the inner model (Sections 8.1 and 8.3) are not uniform in time at fixed $\Theta$: a finite-volume history that nucleates slip always leaves full sliding eventually (Section 8.2).

**Theorem 3 (inner-limit history criterion).** In the inner model, let $q$ be causal and locally of bounded variation, and define velocities by \eqref{eq:velocity} with the kernel \eqref{eq:bessel}, as locally integrable functions of time. For each $r>0$ let $\Lambda_r$ be the probability measure on $[0,\infty)$

\begin{equation}
\Lambda_r(du)=\frac2\pi\int_0^{\pi/2}\ell_{r\sin\theta}(u)\,d\theta\;du,
\qquad
\ell_x(u)=\frac{x}{2\sqrt{\pi\alpha}\,u^{3/2}}e^{-x^2/(4\alpha u)},
\label{eq:subordinator}
\end{equation}

and $\Lambda_0=\delta_0$. Then

\begin{equation}
v_\infty(r,\cdot)=\Lambda_r*v_\infty(0,\cdot)\qquad\text{in }L^1_{\rm loc}(0,\infty).
\label{eq:transfer3}
\end{equation}

Consequently, nonnegative centre velocity for almost every $t\in(0,t_1)$ is necessary and sufficient for nonnegative velocity at every radius for almost every $t\in(0,t_1)$. Single-peakedness is not required.

Here $\ell_x$ is the density of the first time a one-dimensional diffusion with diffusivity $\alpha$ (variance $2\alpha t$) started at zero reaches distance $x$. Equation \eqref{eq:transfer3} therefore says that the velocity at radius $r$ is the centre velocity delayed by a random first-passage time to the random distance $r\sin\theta$, with $\theta$ uniform on $(0,\pi/2)$.

*Proof.* Using $e^{-y}I_0(y)=(2/\pi)\int_0^{\pi/2}e^{-2y\sin^2\theta}d\theta$ in \eqref{eq:bessel},

$$
K_\infty(r,u)=\frac2\pi\int_0^{\pi/2}\frac{A_*}{\sqrt u}\exp\!\left(-\frac{r^2\sin^2\theta}{4\alpha u}\right)d\theta .
$$

For $x>0$, the Laplace transforms

$$
\int_0^\infty e^{-su}\frac{e^{-x^2/(4\alpha u)}}{\sqrt u}\,du=\sqrt{\frac\pi s}\,e^{-x\sqrt{s/\alpha}},
\qquad
\int_0^\infty e^{-su}\ell_x(u)\,du=e^{-x\sqrt{s/\alpha}}
$$

show, by uniqueness of the Laplace transform of locally integrable functions of exponential order, that $A_*u^{-1/2}e^{-x^2/(4\alpha u)}=(\ell_x*K_\infty(0,\cdot))(u)$, and $\int\ell_x=1$. Averaging over $\theta$ gives $K_\infty(r,\cdot)=\Lambda_r*K_\infty(0,\cdot)$. Integrating against $dq$ and applying Fubini's theorem gives \eqref{eq:transfer3}; Fubini is justified on any finite window because

$$
\int_0^{t_1}\!\!\int\!\!\int K_\infty(0,t-s-u)\,\Lambda_r(du)\,|dq|(s)\,dt\le|dq|([0,t_1])\int_0^{t_1}\frac{A_*}{\sqrt y}\,dy<\infty .
$$

 Since $\Lambda_r\ge0$, nonnegativity of $v_\infty(0,\cdot)$ almost everywhere implies the same at every $r$; necessity is the case $r=0$. A common null set for all radii follows by taking rational radii first and then using continuity in $r$ at almost every $t$, which holds by dominated convergence because $0<K_\infty(r,u)\le K_\infty(0,u)$. $\square$

### 7.2 A uniform finite-radius error bound

Write $s_*=\sup_{x>0}xD(x)$. Appendix D.2 gives the numerically verified bound $s_*\le0.6424$ (the maximum, $0.642375$, is at $x\approx1.502$), whereas the cruder bound $D(x)\le1/x$ corresponds to $s_*=1$.

**Proposition 7.2.** For every $u>0$ and $0\le r<R$,

\begin{equation}
0\le K_\infty(r,u)-K_R(r,u)\le\frac{4\alpha s_*}{r}\arcsin\frac rR,
\label{eq:tailbound}
\end{equation}

with centre value $4\alpha s_*/R$. The same holds with $u+\varepsilon$ in place of $u$. Consequently, with $\mathrm{TV}_t(q)=|dq|([0,t])$,

\begin{equation}
\mathcal Hq(t)>\frac{8s_*\sqrt\alpha}{\pi^{3/2}R(t)}\,\mathrm{TV}_t(q)
\label{eq:certificate}
\end{equation}

implies a positive point-source centre margin at radius $R(t)$, and hence, for a single-peaked history, full sliding. Here $t$ is a time at which \eqref{eq:integrable} holds; since $0\le K_\infty-K_R\le4\alpha s_*/R$, this is the same as finiteness of $\int|dq|(s)/\sqrt{t-s}$.

*Proof.* The integrand of $K_\infty-K_R$ is that of \eqref{eq:kernel} over $a>R$; with $z=a/\sqrt{4\alpha u}$, $D(z)/(uz)\le s_*/(uz^2)=4\alpha s_*/a^2$, and $\int_R^\infty da/(a\sqrt{a^2-r^2})=\arcsin(r/R)/r$. For \eqref{eq:certificate}, $|\int(K_\infty-K_R)(0,t-s)\,dq(s)|\le(4\alpha s_*/R)\mathrm{TV}_t(q)$ and $4\alpha/A_*=8\sqrt\alpha/\pi^{3/2}$. $\square$

The constant $s_*$ cannot be replaced by its asymptotic value $\tfrac12$: the numerical check of Section 9.1 finds the bound with $\tfrac12$ violated by 16\%. In the constant-rate case \eqref{eq:certificate} requires $\lambda>4s_*/\pi^{3/2}\approx0.46$, that is $\Theta<1.72$ (with the cruder constant $s_*=1$, $\Theta<1.01$); it is useless in the marginally pressurised regime.

### 7.3 A two-term finite-radius criterion

The uniform bound \eqref{eq:tailbound} treats the finite-radius correction as an error of unknown sign proportional to the total variation. In fact its leading part has a definite form: it is independent of age, so it multiplies the current rate rather than the total variation.

**Proposition 7.3 (two-term centre kernel).** Let $c_D=\sup_{x>0}x^3|D(x)-1/(2x)|$; Appendix D.2 gives the numerically verified bound $c_D\le0.4115$. For $R>0$ and $u>0$,

\begin{equation}
K_R(0,u)=\frac{A_*}{\sqrt u}-\frac{2\alpha}R-\mathcal R_R(u),
\qquad
|\mathcal R_R(u)|\le\frac{16c_D\alpha^2}{3R^3}\,u .
\label{eq:twoterm}
\end{equation}

Consequently, at every time with a positive radius at which \eqref{eq:integrable} holds (for the Gaussian source, at every such time without further condition),

\begin{equation}
\Bigl|\mathcal C_\varepsilon(t)-A_*\!\int_{[0,t]}\frac{dq(s)}{\sqrt{t-s+\varepsilon}}+\frac{2\alpha}{R(t)}\,q(t)\Bigr|
\le\frac{16c_D\alpha^2}{3R(t)^3}\int_{[0,t]}(t-s+\varepsilon)\,|dq|(s).
\label{eq:twotermmargin}
\end{equation}

*Proof.* By \eqref{eq:centrekernel}, $K_\infty(0,u)-K_R(0,u)=2\sqrt{\alpha/u}\int_z^\infty D(x)\,dx/x$ with $z=R/(2\sqrt{\alpha u})$. Write $D(x)=1/(2x)+\varrho(x)$ with $|\varrho(x)|\le c_D/x^3$. Then $\int_z^\infty D(x)\,dx/x=1/(2z)+\theta c_D/(3z^3)$ with $|\theta|\le1$. Multiplying by $2\sqrt{\alpha/u}$ gives $2\alpha/R$ plus a remainder bounded by $2\sqrt{\alpha/u}\,c_D\,8(\alpha u)^{3/2}/(3R^3)=16c_D\alpha^2u/(3R^3)$. For \eqref{eq:twotermmargin}, integrate \eqref{eq:twoterm} at age $t-s+\varepsilon$ against $dq$ and use $\int_{[0,t]}dq=q(t)$; under \eqref{eq:integrable} every term is absolutely convergent. (Without \eqref{eq:integrable}, the statement holds for the integral of the combined kernel difference $K_R(0,u)-A_*u^{-1/2}+2\alpha/R$, which is bounded by $16c_D\alpha^2u/(3R^3)$.) $\square$

The remainder is small relative to the correction when $\alpha(t+\varepsilon)/R^2$ is small, that is in the critically stressed regime. In the linear-taper example of Section 9.2 the two-term root agrees with the exact first negative crossing to $10^{-4}$ in time at $\Theta=0.01$ and to $5\times10^{-3}$ at $\Theta=0.1$, and \eqref{eq:twotermmargin} turns into an enclosure of the root whenever the remainder is smaller than the correction (Table 3). The enclosure is analytic given the computed radius; the root searches themselves are not interval-certified. For a single-peaked history, a positive lower bound in \eqref{eq:twotermmargin} certifies full sliding; this is sharper than \eqref{eq:certificate} whenever the current rate is small compared with the total variation, as late in a taper.

### 7.4 Finite radius is always stricter than the inner limit

By \eqref{eq:centrekernel}, $\varrho_R(u)=K_R(0,u)/K_\infty(0,u)=G(R/(2\sqrt{\alpha u}))/G(\infty)$ strictly decreases with age. For a single-peaked history, the separation argument \eqref{eq:separation}, with the inequality reversed, gives

\begin{equation}
\mathcal C_\varepsilon(t)\le\varrho_R(u_b)\int_{[0,t]}K_\infty(0,t-s+\varepsilon)\,dq(s),
\label{eq:onesided}
\end{equation}

strictly when \eqref{eq:strictness} holds. A finite-radius fully sliding branch therefore satisfies the inner-limit condition, and an inner-limit threshold with zero margin is strictly inadmissible at every finite radius.

## 8. Consequences for injection schedules

*This section draws explicit consequences: the slowest admissible continuation in the inner limit, a time after shut-in by which full sliding must have ended, and thresholds for linear tapers.*

### 8.1 The slowest admissible continuation in the inner limit

Suppose a point source injects at $q_0>0$ until time $T$. Consider continuations for which the causal Abel inversion

\begin{equation}
q(t)=\frac1\pi\int_0^t\frac{\mathcal Hq(s)}{\sqrt{t-s}}\,ds
\label{eq:abelinversion}
\end{equation}

holds, for instance rates that are locally absolutely continuous on $(0,\infty)$ apart from the initial atom [@gorenflo1991]. Among these, the continuations with $\mathcal Hq\ge0$ almost everywhere are bounded below, almost everywhere, by

\begin{equation}
q_{\min}(t)=\frac{2q_0}{\pi}\arcsin\sqrt{\frac Tt},\qquad t\ge T,
\label{eq:arcsine}
\end{equation}

and $q_{\min}$ itself has $\mathcal Hq_{\min}=0$ on $(T,\infty)$. Indeed the first stage fixes $\mathcal Hq(s)=q_0/\sqrt s$ for $s<T$, any later nonnegative values of $\mathcal Hq$ can only increase \eqref{eq:abelinversion}, and setting them to zero gives $(q_0/\pi)\int_0^T ds/\sqrt{s(t-s)}=q_{\min}(t)$. This is the classical surface temperature of a half-space held at constant temperature and then insulated, and $\tfrac2\pi\arcsin\sqrt{T/t}$ is Lévy's arcsine law; the result is a reinterpretation of known formulae in this model. By Section 7.4 the curve \eqref{eq:arcsine} is strictly inadmissible at every finite radius. Since $q_{\min}(t)\sim2q_0\sqrt T/(\pi\sqrt t)$, its total volume is infinite.

### 8.2 Full sliding must end soon after shut-in

**Proposition 8.2 (persistence-time bound).** Let $q\ge0$ be locally integrable, with $q=0$ almost everywhere after a shut-in time $t_s$, and let $\mathcal V=\int_0^{t_s}q\,ds$. For either source,

\begin{equation}
\frac{c_p\mathcal V}{t+\varepsilon}\ \le\ p_\varepsilon(0,t)\ \le\ \frac{c_p\mathcal V}{t-t_s+\varepsilon}\qquad(t>t_s).
\label{eq:centrebound}
\end{equation}

Hence no crack radius exists at any time $t\ge t_s+fc_p\mathcal V/\tau_{\rm d}-\varepsilon$, while one exists at every $t>t_s$ with $t<fc_p\mathcal V/\tau_{\rm d}-\varepsilon$. In the settings of Theorems A and G (with $q$ continuous or jumping only as allowed there), the centre margin becomes strictly negative, and full sliding is lost, at some time before $t_s+fc_p\mathcal V/\tau_{\rm d}-\varepsilon$. After a constant-rate stage of duration $T$ followed by shut-in, the bound is

\begin{equation}
t_{\rm loss}<T\Bigl(1+\frac1\Theta\Bigr)-\varepsilon .
\label{eq:persistence}
\end{equation}

*Proof.* For $t>t_s$, $p_\varepsilon(0,t)=c_p\int_0^{t_s}q(s)(t-s+\varepsilon)^{-1}ds$ and $t-t_s+\varepsilon\le t-s+\varepsilon\le t+\varepsilon$, which gives \eqref{eq:centrebound}. A positive root of \eqref{eq:radius} exists if and only if $fp_\varepsilon(0,t)>\tau_{\rm d}$ (Section 2.4), which gives the two existence statements. If the centre margin were nonnegative up to $t_*=t_s+fc_p\mathcal V/\tau_{\rm d}-\varepsilon$, Proposition 4.1 would give a crack radius at $t_*$, a contradiction. $\square$

The window for the last time at which a crack radius exists, $[fc_p\mathcal V/\tau_{\rm d}-\varepsilon,\ t_s+fc_p\mathcal V/\tau_{\rm d}-\varepsilon]$, has width $t_s$; it is sharp when the stage is short compared with $\mathcal V fc_p/\tau_{\rm d}$. The actual loss of full sliding is usually much earlier (Section 9.2). The bound uses neither single-peakedness nor the transfer argument. It agrees with the arrest of post-injection slip [@saez2023] and with the volume-bounded maximum size in @saez2025. For a Gaussian source and a rate with an integrable tail $W=\int_{t_s}^\infty q$, the same argument gives $p_\varepsilon(0,t)\le c_p[\mathcal V/(t-t_s+\varepsilon)+W/\varepsilon]$; for a point source no tail version holds, because the centre pressure is infinite whenever the current rate is positive.

More generally, every nonnegative integrable rate that nucleates slip must eventually leave full sliding. If a fully sliding branch persisted forever, its radius would be nondecreasing and so bounded below by some $R_0>0$ after a finite time. The edge kernel obeys $0<J_{R_0}(u)\le4\alpha s_*/R_0^2$ and $J_{R_0}(u)\to0$ as $u\to\infty$, so by dominated convergence $\mathcal Ap_\varepsilon(R_0,t)=c_p\int_0^tq(s)J_{R_0}(t-s+\varepsilon)\,ds\to0$. Radial monotonicity then gives $0<\tau_{\rm d}/f=\mathcal Ap_\varepsilon(R(t),t)\le\mathcal Ap_\varepsilon(R_0,t)\to0$, a contradiction. In the inner model the corresponding statement is that a nontrivial nonnegative history with $\mathcal Hq\ge0$ forever has $q(t)\ge M/(\pi\sqrt t)$ for large $t$ by \eqref{eq:abelinversion}, so infinite volume. These conclusions concern the end of the expanding crack, not earthquake risk or the eventual locked geometry.

### 8.3 Linear tapers

Let $q=q_0$ until $T$, decrease linearly over a duration $L>0$ to $q_0(1-d)$, and then stay constant, with $0\le d\le1$. During the taper the Abel half derivative is

\begin{equation}
\mathcal Hq(t)=\frac{q_0}{\sqrt t}-\frac{2dq_0}{L}\sqrt{t-T}.
\label{eq:taperH}
\end{equation}

It decreases during the taper. After the taper, $\sqrt t\,\mathcal Hq(t)/q_0=1-(2d/L)\sqrt t\,[\sqrt{t-T}-\sqrt{t-T-L}]$, and

\begin{equation}
\sqrt t\,[\sqrt{t-T}-\sqrt{t-T-L}]=\frac{L}{\sqrt{1-T/t}+\sqrt{1-(T+L)/t}}
\label{eq:posttaper}
\end{equation}

decreases with $t$. The binding time is therefore $T+L$, and the exact all-time inner-limit criterion is

\begin{equation}
d\le d_\infty=\frac12\sqrt{\frac L{T+L}} .
\label{eq:taperthreshold}
\end{equation}

If $d>d_\infty$, the first negative crossing lies in the taper, at

\begin{equation}
t_*^\infty=\frac{T+\sqrt{T^2+(L/d)^2}}2 .
\label{eq:tapertime}
\end{equation}

For $T=L=1$, $d_\infty=1/(2\sqrt2)\approx0.353553$, and for $d=0.6$, $t_*^\infty\approx1.471825$.

**Corollary 8.4 (point source: no linear taper halves the rate).** For a point source, in the inner limit every linear taper of any duration that reduces the rate by half or more loses full sliding, since $d_\infty<\tfrac12$ for every $L$. At every finite $\Theta$ the supremum of admissible depths is strictly smaller than $d_\infty$.

*Proof.* The first statement is \eqref{eq:taperthreshold}. For the second, every taper history is single-peaked with peak $b=T$, and it is locally Lipschitz near $T+L$, so \eqref{eq:integrable} holds there. If $d\ge d_\infty$, the inner margin $A_*\mathcal Hq(T+L)$ is $\le0$ and, since both signs occur at separated ages, \eqref{eq:onesided} gives a strictly negative finite-radius margin at $T+L$. At $d=d_\infty$ the margin is therefore strictly negative. It depends continuously on $d$: the rate and its derivative depend linearly on $d$; since $q(T+L)=q_0(1-d)>0$ a positive radius exists, and $R(T+L;d)$ is continuous in $d$ by the implicit function theorem ($F_a<0$, and $F$ is continuous in $(a,d)$ for $a>0$); and $K_R(0,u)$ is continuous in $R$ with the integrable bound $A_*u^{-1/2}$. Hence the margin at $T+L$ stays negative for $d\in(d_\infty-\delta,d_\infty]$ for some $\delta>0$, and no $d>d_\infty-\delta$ is admissible. $\square$

The finite-radius part is specific to the point source. For a Gaussian source of width $\varepsilon>T+L$ it fails: since $\ell_R(u)\ge-1/u$ by \eqref{eq:A6}, $K_R(0,u_{\rm o})/K_R(0,u_{\rm y})\ge u_{\rm y}/u_{\rm o}\ge\varepsilon/(T+L+\varepsilon)$ for every pair of ages arising in the taper, so the margin is at least $q_0K_R(0,t+\varepsilon)[1-d(T+L+\varepsilon)/\varepsilon]>0$ for $d=\tfrac12$; with the strength excess small enough that slip has nucleated before $T$ and the crack persists, a half-rate taper keeps full sliding.

The point-source finite-radius threshold $d_{\max}(\Theta)$, the largest depth for which the centre margin stays nonnegative, was estimated numerically on the window $t\le50$ (Section 9.2, Figure 2A). For $\Theta\le0.1$ it is well described by the leading-order formula derived from Proposition 7.3 in Appendix D.3,

\begin{equation}
d_{\max}(\Theta)\approx d_\infty-\kappa\sqrt\Theta,
\qquad
\kappa=\frac{\sqrt L}{\pi^{3/2}}\,(1-d_\infty)\,\sqrt{\frac{2}{T+L(1-d_\infty/2)}},
\label{eq:leadingorder}
\end{equation}

with time measured in the same unit for $T$ and $L$. For $T=L=1$, $\kappa=0.12159$; the error of \eqref{eq:leadingorder} is below $0.033\,\Theta$ for $0.001\le\Theta\le0.1$. This is an asymptotic approximation checked numerically, not a theorem. For larger $\Theta$ the threshold falls faster: $d_{\max}=0.199$ at $\Theta=1$ and $0.043$ at $\Theta=10$.

### 8.4 A dimensional example

The following parameters are illustrative, not a calibrated site: diffusivity $\alpha=0.1$ m$^2$/s, wellbore radius $0.1$ m (so $\varepsilon=0.025$ s and $\varepsilon/T=1.16\times10^{-6}$), and a first stage of $T=6$ h at constant rate, giving a diffusion length $\sqrt{4\alpha T}\approx93$ m.

: Illustrative consequences for a 6 h stage. All rows except $d_{\max}$ use the Gaussian source with $\varepsilon/T=1.16\times10^{-6}$; the $d_{\max}$ row is the point-source estimate of Section 9.2. Taper times are for linear tapers of duration $L=T$; "first loss" is the first negative crossing of the centre margin.

| | $\Theta=0.1$ | $\Theta=1$ | $\Theta=10$ |
|------------------------|--------:|--------:|--------:|
| crack radius at $T$ | 214 m | 67 m | 0.63 m |
| largest abrupt drop | 0.09\% | 0.05\% | 0.0006\% |
| largest admissible taper depth $d_{\max}$ | 0.312 | 0.199 | 0.043 |
| first loss, taper to 40\% ($d=0.6$) | 8.30 h | 6.95 h | 6.00 h |
| first loss, taper to zero ($d=1$) | 6.97 h | 6.35 h | 6.00 h |
| bound after shut-in at $T$, \eqref{eq:persistence} | 66 h | 12 h | 6.6 h |

The inner-limit values are $d_\infty=0.354$ and first-loss times of 8.83 h and 7.24 h. In the marginally pressurised case the crack is only a few wellbore radii across, so a Gaussian source is a poor description there; the entries indicate only that full sliding is then lost almost as soon as the rate starts to fall.

### 8.5 What the criterion is for

For a numerical modeller, the centre margin $\mathcal C_\varepsilon(t)$ is a benchmark. A code that resolves the onset of a back front under stepped, cyclic or tapered injection should reproduce the first negative crossing of $\mathcal C_\varepsilon$ (a tangential zero, as in Section 9.3, need not produce a back front), should never show a noncentral point reversing first, and should reproduce the immediate failure of \eqref{eq:pointjump} at any downward point-source step. Table 3 and Section 9.3 supply reference values.

For an analyst using crack-like volume laws [@saez2025], the first negative crossing of $\mathcal C_\varepsilon$ (or a downward point-source jump) is the time up to which those laws apply to a given schedule, within the classes of Theorems A and G, and Proposition 8.2 gives an a priori upper bound after shut-in.

For schedule design, the results are mainly negative. Abrupt reductions larger than about $\sqrt{\varepsilon/T}$ end full sliding at once; for a point source, linear tapers cannot halve the rate; after shut-in full sliding ends within the time of Proposition 8.2; and any integrable injection history that nucleates slip ends full sliding eventually (Section 8.2), though without an explicit deadline unless injection stops. The criterion predicts when full sliding ends, not whether. It says nothing about seismic hazard: the decision-relevant quantity is how far slip spreads after the crack becomes a pulse [@saez2023], which this paper does not analyse, and keeping slip crack-like is not an established hazard objective [@ji2025].

## 9. Numerical verification

*This section reports independent numerical checks of the kernel facts, the theorems and the new thresholds. All calculations are synthetic and dimensionless; no field or laboratory data were fitted.*

### 9.1 Implementations and tolerances

Two independent implementations are used. The first evaluates kernels by adaptive quadrature (absolute and relative tolerances $2\times10^{-11}$ to $2\times10^{-9}$), and the radius by bracketing with tolerance $10^{-10}$. The second uses composite Gauss--Legendre quadrature, with panels split at every kink of the rate and on a geometric ladder around the diffusive scale $R^2/(4\alpha)$, 24 nodes per panel, the substitution $u=y^2$ to remove the $u^{-1/2}$ singularity, and radius roots to $10^{-13}$. Velocities omit the factor $4fc_p/(\pi\mu)$, and $\alpha=q_0=1$. First negative crossings are located by sampling 90 geometrically spaced times after the start of the reduction (the first sample $10^{-10}$ after it) and then bracketing the first sign change with tolerance $10^{-13}$; they are the first crossings on that sampling, not interval-arithmetic certificates.

The two implementations agree on the ten original taper roots to $3.5\times10^{-11}$. Doubling the Gauss--Legendre order changes every root of Table 3 by less than $1.5\times10^{-14}$. Separate checks confirm: one- and two-dimensional kernel quadratures to $1.1\times10^{-13}$ relative error; a 70-digit expansion of the exact moments $\mathbb EX_r^n=\frac{4^n(n!)^2}{(2n+1)!}\sum_{j}\binom nj\frac{r^{2(n-j)}\bar r^{2j}}{2j+1}$; the age order of Lemma 2 at 763 adjacent age pairs over $u\in[10^{-5},10^4]$; the moving-boundary derivative by centred differences of the slip \eqref{eq:slip}, with second-order convergence; the cap traction against a real-space fractional Laplacian; the two-term expansion \eqref{eq:twoterm}, whose remainder reaches 0.90 of its bound and whose coefficient $2\alpha/R$ replaced by $\alpha/R$ violates it; and the sharpened bound \eqref{eq:tailbound}, which reaches 0.90 of its bound, while the constant $\tfrac12$ in place of $s_*$ is violated by 16\%.

### 9.2 Finite-radius thresholds for a linear taper

Table 3 lists the first negative crossing of the centre margin for the taper $T=L=1$, $d=0.6$. In every row, sampled noncentral velocities at eight radii between $0.01R$ and $0.999R$ and the edge response were positive at the crossing, as Theorems 1 and A require. The inner-limit values are $1.471825$ (point source) and $1.610498$ (Gaussian source with $\varepsilon=0.02$).

: First negative crossing $t_*$ of the centre margin for a linear taper ($T=L=1$, $d=0.6$). $\lambda=R/(2\sqrt{t_*+\varepsilon})$. "Two-term" is the root of \eqref{eq:twotermmargin} without remainder; the enclosure is analytic given the computed radius, and is shown where the remainder bound is smaller than the correction. The last column is the smallest $f\sigma'_0/\tau_{\rm d}$ for which the Gaussian-source centre pressure stays below $\sigma'_0$.

| $\Theta$ | $\varepsilon$ | $t_*$ | $\lambda$ | two-term | enclosure | $f\sigma'_0/\tau_{\rm d}$ |
|----:|-----:|----------:|------:|----------:|---------------------:|------:|
| 0.01 | 0 | 1.444740 | 6.94 | 1.444867 | [1.44465, 1.44509] | -- |
| 0.05 | 0 | 1.409693 | 3.15 | 1.411196 | [1.40882, 1.41358] | -- |
| 0.1 | 0 | 1.381873 | 2.27 | 1.386574 | [1.38025, 1.39295] | -- |
| 0.5 | 0 | 1.251229 | 1.09 | 1.284442 | [1.22963, 1.34433] | -- |
| 1 | 0 | 1.157747 | 0.72 | 1.180910 | [1.04339, 1.40629] | -- |
| 2 | 0 | 1.062273 | 0.39 | -- | -- | -- |
| 5 | 0 | 1.003299 | 0.084 | -- | -- | -- |
| 10 | 0 | 1.000022 | 0.0069 | -- | -- | -- |
| 0.01 | 0.02 | 1.583503 | 6.82 | 1.583647 | [1.58338, 1.58391] | 350 |
| 0.05 | 0.02 | 1.548041 | 3.10 | 1.549779 | [1.54691, 1.55266] | 71 |
| 0.1 | 0.02 | 1.519317 | 2.24 | 1.524816 | [1.51715, 1.53255] | 36 |
| 0.5 | 0.02 | 1.378381 | 1.07 | 1.417371 | [1.34818, 1.49293] | 7.5 |
| 1 | 0.02 | 1.272493 | 0.71 | 1.297237 | [1.09610, 1.62024] | 3.9 |
| 2 | 0.02 | 1.155074 | 0.38 | -- | -- | 2.0 |

With $\varepsilon=0.02$ and $\Theta=5$ or $10$ the centre pressure never reaches the threshold (its maximum is $3.96\,c_pq_0$), so no slip occurs. In the marginally pressurised regime the first negative crossing comes within $10^{-3}T$ to $2\times10^{-5}T$ of the start of the taper: there the crack is much smaller than the diffusion length and responds mainly to the most recent rate change.

For the threshold $d_{\max}(\Theta)$ of Section 8.3, bisection to $2\times10^{-10}$ on the minimum over time of the centre margin (sampled at 70 times up to $t=50$ and refined by bounded minimisation) gives the finite-window numerical estimates $0.34969$, $0.34116$, $0.32496$, $0.31190$, $0.24793$, $0.19943$, $0.14256$, $0.07589$ and $0.04281$ for $\Theta=0.001,0.01,0.05,0.1,0.5,1,2,5,10$. In every case the binding time found is $T+L$, and $d_\infty$ itself gives a negative finite-radius margin, as Corollary 8.4 requires. We have no tail argument for $t>50$, so these are estimates on that window, not certified all-time thresholds.

For Proposition 8.2 we used $q=1$ on $[0,1]$, $q=\cos^2(\pi(t-1)/2)$ on $[1,2]$ and $q=0$ afterwards ($\mathcal V=1.5$, $\Theta=0.1$). The centre pressure satisfied \eqref{eq:centrebound} at 60 times up to $t=30$. The last time a crack radius exists is $15.780$ (point source) and $15.760$ ($\varepsilon=0.02$), inside the proved windows $[15,17]$ and $[14.98,16.98]$, while full sliding was already lost at $t=1.2508$ and $1.3189$.

### 9.3 Tests close to threshold

**Two dips with a tangential centre zero (Theorems A and B).** Take a point source, $\Theta=0.05$, and $q(t)=1-\kappa[\phi(t-1)+\phi(t-3)]$ with $\phi(x)=\sin^2(\pi x)$ on $[0,1]$ and zero elsewhere. This $C^1$ rate falls and recovers twice. Bisection on $\kappa$ gives the depth $\kappa_*=0.1702426$ at which the minimum of the centre margin is zero; it occurs during the second dip, at $t_c=3.370023$, with centre margin $7\times10^{-14}$ and radius $11.586$. At that instant the noncentral velocities at $r/R=0.01,0.05,0.1,0.3,0.6,0.9,0.99$ are $0.140$, $0.604$, $0.891$, $0.733$, $0.272$, $0.080$ and $0.023$, and the edge response is $0.0136$: all strictly positive while the centre is at zero. The centre margin then recovers (values $1.23$, $1.11$, $1.05$ at $t=4.8,5.5,6$), and the radius increased at all 120 sampled times. With dips one per cent deeper, the centre margin becomes negative ($-0.013$). Figure 2B shows the history.

**Stepped Gaussian schedule (Theorem G with jumps).** Take $\varepsilon=0.02$, $\Theta=0.1$, and rate levels $1$, $1-a$, $1$, $1-a$, $1$ on successive unit intervals. The largest step compatible with full sliding is $a_*=0.07183$, limited by the second drop at $t=3$, although the single-drop tolerance \eqref{eq:droptolerance} at $t=1$ is $0.1197$: earlier drops reduce the tolerance of later ones. With $a=0.9a_*$ all sampled right and left centre margins were positive (minimum $0.134$ after normalisation by $K_R(0,\varepsilon)$), noncentral velocities and edge responses were positive at all sampled times, both one-sided, and the radius never decreased. With $a=1.05a_*$ the margin becomes negative at $t=3$. Figure 2C shows the margin.

**Point source with an upward jump (Theorem A).** With levels $0.5$ then $1$ (jump at $t=1$), a later $\sin^2$ dip of depth $0.05$ and $\Theta=0.05$, all sampled centre margins, noncentral velocities and edge responses were positive and the radius increased. The edge response jumps by $0.047073$ at $t=1$, matching the predicted $a_1J_R(0^+)=0.5\cdot2\alpha/R^2$ to $3\times10^{-11}$.

**Downward point-source jump.** For a drop from $1$ to $0.7$ at $T=1$ with $\Theta=0.1$, the ratio of the centre margin to $-jA_*(t-T)^{-1/2}$ is $0.9705$, $0.99705$, $0.999705$ and $0.99997$ at $t-T=10^{-4},10^{-6},10^{-8},10^{-10}$, confirming \eqref{eq:pointjump}.

### 9.4 Counterexamples to stronger statements

**Pairwise radial order.** With $R=\alpha=1$, the ratio $K_R(r,0.01)/K_R(r,0.001)$ is $0.3002$ at the centre, rises to $1.186$ at $r\approx0.27$, and falls to $1.019$ near the rim. The centre is the minimum, as Lemma 2 requires, but the ratio is not monotone in $r$; the kernel family is not totally positive of order two in $(r,u)$.

**An instantaneous centre test for a general history.** Take rate levels $1$, $0$, $0.15$ with jumps at $0$, $0.5$ and $0.9$. At $t=1$, in the inner limit and after a common positive normalisation, the velocities are $0.0601281$ at $r=0$, $-0.0396188$ at $r=0.8$ and $-0.0383173$ at $r=1$. The same failure occurs at $R=30$ with $\varepsilon=0.01$ and the stress-injection parameter $\Theta=0.001146335375$ that makes $R=30$ the exact radius: the velocities are $0.1208972$, $-0.1081508$ and $-0.1043745$. The history had already lost full sliding after its first drop; the example shows only that a positive centre value after an earlier negative interval certifies nothing, in agreement with the historical form of Theorems 3, A and G.

**Gaussian mixtures and an annular source.** For the mixtures $\tfrac12(\rho_{0.001}+\rho_3)$, $0.2\rho_{10^{-4}}+0.3\rho_{0.05}+0.5\rho_5$ and $\tfrac12(\rho_0+\rho_2)$, the ratio $\bar K_R(r,u)/\bar K_R(0,u)$ was nondecreasing on 400 ages in $[10^{-4},10^2]$ at five radii, as Proposition 3.3 requires. For the nonnegative annular source $\rho\propto\rho_{0.1}-0.1\rho_{0.01}$, which vanishes at the centre, the ratio decreases with age by up to 21\% of its maximum. Take a unit step at time zero, evaluate at $t=u_{\rm o}=0.0527$, and drop the rate at age $u_{\rm y}=10^{-4}$ before $t$ by the amount $j=\bar K_1(0,u_{\rm o})/\bar K_1(0,u_{\rm y})\approx0.9818$, which makes the centre margin at radius $R=1$ vanish; then choose $\Theta\approx0.1361$ so that $R=1$ solves the radius equation (with $F>0$ inside the disk). The velocity at $r=0.5$ is $-0.864$ while the centre velocity is zero. A second annular profile, $\rho\propto\rho_{0.02}-0.5\rho_{0.01}$, gives the same conclusion. This shows that the instantaneous centre test is not sufficient for annular sources.

We also followed this example in time with $\Theta$ fixed. Before the drop the history is a single positive step, every kernel contribution is positive, and at the sampled times from $t=0.031$ until the drop the radius equation has a single root and all sampled velocities are positive (minimum $0.37$). At the drop itself, with the recomputed radius $1.000025$, the ring at $r\approx0.34R$ has velocity $-1.095$ while the centre velocity is still positive ($0.0118$). These finite samples are numerical evidence that, on this branch segment, full sliding is lost away from the centre while the centre still slides; they do not provide continuous-time control of the branch or of the roots. Earlier, around $t\approx0.022$--$0.027$, the radius equation has two roots (the annular pressure is not radially decreasing), so the circular branch is not well defined from the start; we therefore do not claim a full trajectory counterexample to a historical theorem.

### 9.5 Figures

![Synthetic verification of the instantaneous criterion. Dimensionless units $\alpha=q_0=T=L=1$; velocities divided by $4fc_p/(\pi\mu)$. A: the ratio of Lemma 2 increases with response age. B: centre margins for a Gaussian source ($\varepsilon=0.02$) and a 60\% linear taper, at three values of $\Theta$; the dashed curve is the inner limit with the same source. C: velocity profiles around the first negative crossing of the centre margin at $\Theta=0.1$, $\varepsilon=0.02$; the profile after the zero is only the formal trial branch. D: the slowest admissible continuation in the inner limit, equation \eqref{eq:arcsine}.](numerics/fault_locking_results.png)

![Finite-radius thresholds and extended history classes. Dimensionless units $\alpha=q_0=1$, time in units of the first stage. A: largest admissible linear-taper depth over $L=T$ against $\Theta$, with the leading-order formula \eqref{eq:leadingorder} and the inner limit $d_\infty$. B: two-dip point-source history tuned to a tangential centre zero (dotted line), with recovery afterwards ($\Theta=0.05$). C: right-continuous centre margin $\mathcal C_\varepsilon(t)/K_{R(t)}(0,\varepsilon)$ for the stepped Gaussian schedule. D: largest abrupt relative drop against source width, equation \eqref{eq:droptolerance}, with the upper bound $\sqrt{\varepsilon/(T+\varepsilon)}$.](numerics/extension_results.png)

## 10. Discussion

*This section relates the results to previous work, collects the limitations of the model in one place, and lists open problems.*

### 10.1 Relation to previous work

The circular, constant-friction, zero-fracture-energy rupture model with zero Poisson ratio, its zero-stress-intensity radius condition \eqref{eq:radius}, the circular inversion \eqref{eq:slip} and the critically stressed and marginally pressurised asymptotics are due to Sáez, Lecampion, Bhattacharya and Viesca [-@saez2022], building on the plane-strain analyses of Garagash and Germanovich [-@garagash2012] and Bhattacharya and Viesca [-@bhattacharya2019]. Our $\Theta$ is their stress-injection parameter. The axisymmetric crack inversion itself is classical [@sneddon1946]. Self-similar fault slip under constant-pressure injection was analysed by Viesca [-@viesca2021], and under constant-rate injection by Viesca [-@viesca2025]; the Bessel kernel \eqref{eq:bessel} follows from the inner solution of the latter. Volume laws for variable injection, conditional on crack-like behaviour, are in @saez2025, which also identifies the source conditions for pulse formation as unresolved. Post-injection slip, the immediate locking of the injection point at shut-in, and the subsequent pulse were analysed by Sáez and Lecampion [-@saez2023; see also @saez2023thesis] for the circular model and by Jacquey and Viesca [-@jacquey2023] for the plane-strain constant-pressure problem. Slip weakening was added in @saez2024, and rate effects on fault stability are discussed in @alghannam2020. Laboratory measurements of slip-front propagation [@passelegue2026] support the fracture-mechanics description but do not test the present criterion, and field studies of post-injection hazard [@ji2025] stress hydraulic connectivity and poroelastic stresses that are outside this model.

Our results are consistent with these: \eqref{eq:pointjump} reproduces the immediate centre locking at point-source shut-in in @saez2023; Theorem B turns the observation that the injection point stops first into a theorem about the first loss of full sliding for graded, stepped and multi-peaked schedules, within its startup classes; and Proposition 8.2 matches post-injection arrest and the volume-bounded size of @saez2023 and @saez2025. The plane-strain constant-pressure case of @jacquey2023 is not covered.

On the mathematical side, the single-crossing argument of Lemma 2 is of the variation-diminishing type, and monotonicity rules for ratios of Laplace transforms are classical [@yang2019]. Complete monotonicity and log-convexity of the centre kernel (Appendix A) are standard consequences of a positive exponential representation. The positive transfer of Appendix B belongs to the theory of positivity for Volterra operators with log-convex kernels; see, for example, Friedman [-@friedman1963] and Gripenberg [-@gripenberg1978] for convolution kernels, Clément and Nohel [-@clement1981] for completely positive kernels, the monograph of Gripenberg, Londen and Staffans [-@gripenberg1990] for the general (including nonconvolution) theory of positive resolvents, as background for a log-convexity condition of the form $A(v,s)A(t,w)\le A(t,s)A(v,w)$ for $s\le w\le v\le t$ (we do not rely on a specific theorem from these works), and the Kaluza--Jurkat coefficient criterion for a discrete analogue [@baricz2011; @feng2024]. Appendix B gives a self-contained proof of the two-kernel factorisation used here; the hypotheses it needs for this kernel are verified in Appendix A (equations \eqref{eq:A3}, \eqref{eq:A4}, \eqref{eq:A6} and \eqref{eq:A7}) and in Lemma 2. The inner-limit transfer of Theorem 3 is subordination by one-sided stable first-passage laws, and \eqref{eq:arcsine} is the arcsine law; Abel inversion is classical [@gorenflo1991].

The new content is therefore: the centre-relative Dawson-kernel order (Lemma 2) and its exact finite-radius consequences, including the mixture extension (Proposition 3.3) and its failure for annular sources; the strict-mass argument that allows earlier tangential centre zeros (Appendix B.5); the normalised continuation through the unslipped interval for a Gaussian source (Appendix C.1); the extensions to stepped rates and the persistence of the crack radius (Theorems A and G, Proposition 4.1); and the explicit finite-radius and schedule consequences of Sections 5, 7 and 8. We did not locate an earlier statement of these criteria, but cannot exclude one in work we have not seen.

### 10.2 Scope and limitations

All results concern the first loss of full sliding in the circular model with zero Poisson ratio, uniform constant friction, zero fracture energy, a homogeneous permeable layer, one-way coupling from pressure to slip and no healing. They identify the irreversible branch up to its first failure; they do not solve the subsequent evolution, in which a locked region grows and slip continues as a pulse. A zero of the centre margin is a threshold contact; a transverse negative crossing proves only that the crack branch is no longer admissible, not that a locked patch of particular size forms.

For the point source, the pressure is infinite at the centre during injection, so the constant-friction, no-opening idealisation fails there; point-source statements are elastic statements on $r>0$ (Section 3.1), and the Gaussian-source results are the physically primary ones. For a Gaussian source, full Coulomb admissibility additionally requires $\tau_0\ge0$ and $p_\varepsilon<\sigma'_0$. On a finite time window this can be arranged by taking $\sigma'_0$ large while raising $\tau_0$ to keep $\tau_{\rm d}$ fixed; Table 3 lists the required $f\sigma'_0/\tau_{\rm d}$ at the first negative crossings. Constant positive Gaussian injection has $p_\varepsilon(0,t)=c_pq_0\log(1+t/\varepsilon)$, so no such statement holds for all time.

Nonzero Poisson ratio makes the rupture quasi-elliptical [@saez2022] and replaces the scalar operator $\mathfrak T$, on which the circular inversion and Lemma 2 depend. Annular sources violate the age order (Section 9.4), so the centre-first conclusion is source-profile dependent. Finite wellbore boundary conditions, hydraulic anisotropy, heterogeneous prestress, finite fracture energy [@saez2024], dilatancy, poroelastic coupling and rate-and-state friction may change both the geometry and the ordering, and are not treated. The historical criteria use the startup conditions stated in Theorems A and G. The numerical results are synthetic; the dimensional example is illustrative.

### 10.3 Implications

Within the model and the stated classes, the centre margin is the single number that decides full sliding, and its first negative crossing (or a downward point-source jump) dates the end of crack-like behaviour exactly; a zero alone is only a threshold contact. For a modeller this is a benchmark; for users of crack-like volume laws it is a validity limit; for schedule design it shows that the end of full sliding is generic. Abrupt reductions above roughly $\sqrt{\varepsilon/T}$, about $10^{-3}$ at wellbore scale, end it at once; for a point source, linear tapers cannot halve the rate without ending it; after shut-in it ends within the time of Proposition 8.2; and any integrable history that nucleates slip ends it eventually. The criterion therefore predicts when full sliding ends, not whether, and its consequences for hazard depend on the post-locking pulse, which is not analysed here.

### 10.4 Open problems

1. Gaussian histories whose centre pressure decreases before nucleation, and tangential nucleation (Theorem G).
2. The post-locking free-boundary problem: existence of a locked neighbourhood of the centre after a transverse crossing, its growth rate, and bounds on the final slip radius.
3. Source profiles: a characterisation of the radial sources for which Lemma 2 holds (Proposition 3.3 covers Gaussian mixtures; Section 9.4 shows that annular sources fail), and the case of a finite wellbore with a flux or pressure boundary condition.
4. A historical (moving-radius) version of Proposition 3.3 for Gaussian mixtures.
5. Nonzero Poisson ratio and the plane-strain analogue with Hilbert-transform inversion.
6. The finite-radius minimal continuation, solving $\mathcal C_\varepsilon=0$ jointly with \eqref{eq:radius}, and a proof of the leading-order formula \eqref{eq:leadingorder}.

\appendix

## Appendix A. Properties of the centre kernel

\setcounter{equation}{0}
\renewcommand{\theequation}{A.\arabic{equation}}\renewcommand{\theHequation}{A.\arabic{equation}}

*Reading guide.* This appendix proves three properties of the centre kernel $K_R(0,u)$ used by the historical theorems: the value $G(\infty)$, complete monotonicity in age (so log-convexity), and the fact that its logarithmic age slope increases with radius (Lemma A.2). Section A.4 gives the detailed proof of Lemma 2. Nothing here depends on the injection history.

### A.1 Two identities

Equation \eqref{eq:dawsonintegral} follows from $D(z)=\int_0^ze^{-(z^2-y^2)}dy$ with $y\mapsto zy$. By Tonelli's theorem and $\int_0^\infty e^{-x^2w}dx=\tfrac{\sqrt\pi}2w^{-1/2}$,

\begin{equation}
G(\infty)=\int_0^\infty\frac{D(x)}x\,dx=\frac{\sqrt\pi}2\int_0^1\frac{dy}{\sqrt{1-y^2}}=\frac{\pi^{3/2}}4 .
\label{eq:A1}
\end{equation}

The sine-transform identity $D(x)=\tfrac12\int_0^\infty e^{-k^2/4}\sin(xk)\,dk$ will also be used.

### A.2 Complete monotonicity in age

Insert the sine transform into $G$ and change variables $k\mapsto2\sqrt{\alpha u}\,k$:

\begin{equation}
K_R(0,u)=2\alpha\int_0^\infty e^{-\alpha uk^2}\operatorname{Si}(kR)\,dk,
\qquad
\operatorname{Si}(x)=\int_0^x\frac{\sin y}y\,dy .
\label{eq:A3}
\end{equation}

The interchange of integrals is legitimate for $u>0$: after integrating $\sin(xk)/x$ over $x\in(0,R/(2\sqrt{\alpha u}))$ one obtains the bounded function $\operatorname{Si}$, which tends to $\pi/2$, and $e^{-\alpha uk^2}$ makes the $k$-integral absolutely convergent. Moreover $\operatorname{Si}(x)>0$ for $x>0$, because the successive half-period areas of $\sin y/y$ alternate in sign, decrease in magnitude and start positive. Thus $K_R(0,\cdot)$ is a positive mixture of decaying exponentials, hence completely monotone and log-convex. In particular,

\begin{equation}
\ell_R(u):=\partial_u\log K_R(0,u)\quad\text{is nondecreasing in }u .
\label{eq:A4}
\end{equation}

(The variance of the exponent under the normalised positive measure in \eqref{eq:A3} equals $\partial_u\ell_R\ge0$.)

### A.3 The logarithmic age slope increases with radius

**Lemma A.2.** The function $e(z)=D(z)/G(z)$ decreases strictly from $1$ to $0$ on $(0,\infty)$.

*Proof.* Let $\Psi=G/D$, which is positive and smooth on $(0,\infty)$. Dawson's equation $D'=1-2zD$ and $G'=D/z$ give

$$
\Psi'=\frac1z-\Psi\,\frac{D'}D .
$$

*Step 1 (near zero).* From $D=z-\tfrac23z^3+O(z^5)$ and $G=z-\tfrac29z^3+O(z^5)$, $\Psi=1+\tfrac49z^2+O(z^4)$, so $\Psi'=\tfrac89z+O(z^3)$, and there is $\eta>0$ with $\Psi'>0$ on $(0,\eta)$.

*Step 2 (at a stationary point).* Suppose $\Psi'(z_0)=0$ at some $z_0>0$, and put $a=z_0D'(z_0)/D(z_0)$. The stationary-point equation gives $\Psi=1/a$, so $a>0$. Differentiating $\Psi'$ and using $\Psi'(z_0)=0$,

$$
\Psi''=-\frac1{z^2}-\Psi\Bigl(\frac{D''}D-\frac{D'^2}{D^2}\Bigr).
$$

Since $D''=-2D-2zD'$, we have $D''/D=-2-2a$, and $(D'/D)^2=a^2/z^2$; hence

\begin{equation}
\Psi''(z_0)=\frac{a-1}{z_0^2}+2+\frac2a .
\label{eq:A5}
\end{equation}

Because $0<D(z)<z$ for $z>0$, $a=z/D-2z^2>1-2z^2$, so $(a-1)/z_0^2>-2$ and $\Psi''(z_0)>2/a>0$.

*Step 3 (no stationary point).* If $\Psi'$ vanished somewhere, let $z_*=\inf\{z\ge\eta:\Psi'(z)=0\}$. Then $z_*>0$, $\Psi'(z_*)=0$ by continuity, and $\Psi'>0$ on $(0,z_*)$. Hence $\Psi''(z_*)=\lim_{z\uparrow z_*}(\Psi'(z_*)-\Psi'(z))/(z_*-z)\le0$, contradicting Step 2. So $\Psi'>0$ on $(0,\infty)$ and $e=1/\Psi$ strictly decreases. The limit $e\to1$ at zero follows from Step 1; $e\to0$ at infinity follows from $D(z)\le1/z$ and $G(z)\uparrow\pi^{3/2}/4$. $\square$

With $z=R/(2\sqrt{\alpha u})$ and $\partial_uz=-z/(2u)$, \eqref{eq:centrekernel} gives

\begin{equation}
\ell_R(u)=-\frac{1+e(z)}{2u},\qquad
-\frac1u<\ell_R(u)<-\frac1{2u},\qquad
\partial_R\ell_R(u)>0 .
\label{eq:A6}
\end{equation}

Thus $\ell_R(u)$ increases in both $u$ and $R$. Finally, from \eqref{eq:edgekernel},

\begin{equation}
\frac{J_R(u)}{K_R(0,u)}=\frac{e(z)}R\quad\text{strictly increases with age } u,
\label{eq:A7}
\end{equation}

which is the edge counterpart of Lemma 2.

### A.4 Proof of Lemma 2

*Proof of Lemma 2.* Set $\bar r=\sqrt{R^2-r^2}$ and $\xi=(4\alpha u)^{-1}$. The identity

\begin{equation}
\frac{D(z)}z=\int_0^1e^{-z^2(1-y^2)}\,dy
\label{eq:dawsonintegral}
\end{equation}

and the substitution $x=\sqrt{a^2-r^2}$ in \eqref{eq:kernel} give

\begin{equation}
K_R(r,u)=\frac{\bar r}{u}M_r(\xi),\qquad
M_r(\xi)=\mathbb Ee^{-\xi X_r},\qquad
X_r=(r^2+\bar r^2Z^2)(1-Y^2),
\label{eq:laplace}
\end{equation}

where $Z,Y$ are independent and uniform on $[0,1]$. With the same $Z,Y$ for every radius,

\begin{equation}
X_r-X_0=r^2(1-Z^2)(1-Y^2)>0\quad\text{almost surely}.
\label{eq:coupling}
\end{equation}

Hence $c(\xi)=M_r(\xi)/M_0(\xi)$ lies strictly between zero and one for $\xi>0$.

The product-density formula gives the densities of $X_r$ and $X_0$ on $(0,R^2)$:

\begin{equation}
\varphi_r(s)=\frac1{4\bar r}\int_{\max(r^2,s)}^{R^2}\frac{dp}{\sqrt{p-r^2}\,\sqrt p\,\sqrt{p-s}},
\qquad
\varphi_0(s)=\frac{\arccos(\sqrt s/R)}{2R\sqrt s}.
\label{eq:densities}
\end{equation}

On $(0,r^2)$ the lower limit is $r^2$, so $\varphi_r$ strictly increases in $s$, while $\varphi_0$ strictly decreases. The ratio $\varphi_r/\varphi_0$ tends to zero as $s\downarrow0$, and to infinity as $s\uparrow r^2$, because $\varphi_r(s)\to\infty$ there (a logarithmic, integrable singularity). On $(r^2,R^2)$ both integrals in \eqref{eq:densities}, after $p=s+y^2$, run over the same range, and comparing integrands gives

\begin{equation}
\frac{\varphi_r(s)}{\varphi_0(s)}>\frac R{\bar r}>1 .
\label{eq:ratiobound}
\end{equation}

Therefore for every $0<c\le1$ the function $\varphi_r-c\varphi_0$ changes sign exactly once, from negative to positive, at a point $s_c\in(0,r^2)$. Take $c=c(\xi)$. By definition,

\begin{equation}
\int_0^{R^2}e^{-\xi s}\bigl(\varphi_r-c\varphi_0\bigr)(s)\,ds=0 .
\label{eq:balance}
\end{equation}

All measures have bounded support, so we may differentiate under the integral. Subtracting $s_c$ times \eqref{eq:balance},

\begin{equation}
c'(\xi)=-\frac1{M_0(\xi)}\int_0^{R^2}(s-s_c)\,e^{-\xi s}\bigl(\varphi_r-c\varphi_0\bigr)(s)\,ds<0,
\label{eq:derivative}
\end{equation}

since $(s-s_c)(\varphi_r-c\varphi_0)\ge0$, and it is positive on a set of positive measure because $\varphi_r\not\equiv c\varphi_0$. As $\xi$ decreases with $u$ and $K_R(r,u)/K_R(0,u)=(\bar r/R)\,c(\xi)$, the lemma follows. $\square$

## Appendix B. Proof of Theorems A and B and of Proposition 4.1

\setcounter{equation}{0}
\renewcommand{\theequation}{B.\arabic{equation}}\renewcommand{\theHequation}{B.\arabic{equation}}

*Reading guide.* The proof has four steps. (B.2) Along any nondecreasing radius path, the velocity at an off-centre point or at the edge is a positive combination of present and past values of the centre margin, for an auxiliary source of small width $\eta$. (B.3--B.4) Startup and the limit $\eta\to0$ are controlled uniformly. (B.5) A definite part of that positive combination samples the start of injection, where the centre margin is strictly positive; this makes noncentral velocities strictly positive even after earlier centre zeros. (B.6) A first-zero argument for the edge response shows that the radius path really is nondecreasing, which closes the circle. B.7 proves Proposition 4.1 and B.8 adds rate jumps. Sections B.2--B.6 are written for rates that are $C^1$ on $[0,T]$; B.8 lists the changes for jumps.

### B.1 Setting

Throughout, $\varepsilon=0$ for the physical source and $\eta>0$ denotes the auxiliary age shift. Write $\mathcal C(t)=\mathcal C_0(t)$, $M=\sup|q'|$, and $q_0=q(0)$. Physical velocity is $4fc_pV/(\pi\mu)$.

### B.2 Positive transfer along a nondecreasing radius path

This step is an auxiliary statement about a prescribed path. Fix $t>0$ and let

\begin{equation}
R\in C([0,t]),\qquad R(s)>0\ (s>0),\qquad R\ \text{nondecreasing};
\label{eq:B1}
\end{equation}

$R(0)$ may be zero. For $\eta>0$ put $A_\eta(v,s)=K_{R(v)}(0,v-s+\eta)$ for $0\le s\le v\le t$. Let the output kernel $\beta(u)$ be either $K_{R(t)}(r,u)$ for a fixed $0<r<R(t)$, or $J_{R(t)}(u)$, and put $\Phi(u)=\beta(u)/K_{R(t)}(0,u)$, $k_\eta=\Phi(\eta)$. By Lemma 2 and \eqref{eq:A7}, $\Phi'>0$.

**Proposition B.1.** There is a nonnegative kernel $h_\eta(t,v)$ such that for every $0\le s\le t$

\begin{equation}
\beta(t-s+\eta)=k_\eta A_\eta(t,s)+\int_s^th_\eta(t,v)A_\eta(v,s)\,dv .
\label{eq:B2}
\end{equation}

*Proof.* Suppress $t,\eta$. Let $\zeta$ solve the backward Volterra equation

\begin{equation}
\begin{aligned}
\zeta(s)&=A(t,s)\,\Phi'(t-s+\eta)+\int_s^tP(s,v)\zeta(v)\,dv,\\
P(s,v)&=\frac{A(v,s)}{A(v,v)}\bigl[\ell_{R(t)}(t-s+\eta)-\ell_{R(v)}(v-s+\eta)\bigr].
\end{aligned}
\label{eq:B3}
\end{equation}

The bracket is nonnegative by \eqref{eq:A4}, \eqref{eq:A6} and monotonicity of $R$; this is exactly the nonconvolution log-convexity $A(v,s)A(t,w)\le A(t,s)A(v,w)$ for $s\le w\le v\le t$. Since the centre kernel decreases with age, $A(v,s)/A(v,v)\le1$, and \eqref{eq:A6} gives $0\le P\le1/\eta$. The forcing is continuous and positive, so the Neumann series converges and gives a bounded nonnegative $\zeta$ (its iterates are bounded by the exponential-series majorant). If $R(0)=0$ the ratios extend continuously to the corner, using $K_R(0,u)\sim R/u$ as $R\downarrow0$.

For $s>0$ put $h(t,s)=\zeta(s)/A(s,s)$, locally integrable away from zero. Dividing the right side of \eqref{eq:B2} by $A(t,s)$ and differentiating in $s$ gives $-\Phi'(t-s+\eta)$ by \eqref{eq:B3}, and its value at $s=t$ is $\Phi(\eta)$; this proves \eqref{eq:B2} for $s>0$. Since $0\le h(t,v)A(v,s)\le\zeta(v)$ for $s\le v$, dominated convergence extends \eqref{eq:B2} to $s=0$. No integrability of $h$ at zero is needed. $\square$

For any finite signed measure $dQ$ on $[0,t]$ define $\mathcal C^Q_\eta(v)=\int_{[0,v]}A_\eta(v,s)\,dQ(s)$. Fubini's theorem in \eqref{eq:B2} gives the *positive causal transfer*

\begin{equation}
\int_{[0,t]}\beta(t-s+\eta)\,dQ(s)=k_\eta\,\mathcal C^Q_\eta(t)+\int_0^th_\eta(t,v)\,\mathcal C^Q_\eta(v)\,dv,
\label{eq:B9}
\end{equation}

with absolute integrability from Tonelli's theorem applied with $|dQ|$: the left side is at most $|dQ|([0,t])\max_{\eta\le u\le t+\eta}\beta(u)$. Atoms of $dQ$ at positive times are allowed; the endpoint convention for atoms at $v$ is immaterial because the $v$-integral is a Lebesgue integral.

### B.3 Startup

For either startup condition the point-source radius is continuous with $R(0^+)=0$: for any $a>0$, $J_a(u)\le4\alpha s_*/a^2$ gives $\mathcal Ap(a,s)\le4\alpha s_*c_pa^{-2}\int_0^sq\to0$, so the root eventually lies below $a$. At positive times continuity and differentiability follow from the strictly decreasing Abel average and the implicit function theorem.

If $q_0>0$, then

\begin{equation}
R(s)=\gamma_0\sqrt s\,[1+o(1)]\qquad(s\downarrow0)
\label{eq:B4}
\end{equation}

for some $\gamma_0>0$. Indeed, with $a=x\sqrt s$, the Abel-averaged pressure converges uniformly on compact $x$-intervals to the constant-rate value for $q_0$, which decreases continuously from infinity to zero with a simple root; the correction from $q(u)-q_0=O(u)$ is $O(s)$ uniformly on compact $x$-sets, because the Abel weight is integrable against the logarithmic singularity of the exponential integral at small $x$.

The coupling \eqref{eq:coupling} gives

\begin{equation}
\frac{K_R(r,u)}{\sqrt{R^2-r^2}}\le\frac{K_R(0,u)}R .
\label{eq:B5}
\end{equation}

When $q_0>0$ the initial atom's contribution to $V(r,s)/\sqrt{R^2-r^2}$ is $q_0/s$ times a positive continuous function of $r/R\in[0,1]$, so by \eqref{eq:B4} it is bounded below by a positive multiple of $1/s$. By \eqref{eq:B5} and $K_R(0,u)\le A_*u^{-1/2}$ the $q'$ contribution is at most $2MA_*\sqrt s/R(s)=O(1)$. Hence all velocities, including the edge-normalised one, are strictly positive for small $s$. In the monotone-ramp case every increment up to $t_{\rm start}$ is nonnegative with positive total mass $q(s)$, so positivity on $(0,t_{\rm start}]$ is immediate.

Write $Y_\eta(s)=K_{R(s)}(0,s+\eta)$. The auxiliary centre history along the physical radius is

\begin{equation}
\mathcal C_\eta(s)=q_0Y_\eta(s)+\int_0^sq'(a)\,K_{R(s)}(0,s-a+\eta)\,da .
\label{eq:B6}
\end{equation}

If $q_0>0$, \eqref{eq:B4} gives $c_-\sqrt s\le R(s)\le c_+\sqrt s$ for small $s$, and there is $B$ with

\begin{equation}
\frac{\int_0^sK_{R(s)}(0,u+\eta)\,du}{K_{R(s)}(0,s+\eta)}\le Bs
\label{eq:B7}
\end{equation}

for all small $s>0$, uniformly in $\eta>0$. For $\eta\le s$, bound the numerator by $2A_*\sqrt s$ and the denominator below by $c/\sqrt s$, since $s+\eta\le2s$ and $R(s)\ge c_-\sqrt s$. For $\eta\ge s$, use $K_R(0,u)\le R/u$ in the numerator, and in the denominator the representation $K_R(0,u)=Ru^{-1}\int_0^1D(Rx/(2\sqrt{\alpha u}))/(Rx/(2\sqrt{\alpha u}))\,dx$, which is at least a positive multiple of $R/(s+\eta)$ because $R(s)\le c_+\sqrt s$. Choosing $s_0$ with $MBs_0\le q_0/2$,

\begin{equation}
\mathcal C_\eta(s)\ge\tfrac12q_0Y_\eta(s)>0,\qquad0<s\le s_0,
\label{eq:B8}
\end{equation}

uniformly in $\eta$. In the monotone-ramp case $\mathcal C_\eta>0$ on $(0,t_{\rm start}]$ directly.

### B.4 Uniform control as $\eta\to0$

For every $\delta_0>0$,

\begin{equation}
\sup_{\delta_0\le s\le T}|\mathcal C_\eta(s)-\mathcal C(s)|\le q_0A_*\eta\,\delta_0^{-3/2}+2A_*M\sqrt\eta,
\label{eq:B10}
\end{equation}

using $|\partial_uK_R(0,u)|\le K_R(0,u)/u\le A_*u^{-3/2}$ (from \eqref{eq:A6}) for the atom, and $\int_0^s[K_R(0,u)-K_R(0,u+\eta)]\,du\le\int_0^\eta K_R(0,u)\,du\le2A_*\sqrt\eta$ for the rest, with the radius held at $R(s)$.

For the test input $dQ=ds$, $\int_0^sK_{R(s)}(0,u+\eta)\,du\ge\int_0^{\delta_0}K_{R(\delta_0)}(0,u+\eta_0)\,du=:m_{\delta_0}>0$ for $s\ge\delta_0$ and $\eta\le\eta_0$, because $R$ is nondecreasing. Then \eqref{eq:B9} gives

\begin{equation}
\int_{\delta_0}^th_\eta(t,v)\,dv\le\frac1{m_{\delta_0}}\int_0^t\beta(u+\eta)\,du\le C_{\delta_0},
\label{eq:B11}
\end{equation}

uniformly as $\eta\to0$, since $\beta(u)\le A_*u^{-1/2}$ for an interior output and $J_R(u)\le4\alpha s_*/R^2$ for the edge. Also $k_\eta\le1$ (interior) or $k_\eta\le1/R(t)$ (edge).

### B.5 Strict positivity after earlier centre zeros

Fix $t>0$, assume $\mathcal C(s)\ge0$ for $0<s\le t$, and let $R$ be nondecreasing on $[0,t]$. Choose $0<t_d<t$ inside the startup interval of B.3 and a comparator measure $dQ_+$ supported in $[0,\tau]$, $\tau<t_d$: $dQ_+=\delta_0$ if $q_0>0$, or $dQ_+=\mathbf 1_{[0,\tau]}q'(a)\,da$ in the ramp case, which has mass $q(\tau)>0$. Put

\begin{equation}
U_\eta(v)=\int_{[0,v]}A_\eta(v,a)\,dQ_+(a),\qquad W_\eta(t)=\int_{[0,\tau]}\beta(t-a+\eta)\,dQ_+(a).
\label{eq:B12}
\end{equation}

On $(0,t_d]$, $\mathcal C_\eta\ge m_0U_\eta$ with $m_0=q_0/2$ (by \eqref{eq:B8}) or $m_0=1$ (ramp case, since the comparator truncates nonnegative increments).

For $a<t_d\le v\le t$,

$$
\log\frac{A_\eta(v,a)}{A_\eta(v,t_d)}=\int_0^{t_d-a}\ell_{R(v)}(v-t_d+\eta+x)\,dx
$$

is nondecreasing in $v$ by \eqref{eq:A4} and \eqref{eq:A6}, so $U_\eta(v)/A_\eta(v,t_d)\le U_\eta(t)/A_\eta(t,t_d)$ for $t_d\le v\le t$. Let $\Xi_\eta(dv)=h_\eta(t,v)U_\eta(v)\,dv$. The transfer \eqref{eq:B9} for $dQ_+$, then \eqref{eq:B2} at $s=t_d$, give

\begin{equation}
\begin{aligned}
\Xi_\eta([0,t_d])
&=W_\eta(t)-k_\eta U_\eta(t)-\Xi_\eta([t_d,t])\\
&\ge W_\eta(t)-k_\eta U_\eta(t)-\frac{U_\eta(t)}{A_\eta(t,t_d)}\bigl[\beta(t-t_d+\eta)-k_\eta A_\eta(t,t_d)\bigr]\\
&=\int_{[0,\tau]}A_\eta(t,a)\bigl[\Phi(t-a+\eta)-\Phi(t-t_d+\eta)\bigr]\,dQ_+(a)=:L_\eta .
\end{aligned}
\label{eq:B13}
\end{equation}

All ages in the last line stay positive as $\eta\to0$; since $\Phi$ is strictly increasing and $a\le\tau<t_d$, $L_\eta\to L_0>0$, regardless of intervening centre zeros.

On $[t_d,t]$, $\mathcal C\ge0$ and \eqref{eq:B10} give $\mathcal C_\eta\ge-\eta'_\eta$ with $\eta'_\eta\to0$. By \eqref{eq:B9}, \eqref{eq:B11} and \eqref{eq:B13},

$$
V_\eta(r,t)\ge m_0L_\eta-\eta'_\eta\Bigl[k_\eta+\int_{t_d}^th_\eta(t,v)\,dv\Bigr],
$$

with a bounded bracket. The left side converges to $V(r,t)$ (respectively the edge response): the atom has positive age, and the $q'$ part is dominated by $A_*M/\sqrt u$ or $4\alpha s_*M/R(t)^2$. Hence $V(r,t)\ge m_0L_0>0$ for every noncentral interior output and for the edge. This proves the following. **Lemma B.2 (strict transfer).** A nonnegative centre history along a nondecreasing radius gives strictly positive noncentral and edge responses, whatever tangential centre zeros occurred earlier.

### B.6 Radius growth; proof of Theorems A and B

Let $E(t)=\int_{[0,t]}J_{R(t)}(t-s)\,dq(s)$. It is continuous at positive times, and by \eqref{eq:edge} $R'(t)=-fc_pE(t)/F_a(R(t),t)$ with $F_a<0$, so $E$ and $R'$ have the same sign; B.3 gives $E>0$ initially. Suppose $\mathcal C\ge0$ on $(0,T]$ and the radius exists there. If $E$ had a nonpositive value, it would have a first zero $t_e>0$, with $R$ nondecreasing on $[0,t_e]$; Lemma B.2 at $t_e$ gives $E(t_e)>0$, a contradiction. So $E>0$ and $R'>0$ throughout, and Lemma B.2 at each $t$ gives strictly positive noncentral velocities. This proves (ii)$\Rightarrow$(i) in Theorem A once the radius is known to exist (B.7); (i)$\Rightarrow$(ii) is the case $r=0$.

For Theorem B, the centre margin is strictly positive initially; if $t_c$ is its first zero and there is no downward jump in $(0,t_c]$, the centre history up to $t_c$ is nonnegative and the above applies on $(0,t_c]$. The same holds at any later zero preceded by a nonnegative centre history. A positive centre value after a negative interval certifies nothing (Section 9.4).

### B.7 Proof of Proposition 4.1

Let $\mathcal T=\{t\in(0,T]:fp_\varepsilon(0,t)>\tau_{\rm d}\}$ be the set of times at which a crack radius exists. It is relatively open: for $\varepsilon>0$, $p_\varepsilon(0,\cdot)$ is continuous; for $\varepsilon=0$, $p_0(0,t)=c_p\int_0^tq(s)(t-s)^{-1}ds$ is lower semicontinuous by Fatou's lemma, since the integrand is nonnegative and continuous in $t$ for each $s<t$.

Let $t_0=0$ for Theorem A and $t_0=t_n$ for Theorem G. In both cases $(t_0,t_0+\eta_0)\subset\mathcal T$ for some $\eta_0>0$: for the point source, $q>0$ just after zero makes $p_0(0,t)=\infty$; for the Gaussian source, $\partial_t^+p_\varepsilon(0,t_n)>0$. Let $t_R=\sup\{\tau\le T:(t_0,\tau)\subset\mathcal T\}$, and assume $\mathcal C_\varepsilon\ge0$ on $(t_0,t_R)$ (outside jump times for the point source). By B.6 (point source) or Lemma C.1 (Gaussian source), each of which assumes only that the radius exists on $(t_0,\tau]$, applied for each $\tau<t_R$, $R$ is nondecreasing on $(t_0,t_R)$. It is bounded: $J_a(u)\le4\alpha s_*/a^2$ gives $\tau_{\rm d}/f=\mathcal Ap_\varepsilon(R,t)\le4\alpha s_*c_p\mathcal V(t)/R^2$, so $R(t)^2\le4\alpha s_*fc_p\mathcal V(T)/\tau_{\rm d}$. Hence $R_1=\lim_{t\uparrow t_R}R(t)\in(0,\infty)$ exists. For $a>0$ the function $(a,t)\mapsto\mathcal Ap_\varepsilon(a,t)$ is continuous (its kernel $J_a$ is bounded and $q$ is bounded), so $f\mathcal Ap_\varepsilon(R_1,t_R)=\tau_{\rm d}$. Because $p_\varepsilon(\cdot,t_R)$ strictly decreases in $r$, $p_\varepsilon(0,t_R)>\mathcal Ap_\varepsilon(R_1,t_R)$, so $t_R\in\mathcal T$. If $t_R<T$, openness of $\mathcal T$ contradicts the definition of $t_R$. So $t_R=T$ and $(t_0,T]\subset\mathcal T$. Under hypothesis (ii) of Theorem A or G this applies, and the radius exists throughout. $\square$

### B.8 Rate jumps for the point source

Let $q$ be piecewise $C^1$ with jump times $\mathcal J$, and $M$ the largest one-sided derivative.

*Downward jumps.* If $q$ jumps down by $j>0$ at some $t_j<T$ and the crack exists at $t_j$, then the rest of the history contributes a bounded amount to $\mathcal C(t)$ near $t_j$, while the atom contributes $-jK_{R(t)}(0,t-t_j)\to-\infty$ (Section 5.2). So (ii) of Theorem A fails, and so does (i). Hence under (ii) all jumps in $[0,T)$ are upward; a jump at the final time $T$ is not constrained by either condition and is excluded from the theorem's conclusions.

*Changes in B.2--B.6 for upward jumps $a_j>0$ at $t_j\in\mathcal J$.* The transfer \eqref{eq:B9} holds for measures with atoms. Startup (B.3) is unaffected, choosing $s_0$ below the first jump time. The radius remains continuous, since $\mathcal Ap(a,t)$ is continuous in $t$ for $a>0$, with one-sided derivatives at jump times. In B.5, \eqref{eq:B10} is replaced by the lower bound

\begin{equation}
\mathcal C_\eta(s)\ge-\eta'_\eta,\qquad \eta'_\eta=\Bigl(q_0+\sum_ja_j\Bigr)A_*\eta\,\delta_0^{-3/2}+2A_*M\sqrt\eta,\qquad t_d\le s\le t,
\label{eq:B14}
\end{equation}

for $\eta\le\delta_0$, where $\delta_0\in(0,t_d]$ is fixed as follows (so that the initial atom also has age at least $\delta_0$ on $[t_d,t]$). All atoms are upward, so they contribute nonnegatively to $\mathcal C_\eta$, and the absolutely continuous part has modulus at most $2A_*M\sqrt{T+1}$. Choose $\delta_0$ so small that $a_jK_{R(t_j)}(0,2\delta_0)>2A_*M\sqrt{T+1}$ for every $j$, which is possible because $K_R(0,u)\to\infty$ as $u\to0$. For $s\in[t_j,t_j+\delta_0]$ the atom at $t_j$ alone gives $a_jK_{R(s)}(0,s-t_j+\eta)\ge a_jK_{R(t_j)}(0,2\delta_0)$, since $K_R(0,u)$ increases with $R$ and decreases with $u$; so $\mathcal C_\eta(s)>0$ there. At all other $s\in[t_d,t]$ every atom has age at least $\delta_0$, $\mathcal C(s)\ge0$, and the error estimate \eqref{eq:B10}, applied to each atom, gives \eqref{eq:B14}. The rest of B.5 is unchanged.

In B.6, $E$ is right-continuous and jumps only upward, by $a_jJ_{R(t_j)}(0^+)=2\alpha a_j/R(t_j)^2$. Let $t_e=\inf\{t:E(t)\le0\}$. If $t_e$ were a jump time, $E(t_e)\ge E(t_e^-)+2\alpha a_j/R^2>0$, contradicting right-continuity and the definition of $t_e$; so $E(t_e)=0$ and Lemma B.2 gives the same contradiction as before. A continuous function with positive right derivative is nondecreasing, so $R$ increases. Velocities at non-jump times are covered by Lemma B.2; at a jump time the left limit is the transfer applied to $dq$ restricted to $[0,t_j)$, and the right limit adds $a_jK_R(r,0^+)>0$ for $r>0$. This proves Theorem A as stated. $\square$

## Appendix C. Proof of Theorem G

\setcounter{equation}{0}
\renewcommand{\theequation}{C.\arabic{equation}}\renewcommand{\theHequation}{C.\arabic{equation}}

*Reading guide.* For a Gaussian source the fault is unslipped before nucleation, so the physical centre slip rate is zero there and records nothing. A normalised kernel (C.1) continues the centre history through that interval as the latent forcing \eqref{eq:latent}. With it, the positive transfer of Appendix B holds without any limit in the source width (C.2), and nucleation is transverse (C.3). The first-zero argument then proceeds as before, now allowing jumps of both signs (C.4).

### C.1 A normalised kernel through the unslipped interval

Fix $\varepsilon>0$. Set $R(t)=0$ for $0\le t\le t_n$ and, for $0\le s\le v\le T$,

\begin{equation}
a(v,s)=
\begin{cases}
\dfrac{K_{R(v)}(0,v-s+\varepsilon)}{K_{R(v)}(0,\varepsilon)}, & R(v)>0,\\[8pt]
\dfrac{\varepsilon}{v-s+\varepsilon}, & R(v)=0.
\end{cases}
\label{eq:C1}
\end{equation}

Since $K_R(0,u)\sim R/u$ as $R\downarrow0$, this is a continuous positive extension with $a(v,v)=1$ and $a(v,s)\le1$. Define the normalised centre history

\begin{equation}
H(v)=\int_{[0,v]}a(v,s)\,dq(s).
\label{eq:C2}
\end{equation}

After nucleation $H(v)=\mathcal C_\varepsilon(v)/K_{R(v)}(0,\varepsilon)$; up to and including nucleation $H=H_{\rm pre}$ of \eqref{eq:latent}, because differentiating \eqref{eq:pressure} gives $\partial_t^+p_\varepsilon(0,v)=c_p\int_{[0,v]}(v-s+\varepsilon)^{-1}dq(s)$. The kernel extension \eqref{eq:C1} is continuous, but $H$ itself is only right-continuous with left limits: since $a(v,v)=1$, $H(v)-H(v^-)$ equals the jump of $q$ at $v$, including at $v=t_n$ if $q$ jumps there. Only right-continuity is used below. Before nucleation it is a latent forcing, not the physical slip rate, which is zero. Under \eqref{eq:startupG} and hypothesis (ii), $H\ge0$ throughout, and $H>0$ on a nonempty interval $[t_n,t_n+\eta_1)$ by right-continuity.

### C.2 Strict positive transfer

Prescribe a continuous nondecreasing path $R\ge0$, including its zero interval, and fix $t>t_n$. The logarithmic age slope $\ell_R(u)$ increases in $u$ and in $R>0$ and extends to $R=0$ as $\ell_0(u)=-1/u$, which lies below $\ell_R$ by \eqref{eq:A6}. Row normalisation in \eqref{eq:C1} does not change the derivative in $s$. Let $\beta$ be an interior or edge output at $R(t)$ as in B.2, $\Phi=\beta/K_{R(t)}(0,\cdot)$, $d_t=K_{R(t)}(0,\varepsilon)$. Solving

\begin{equation}
\begin{aligned}
h(t,s)&=d_t\,a(t,s)\,\Phi'(t-s+\varepsilon)+\int_s^tP(s,v)h(t,v)\,dv,\\
P(s,v)&=a(v,s)\bigl[\ell_{R(t)}(t-s+\varepsilon)-\ell_{R(v)}(v-s+\varepsilon)\bigr],
\end{aligned}
\label{eq:C3}
\end{equation}

with $0\le P\le1/\varepsilon$ and continuous strictly positive forcing, the uniformly convergent Neumann series gives a continuous $h>0$, and differentiation in $s$ verifies

\begin{equation}
\beta(t-s+\varepsilon)=\beta(\varepsilon)\,a(t,s)+\int_s^th(t,v)\,a(v,s)\,dv .
\label{eq:C4}
\end{equation}

Integrating against $dq$ on $[0,t]$ (atoms allowed) gives

\begin{equation}
\int_{[0,t]}\beta(t-s+\varepsilon)\,dq(s)=\beta(\varepsilon)\,H(t)+\int_0^th(t,v)\,H(v)\,dv,
\label{eq:C7}
\end{equation}

and, with $dq$ restricted to $[0,t)$, the same identity with $H(t)$ replaced by $H(t^-)$, which gives the left limit of the output. All kernels are bounded on the compact triangle. If $H\ge0$ on $[0,t]$ and $H>0$ on a set of positive measure, the output is strictly positive.

### C.3 Transverse nucleation

At nucleation,

\begin{equation}
\partial_{rr}p_\varepsilon(0,t_n)=-\frac{c_p}{2\alpha}\int_0^{t_n}\frac{q(s)}{(t_n-s+\varepsilon)^2}\,ds<0,
\label{eq:C10}
\end{equation}

since nucleation requires a nonzero history. Radial smoothness gives $\mathcal Ap_\varepsilon(R,t)=p_\varepsilon(0,t)+\tfrac13\partial_{rr}p_\varepsilon(0,t)R^2+O(R^4)$, using $\int_0^1s^3(1-s^2)^{-1/2}ds=\tfrac23$. On the interval after $t_n$ free of jumps, the implicit function theorem in the variable $R^2$ gives a $C^1$ branch with

\begin{equation}
R(t)^2=\frac{-3\,\partial_t^+p_\varepsilon(0,t_n)}{\partial_{rr}p_\varepsilon(0,t_n)}\,(t-t_n)+o(t-t_n),
\label{eq:C11}
\end{equation}

with positive coefficient by \eqref{eq:startupG}. The edge response $E(t)=\int_{[0,t]}J_{R(t)}(t-s+\varepsilon)\,dq(s)$ extends right-continuously to $E(t_n)=\partial_t^+p_\varepsilon(0,t_n)/c_p>0$, since $J_R(u)\to1/u$ as $R\downarrow0$.

### C.4 Proof of Theorem G

For positive radius $R'^{+}(t)=-fc_pE(t)/F_a(R(t),t)$ with $F_a<0$, where $R'^+$ is the right derivative and $E$ the right-continuous edge response; $R$ is continuous because $\mathcal Ap_\varepsilon$ is continuous in $t$.

**Lemma C.1 (conditional edge positivity).** Assume \eqref{eq:startupG}, let $t_n<\tau\le T$, suppose the crack radius exists on $(t_n,\tau]$, and suppose $\mathcal C_\varepsilon\ge0$ there. Then $E>0$ and $R$ strictly increases on $(t_n,\tau]$, and every noncentral and edge velocity is strictly positive there, on both sides of every jump.

*Proof.* Let $t_e=\inf\{t\in(t_n,\tau]:E(t)\le0\}$, assuming this set is nonempty; then $t_e>t_n$ by C.3. On $[t_n,t_e)$, $E>0$, so $R$ is nondecreasing on $[0,t_e]$. By C.1, $H\ge0$ on $[0,t_e]$ with $H>0$ on a set of positive measure, so \eqref{eq:C7} for the edge output gives $E(t_e)>0$. Then right-continuity gives $E>0$ on a right neighbourhood of $t_e$, so $t_e$ cannot be the infimum of the set where $E\le0$. Hence that set is empty, $E>0$, and $R$ strictly increases on $(t_n,\tau]$. Applying \eqref{eq:C7} at each $t$, and its left-limit form, proves strict positivity of all noncentral and edge velocities on both sides of every jump. $\square$

*Proof of Theorem G.* Assume (ii). Lemma C.1, applied on $(t_n,\tau]$ for each $\tau$ below the maximal existence time, supplies the monotonicity used in Appendix B.7, so Proposition 4.1 gives a crack radius on all of $(t_n,T]$. Lemma C.1 with $\tau=T$ then gives (i) and the strict positivity statements. Necessity is the case $r=0$. If $q$ is nondecreasing on $[0,t_n]$, then $dq\ge0$ there and $H_{\rm pre}\ge0$, with $H_{\rm pre}(t_n)>0$ because the history is nonzero. $\square$

## Appendix D. Constants and asymptotics

\setcounter{equation}{0}
\renewcommand{\theequation}{D.\arabic{equation}}\renewcommand{\theHequation}{D.\arabic{equation}}

*Reading guide.* D.1 proves the radius map \eqref{eq:lambdamap}. D.2 bounds the constants $s_*$ and $c_D$ used in Propositions 7.2 and 7.3. D.3 derives the leading-order taper formula \eqref{eq:leadingorder}, which is an approximation, not a theorem.

### D.1 The constant-rate radius map

For constant rate $q_0$ and a point source, substituting $z=R/(2\sqrt{\alpha u})$ in $\mathcal Ap(R,t)=c_pq_0\int_0^tJ_R(u)\,du$ gives $J_R(u)\,du=-2D(z)z^{-2}dz$; reversing the limits ($u\in(0,t)$ corresponds to $z\in(\lambda,\infty)$) gives $\Theta=2\int_\lambda^\infty D(z)z^{-2}dz$. As $\lambda\to\infty$, $D(z)=1/(2z)+O(z^{-3})$ gives $\Theta=1/(2\lambda^2)+O(\lambda^{-4})$. As $\lambda\to0$, write instead $p(r,t)=c_pq_0\,\mathrm E_1(r^2/(4\alpha t))$ with the exponential integral $\mathrm E_1(x)=-\gamma_{\rm E}-\log x+O(x)$; then

$$
\Theta=\int_0^1\mathrm E_1(\lambda^2s^2)\frac{s\,ds}{\sqrt{1-s^2}}
=-\gamma_{\rm E}-2\log\lambda-2\int_0^1\frac{s\log s}{\sqrt{1-s^2}}\,ds+O(\lambda^2\log\lambda).
$$

With $w=\sqrt{1-s^2}$ the last integral is $\tfrac12\int_0^1\log(1-w^2)\,dw=\log2-1$, so $\Theta=2-\gamma_{\rm E}-2\log(2\lambda)+o(1)$, which is \eqref{eq:lambdamap}.

### D.2 The constants $s_*$ and $c_D$

From $D(x)/x=\int_0^1e^{-x^2w}\,\tfrac12(1-w)^{-1/2}dw$ and $1+\tfrac w2\le(1-w)^{-1/2}\le1+\tfrac w2+\tfrac{3}{8}2^{5/2}w^2$ on $[0,\tfrac12]$, together with $\int_{1/2}^1\tfrac12(1-w)^{-1/2}dw=2^{-1/2}$, one obtains for $x>0$

\begin{equation}
\frac1{2x}+\frac1{4x^3}-e^{-x^2}\Bigl(\frac1x+\frac1{x^3}\Bigr)
\le D(x)\le
\frac1{2x}+\frac1{4x^3}+\frac{2.1214}{x^5}+0.7072\,x\,e^{-x^2/2}.
\label{eq:D1}
\end{equation}

For $x\ge10$ this gives $xD(x)\le0.5028$ and $0\le x^3(D(x)-1/(2x))\le0.2713$. On $[0,10]$ we use $0\le D\le\min(x,1/x)\le1$, which bounds the derivatives: $|(xD)'|\le1+x$ and $|(x^3D-x^2/2)'|\le3x^2+x^3+x$. Evaluating on a grid of spacing $10^{-5}$ and adding half the spacing times the derivative bound on each cell gives $0.6423872$ and $0.4114363$ as bounds on $[0,10]$, after adding an explicit allowance of $10^{-13}$ for the floating-point error of every evaluation of $D$ (scaled by $x$ and $x^3$ respectively). The allowance is supported numerically, not proved: on 2001 points of $[0,10]$ the double-precision values differ from an 80-digit Taylor series by at most $2.2\times10^{-16}$. We therefore state $s_*\le0.6424$ and $c_D\le0.4115$ as numerically verified upper bounds with these margins; the grid maxima are $0.6423747$ at $x\approx1.5020$ and $0.4113317$ at $x\approx1.9556$, and independent high-precision evaluation gives the same values. Interval arithmetic would make them fully rigorous.

### D.3 Leading-order finite-radius taper threshold

In the critically stressed regime, the edge kernel is $J_R(u)=2\alpha/R^2+O(\alpha^2u/R^4)$ by \eqref{eq:D1}, so the radius equation gives $R(t)^2=2\alpha fc_p\mathcal V(t)/\tau_{\rm d}\,(1+O(\Theta))$. Insert this and \eqref{eq:twotermmargin} at the binding time $T+L$ of the inner-limit taper problem, where $\mathcal V=q_0(T+L-dL/2)$; neglecting the remainder,

$$
\frac{\pi^{3/2}}2\Bigl[\frac1{\sqrt{T+L}}-\frac{2d}{\sqrt L}\Bigr]=(1-d)\sqrt{\frac{2\Theta}{T+L-dL/2}} .
$$

At $\Theta=0$ the root is $d_\infty$. Expanding to first order in $\sqrt\Theta$ gives \eqref{eq:leadingorder}. The derivation assumes that the binding time stays at $T+L$ and neglects terms of relative order $\Theta$; the computation of Section 9.2 confirms both for $\Theta\le0.1$, with error below $0.033\,\Theta$.

## Data and code availability

The manuscript source, bibliography, verification scripts, their retained outputs and a one-command runner are archived at Zenodo, DOI [10.5281/zenodo.23838529](https://doi.org/10.5281/zenodo.23838529) (version 0.1.0-candidate), and in the repository <https://github.com/ipitchford/fault-sliding-history-criteria> (tag `v0.1.0-candidate`). A plain-English summary is at <https://evidencepress.org/releases/fault-sliding-history-criteria/>. Text, figures and data are released under CC0-1.0 and code under the MIT licence. This is an unrefereed research candidate; it has had internal AI-assisted review only.

## References

::: {#refs}
:::
