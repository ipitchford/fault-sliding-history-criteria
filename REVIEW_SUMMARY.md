# Review summary (rating-free public record)

This is a summary of the **internal, AI-assisted review** of this paper, 31 October 2026. It is not peer review and not independent reproduction. The original reports are kept privately because they contain editorial assessments that are not published; this record keeps their substantive objections, the responses and the remaining limits. Section numbers refer to the released manuscript.

## Who reviewed what

| Stage | Route | Scope |
|---|---|---|
| Round 1: editor, methodology | Anthropic model (Claude Opus 5.5) via API | Whole manuscript and supporting notes |
| Round 1: domain, perspective, devil's advocate | Claude Code subagents | Whole manuscript and supporting notes |
| Round 1: adversarial correctness review | OpenAI reasoning model | Search for counterexamples and gaps in every theorem |
| Round 1: clean replay | Lead agent | All six original scripts from a fresh extraction |
| Verification: re-review | Codex companion route (OpenAI model) | Every change of the revision |
| Verification: proof audits (two parts, then a second round) | Codex companion route (OpenAI model) | New or rewritten proofs |

## Round 1: main objections and what was done

No reviewer found a critical error, and every number recomputed by a reviewer agreed with the paper. The objections were about scope wording, positioning, readability and missing quantitative consequences.

1. **"Locking" overstated what is proved.** The paper identifies the first time the forward-slipping circular branch stops being admissible, not a locked patch. *Response:* retitled; "first loss of full sliding" used throughout; threshold contact (a zero of the centre margin) distinguished from loss (a negative crossing); Section 10.2 states that a crossing does not prove a locked patch.
2. **Instantaneous and trajectory statements were conflated; weak and classical derivatives were mixed.** *Response:* Theorem 1 is now an instantaneous criterion; the trajectory form is Corollary 3.1; the velocity is defined as a signed-measure integral and identified with the classical derivative only at regular times.
3. **Uniqueness was asserted without a solution class.** *Response:* a variational forward-slip class is defined and uniqueness proved in it (Proposition 6.1); membership is proved for the Gaussian source only, so the point source is claimed admissible but not unique.
4. **The point source is singular at the centre.** *Response:* point-source results are stated as elastic statements on r > 0; Gaussian-source results are presented as physically primary.
5. **Radius existence was an unexamined hypothesis.** *Response:* Proposition 4.1 proves that the crack radius exists while the centre history stays nonnegative; the hypothesis was removed from Theorems A and G.
6. **Attribution and positioning.** The model and radius condition belong to Sáez, Lecampion, Bhattacharya and Viesca (2022); the dimensionless parameter is their stress-injection parameter; the positive-transfer mechanism is an instance of classical Volterra positivity theory. *Response:* attributions added; the missing references were added, each copied from its Crossref or DataCite record; novelty confined to the centre-relative Dawson-kernel order and its exact consequences.
7. **Hard to read.** *Response:* new abstract and introduction (who needs this, the result in words, contributions, roadmap), a results-at-a-glance table, a notation table, section-goal sentences, appendix reading guides, one consolidated scope section.
8. **Missing consequences that would make the result usable.** *Response, as extensions:* a closed-form deadline after shut-in by which full sliding must end (Proposition 8.2); a two-term finite-radius criterion with a rigorous remainder (Proposition 7.3); realistic drop tolerances and a dimensional example (Sections 5.1, 8.4); the point-source corollary that no linear taper can halve the rate (Corollary 8.4); rate jumps (Theorems A and G); near-threshold and stepped numerical tests (Section 9.3); Gaussian mixtures (Proposition 3.3) with an annular-source counterexample (Section 9.4).
9. **Replay.** Two scripts needed sibling-import fixes to run in isolated mode, and the checks relied on `assert`. *Response:* both fixed; all checks are explicit and run under `python -O`; a single runner was added.

The point-by-point response is [REVISION_RESPONSE.md](REVISION_RESPONSE.md).

## Verification

- **Re-review:** substantial improvement; remaining items were scope and presentation (table rows missing conditions, an over-strong finiteness sentence, illustrative parameters to be labelled as such, a single priority caveat).
- **First proof audit:** no fatal defect; the central kernel argument survived. Four major scope defects were found and repaired: Corollary 3.1 needed positivity from the start of slip rather than almost everywhere on a later interval; Theorem A made a claim about a jump at the final time; Theorem B's "first zero" could be a recovery after a downward jump; and the Gaussian persistence proof was circular (reorganised around a new Lemma C.1). A source-scope defect in Corollary 8.4 was repaired by restricting the taper statement to the point source, with a Gaussian example showing it can fail for wide sources.
- **Second proof audit:** no fatal or major defect. Six minor items were corrected by the editor without a further round: the downward-jump exclusion before the final time, the zero-age ratio at the peak time, the uniqueness clause of Corollary 3.1, a missing q0 in the taper corollary, the annular-source time tracking described as numerical evidence only, and background-only citation of the classical Volterra references. See [FINAL_FIXES.md](FINAL_FIXES.md).

## Limits that remain

- The numerical constants (Appendix D.2) are numerically verified upper bounds with a floating-point allowance, not interval-certified; taper thresholds are finite-window estimates; the leading-order taper formula is an approximation.
- Gaussian histories whose centre pressure falls before nucleation are open; annular sources can violate the centre-first property.
- The model class (zero Poisson ratio, constant friction, zero fracture energy, one-way coupling) is narrow, and nothing is claimed about the slip pulse after first loss or about seismic hazard.
- Priority holds only within bounded literature searches.
