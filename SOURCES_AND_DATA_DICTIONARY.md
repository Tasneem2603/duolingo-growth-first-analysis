# Duolingo quarterly KPI dataset: sources and data dictionary

Independent student analysis. Not affiliated with Duolingo. All figures come from Duolingo's public shareholder letters (SEC Form 8-K exhibits). Coverage: Q1 2023 to Q2 2026 (14 quarters). Units: users in millions, money in USD millions.

## Files
| File | Purpose |
|---|---|
| duolingo_quarterly_kpis.csv | One row per quarter. The fact table for Power BI. |
| duolingo_context_events.csv | Dated company events (campaigns, strategy shifts, streak signals) to annotate charts. |
| verify_dataset.py | Re-computes growth rates, DAU/MAU and full-year totals and compares them with the numbers Duolingo printed. |

## Column definitions (quarterly KPIs)
| Column | Definition (as used by Duolingo) |
|---|---|
| dau_m | Daily active users: unique users active each calendar day, averaged over the quarter. |
| mau_m | Monthly active users: unique users active each month, averaged over the quarter. Described as a supplementary metric from Q1 2026. |
| paid_subs_m | Paid subscribers at period end. Excludes free trials and non-paying family-plan members. |
| total_bookings_usd_m | Subscription bookings plus advertising, Duolingo English Test and in-app purchases. Cash-like measure, recognised when received. |
| subscription_bookings_usd_m | Amounts received from subscription purchases. Blank for 2023 (not collected). |
| revenue_usd_m | GAAP revenue, recognised over the subscription life. |
| net_income_usd_m | GAAP net income. Q3 2025 includes a one-time tax benefit of $222.7M. Do not use it for trend analysis. |
| adj_ebitda_usd_m | Non-GAAP adjusted EBITDA. Use this for profitability trends. |

## Derived metrics (build these yourself in Power BI)
DAU/MAU ratio, bookings per DAU, paid subscribers per DAU, adjusted EBITDA margin, year-over-year growth for each measure.

## Known caveats
1. Duolingo states that metric methodologies may change, so older periods may not be perfectly comparable.
2. Bookings are seasonal. Q4 is high because of the New Year promotion. Compare a quarter with the same quarter a year earlier, not with the previous quarter.
3. Reported growth rates include currency effects. Constant-currency growth is lower in several 2026 quarters (see letters).
4. Q2 2026 DAU growth was helped by a one-time Streak Revival event in June (see context events). Do not extrapolate it.
5. Duolingo's own claims about streaks (for example the share of users with long streaks) are company-reported and correlational.
6. 2023 values come from the prior-year columns of the 2024 letters (Q4 2023 from its own letter).

## Sources (one per quarter)
| Quarter | Document |
|---|---|
| Q4 2023 | https://www.sec.gov/Archives/edgar/data/1562088/000156208824000048/q4fy23shareholderletter.htm |
| Q1 2024 (also Q1 2023 comparison) | https://www.sec.gov/Archives/edgar/data/1562088/000156208824000117/q1fy24shareholderletter1.htm |
| Q2 2024 (also Q2 2023 comparison) | https://www.sec.gov/Archives/edgar/data/1562088/000156208824000203/q2fy24duolingo06-30x24shar.htm |
| Q3 2024 (also Q3 2023 comparison) | https://www.sec.gov/Archives/edgar/data/1562088/000156208824000248/q3fy24duolingo09-30x24shar.htm |
| Q4 2024 | https://www.sec.gov/Archives/edgar/data/1562088/000156208825000039/q4fy24duolingo12-31x24shar.htm |
| Q1 2025 | https://www.sec.gov/Archives/edgar/data/1562088/000156208825000098/q1fy25duolingo3-31x25share.htm |
| Q2 2025 | https://www.sec.gov/Archives/edgar/data/1562088/000156208825000165/q2fy25duolingo6-30x25share.htm |
| Q3 2025 | https://www.sec.gov/Archives/edgar/data/1562088/000162828025049514/q3fy25duolingo9-30x25share.htm |
| Q4 / FY 2025 | https://investors.duolingo.com/node/11661/html |
| Q1 2026 | https://www.sec.gov/Archives/edgar/data/1562088/000162828026029790/q1fy26duolingo3-31x26share.htm |
| Q2 2026 | https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26share.htm |

## Your verification task
Spot-check at least 5 rows against the linked letters yourself (open the highlights table on page 2 or 3) and note the date you checked. Recruiters value this habit.
