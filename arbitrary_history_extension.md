# Arbitrary-history extension for the point-source circular branch

> **Status (31 October 2026).** This supporting note is superseded by Appendices A and B of the revised manuscript wherever the two differ. Changes there: (i) the existence of the crack radius is no longer assumed but proved (Proposition 4.1, Appendix B.7); (ii) Theorem A allows piecewise-$C^1$ rates with jumps, with downward jumps shown to violate both sides of the equivalence and upward jumps handled in Appendix B.8; (iii) the stationary-point argument of Lemma C is expanded (Lemma A.2); (iv) Theorem B is restricted explicitly to the startup classes of Theorem A; (v) symbols are renamed (auxiliary shift $\eta$, output kernel $\beta$, comparator $U_\eta$, strength excess $\tau_{\rm d}$). The statements below remain correct for the class they state. Equation labels (E1)--(E19) are those of this note.


Research proof supplement, 28 October 2026. The manuscript's original finite-source, single-peaked theorem remains separate. This supplement proves a broader point-source theorem under explicitly stronger time regularity. The companion `gaussian_startup_extension.md` proves the corresponding fixed-Gaussian-source theorem under monotone central pressure through transverse nucleation; general Gaussian prebirth pressure histories remain outside that extension.

## 1. Frozen scope and statements

Use the constants, pressure, Abel transform, circular inversion and kernel of the manuscript. In particular,

\[
K_R(r,u)=2\sqrt{\frac\alpha u}\int_r^R
\frac{D(a/(2\sqrt{\alpha u}))}{\sqrt{a^2-r^2}}\,da,
\quad
K_R(0,u)=\frac{2\sqrt\alpha}{\sqrt u}G\left(\frac R{2\sqrt{\alpha u}}\right),
\]

where \(G(z)=\int_0^zD(x)\,dx/x\). Define the edge-normalised kernel

\[
J_R(u)=\lim_{r\uparrow R}\frac{K_R(r,u)}{\sqrt{R^2-r^2}}
=\frac{D(z)}{u z},\qquad z=\frac R{2\sqrt{\alpha u}}.
\tag{E1}
\]

Let \(q\in C^1([0,T])\), \(q\ge0\), extended by zero before zero, and impose one of the following startup assumptions:

1. \(q(0)=q_0>0\); or
2. \(q(0)=0\), and for some \(t_{\rm start}>0\), the rate is nondecreasing on \([0,t_{\rm start}]\) and satisfies \(q(t)>0\) for every \(0<t\le t_{\rm start}\).

The second case includes smooth ramps from zero; no restriction on the number of later rate reversals is imposed. Its initial positivity condition excludes a dormant interval at the chosen time origin and excludes arbitrarily early sign changes of \(q'\). The causal rate-increment measure is \(dq=q_0\delta_0+q'(s)ds\). Suppose the unique positive point-source zero-SIF radius \(R(t)\) exists for \(0<t\le T\). Write

\[
C(t)=\int_{[0,t)}K_{R(t)}(0,t-s)\,dq(s),
\quad
V(r,t)=\int_{[0,t)}K_{R(t)}(r,t-s)\,dq(s).
\tag{E2}
\]

Physical velocity is \(4fc_pV/(\pi\mu)\).

**Theorem A (historical centre criterion, arbitrary rate shape).** Under these assumptions,

\[
V(r,t)\ge0\quad\text{for every }0\le r<R(t),\ 0<t\le T
\]

if and only if

\[
C(t)\ge0\qquad\text{for every }0<t\le T.
\]

