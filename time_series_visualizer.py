import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates = True)

# Clean data
df = df[df["value"] >= df["value"].quantile(0.025)]
df = df[df["value"] <= df["value"].quantile(0.975)]


def draw_line_plot():
    # Draw line plot
  lines = df.plot()
  lines.set_xlabel("Date")
  lines.set_ylabel("Page Views")
  lines.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")





    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar["month"]= df.index.month
  df_bar["year"]= df.index.year
  df_bar= df.groupby(["year","month"])["value"].mean().unstack()

    # Draw bar plot
  axes = df_bar_grouped.plot.bar(figsize=(14,5))
  axes.set_xlabel("Years")
  axes.set_ylabel("Average Page Views")
# import datetime for the below line
  axes.legend(labels = [datetime.datetime.strptime(str(d), "%m").strftime("%B") for d in sorted(df_bar.index.month.unique())])





    # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1,2)
  box1 = sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
  box1.set_xlabel("Year")
  box1.set_ylabel("Page Views")
  box1.set_title("Year-wise Box Plot (Trend)")

  box2 = sns.boxplot(data=df_box, x="month", y="value", ax=axes[1])
  box2.set_xlabel("Month")
  box2.set_ylabel("Page Views")
  box2.set_title("Month-wise Box Plot (Seasonality)")





    # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
