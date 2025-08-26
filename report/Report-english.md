### Retention Calculation Methodology

The analysis uses a **full inclusion approach** — i.e., all users are counted, including those who played **zero game rounds (4.4%)**. This is the most relevant strategy from a business perspective, as it allows us to evaluate the **total impact** of product changes on the entire user base.

To ensure robustness, we also ran a sensitivity analysis on a filtered subset of only active players. The key conclusions **remained unchanged**.

### 1. Group Balance Summary (full data)

| Version | Users  | Percentage |
| ------- | ------ | ---------- |
| gate_30 | 44,700 | 49.56%     |
| gate_40 | 45,489 | 50.44%     |
-> The experimental groups are **almost perfectly balanced** in terms of user count (49.56% vs 50.44%).

### Retention 
| Version | Retention 1 day | Retention 7 day |
| ------- | --------------- | --------------- |
| gate_30 | 44.81%          | 19.02%          |
| gate_40 | 44.22%          | 18.2%           |
| Разница | +0.59%          | +0.82%          |
- Day 1 retention was **0.59% higher** in the `gate_30` group.
- Day 7 retention was **0.82% higher** in `gate_30` as well.

This indicates that the **group with the gate at level 30 performed slightly better in user retention**.

### 2. Zero-Round Players (based on full data)

| Version | Zero Players | Total Users | Percentage | p-value |
| ------- | ------------ | ----------- | ---------- | ------- |
| gate_30 | 1,937        | 44,700      | 4.33%      | -       |
| gate_40 | 2,057        | 45,489      | 4.52%      | 0.169   |
The share of users who didn’t play any rounds was:
- **4.33% in `gate_30`**
- **4.52% in `gate_40`**
The difference is **not statistically significant** (p = 0.169, Z-test for proportions).  
→ No evidence that gate placement impacts initial engagement.
### 3. Outliers Treatment

We removed:
- Users with **zero rounds** (~4.4%)
- Users who played **more than the 99th percentile (493 rounds)** (~1%)

This cleaning removed ~5.4% of the data.  
There were **no major differences** in the 99th percentile between groups (493 vs 492), confirming that "hardcore" player behavior is comparable across versions.

### 4. Impact of Preprocessing on Metrics

### Sensitivity Analysis
| Metric           | Full data        | Active players only |
| ---------------- | ---------------- | ------------------- |
| **Retention 1d** | 44.81% vs 44.22% | 46.21% vs 45.67%    |
| **Difference**   | -0.59%           | -0.54%              |
After excluding outliers and zero-round users, retention remained stable:

- Full data: **44.81% vs 44.22%**
- Active players only: **46.21% vs 45.67%**

→ **Conclusion stays the same**: `gate_30` performs slightly better in terms of retention.

User segmentation.
The users divided into segments to estimate the average number of levels on the cleaned data.
- The first segment includes late starters (retention_1 = false, retention_7 = true)
- The second segment includes loyal users (retention_1 = true, retention_7 = true)
- We will also analyze all users separately by the number of levels completed

## 5. Segment: Late Starters (retention_7 = True, retention_1 = False)

## Before outlier removal:

| Group   | Users | Avg Rounds |
| ------- | ----- | ---------- |
| gate_30 | 1,826 | 100.4      |
| gate_40 | 1,773 | 75.3       |
- Players in `gate_30` **appeared** more engaged (100 vs 75 avg rounds), but this was a **misleading result** due to outliers.

### After cleaning (99th percentile):

| **Group** | **Users** | **Avg. levels** | **Difference** | **p-value** | **t-value** | **Cohen's d** |
| --------- | --------- | --------------- | -------------- | ----------- | ----------- | ------------- |
| gate_30   | 1,800     | 70.1            | —              | —           | —           | —             |
| gate_40   | 1,755     | 72.0            | +1.9           | 0.456       | -0.746      | -0.025        |

After cleaning:
- Average levels played: **70.1 vs 72.0**
- **No statistically significant difference** (p = 0.456, t-test)
- Effect size is **negligible** (Cohen's d = -0.025)

Conclusion: **Gate position does not influence engagement** of users who return after 7 days.

## 6. Segment: Users with Retention 1d and 7d = TRUE

| **Group** | **Users** | **Avg. levels** | **Difference** | **p-value** | **t-value** | **Cohen's d** |
| --------- | --------- | --------------- | -------------- | ----------- | ----------- | ------------- |
| gate_30   | 6,257     | 148.4           | —              | —           | —           | —             |
| gate_40   | 6,074     | 151.9           | +3.5           | 0.08        | -1.75       | -0.03         |
Conclusions:
- `gate_40` group played **+3.5 more levels on average**
- **Statistically insignificant** (p = 0.08)
- Effect size is **very small** (Cohen's d = -0.03)
- **Test power is high** (n > 6,000 per group) → if the effect was real, we’d likely detect it

Conclusion: Though there's a small trend favoring `gate_40`, **there is no statistically reliable difference** in player engagement.

## 7. All Users: Average Game Rounds Played

| **Group** | **Users** | **Avg. levels** | **Difference** | **p-value** | **t-value** | **Cohen's d** |
| --------- | --------- | --------------- | -------------- | ----------- | ----------- | ------------- |
| gate_30   | 42312     | 46.7            | —              | —           | —           | —             |
| gate_40   | 42977     | 46.5            | -0.2           | 0.748       | 0.321       | 0.002         |

Average number of levels played was virtually identical:
- `gate_30`: 46.7 levels
- `gate_40`: 46.5 levels
    
→ p = 0.748 → **no significant difference**

## 8. Final Conclusion

Although loyal users in `gate_40` **played 3.5 more levels on average**, the difference is **not statistically significant** (p = 0.08), and the effect size is **negligible**.

→ **From the data, the best decision would be to keep the gate at level 30.**

It’s worth noting that the gate is currently set to level 40 in production. This decision may have been influenced by **other business metrics** (e.g., monetization, LTV, churn), or later test results not available in this dataset.