Whenever these equivalent conditions hold, every noncentral interior velocity and the edge-normalised velocity is strictly positive throughout \((0,T]\), and \(R'(t)>0\). The condition concerns the entire elapsed centre history; earlier tangential centre zeros are allowed. An instantaneous centre test after an earlier negative centre value is not asserted.

**Theorem B (first threshold is central).** Start on the positive initial branch described above. Let \(t_c>0\) be its first centre zero, if one exists. Before \(t_c\), every interior velocity and the edge-normalised velocity is strictly positive. At \(t_c\), every noncentral interior velocity and the edge-normalised velocity remains strictly positive. Thus the first threshold contact occurs at the centre for an arbitrary smooth nonnegative rate history. If the centre crosses below zero there, this is the first loss of forward-slip admissibility.

More generally, every centre zero preceded by a nonnegative centre history has strictly positive noncentral and edge-normalised velocities at that time. Thus previous tangential centre contacts do not create an exception to Theorem A. Neither theorem continues the physical solution after locking.

## 2. Two properties of the centre kernel

### 2.1 Complete monotonicity in response age

The sine-transform identity

\[
D(x)=\frac12\int_0^\infty e^{-z^2/4}\sin(xz)\,dz
\]

and the change \(z=2\sqrt{\alpha u}\,k\) give

\[
K_R(0,u)=2\alpha\int_0^\infty e^{-\alpha u k^2}\operatorname{Si}(kR)\,dk,
\qquad
\operatorname{Si}(x)=\int_0^x\frac{\sin y}{y}\,dy.
\tag{E3}
\]

The interchange is legitimate for \(u>0\), using absolute integrability after integrating the sine quotient over the finite radius interval. Also \(\operatorname{Si}(x)>0\) for \(x>0\): successive positive and negative half-period areas of \(\sin y/y\) decrease in magnitude, and the first area is positive. Therefore (E3) is a positive mixture of exponentials in \(u\). The centre kernel is completely monotone and log-convex. In particular,

\[
\ell_R(u):=\partial_u\log K_R(0,u)
\quad\text{is nondecreasing in }u.
\tag{E4}
\]

The usual variance proof of log-convexity applies directly to the positive measure in (E3), so no external transform-order theorem is needed for this step.

### 2.2 The logarithmic age slope increases with radius

**Lemma C.** \(e(z)=D(z)/G(z)\) strictly decreases from \(1\) to \(0\) on \((0,\infty)\).

Here is a short proof. Set \(H=G/D\). Dawson's equation \(D'=1-2zD\) and \(G'=D/z\) give

\[
H'=\frac1z-H\frac{D'}D.
\]

The expansions at zero give \(H'=8z/9+O(z^3)>0\) initially. At any stationary point of \(H\), put \(a=zD'/D\). The stationary-point equation implies \(a>0\), \(H=1/a\), and differentiation gives

\[
H''=\frac{a-1}{z^2}+2+\frac2a.
\tag{E5}
\]

