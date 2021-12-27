import pandas as pd
import numpy as np
from pandas.core.indexes import base
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_census = pd.read_csv('./census.csv')
# print(base_census)
# print(base_census.isnull().sum())

# print(np.unique(base_census['income'], return_counts=True))
# sns.countplot(x = base_census['income']);
# plt.hist(x = base_census['hour-per-week']);
# plt.hist(x = base_census['education-num']);
# plt.hist(x = base_census['age']);


# grafico = px.treemap(base_census, path=['workclass', 'age'])
# grafico.show()

# grafico = px.treemap(base_census, path=['occupation', 'relationship', 'age'])
# grafico.show()

# grafico = px.parallel_categories(base_census, dimensions=['occupation', 'relationship'])
# grafico.show()

# grafico = px.parallel_categories(base_census, dimensions=['workclass', 'occupation', 'income'])
# grafico.show()

# grafico = px.parallel_categories(base_census, dimensions=['education', 'income'])
# grafico.show()