# PHASE 6 — Model B: Direct-to-Consumer + Telehealth Partnership

> **Compliance disclaimer:** This section is a strategic/operational framework, not legal advice. Direct-to-consumer lab testing involving telehealth provider order entry implicates CLIA, state clinical laboratory licensure, corporate practice of medicine (CPOM), anti-kickback statute (AKS), Eliot-Stark physician self-referral law (Stark applies to Medicare; many states have analogous "mini-Stark" laws), state telehealth practice acts, and informed consent/results-release rules (which vary significantly by state, especially for results like pregnancy tests). **Have Pennsylvania healthcare regulatory counsel review the final structure, partner agreements, and patient-facing flows before launch**, especially before marketing across state lines (NJ, DE, MD, NY are all plausibly within or near a 50-mile radius of Hatfield).

## 6.1 Model B Overview

```
Patient → Online Intake/Request → Telehealth Provider Review → Provider Issues Lab Order
   → Patient visits Labstar (or partner draw site) for specimen collection
   → Labstar performs CLIA-waived testing (UA / hCG)
   → Results routed to ordering telehealth provider
   → Provider releases results to patient per state regulations (with clinical interpretation if needed)
```

## 6.2 Telehealth Partner Requirements

Labstar should NOT employ ordering physicians directly (CPOM risk in most states). Instead, partner with an existing licensed telehealth platform/group. Selection criteria:

| Requirement | Why It Matters |
|---|---|
| Licensed in Pennsylvania (and any other states marketed to within 50-mile radius — NJ, DE, MD) | Providers must be licensed in the state where the *patient* is located at time of the encounter |
| Independent medical group structure (telehealth platform contracts with an independent physician-owned PC/group) | Avoids CPOM violations — Labstar should not control clinical decision-making |
| Established asynchronous + synchronous visit capability | Supports both "fill out a form, get an order" (async) and "video visit" (sync) workflows depending on test type and state requirements |
| Clear, written **fee-for-service or platform-license fee** arrangement (NOT per-test or per-referral compensation to/from Labstar) | Avoids Anti-Kickback Statute / fee-splitting issues — Labstar pays for *platform access or technology*, not for *referrals of lab orders* |
| EHR/ordering system that can generate a valid lab requisition addressed to Labstar | Operational requirement for order flow |
| Documented protocols for result review, patient notification, and escalation (e.g., positive pregnancy test, abnormal UA suggestive of UTI/kidney issue) | Patient safety + regulatory requirement that a *licensed provider*, not the lab, interprets and communicates clinically significant results |

**Suggested partner types:** regional telehealth groups already serving PA (rather than large national platforms, for easier negotiation and a more "local" brand story), or a direct relationship with 1–2 independent PA-licensed physicians/NPs willing to serve as medical director(s) for the program under a compliant medical director or platform-license agreement.

## 6.3 Physician Network Requirements

- Minimum 1 PA-licensed Medical Director (telehealth partner physician) providing oversight, available for escalations.
- Sufficient provider coverage for expected volume + state licensure footprint (start with PA-only patients to simplify; expand to NJ/DE only after compliance review).
- Providers must independently determine medical necessity for each test ordered — Labstar cannot dictate or pre-select "the test the patient wants" as the order; the provider's clinical judgment must be documented (even if brief, for low-risk CLIA-waived tests like UA/hCG).
- Standing orders / clinical protocols for common scenarios (e.g., "patient requests pregnancy test — provider reviews intake questionnaire, confirms appropriateness, issues order") should be drafted by the telehealth medical group, reviewed by counsel.

## 6.4 Patient Workflow

1. Patient visits Labstar-branded (or co-branded) landing page → selects test (e.g., "Urine Pregnancy Test" or "Urinalysis / UTI Screen").
2. Patient completes a brief online intake/questionnaire (symptoms, reason for testing, relevant history) and pays for the service (test + telehealth review fee bundled).
3. Telehealth provider reviews intake (async, typically <30 min during business hours) and either:
   - Issues a lab order to Labstar, **or**
   - Determines testing isn't appropriate / recommends an in-person visit instead (documented, patient notified, refund per policy).
4. Patient receives confirmation + scheduling link to visit Labstar's Hatfield location (or a future satellite/partner draw site) for specimen collection — **walk-in or scheduled appointment**.
5. Patient provides specimen at Labstar; staff verify identity and match to the electronic order.
6. Labstar performs CLIA-waived testing same-day.
7. Results are transmitted securely to the ordering telehealth provider.
8. Telehealth provider reviews results and releases to patient via secure portal, with clinical guidance/next steps as needed (per state results-release law — note Pennsylvania does not currently restrict direct-to-patient release of most lab results the way some states do, but **pregnancy test results and any results suggestive of a reportable condition should always go through provider review first** as a clinical best practice).

## 6.5 Ordering Workflow

1. Telehealth provider's EHR generates an electronic or printable lab requisition addressed to Labstar (CLIA #, NPI, ordering provider info, test(s) ordered, patient demographics, ICD-10 code for medical necessity/diagnosis).
2. Requisition transmitted to Labstar via secure fax, EHR interface (if available), or patient-presented printout/QR code.
3. Labstar front desk matches requisition to walk-in/scheduled patient, verifies ID, collects specimen, performs testing.
4. Labstar logs the order in its LIS (Laboratory Information System) / tracking spreadsheet (if pre-LIS) with a unique order ID tying back to the telehealth encounter.

