#%%
import seaborn as sns
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import util 


BASE_DIR = Path(__file__).parents[1]
OUTPUT_DIR = BASE_DIR / "output"
ANALYSIS_DIR = BASE_DIR / "analysis"
print(OUTPUT_DIR)

data_df = pd.read_csv(OUTPUT_DIR/ 'input.csv.gz')
#%%
#data_df = pd.read_csv(OUTPUT_DIR / "dummy_df.csv")

data_df.first_sv_prescription_date =  data_df.first_sv_prescription_date.astype(
    'datetime64[ns]'
)

monthly_perscription_counts = data_df.groupby(
    data_df["first_sv_prescription_date"].dt.strftime("%Y-%m")
).size()

monthly_perscription_counts = monthly_perscription_counts.rename(
    'count'
).rename_axis('date').reset_index()

monthly_perscription_counts.date =  monthly_perscription_counts.date.astype(
    'datetime64[ns]'
)

monthly_perscription_counts.to_csv(
    OUTPUT_DIR / 'monthly_perscription_counts.csv'
)

#%%%

fig, ax = plt.subplots()
monthly_count_plot = sns.lineplot(
    data = monthly_perscription_counts,
    x = 'date',
    y = 'count',
    ax=ax,
    linewidth=2,
)
# date_string
ax.xaxis.set_major_formatter(
    mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

ax = util.set_labels(ax, "Monthly Perscription Rate", fontsize=12)
ax = util.style_plot(ax)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

plt.savefig(
    OUTPUT_DIR / "monthly_perscription_rate.svg"
)