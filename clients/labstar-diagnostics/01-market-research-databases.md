# PHASE 1 — Market Research & Prospect Databases

## 1.0 Database Schema (use for every category)

Build one spreadsheet/CRM table per category with these columns:

| Field | Description |
|---|---|
| Practice Name | Legal/DBA name |
| Address | Street, city, state, zip |
| Phone | Main line |
| Website | URL |
| Distance from Labstar (mi) | Driving miles from 2321 N. Penn Rd, Hatfield, PA 19440 |
| # Providers | MDs/DOs/NPs/PAs on staff (proxy for volume) |
| Administrator / Practice Manager | **TBD via discovery call** |
| Office Manager | **TBD via discovery call** |
| Decision Maker (clinical + business) | **TBD via discovery call** |
| Existing Lab Relationship | **TBD via discovery call** (Quest / Labcorp / in-house / other) |
| Est. Monthly UA/hCG Volume | Estimated from facility type/size (refine after discovery) |
| Opportunity Score (1–100) | See Phase 2 scoring model |
| Source | URL(s) where info was found |
| Status | New / Contacted / etc. (Phase 8 CRM) |

> **Why admin/decision-maker/volume/lab-relationship fields are blank:** these are not published anywhere. They are *discovered on the first 1–2 calls* using the Gatekeeper and Office Manager scripts in Phase 3. Filling these in is the literal output of Week 1–2 of the 90-day plan (Phase 9).

---

## 1.1 Full-Database Build SOP (to scale beyond the seed lists below)

The seed lists below (Section 1.2) are **real, sourced examples** to start calling immediately, concentrated in the 0–15 mile "home turf" ring. To build the *complete* database of every facility in the 50-mile radius (realistically 800–1,500+ records across all categories), run this repeatable process:

