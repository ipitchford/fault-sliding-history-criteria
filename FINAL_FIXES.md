# Final fixes, 31 October 2026

These changes follow the independent proof audit and the re-review. None changes a main result; several narrow statements to what is proved.

- **Trajectory statements.** The trajectory form of the instantaneous criterion now requires the centre test at every time from the start of slip, not just almost everywhere on a later interval, and claims uniqueness only for the Gaussian source.
- **Rate jumps.** The point-source theorem no longer claims anything about a jump at the final time. The "first loss is central" theorem now excludes downward jumps before the contact, because after such a jump the first zero can be a recovery.
- **Loss versus contact.** Throughout, loss of full sliding is the first *negative crossing* of the centre margin (or a downward point-source jump); a zero alone is only a threshold contact.
- **Proof order.** The Gaussian proof is reorganised so that the persistence of the crack radius does not depend on itself (new Lemma C.1).
- **Convergence conditions.** Point-source velocity, the certificate and the two-term formula are stated only at times where the centre integral converges; a continuous rate can violate this.
- **Taper corollary.** "No linear taper halves the rate" is now explicitly a point-source result, with a full proof that the finite-radius threshold lies strictly below the inner-limit value, and a Gaussian example showing it can fail for wide sources.
- **Shut-in deadline.** The explicit deadline applies after shut-in; integrable histories that never stop are only shown to lose full sliding eventually.
- **Numbers.** Taper thresholds are called finite-window estimates; the two-term enclosures are distinguished from the uncertified root searches; the Dawson constants are called numerically verified upper bounds with an explicit floating-point allowance.
- **Annular source.** Reworded as a failure of the instantaneous centre test; a new check follows the example in time and finds the ring reversing first on the part of the history where the crack is well defined.
- **Readability and references.** A four-step "how to use" paragraph; Lemma 2's detailed proof moved to Appendix A.4; table entries marked by source type; Viesca (2021) correctly described as constant-pressure injection; one priority caveat only.

## Editor's final corrections (after the second targeted audit)

A last targeted audit found no fatal or major defect; the editor made its six minor corrections directly:
the downward-jump exclusion in Appendix B.8 now applies only before the final time; the zero-age ratio in
Theorem 1's proof at the peak time is defined by its limit; the uniqueness clause of Corollary 3.1 requires
the full hypotheses of Theorem G; the missing q0 is restored in the taper corollary and its Gaussian example;
the annular-source time-tracking is described as numerical evidence only; and the classical Volterra
references are cited as background, not for a specific theorem. The Dawson constants remain numerically
verified upper bounds (not interval-certified), as stated in Appendix D.2.
