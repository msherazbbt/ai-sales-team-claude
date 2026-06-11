# PHASE 8 — CRM System Design

## 8.1 Recommended Tooling

For a single-location lab launching B2B sales, a lightweight CRM is sufficient — **HubSpot Free/Starter, Airtable, or even a well-structured Google Sheet** can run this system. The structure below is tool-agnostic; migrate to a dedicated CRM (HubSpot, Pipedrive, Zoho) once the prospect list exceeds ~300 records or multiple BDRs are involved.

## 8.2 Core Object: Prospect/Account Record

Every record (one per facility, from Phase 1 databases) includes:

| Field | Type | Notes |
|---|---|---|
| Practice/Facility Name | Text | |
| Category | Dropdown | PCP, Urgent Care, Pediatrics, AL, SNF, Home Health, Addiction, Occ Med, Concierge, Behavioral Health, Specialty, Community Health |
| Address / Distance from Labstar | Text / Number | |
| Phone, Website | Text | |
| # Providers | Number | |
| **Lead Status** | Dropdown (pipeline stage) | New → Contacted → Appointment Scheduled → Proposal Sent → Follow-Up → Negotiation → Won → Lost |
| Tier | Dropdown | A / B / C (Phase 2) |
| Opportunity Score | Number (1–100) | Recalculated per Phase 2 formula |
| Decision Maker — Clinical | Text | Name, title, direct contact (filled via discovery) |
| Decision Maker — Administrative | Text | Office manager/administrator name, contact |
| Existing Lab Relationship | Dropdown | Quest / Labcorp / In-house / Other / Unknown |
| Estimated Monthly Volume | Number | Specimens/month |
| Estimated Annual Revenue Potential | Currency (calc) | Est. monthly volume × 12 × $10.50 net/specimen (Phase 7) |
| Conversion Probability | Percent | Sales rep estimate, updated each stage |
| Assigned BDR | Text | |
| Route Assignment | Dropdown | Route A–E (Phase 5) |
| Last Contact Date | Date | |
| Next Action / Follow-Up Date | Date | |
| Notes | Long text | Free-form |

## 8.3 Activity/Contact History Sub-Table (one-to-many per Account)

| Field | Notes |
|---|---|
| Date | |
| Channel | Call / Email / LinkedIn / Direct Mail / In-Person Visit |
| Outcome | Connected / Voicemail / No Answer / Meeting Booked / Objection Raised / Won / Lost |
| Notes | Key info learned (e.g., "Confirmed current lab = Labcorp, contract renews Jan", "Office manager = Karen, decides on lab vendors") |
| Next Step | |

## 8.4 Lead Status Pipeline Definitions

| Status | Definition | Exit Criteria |
|---|---|---|
| **New** | Record created from Phase 1 research, no contact attempted | First call/email logged → Contacted |
| **Contacted** | At least one outreach touch made (call, email, LinkedIn, mail) | Decision-maker engages or meeting requested → Appointment Scheduled |
| **Appointment Scheduled** | In-person visit or call booked with decision-maker | Meeting occurs → Proposal Sent (or back to Follow-Up if rescheduled) |
| **Proposal Sent** | Trial offer / pricing / account setup info sent | Prospect responds → Negotiation, or no response → Follow-Up |
| **Follow-Up** | Awaiting response, in active cadence (Phase 3 sequences) | Response received → Negotiation/Won/Lost, or cadence exhausted → Lost (long-term nurture) |
| **Negotiation** | Discussing terms (pickup schedule, pricing, exclusivity, trial period) | Agreement reached → Won, or declined → Lost |
| **Won** | Active account, first specimens received | Ongoing — track volume in Activity log |
| **Lost** | Declined, not interested, or locked into contract | Move to quarterly nurture cadence (Phase 3.6); re-activate if status changes (e.g., contract renewal approaching) |

## 8.5 Dashboard / Reporting Views

Build these saved views/reports for weekly review:

1. **Pipeline by Stage** — count and estimated revenue potential by Lead Status (funnel view)
2. **Tier A Accounts — Action Needed** — Tier A records with no activity in >7 days, sorted by Opportunity Score
3. **This Week's Follow-Ups** — records where Next Action date = current week
4. **Won Accounts — Volume Tracking** — Won accounts with actual specimens/month vs. estimated, feeding Phase 7 revenue tracking
5. **Route Coverage** — Won accounts grouped by Route Assignment, to validate route mileage/capacity assumptions (Phase 5)
6. **Conversion Funnel Metrics** — conversion rate at each pipeline stage transition (e.g., Contacted → Appointment Scheduled %), to identify where the process leaks

## 8.6 Automation Recommendations (once on HubSpot/Pipedrive/Zoho)

- Auto-create follow-up tasks based on Phase 3 cadence (Day 1 call → Day 4 email → Day 7 call → etc.)
- Auto-flag Tier A accounts in "Follow-Up" status >14 days for manager review
- Auto-move "Lost" records to a quarterly nurture sequence (re-surface every 90 days)
- Sync "Won" accounts to a route-planning view (Phase 5) for courier scheduling

## 8.7 Weekly CRM Hygiene Checklist (BDR responsibility)

- [ ] Every call/email/visit logged same-day in Activity History
- [ ] Lead Status updated immediately after each meaningful interaction
- [ ] Decision-maker fields filled in as soon as discovered
- [ ] Opportunity Score re-calculated when new info changes Volume/Independence/Access/Speed inputs
- [ ] Next Action date set for every non-Won/Lost record (no record should be "stale" with no next step)