## 6.6 Reporting Workflow

1. Labstar completes testing (same-day) and generates a result report (CLIA-compliant format: patient ID, test, result, reference range, date/time performed, performing lab CLIA #, testing personnel).
2. Result transmitted securely (encrypted email, fax, or EHR/portal interface) to the ordering telehealth provider — **never directly to the patient from Labstar** (Labstar is the testing lab, not the ordering/treating provider, and is generally not the appropriate party to interpret/release clinical results to patients under CLIA's role separation).
3. Telehealth provider reviews and releases results to patient (per Section 6.4, step 8), typically same-day given Labstar's fast TAT — this is a major selling point for the Model B program ("test today, results today").
4. Labstar retains records per CLIA retention requirements (minimum 2 years for test records, longer for some result types — confirm with lab director).

## 6.7 Revenue Model

| Revenue Stream | Description | Who Collects |
|---|---|---|
| Patient self-pay testing fee | Patient pays for the lab test (UA, hCG) | Labstar (or bundled, see below) |
| Telehealth visit/review fee | Patient pays for provider review/order issuance | Telehealth partner |
| **Bundled package price (recommended)** | Single price covers both telehealth review + lab test, split per pre-negotiated revenue-share agreement with telehealth partner | Labstar collects, remits agreed share to telehealth partner — OR telehealth platform collects and remits to Labstar; either is fine **as long as the split reflects fair market value for services rendered, not a per-referral kickback** |

**Important:** revenue-sharing arrangements between Labstar and the telehealth partner must reflect **fair market value for actual services performed by each party** (testing vs. clinical review), documented in a written agreement, and should NOT vary based on the volume or value of referrals in a way that could be construed as "payment for referrals." A flat per-encounter technology/administrative fee structure (rather than a percentage of lab revenue) is generally viewed as lower-risk — confirm structure with counsel.

## 6.8 Pricing Structure (Illustrative — validate against local self-pay market rates)

| Service | Suggested Self-Pay Price |
|---|---|
| Urine pregnancy test (hCG) + telehealth review | $35–$50 |
| Urinalysis (UTI screen) + telehealth review | $45–$65 |
| Urinalysis with microscopy/reflex (if abnormal dipstick) | +$15–$25 add-on |
| "Express" same-day result fee (if offered as premium tier) | +$10–$15 |

Compare against local urgent care self-pay rates (often $100–$200+ for a visit including UA) — Model B should be priced as a **convenient, lower-cost alternative** for patients who don't need a full visit, while still being profitable after telehealth partner revenue share and lab costs.

## 6.9 Compliance Considerations Checklist

- [ ] CLIA certificate scope covers all tests offered via Model B (waived tests only, per current Labstar certificate)
- [ ] Telehealth partner physicians licensed in all states where patients will be located
- [ ] Written agreement between Labstar and telehealth partner reviewed by healthcare counsel for AKS/Stark/fee-splitting compliance
- [ ] Patient consent forms address: testing purpose, result release process, telehealth visit terms, payment/refund policy
- [ ] Privacy/HIPAA: Business Associate Agreement (BAA) between Labstar and telehealth platform if PHI is shared between systems
- [ ] Pregnancy test results and any abnormal/positive results routed through provider review before patient notification
- [ ] State-specific rules reviewed before marketing to patients outside Pennsylvania (NJ, DE, MD if within 50-mile radius)
- [ ] Advertising/marketing materials reviewed for compliance with state lab advertising rules and FTC truth-in-advertising standards (no implied diagnosis, no guaranteed turnaround claims that can't be met)

## 6.10 Risk Mitigation

| Risk | Mitigation |
|---|---|
| CPOM violation (Labstar perceived as controlling clinical decisions) | Telehealth partner is fully independent; Labstar provides only testing + technology/scheduling infrastructure |
| AKS/Stark exposure from revenue-sharing | Flat fee or FMV-documented split, written agreement, periodic legal review |
| Patient receives bad news (positive pregnancy test, signs of UTI) without clinical support | All results routed through telehealth provider for interpretation and patient communication, not direct lab-to-patient |
| Out-of-state patients ordering tests | Geo-fence the Model B intake to Pennsylvania initially; expand only after state-specific legal review |
| CLIA scope creep (non-waived tests accidentally offered via Model B) | Hard-code Model B test menu to match current CLIA-waived certificate; require lab director sign-off before adding any new test to the DTC menu |
| Reputational risk if turnaround promises aren't met | Launch Model B only after Model A operations have proven consistent same-day TAT for 60–90 days |

## 6.11 Recommended Launch Sequencing

1. **Months 1–3:** Focus entirely on Model A (provider-ordered) to build volume, prove turnaround, and generate cash flow.
2. **Months 4–5:** Identify and negotiate with telehealth partner; engage healthcare counsel to review structure and draft agreements.
3. **Month 6:** Soft-launch Model B to a limited audience (e.g., existing Model A practices' patient populations, or a geo-fenced PA-only digital ad campaign) with the urine pregnancy test as the lead product (lower regulatory complexity than UTI/UA workflows requiring clinical follow-up).
4. **Month 7+:** Expand Model B test menu (UA/UTI screen) and marketing reach based on initial results and compliance review outcomes.