1. **NPPES NPI Registry** (https://npiregistry.cms.hhs.gov/) — free bulk search by taxonomy code + ZIP radius. Pull NPI Type 2 (organizational) records for:
   - Family Medicine (207Q00000X), Internal Medicine (207R00000X), Pediatrics (208000000X)
   - Urgent Care (261QU0200X)
   - Behavioral Health Outpatient Clinics (261QM0850X), Substance Abuse Rehab (261QR0405X / 324500000X)
   - Occupational Medicine (207XX0005X)
   - Home Health (251E00000X)
   - Skilled Nursing (314000000X), Assisted Living (310400000X)
2. **PA Department of Health facility licensing lists** (https://www.pa.gov/agencies/health.html) — official lists of licensed nursing homes, personal care homes, assisted living residences, home health agencies, and drug & alcohol treatment facilities by county (Montgomery, Bucks, Chester, Delaware, Philadelphia, Berks, Lehigh, Northampton).
3. **Google Maps / Places API** — search each category + each town within 50 miles (use a 10-mile grid of town centers radiating from Hatfield: Lansdale, North Wales, Montgomeryville, Souderton, Telford, Harleysville, Colmar, Chalfont, Doylestown, Quakertown, Perkasie, Sellersville, Hatboro, Horsham, Warminster, Willow Grove, Ambler, Blue Bell, Plymouth Meeting, Norristown, King of Prussia, Pottstown, Collegeville, Phoenixville, Reading (edge), Allentown/Bethlehem (edge), Trenton NJ (edge), Philadelphia (Northeast/North).
4. **State medical board / licensing lookups** for individual provider counts at multi-provider practices.
5. **Concierge medicine networks**: MDVIP (https://www.mdvip.com/physicians-directory), SignatureMD, PartnerMD — directory search by ZIP.
6. **County health department & MH/DD/EI offices** for behavioral health and addiction treatment provider directories (e.g., Montgomery County Office of Drug & Alcohol, Bucks County Drug & Alcohol Commission).
7. De-duplicate, geocode, and calculate driving distance from Labstar (Google Distance Matrix API) to populate "Distance from Labstar."
8. Apply the Phase 2 Opportunity Score formula to rank.

**Recommended tooling:** a simple Google Sheet or Airtable base with one tab per category (matching Section 1.2 below), feeding into the CRM (Phase 8) once a record reaches "Contacted."

---

## 1.2 Seed Databases (Real, Sourced — Home Turf Ring, 0–15 miles)

> Distances are estimated driving distance from 2321 N. Penn Road, Hatfield, PA 19440. Provider counts are estimates based on website/listing info and should be confirmed. Opportunity Scores use the Phase 2 model (independence + proximity + facility-type volume potential + access ease).

### A. Primary Care / Family Medicine / Internal Medicine

| Practice | Address | Phone | Website | Dist (mi) | Providers (est) | Likely Lab | Est. Monthly UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|---|
| LMG Family Practice | Lansdale, PA (Blue Bell/Chalfont/Lansdale service area) | TBD | lmgfamilypractice.com | ~3 | 2–4 | Quest/Labcorp (TBD) | 80–150 | 78 |
| Green & Seidner Family Practice Associates | Lansdale, PA | TBD | greenandseidner.com | ~3 | 2–3 | TBD | 80–150 | 80 |
| TriValley Primary Care — Lansdale Office | 1101 S. Broad St, Lansdale, PA 19446 | TBD | trivalleypc.com | ~3 | 3–6 (multi-site group) | TBD | 100–200 | 75 |
| TriValley Primary Care — Indian Valley (Souderton) Office | 777 Route 113, Souderton, PA 18964 | TBD | trivalleypc.com | ~6 | included above | TBD | 80–150 | 72 |
| TriValley Primary Care — Telford Office | 211 Telford Pike, Telford, PA 18969 | TBD | trivalleypc.com | ~8 | included above | TBD | 60–120 | 70 |
| Primary Care Associates of Lansdale (Jefferson Health) | Lansdale, PA | TBD | jeffersonhealth.org | ~3 | 4–8 (health-system owned) | Health-system lab (locked) | 150–300 | 35 |
| Penn Medicine Primary Care – Lansdale | Lansdale, PA | TBD | pennmedicine.org | ~3 | 3–6 (health-system owned) | Health-system lab (locked) | 100–250 | 30 |

**Notes:** Independent groups (LMG, Green & Seidner, TriValley) are Tier A candidates — owner-operators can switch labs quickly. Health-system-owned practices (Jefferson, Penn) are Tier C — locked into in-network lab contracts; deprioritize for now.

### B. Urgent Care Centers

| Practice | Address | Phone | Website | Dist (mi) | Providers (est) | Likely Lab | Est. Monthly UA/hCG Vol | Opp. Score |
|---|---|---|---|---|---|---|---|---|
| AFC Urgent Care Lansdale | 1551 S. Valley Forge Rd, Lansdale, PA 19446 | (215) 855-7011 (verify) | afcurgentcare.com/lansdale | ~3 | 2–4 (rotating) | Franchise — may have local flexibility | 200–400 | 70 |
| Jefferson Urgent Care – Lansdale | 1715 Sumneytown Pike, Lansdale, PA 19446 | TBD | jeffersonhealth.org | ~3 | 2–3 | Health-system lab (locked) | 150–300 | 30 |
| Patient First – Montgomeryville | 713 Bethlehem Pike, Montgomeryville, PA 18936 | TBD | patientfirst.com | ~5 | 3–5 | Patient First in-house lab (locked) | 250–500 | 20 |
| Tower Health Urgent Care – North Wales | North Wales, PA | TBD | towerhealth.org | ~4 | 2–3 | Health-system lab (locked) | 150–300 | 30 |
| vybe urgent care (nearest location, verify) | Philadelphia/Montgomery border (verify nearest site) | TBD | vybeurgentcare.com | ~10–15 | 2–4 | TBD | 150–300 | 50 |

**Notes:** Franchise/independent urgent cares (AFC) are best near-term targets — local franchisee owners often have lab vendor flexibility. Health-system and Patient First locations run their own labs — long-shot/Tier C.

### C. Pediatrics

| Practice | Address | Phone | Website | Dist (mi) | Providers (est) | Likely Lab | Est. Monthly UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|---|
| Advocare Lansdale Pediatrics | Lansdale, PA | TBD | advocarelansdalepeds.com | ~3 | 3–6 | TBD | 60–120 | 70 |
| True North – North Penn Pediatrics | 2031 N. Broad St, Suite 145, Lansdale, PA 19446 | (215) 368-1114 | northpenn.truenorthdocs.com | ~3 | 2–4 | TBD | 50–100 | 72 |
| Lansdale Pediatric & Adolescent Medical Associates | Lansdale, PA (+ Chalfont location) | TBD | (Healthgrades/Yelp listing) | ~3–8 | 3–6 (multi-site) | TBD | 70–140 | 70 |
| Pennridge Pediatrics | Sellersville, (215) 257-2727; Harleysville, (215) 256-1999 | see phones | pennridgepediatrics.com | ~7–9 | 4–8 (multi-site) | TBD | 80–160 | 68 |
| CHOP Primary Care – Lansdale (verify location) | Lansdale, PA | TBD | chop.edu | ~3 | 3–5 (health-system owned) | CHOP lab network (locked) | 60–120 | 25 |

**Notes:** Pediatric UA volume is driven by UTI work-ups, sports-physical urinalysis, and adolescent pregnancy testing. Independent groups (Advocare, True North, Pennridge) are Tier A/B.

### D. Assisted Living Facilities

| Facility | Address | Phone | Website | Dist (mi) | Beds (est) | Likely Lab | Est. Monthly UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|---|
| Paradise Manor | 206 E. Lincoln Ave, Hatfield, PA 19440 | TBD | (SeniorGuidance listing) | ~1 | ~38 | TBD | 40–80 | 75 |
| Hatfield Mennonite Home | 2343 Bethlehem Pike, Hatfield, PA 19440 | TBD | hatfieldmennonite.org (verify) | ~2 | TBD (CCRC) | TBD | 80–150 | 78 |
| Greenfield of Lansdale | Lansdale, PA | TBD | (SeniorAdvice listing) | ~3 | ~150 | TBD | 100–200 | 76 |
| St. Mary Villa (Independent & Retirement Living) | Lansdale, PA | TBD | (SeniorLiving.org listing) | ~3 | ~90 | TBD | 60–120 | 70 |
| Brittany Pointe Estates (Acts Retirement) | 1001 Valley Forge Rd, Lansdale, PA 19446 | TBD | actsretirement.org | ~4 | ~92 (AL) + SNF/memory care | Likely contracted national lab | 120–250 | 55 |
| Elm Terrace Gardens | Lansdale, PA | TBD | (SeniorAdvice listing) | ~3 | ~250 (campus) | TBD | 150–300 | 60 |
| Living Branches (Souderton & Lansdale campuses) | Souderton/Lansdale, PA | TBD | livingbranches.org | ~5–6 | Multi-level campus | TBD | 150–300 | 62 |

**Notes:** UTIs are extremely common in elderly residents — UA is one of the highest-frequency tests ordered in AL/SNF settings. The on-site nursing/medical director is the decision maker, not corporate (for independently-operated facilities like Paradise Manor, Hatfield Mennonite). High priority — also closest geographically to Labstar.

### E. Skilled Nursing Facilities / Nursing Homes

| Facility | Address | Phone | Website | Dist (mi) | Beds (est) | Likely Lab | Est. Monthly UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|---|
| Gwynedd Healthcare & Rehabilitation Center | Lansdale, PA | TBD | gwyneddhc.com | ~4 | ~180 | Contracted national lab (verify) | 200–400 | 58 |
| Brittany Pointe Estates (SNF unit) | 1001 Valley Forge Rd, Lansdale, PA 19446 | TBD | actsretirement.org | ~4 | TBD | TBD | 150–300 | 55 |
| Dock Woods | Lansdale, PA | TBD | dock.org (verify) | ~5 | TBD (CCRC, 108-acre campus) | TBD | 150–300 | 55 |
| Souderton Mennonite Homes | Souderton, PA | TBD | (community listing) | ~6 | TBD | TBD | 100–200 | 58 |
| St. Mary Center for Rehabilitation & Healthcare | Lansdale, PA | TBD | (Catholic Health Group) | ~3 | TBD | TBD | 150–300 | 58 |
| ManorCare Health Services – Lansdale | 640 Bethlehem Pike, Montgomeryville, PA 18936 | TBD | proMedica/ManorCare | ~5 | ~170 | National contracted lab (likely locked) | 200–400 | 35 |

**Notes:** SNFs typically have existing national-lab contracts (often Quest/Labcorp via corporate agreements at the chain level), but **STAT/same-day UA for UTI rule-outs** is a recurring pain point — a "STAT supplemental" relationship alongside the existing contract is often the realistic entry wedge, not a full contract replacement.

### F. Home Healthcare Agencies

| Agency | Address | Phone | Website | Dist (mi) | Likely Lab | Est. Monthly UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|
| 365 Health Services | 1555 Bustard Rd, Suite 200, Lansdale, PA 19446 | 484-368-0699 | 365healthservices.com | ~3 | TBD | 30–80 | 70 |
| SYNERGY HomeCare of Montgomery & Bucks | 14 E. 6th St, Lansdale, PA 19446 | 267-222-8642 | synergyhomecare.com | ~3 | TBD | 20–60 | 65 |
| Home Helpers of Montgomery County | 213 N. Broad St, Ste 3, Lansdale, PA 19446 | 215-585-2677 | homehelpershomecare.com | ~3 | TBD | 20–60 | 65 |
| BrightStar Care of Lansdale | Lansdale, PA (serves Lansdale/Montgomeryville/Souderton) | 267-436-4011 | brightstarcare.com/locations/lansdale | ~3 | BrightStar has skilled-care option — may need lab partner | 30–80 | 68 |
| ComForCare Home Care – Montgomery North | 1001 N. Broad St, Lansdale, PA 19446 | 267-297-1818 | carescout.com (ComForCare) | ~3 | TBD | 20–60 | 62 |
| Visiting Angels – Lansdale | Lansdale, PA | TBD | visitingangels.com/lansdale | ~3 | TBD | 20–50 | 60 |
| Victory Home Care | Serves all of Montgomery County | TBD | victoryhomecarepa.com | varies | TBD | 20–60 | 58 |

**Notes:** Most home-care agencies are non-medical (companion care) — limited direct UA volume, but they refer to/coordinate with physicians who order labs. Higher value: agencies with **skilled (RN) home health** components that can do mobile specimen collection and route to Labstar — frame Labstar as their lab partner for at-home draws. Lower priority for direct UA volume vs. AL/SNF, but valuable referral partners.

### G. Addiction Treatment Centers / Behavioral Health (Substance Use)

| Facility | Address | Phone | Website | Dist (mi) | Likely Lab | Est. Monthly Drug Screen / UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|
| High Focus Centers – Lansdale | 157 S. Broad St, Suite 201, Lansdale, PA 19446 | (215) 709-6483 | pa.highfocuscenters.com/location/lansdale | ~3 | TBD | 100–300 (UDS-heavy) | 80 |
| NHS Montgomery County (Detox & Drug Rehab) | Lansdale, PA 19446 | TBD | yourfirststep.org | ~3 | TBD | 150–400 | 78 |
| Sobriety Solutions of Pennsylvania | Plymouth Meeting, PA | TBD | (Psychology Today listing) | ~12 | TBD | 100–250 | 65 |
| ETHOS Treatment | (verify nearest PA location) | TBD | ethostreatment.com | varies | TBD | 100–250 | 60 |
| Rehab After Work – Lansdale | Lansdale, PA | TBD | rehabafterwork.com | ~3 | TBD | 100–250 | 75 |

**Notes:** This category is **the highest-volume UDS opportunity** of any segment but requires confirming whether their drug-screen needs fit Labstar's CLIA-waived menu (point-of-care UDS cups vs. lab-based confirmation/GC-MS — confirmatory testing is send-out, but the **point-of-care screening cup component** plus pregnancy testing for intake is squarely in Labstar's wheelhouse). Validate scope of work before pricing.

### H. Occupational Medicine Clinics

| Facility | Address | Phone | Website | Dist (mi) | Likely Lab | Est. Monthly UA/Drug Screen Vol | Opp. Score |
|---|---|---|---|---|---|---|---|
| St. Luke's Occupational Medicine (nearest PA location, verify) | Serves Lansdale/Montgomeryville area per network | TBD | slhn.org/occupational-medicine | varies | Health-system lab (likely locked) | 150–400 | 40 |
| Penn Medicine Occupational Medicine (nearest, verify) | Greater Philadelphia | TBD | pennmedicine.org/services/occupational-medicine | varies | Health-system lab (locked) | 150–400 | 30 |
| Independent IME / Workers' Comp clinics (research via county directories) | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

**Notes:** Health-system occupational medicine programs are largely locked into their own labs. **The real opportunity here is independent occupational health/IME clinics and small employer wellness programs** that need pre-employment UA drug screens — these are not yet identified by name and require local business-directory research (search "DOT physical" + "pre-employment drug testing" + town names).

### I. Concierge Medicine Practices

| Practice | Address | Phone | Website | Dist (mi) | Likely Lab | Est. Monthly UA Vol | Opp. Score |
|---|---|---|---|---|---|---|---|
| MDVIP-affiliated practices in Lansdale (Drs. Barone, Cavuto, Dickerman, Fleischer, Flynn — verify which remain active/local) | Lansdale, PA | TBD | mdvip.com/physicians-directory/pa/lansdale | ~3 | TBD | 30–60 | 75 |
| MDVIP-affiliated — Horsham (Dr. Maouelainin) | Horsham, PA | TBD | mdvip.com | ~9 | TBD | 30–60 | 65 |
| MDVIP-affiliated — King of Prussia (Dr. Till) | King of Prussia, PA | TBD | mdvip.com | ~15 | TBD | 30–60 | 55 |

**Notes:** Concierge practices have small panels (~400–600 patients) so per-practice UA volume is modest, but physicians are solo decision-makers who value white-glove service — strong fit for Labstar's "personal relationship" pitch and easy, fast yes/no decisions. Good for relationship-building and referrals to other practices in their network.

### J. Specialty Practices (OB/GYN, Urology, Nephrology, etc.)

| Practice Type | Notes / Research Direction |
|---|---|
| OB/GYN groups | Highest hCG + UA volume of any specialty (every prenatal visit includes a UA dipstick + protein/glucose check). Search "OB/GYN Lansdale/Montgomeryville/Souderton/Telford." Target independent groups first. |
| Urology | Very high UA volume (hematuria work-ups, UTI, post-procedure checks). Search "urology Lansdale Montgomery County." |
| Nephrology | High UA volume (proteinuria monitoring). |
| Endocrinology | Moderate UA volume (microalbumin/diabetes monitoring — note: requires quantitative microalbumin, confirm CLINITEK Status+ menu covers this). |
| Podiatry / Wound Care | Lower UA volume but frequent for diabetic patients. |

**Action:** Run NPI registry searches for taxonomy codes 207V00000X (OB/GYN), 208800000X (Urology), 207RN0300X (Nephrology) within 15 miles of 19440, then expand.

### K. Community Health Centers

| Facility | Notes |
|---|---|
| Federally Qualified Health Centers (FQHCs) in Montgomery/Bucks County | Search HRSA Health Center Locator (https://findahealthcenter.hrsa.gov/) for sites within 50 miles. FQHCs have high patient volume but often have existing 340B-linked lab contracts — Tier C/long-term, but worth a relationship. |

---

## 1.3 Category Summary & Next-Step Priorities

| Category | Seed Records Found | Priority for Week 1 Calls |
|---|---|---|
| Independent PCP/FM/IM | 5 | HIGH |
| Urgent Care (independent/franchise) | 1–2 | HIGH |
| Pediatrics (independent) | 4 | HIGH |
| Assisted Living | 7 | HIGH (closest geographically) |
| Skilled Nursing | 6 | MEDIUM (existing contracts likely) |
| Home Health Agencies | 7 | MEDIUM (referral partners) |
| Addiction/Behavioral Health | 5 | HIGH (volume-dense) |
| Occupational Medicine | 0 (needs local research) | MEDIUM |
| Concierge Medicine | 3 | MEDIUM (relationship value) |
| Specialty (OB/GYN, Uro, Nephro) | 0 (needs NPI pull) | HIGH (highest per-visit UA rate) |
| Community Health Centers | 0 (needs HRSA pull) | LOW (long sales cycle) |

**Immediate action item:** Before Day 1 of the 90-day plan (Phase 9), spend 4–6 hours running the NPI/HRSA/Google Maps pulls described in Section 1.1 for OB/GYN, Urology, Occupational Medicine, and the wider 15–50 mile ring, to bring total Tier A+B prospect count to 150–250 records.
