
# Load External Libraries
# Pandas DataFrames for reading and manipulating data.
# Think of it as in-memory Excel sheets, but more practical and powerful!
import pandas as pd

import numpy as np

# Matplotlib & PyPlot for visualization.
import matplotlib.pyplot as plt

# Tell Matplotlib to use Ggplot-style charts as in R.
#plt.style.use('ggplot')

# Seaborn is a helper library makeing Matplotlib easier to use.
import seaborn as sns

# Stats tools
from scipy import stats

from statistics import median

# Read the Dataset
df = pd.read_csv("diabetes.csv")
df.describe()

# Plot Boxplots with Seaborn
box = sns.boxplot(x=df['SerumInsulin'])
box.set_title = "SerumInsulin Boxplot"
plt.show()