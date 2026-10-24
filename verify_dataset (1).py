"""Cross-check duolingo_quarterly_kpis.csv against figures Duolingo itself reports.

Run:  python3 verify_dataset.py
Every check compares a value computed from the CSV with a number printed in the
shareholder letters (YoY growth rates, DAU/MAU ratios, full-year totals).
"""
import pandas as pd

df = pd.read_csv("duolingo_quarterly_kpis.csv").set_index("quarter")
problems = []


def check(label, computed, reported, tol):
    ok = abs(computed - reported) <= tol
    flag = "OK " if ok else "FAIL"
    print(f"  [{flag}] {label}: computed {computed:.1f} vs reported {reported:.1f} (tol {tol})")
    if not ok:
        problems.append(label)


def yoy(col, q):
    year, qn = q.split("-Q")
    prev = f"{int(year) - 1}-Q{qn}"
    return (df.loc[q, col] / df.loc[prev, col] - 1) * 100


print("1) Full-year totals (sum of quarters vs reported FY figure)")
fy = {
    ("2024", "total_bookings_usd_m"): 870.6, ("2025", "total_bookings_usd_m"): 1158.4,
    ("2024", "subscription_bookings_usd_m"): 730.7, ("2025", "subscription_bookings_usd_m"): 996.3,
    ("2024", "revenue_usd_m"): 748.0, ("2025", "revenue_usd_m"): 1037.6,
    ("2024", "adj_ebitda_usd_m"): 191.9, ("2025", "adj_ebitda_usd_m"): 305.9,
    ("2025", "net_income_usd_m"): 414.1,
}
for (y, col), rep in fy.items():
    total = df[df.year == int(y)][col].sum()
    check(f"FY{y} {col}", total, rep, 0.3)

print("2) DAU/MAU ratio vs ratio stated in filings")
for q, rep in {"2024-Q1": 32.1, "2024-Q4": 34.7, "2025-Q1": 35.8, "2025-Q4": 39.6}.items():
    check(f"DAU/MAU {q}", df.loc[q, "dau_m"] / df.loc[q, "mau_m"] * 100, rep, 0.3)

print("3) Year-over-year growth vs growth printed in letters")
reported = {
    "dau_m": {"2024-Q1": 54, "2024-Q2": 59, "2024-Q3": 54, "2024-Q4": 51, "2025-Q1": 49,
              "2025-Q2": 40, "2025-Q3": 36, "2025-Q4": 30, "2026-Q1": 21, "2026-Q2": 23},
    "total_bookings_usd_m": {"2024-Q1": 41, "2024-Q2": 38, "2024-Q3": 38, "2024-Q4": 42, "2025-Q1": 38,
                             "2025-Q2": 41, "2025-Q3": 33, "2025-Q4": 24, "2026-Q1": 14, "2026-Q2": 8},
    "revenue_usd_m": {"2024-Q1": 45, "2024-Q2": 41, "2024-Q3": 40, "2024-Q4": 39, "2025-Q1": 38,
                      "2025-Q2": 41, "2025-Q3": 41, "2025-Q4": 35, "2026-Q1": 27, "2026-Q2": 18},
    "paid_subs_m": {"2024-Q1": 54, "2024-Q2": 52, "2024-Q3": 47, "2024-Q4": 43, "2025-Q1": 40,
                    "2025-Q2": 37, "2025-Q3": 34, "2025-Q4": 28, "2026-Q1": 21, "2026-Q2": 17},
}
for col, qs in reported.items():
    tol = 2.0 if col == "paid_subs_m" else 1.0  # subscriber counts are rounded to 0.1M
    for q, rep in qs.items():
        check(f"YoY {col} {q}", yoy(col, q), rep, tol)

print("4) Derived metrics the dashboard will use")
out = pd.DataFrame({
    "DAU/MAU %": df.dau_m / df.mau_m * 100,
    "Bookings per DAU $": df.total_bookings_usd_m / df.dau_m,
    "Paid subs / DAU %": df.paid_subs_m / df.dau_m * 100,
    "Adj EBITDA margin %": df.adj_ebitda_usd_m / df.revenue_usd_m * 100,
}).round(1)
print(out.to_string())

print()
print("RESULT:", "all checks passed" if not problems else f"{len(problems)} check(s) failed: {problems}")
