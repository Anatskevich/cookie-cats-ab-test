import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scripts.data_loader import load_postgres_table, load_csv_data
from scripts.data_cleaner import clean_dataset, calculate_zero_players, get_outliers_value
from scripts.ab_distribution import calculate_ab_distribution
from scripts.ab_retention import calculate_retention
from scripts.data_segment_analyze import get_late_starters, get_loyal_users, analyze_segment
from scripts.dashboard_tools import get_list_data_from_segment, get_loc_values_list

df = load_csv_data('cookie_cats.csv')
clean_df = clean_dataset(df, 'sum_gamerounds', 0.99, True)

distribution_full = calculate_ab_distribution(df, 'test_version', 'userid')
distribution_clean = calculate_ab_distribution(clean_df, 'test_version', 'userid')

groups = distribution_full["test_version"].tolist()

st.title("Groups and Impact of Data Cleaning on Retention")

# ---------- Raw numbers from your report ----------
group_data = {
    "Group": groups,
    "Users (Full)": distribution_full.set_index("test_version")["number_of_players"].loc[groups].tolist(),
    "Users (Cleaned)": distribution_clean.set_index("test_version")["number_of_players"].loc[groups].tolist(),
    "% of Total (Full)": distribution_full.set_index("test_version")["percent"].loc[groups].tolist(),
    "% of Total (Cleaned)": distribution_clean.set_index("test_version")["percent"].loc[groups].tolist(),
}
df_groups = pd.DataFrame(group_data)

retention_full = calculate_retention(df, 'test_version', ['retention_1', 'retention_7'])
retention_clean = calculate_retention(clean_df, 'test_version', ['retention_1', 'retention_7'])
retention_full = retention_full.round(2)
retention_clean = retention_clean.round(2)

retention_1_full = retention_full.set_index('test_version')['retention_1'].loc[groups].round(2).tolist()
retention_7_full = retention_full.set_index('test_version')['retention_7'].loc[groups].round(2).tolist()
retention_1_clean = retention_clean.set_index('test_version')['retention_1'].loc[groups].round(2).tolist()
retention_7_clean = retention_clean.set_index('test_version')['retention_7'].loc[groups].round(2).tolist()

# ---------- Retention data ----------
retention_data = {
    "Dataset": ["Full Data", "Cleaned (No Zero-Players + No Outliers)"],
    "gate_30 (1d)": [retention_1_full[0], retention_1_clean[0]],
    "gate_40 (1d)": [retention_1_full[1], retention_1_clean[1]],
    "gate_30 (7d)": [retention_7_full[0], retention_7_clean[0]],
    "gate_40 (7d)": [retention_7_full[1], retention_7_clean[1]]
}
df_retention = pd.DataFrame(retention_data)

# ---------- Display tables ----------
st.subheader("Group Balance by Users")
st.dataframe(df_groups)

st.subheader("Retention by Groups (Before and After Cleaning)")
st.dataframe(df_retention)

# ---------- Plot 1d Retention ----------
st.subheader("Cleaning Impact on Retention Day 1")
fig, ax = plt.subplots()
labels = df_retention["Dataset"]
x = range(len(labels))
width = 0.35

ax.bar([i - width/2 for i in x], df_retention["gate_30 (1d)"], width, label="gate_30", color="#1f77b4")
ax.bar([i + width/2 for i in x], df_retention["gate_40 (1d)"], width, label="gate_40", color="#ff7f0e")

ax.set_ylabel("Retention Day 1 (%)")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15)
ax.set_title("Retention Before and After Cleaning (Day 1)")
ax.legend()

st.pyplot(fig)

st.title("Player Behavior by Segments")

late_segment = analyze_segment(get_late_starters(clean_df))
loyal_segment = analyze_segment(get_loyal_users(clean_df))
all_users = analyze_segment(clean_df)

segments = [late_segment, loyal_segment, all_users]

# Segmented data
segment_data = {
    "Segment": ["Late Starters", "Loyal Users", "All Users"],
    "gate_30": get_list_data_from_segment(segments, 'test_version', 'avg_levels', 'gate_30'),
    "gate_40": get_list_data_from_segment(segments, 'test_version', 'avg_levels', 'gate_40'),
    "Difference": get_list_data_from_segment(segments, 'test_version', 'difference', 'gate_40'),
    "p-value": get_list_data_from_segment(segments, 'test_version', 'p_value', 'gate_40'),
    "Cohen's d": get_list_data_from_segment(segments, 'test_version', 'Cohen_s d', 'gate_40'),
}
df_segments = pd.DataFrame(segment_data)

# Table with segments
st.subheader("Average Number of Levels by Segment")
st.dataframe(df_segments)

# Select segment by select-box
segment_selected = st.selectbox("Select segment for chart", df_segments["Segment"])

# Bar chart
selected_row = df_segments[df_segments["Segment"] == segment_selected].iloc[0]

fig, ax = plt.subplots()
ax.bar(["gate_30", "gate_40"], [selected_row["gate_30"], selected_row["gate_40"]],
       color=["#1f77b4", "#ff7f0e"])
ax.set_ylabel("Average Number of Levels")
ax.set_title(f"{segment_selected}: gate_30 vs gate_40")
st.pyplot(fig)

# Conclusions
st.markdown(f"""
### Statistics:
- Difference: **{selected_row['Difference']} game rounds**
- p-value: **{selected_row['p-value']}**
- Cohen's d: **{selected_row["Cohen's d"]}**

{ "Difference is NOT statistically significant" if selected_row['p-value'] > 0.05 else "Difference IS statistically significant" }
""")

st.title("Final Conclusions")

percents = distribution_full.set_index("test_version")["percent"].loc[groups].tolist()
retention_1_difference = retention_full.set_index('test_version')['retention_1'].loc['difference']
retention_7_difference = retention_full.set_index('test_version')['retention_7'].loc['difference']
zero_players = calculate_zero_players(df, 'test_version', 'userid', 'sum_gamerounds')
zero_percents = zero_players.set_index('test_version')['percent'].loc[groups].tolist()
outliers_value = get_outliers_value(df, 'sum_gamerounds', 0.99)

st.markdown(f"""
### Key Results

- Groups are **almost perfectly balanced**: `gate_30` ({percents[0]}%) vs `gate_40` ({percents[1]}%)
- In **retention metrics**:
    - **Day 1**: `gate_30` retention is **{retention_1_difference}% higher**
    - **Day 7**: retention also higher for `gate_30` by **{retention_7_difference}%**
    - After data cleaning, the difference **remains**, confirming **stability**

---

### Data Cleaning

- Removed:
    - **Zero-activity players (~{zero_percents[0]}%)**
    - Top 1% outliers (over {outliers_value} levels, ~1%)
- After cleaning:
    - Metrics **did not change direction**
    - This indicates **result reliability**

---

### Segment Analysis

- **Late Starters**:
    - gate_40 performed slightly better (**+1.9 levels**), but **p = 0.456**
    - → **Not statistically significant**
- **Loyal Users**:
    - gate_40 completed on average **3.5 more levels**, but **p = 0.08**
    - → **Still not statistically significant**
- **All Users**:
    - Averages almost identical (**46.7 vs 46.5 levels**), **p = 0.748**

---

### Final Summary

- **gate_30 showed better retention** on both Day 1 and Day 7
- **No statistically significant difference** in engagement (levels)
- Based on retention metrics — **setting the gate at level 30 is more effective**

> However, the gate is set to level 40 in production — possibly due to **other business factors** like LTV or monetization
""")