import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import os

# -----------------------------------------------------------------------------
# SETUP
# -----------------------------------------------------------------------------

df = pd.read_csv("data/processed/happiness_clean.csv")

os.makedirs("outputs/figures", exist_ok=True)

sns.set_theme(style="whitegrid")
PALETTE = "Blues_d"

print("=" * 60)
print("Generating visualizations...")
print("=" * 60)

# -----------------------------------------------------------------------------
# VISUAL 1: TOP 10 VS BOTTOM 10 HAPPIEST COUNTRIES
# -----------------------------------------------------------------------------

avg = (
    df.groupby("country")["happiness_score"]
    .mean()
    .round(3)
    .reset_index()
    .rename(columns={"happiness_score": "avg_score"})
    .sort_values("avg_score", ascending=False)
)

top10    = avg.head(10)
bottom10 = avg.tail(10).sort_values("avg_score")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].barh(top10["country"], top10["avg_score"], color="#2166ac")
axes[0].set_title("Top 10 Happiest Countries (2015-2019)", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Average Happiness Score")
axes[0].set_xlim(0, 8)
for i, v in enumerate(top10["avg_score"]):
    axes[0].text(v + 0.05, i, str(v), va="center", fontsize=9)

axes[1].barh(bottom10["country"], bottom10["avg_score"], color="#d6604d")
axes[1].set_title("Bottom 10 Happiest Countries (2015-2019)", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Average Happiness Score")
axes[1].set_xlim(0, 8)
for i, v in enumerate(bottom10["avg_score"]):
    axes[1].text(v + 0.05, i, str(v), va="center", fontsize=9)

plt.suptitle("World Happiness Rankings (Average 2015-2019)", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/figures/01_top_bottom_countries.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Visual 1 saved: 01_top_bottom_countries.png")

# -----------------------------------------------------------------------------
# VISUAL 2: GLOBAL AVERAGE HAPPINESS TREND 2015-2019
# -----------------------------------------------------------------------------

yearly = (
    df.groupby("year")["happiness_score"]
    .mean()
    .round(3)
    .reset_index()
)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(yearly["year"], yearly["happiness_score"], marker="o", linewidth=2.5,
        color="#2166ac", markersize=8)

for _, row in yearly.iterrows():
    ax.text(row["year"], row["happiness_score"] + 0.005,
            str(row["happiness_score"]), ha="center", fontsize=10)

ax.set_title("Global Average Happiness Score (2015-2019)",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Average Happiness Score")
ax.set_ylim(5.2, 5.6)
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))

plt.tight_layout()
plt.savefig("outputs/figures/02_global_trend.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Visual 2 saved: 02_global_trend.png")

# -----------------------------------------------------------------------------
# VISUAL 3: CORRELATION HEATMAP
# -----------------------------------------------------------------------------

features = [
    "happiness_score", "gdp_per_capita", "social_support",
    "life_expectancy", "freedom", "corruption", "generosity"
]

corr = df[features].corr().round(2)

fig, ax = plt.subplots(figsize=(9, 7))
sns.heatmap(
    corr, annot=True, fmt=".2f", cmap="coolwarm",
    linewidths=0.5, ax=ax, annot_kws={"size": 10}
)
ax.set_title("Correlation Heatmap of Happiness Factors",
             fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig("outputs/figures/03_correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Visual 3 saved: 03_correlation_heatmap.png")

# -----------------------------------------------------------------------------
# VISUAL 4: SCATTER PLOT — GDP VS HAPPINESS SCORE
# -----------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(
    df["gdp_per_capita"], df["happiness_score"],
    alpha=0.5, c=df["happiness_score"], cmap="Blues", edgecolors="grey", linewidth=0.3
)

plt.colorbar(scatter, ax=ax, label="Happiness Score")
ax.set_title("GDP per Capita vs Happiness Score (2015-2019)",
             fontsize=14, fontweight="bold")
ax.set_xlabel("GDP per Capita")
ax.set_ylabel("Happiness Score")

plt.tight_layout()
plt.savefig("outputs/figures/04_gdp_vs_happiness.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Visual 4 saved: 04_gdp_vs_happiness.png")

# -----------------------------------------------------------------------------
# VISUAL 5: AVERAGE HAPPINESS BY REGION
# -----------------------------------------------------------------------------

regional = (
    df[df["region"] != "Unknown"]
    .groupby("region")["happiness_score"]
    .mean()
    .round(3)
    .sort_values()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(11, 6))
bars = ax.barh(regional["region"], regional["happiness_score"],
               color=sns.color_palette("Blues_d", len(regional)))

for bar, val in zip(bars, regional["happiness_score"]):
    ax.text(val + 0.03, bar.get_y() + bar.get_height() / 2,
            str(val), va="center", fontsize=9)

ax.set_title("Average Happiness Score by Region (2015-2016)",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Average Happiness Score")
ax.set_xlim(0, 8)

plt.tight_layout()
plt.savefig("outputs/figures/05_happiness_by_region.png", dpi=150, bbox_inches="tight")
plt.close()
print("✅ Visual 5 saved: 05_happiness_by_region.png")

# -----------------------------------------------------------------------------
# VISUAL 6: MOST IMPROVED VS MOST DECLINED COUNTRIES
# -----------------------------------------------------------------------------

df_2015 = df[df["year"] == 2015][["country", "happiness_score"]].rename(
    columns={"happiness_score": "score_2015"})
df_2019 = df[df["year"] == 2019][["country", "happiness_score"]].rename(
    columns={"happiness_score": "score_2019"})

change = pd.merge(df_2015, df_2019, on="country")
change["change"] = (change["score_2019"] - change["score_2015"]).round(3)
change = change.sort_values("change", ascending=False)

top5    = change.head(5)
bottom5 = change.tail(5).sort_values("change")

combined = pd.concat([top5, bottom5])
colors   = ["#2166ac" if x > 0 else "#d6604d" for x in combined["change"]]

fig, ax = plt.subplots(figsize=(11, 6))
ax.barh(combined["country"], combined["change"], color=colors)
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("Most Improved vs Most Declined Countries (2015 vs 2019)",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Change in Happiness Score")

for bar, val in zip(ax.patches, combined["change"]):
    offset = 0.02 if val >= 0 else -0.08
    ax.text(val + offset, bar.get_y() + bar.get_height() / 2,
            str(val), va="center", fontsize=9)

plt.tight_layout()
plt.savefig("outputs/figures/06_most_improved_declined.png", dpi=150, bbox_inches="tight")
plt.close()
print("Visual 6 saved: 06_most_improved_declined.png")

print("\n" + "=" * 60)
print("All 6 visualizations saved to outputs/figures/")
print("=" * 60)