Since \(0<D(z)<z\),
\(a=z/D-2z^2>1-2z^2\). Hence every stationary point would have \(H''>2/a>0\). A derivative that starts positive cannot have a first zero with strictly positive second derivative. Thus \(H'>0\) everywhere, proving the strict decrease of \(e=1/H\). The endpoint limits follow from the Dawson and \(G\) limits already calculated in the kernel note.

Consequently,

\[
\ell_R(u)=-\frac{1+e(z)}{2u},
\quad
-\frac1u<\ell_R(u)<-\frac1{2u},
\quad
\partial_R\ell_R(u)>0.
\tag{E6}
\]

Thus \(\ell_R(u)\) increases in both \(R\) and \(u\). Also

\[
\frac{J_R(u)}{K_R(0,u)}=\frac{e(z)}R
\tag{E7}
\]

strictly increases with age. This proves the edge version of the centre-relative age order. The interior version is the already proved Lemma 2 of the manuscript.

## 3. Positive transfer along a nondecreasing radius path

The following is an auxiliary mathematical statement. Its age shift regularises the kernels while leaving the prescribed path \(R\) unchanged. It is not a claim that this path solves a Gaussian-source radius equation.

Fix an observation time \(t>0\), and suppose

\[
R\in C([0,t]),\qquad R(s)>0\ (s>0),\qquad R\text{ is nondecreasing}.
\tag{E8}
\]

The initial radius may be zero, with no lower bound on how rapidly \(R(s)\) tends to zero.

For \(\varepsilon>0\), put

\[
A_\varepsilon(v,s)=K_{R(v)}(0,v-s+\varepsilon),\quad 0\le s\le v\le t.
\]

Choose an output kernel \(b(u)\) equal either to \(K_{R(t)}(r,u)\) for a fixed \(0<r<R(t)\), or to \(J_{R(t)}(u)\). Let

\[
\Phi(u)=\frac{b(u)}{K_{R(t)}(0,u)},\quad c_\varepsilon=\Phi(\varepsilon).
\]

Both choices have \(\Phi'>0\). There is a nonnegative kernel \(h_\varepsilon(t,v)\) such that, for every \(0\le s\le t\),

\[
b(t-s+\varepsilon)
=c_\varepsilon A_\varepsilon(t,s)
+\int_s^t h_\varepsilon(t,v)A_\varepsilon(v,s)\,dv.
\tag{E9}
\]

**Construction and proof.** Suppress \(t,\varepsilon\) in the notation, and set \(z(s)=h(t,s)A(s,s)\). Solve the backward Volterra equation

\[
\begin{aligned}
z(s)&=A(t,s)\Phi'(t-s+\varepsilon)
+\int_s^t P(s,v)z(v)\,dv,\\
P(s,v)&=\frac{A(v,s)}{A(v,v)}
\left[\ell_{R(t)}(t-s+\varepsilon)
-\ell_{R(v)}(v-s+\varepsilon)\right].
\end{aligned}
\tag{E10}
\]

The bracket is nonnegative by (E4), (E6) and monotonicity of \(R\). Since the centre kernel decreases in age, \(A(v,s)/A(v,v)\le1\). Equation (E6) also gives \(0\le P\le1/\varepsilon\). The inhomogeneous term is continuous and positive. The convergent Volterra Neumann series therefore gives a bounded nonnegative \(z\); on a finite interval its iterates are bounded by the usual exponential-series majorant. If \(R(0)=0\), the ratios extend continuously at the triangular corner using \(K_R(0,u)\sim R/u\) as \(R\downarrow0\).

For \(s>0\), define \(h=z/A(s,s)\). It is locally integrable away from zero. Differentiating the proposed right-hand side of (E9), after dividing by \(A(t,s)\), gives \(-\Phi'(t-s+\varepsilon)\) by (E10). Its terminal value at \(s=t\) is \(\Phi(\varepsilon)\). This proves (E9) for \(s>0\). To extend the identity to zero, observe that

\[
0\le h(t,v)A(v,s)\le h(t,v)A(v,v)=z(v),\qquad 0\le s\le v\le t.
\]

The bounded function \(z\) dominates the integrand as \(s\downarrow0\), so dominated convergence proves (E9) also at \(s=0\). The value assigned to \(h(t,0)\) is immaterial. No assertion that \(h\) itself is integrable at zero is required; for a rapidly vanishing radius it need not be.

For any finite signed increment measure \(dQ\), define its auxiliary centre history

\[
C_\varepsilon^Q(v)=\int_{[0,v]}A_\varepsilon(v,s)\,dQ(s).
\]

The endpoint convention is immaterial for the smooth histories used below, apart from the prescribed atom at zero. Fubini in (E9) yields

\[
\int_{[0,t]}b(t-s+\varepsilon)dQ(s)
=c_\varepsilon C_\varepsilon^Q(t)
+\int_0^t h_\varepsilon(t,v)C_\varepsilon^Q(v)\,dv.
\tag{E11}
\]

Absolute integrability follows from Tonelli's theorem applied with \(|dQ|\) in (E9): its left side is bounded by the finite measure's total variation times \(\max_{\varepsilon\le u\le t+\varepsilon}b(u)\). In particular, the product \(hC_\varepsilon^Q\) is absolutely integrable even when \(h\) alone is not. All kernels on the right are nonnegative. This is the required positive causal transfer for arbitrary signed rate increments, along the prescribed nondecreasing path. For fixed positive \(R\), it is a positive convolution transfer. Its general inverse-positivity mechanism is classical; the specific kernel and moving-radius application are what require the preceding calculations.

## 4. Startup positivity and the zero-shift limit

For either startup assumption, the actual point-source radius is continuous down to \(R(0)=0\). To see the limiting value, fix any \(a>0\). The bound \(J_a(u)\le4\alpha/a^2\) gives \(\mathcal A p(a,s)\le4\alpha c_p a^{-2}\int_0^s q(u)du\to0\), so the positive root eventually lies below \(a\). Continuity and differentiability at positive times follow from the strictly decreasing Abel average and the implicit radius equation.

For the actual point-source radius with \(q\in C^1\) and \(q_0>0\), the zero-SIF equation implies

\[
R(s)=\gamma\sqrt s\,[1+o(1)]\quad(s\downarrow0)
\tag{E12}
\]

for a finite \(\gamma>0\). Indeed, after setting radius \(a=x\sqrt s\), the pressure's Abel average converges uniformly on compact positive \(x\)-intervals to the constant-rate average for \(q_0\). That average decreases continuously from infinity to zero, and its root is unique and simple. The correction from \(q(u)-q_0=O(u)\) is \(O(s)\). This proves (E12).

The initial strict positivity is uniform up to the edge. The probability coupling used in the main kernel proof gives

\[
\frac{K_R(r,u)}{\sqrt{R^2-r^2}}\le\frac{K_R(0,u)}R.
\tag{E12a}
\]

In the positive-initial-rate case, the initial-atom contribution, after division by \(\sqrt{R^2-r^2}\), is \(q_0/s\) times a positive continuous function of the scaled radius \(r/R\in[0,1]\). By (E12), its minimum is bounded below by a positive multiple of \(1/s\). Equations (E12a) and \(K_R(0,u)\le A_*/\sqrt u\) bound the continuous \(q'\) contribution to the same normalised velocity by \(2MA_*\sqrt s/R(s)=O(1)\). It is therefore a relative \(O(s)\) correction, proving initial strict positivity uniformly across the disk and at the normalised edge.

In the monotone-ramp case, every initial increment is nonnegative, and \(\int_0^s q'(a)da=q(s)>0\). The strict positivity of \(K_R\) and \(J_R\) therefore gives strictly positive interior and edge-normalised velocities at every \(0<s\le t_{\rm start}\), directly. No square-root radius scaling is asserted or needed in that case.

Set

\[
A_* =\frac{\pi^{3/2}\sqrt\alpha}{2},\qquad
Y_\varepsilon(s)=K_{R(s)}(0,s+\varepsilon),
\quad M=\sup_{[0,T]}|q'|.
\]

The auxiliary centre history satisfies

\[
C_\varepsilon(s)=q_0Y_\varepsilon(s)
+\int_0^s q'(a)K_{R(s)}(0,s-a+\varepsilon)da.
\tag{E13}
\]

### 4.1 Uniform positivity at early times

In the case \(q_0>0\), (E12) gives constants \(c_-,c_+>0\) with \(c_-\sqrt s\le R(s)\le c_+\sqrt s\) initially. There is a constant \(B\), depending on these bounds, such that

\[
\frac{\int_0^sK_{R(s)}(0,u+\varepsilon)du}
{K_{R(s)}(0,s+\varepsilon)}\le Bs
\tag{E14}
\]

for all sufficiently small \(s>0\), uniformly in \(\varepsilon>0\).

For \(\varepsilon\le s\), bound the numerator by \(2A_*\sqrt s\) using \(K_R(0,u)\le A_*/\sqrt u\). The denominator is bounded below by \(c/\sqrt s\), because \(s+\varepsilon\le2s\) and \(R(s)\ge c_-\sqrt s\). For \(\varepsilon\ge s\), use \(K_R(0,u)\le R/u\) in the numerator. In the denominator, the representation \(K_R(0,u)=R u^{-1}\int_0^1D(Rx/(2\sqrt{\alpha u}))/(Rx/(2\sqrt{\alpha u}))dx\) gives a positive lower multiple of \(R/(s+\varepsilon)\), since \(R(s)\le c_+\sqrt s\). The ratio is again bounded by a constant times \(s\).

Choose \(s_0>0\) so that \(MBs_0\le q_0/2\). Equations (E13)--(E14) give

\[
C_\varepsilon(s)\ge\frac{q_0}{2}Y_\varepsilon(s)>0,
\qquad 0<s\le s_0,
\tag{E15}
\]

uniformly in the auxiliary shift.

In the monotone-ramp case, positivity is more immediate: (E13) has only nonnegative increments on \((0,t_{\rm start}]\), with positive total mass at every positive time. Hence \(C_\varepsilon(s)>0\) throughout that interval for every \(\varepsilon>0\). Both startup assumptions therefore supply an interval \((0,s_0]\) on which the auxiliary centre history is nonnegative, uniformly in \(\varepsilon\).

### 4.2 Uniform convergence away from zero

For every \(\delta>0\),

\[
\sup_{\delta\le s\le T}|C_\varepsilon(s)-C(s)|
\le q_0 A_*\varepsilon\delta^{-3/2}+2A_*M\sqrt\varepsilon.
\tag{E16}
\]

The initial-atom term follows from \(|\partial_uK_R(0,u)|\le K_R(0,u)/u\le A_*u^{-3/2}\), which is (E6). For the continuous increment term, monotonicity of \(K_R(0,u)\) in age gives

\[
\int_0^s[K_R(0,u)-K_R(0,u+\varepsilon)]du
\le\int_0^\varepsilon K_R(0,u)du\le2A_*\sqrt\varepsilon.
\]

The radius is held fixed at its actual value \(R(s)\) in each of these inequalities.

### 4.3 Transfer masses stay bounded away from the initial time

For the test input \(dQ=ds\), let

\[
Z_\varepsilon(s)=\int_0^sK_{R(s)}(0,u+\varepsilon)du.
\]

If \(R\) is nondecreasing, then for \(s\ge\delta>0\) and \(0<\varepsilon\le\varepsilon_0\),

\[
Z_\varepsilon(s)\ge
\int_0^\delta K_{R(\delta)}(0,u+\varepsilon_0)du=:m_\delta>0.
\]

Equation (E11) and positivity therefore imply

\[
\int_\delta^t h_\varepsilon(t,v)dv
\le\frac1{m_\delta}\int_0^t b(u+\varepsilon)du\le C_\delta,
\tag{E17}
\]

uniformly as \(\varepsilon\downarrow0\). For an interior output use \(b(u)\le A_*/\sqrt u\). For the edge output, \(D(z)\le1/z\) gives \(J_R(u)\le4\alpha/R^2\). The coefficient \(c_\varepsilon\) is bounded as well: it is at most \(1\) for an interior output and at most \(1/R(t)\) for the edge output.

## 5. Strict transfer from a positive startup interval

We first prescribe a nondecreasing radius path. The key improvement over a merely nonnegative transfer is that a definite amount of its mass must sample the initially positive centre history. Later centre zeros therefore cause no loss of strictness at a noncentral output.

Fix \(t>0\), assume \(C(s)\ge0\) for \(0<s\le t\), and suppose \(R\) is nondecreasing up to \(t\). Choose \(0<d<t\) inside the uniform startup-positivity interval from Section 4.1. Define a nonzero positive comparator measure \(dQ_+\), supported in \([0,\tau]\) with \(\tau<d\), by

- \(dQ_+=\delta_0\) if \(q_0>0\);
- \(dQ_+=\mathbf 1_{[0,\tau]}q'(a)da\), with \(0<\tau<d\le t_{\rm start}\), for a monotone ramp.

The ramp comparator has positive mass \(q(\tau)>0\). Set

\[
P_\varepsilon(v)=\int_{[0,v]}A_\varepsilon(v,a)\,dQ_+(a),
\qquad
B_\varepsilon(t)=\int_{[0,\tau]}b(t-a+\varepsilon)\,dQ_+(a).
\tag{E17a}
\]

On \((0,d]\),

\[
C_\varepsilon(v)\ge mP_\varepsilon(v)
\tag{E17b}
\]

for a fixed \(m>0\), uniformly in \(\varepsilon\): use \(m=q_0/2\) and (E15) in the first case; in the ramp case use \(m=1\), because every actual increment up to \(d\) is nonnegative and the comparator is a truncation of those increments.

### 5.1 Positive transfer mass before \(d\)

For \(a<d\le v\le t\),

\[
\log\frac{A_\varepsilon(v,a)}{A_\varepsilon(v,d)}
=\int_0^{d-a}\ell_{R(v)}(v-d+\varepsilon+x)\,dx.
\tag{E18}
\]

Both the age and the prescribed radius are nondecreasing with \(v\). Equations (E4) and (E6) therefore show that this ratio is nondecreasing in \(v\). Integrating against the positive startup measure gives

\[
\frac{P_\varepsilon(v)}{A_\varepsilon(v,d)}
\le\frac{P_\varepsilon(t)}{A_\varepsilon(t,d)},\qquad d\le v\le t.
\]

Let \(d\nu_\varepsilon(v)=h_\varepsilon(t,v)P_\varepsilon(v)dv\). The total mass identity (E11) for \(dQ_+\), followed by (E9) at the input time \(d\), yields

\[
\begin{aligned}
\nu_\varepsilon([0,d])
&=B_\varepsilon(t)-c_\varepsilon P_\varepsilon(t)
  -\nu_\varepsilon([d,t])\\
&\ge B_\varepsilon(t)-c_\varepsilon P_\varepsilon(t)
 -\frac{P_\varepsilon(t)}{A_\varepsilon(t,d)}
   \left[b(t-d+\varepsilon)-c_\varepsilon A_\varepsilon(t,d)\right]\\
&=\int_{[0,\tau]}A_\varepsilon(t,a)
\left[\Phi(t-a+\varepsilon)-\Phi(t-d+\varepsilon)\right]dQ_+(a)
=:L_\varepsilon.
\end{aligned}
\tag{E19}
\]

The measure \(\nu_\varepsilon\) has a Lebesgue density, so the repeated endpoint \(d\) is immaterial. Every age on the last line stays strictly positive as \(\varepsilon\downarrow0\). Since \(\Phi\) is strictly increasing, \(a\le\tau<d\), and \(Q_+\) has positive mass,

\[
L_\varepsilon\longrightarrow L_0>0.
\]

This lower bound holds independently of any intervening centre zeros.

### 5.2 Strict noncentral and edge output

On \([d,t]\), the assumed \(C\ge0\) and (E16) give \(C_\varepsilon\ge-\eta_\varepsilon\), with \(\eta_\varepsilon\to0\). Equations (E11), (E17), (E17b) and (E19) imply

\[
V_\varepsilon(r,t)
\ge mL_\varepsilon
-\eta_\varepsilon\left[c_\varepsilon+
\int_d^t h_\varepsilon(t,v)dv\right].
\]

The bracket is uniformly bounded. The original input-kernel formula converges to \(V(r,t)\): the initial atom has positive age, and the \(q'\) contribution is dominated by \(A_*M/\sqrt u\) for an interior output or by \(4\alpha M/R(t)^2\) for the edge output. Consequently,

\[
V(r,t)\ge mL_0>0
\]

for every noncentral interior output and for the edge-normalised output. We have proved the following intermediate fact: **a nonnegative entire centre history along a nondecreasing radius path gives strictly positive noncentral and edge responses**, including when the centre has had tangential zeros.

## 6. Automatic radius growth and proof of Theorems A and B

Define the edge response

\[
E(t)=\int_{[0,t)}J_{R(t)}(t-s)\,dq(s).
\]

The positive-time regularity of \(q\) and \(R\) makes \(E\) continuous. Differentiating the zero-SIF equation gives

\[
R'(t)=-\frac{f c_pE(t)}{F_a(R(t),t)},\qquad F_a<0.
\]

Thus \(E\) and \(R'\) have the same sign. Section 4 proves \(E>0\) on an initial interval for either startup assumption.

Suppose now that \(C(t)\ge0\) throughout \((0,T]\). If \(E\) had a zero or a negative value, continuity and initial strict positivity would give a first zero \(t_e>0\). Up to \(t_e\), \(E\ge0\), so \(R\) is nondecreasing on \([0,t_e]\). Section 5, applied at \(t_e\), would then give \(E(t_e)>0\), a contradiction. Hence \(E(t)>0\) and \(R'(t)>0\) throughout the interval. Applying Section 5 at every \(t\) now gives strictly positive noncentral velocities; the centre itself is nonnegative by hypothesis. This proves sufficiency in Theorem A. Necessity is immediate by setting \(r=0\).

For Theorem B, the centre is strictly positive initially. If \(t_c\) is its first zero, its entire history through \(t_c\) is nonnegative, so Theorem A applies on that prefix. Every noncentral and edge-normalised velocity is strictly positive there. The same argument applies to any later centre zero whose entire preceding centre history is still nonnegative, including after earlier tangential contacts. Theorem A therefore detects any first loss of forward-slip admissibility from the centre history alone.

The criterion remains historical: a positive centre value after an earlier negative centre interval does not certify the disk branch. The instantaneous multi-stage counterexample in the manuscript is consistent with this theorem.

## 7. Boundary of the extension

The proof uses an auxiliary shifted kernel, but the principal theorem above is for the point-source radius. An actual Gaussian-source branch has \(R=0\) before nucleation. During that interval, physical centre slip is identically zero and does not record the possibly signed injection memory. A unit-diagonal normalization resolves this issue under a concrete startup hypothesis: the companion `gaussian_startup_extension.md` proves the historical centre criterion for arbitrary subsequent smooth nonnegative rates when central pressure is nondecreasing before first nucleation and crosses the nucleation threshold transversely. Nondecreasing injection through nucleation is a sufficient practical condition. That proof explicitly retains a normalized prebirth forcing history; it does not identify physical zero slip with positivity of the missing history.

General pressure-decreasing prebirth histories and tangential Gaussian nucleation remain open in this work. A finite numerical probe of 1,200 nonnegative eight-stage Gaussian histories found no off-centre-first candidate, but that is not a proof and is not used in either extension. The original single-peaked Gaussian theorem has separate assumptions and remains applicable as stated.

### 7.1 A finite-volume obstruction without unimodality

There is nevertheless a stronger finite-volume conclusion that does not require the Gaussian transfer problem to be solved. Suppose \(q\ge0\), \(q\in L^1(0,\infty)\), and a regular fully sliding branch has nucleated. For either source type, it cannot remain fully sliding for all future time, regardless of how often the injection rate changes direction.

If it did, nonnegative velocity and the edge calculation would force \(R\) to be nondecreasing. Choose a time after nucleation and a fixed \(R_0>0\) below its radius. At the fixed radius,

\[
\mathcal A p_\varepsilon(R_0,t)
=c_p\int_0^tq(s)J_{R_0}(t-s+\varepsilon)ds.
\tag{E20}
\]

The kernel satisfies \(0\le J_{R_0}(u)\le4\alpha/R_0^2\) for all \(u>0\), and tends to zero as \(u\to\infty\). Dominated convergence against the integrable rate therefore gives \(\mathcal A p_\varepsilon(R_0,t)\to0\). Since the pressure average decreases with radius and \(R(t)\ge R_0\),

\[
\frac\Delta f=\mathcal A p_\varepsilon(R(t),t)
\le\mathcal A p_\varepsilon(R_0,t)\longrightarrow0,
\]

a contradiction. For the point source the finite limit of \(J\) at zero age may be assigned without changing the integral. For a Gaussian source, the assertion remains conditional on a disk having nucleated; a small injection may never cause slip. The conclusion is departure from the fully sliding class, not a particular pulse geometry or seismic event.

## 8. Novelty boundary

The new structural simplification was sent through a separate novelty search. The generic relation between log-convex kernels, increasing coefficient/kernel ratios and positive inversion is classical: the discrete lineage includes Kaluza and Jurkat, and continuous first-kind Volterra inversion includes work of Gripenberg. Equation (E10) proves the needed nonconvolution transfer directly rather than claiming a new general resolvent theory. The contribution under consideration is the exact Dawson-kernel properties, their moving-radius use, and the resulting geological historical-centre and first-threshold statements. Historical priority is bounded by the separately recorded search; no claim of being the first proof is warranted solely from a failed search.
