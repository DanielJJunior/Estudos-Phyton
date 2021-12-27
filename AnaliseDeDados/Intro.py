import pandas as pd
import numpy as np
from pandas.core.indexes import base
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

credit_base = pd.read_csv('./credit_data.csv')
# credit_base # defaulted
# print(credit_base.head())
# print(credit_base.tail())
# print(credit_base.describe())
# print(credit_base[credit_base['income'] >= 69995.685578])
# print(credit_base[credit_base['loan'] <= 1.377630])

# print(np.unique(credit_base['default'], return_counts=True))

# print(sns.countplot(x = credit_base['default']));
# print(plt.hist(x = credit_base['loan']));
# print(plt.hist(x = credit_base['income']));
# print(plt.hist(x = credit_base['age']));
# grafico = px.scatter_matrix(credit_base, dimensions=['age', 'income', 'loan'], color = 'default')
# grafico.show()


# print(credit_base.loc[credit_base['age'] < 0])
# print(credit_base[credit_base['age'] < 0])

# credit_base3 = credit_base.drop(credit_base[credit_base['age'] < 0].index)
# print(credit_base3)
# print(credit_base3.loc[credit_base3['age'] < 0])

# print(credit_base.mean())
# print(credit_base['age'].mean())
# print(credit_base['age'][credit_base['age'] > 0].mean()) #media de idades sem negativos
# credit_base.loc[credit_base['age'] < 0, 'age'] = 40.92
# print(credit_base.loc[credit_base['age'] < 0])


# credit_base['age'].fillna(credit_base['age'].mean(), inplace = True)
# print(credit_base.loc[pd.isnull(credit_base['age'])])
# credit_base.loc[credit_base['clientid'].isin([29, 31, 32])]


# type(credit_base)

# X_credit = credit_base.iloc[:, 1:4].values
# # print(X_credit)
# type(X_credit)

# Y_credit = credit_base.iloc[:, 4].values
# # print(Y_credit)
# type(Y_credit)


# # print(X_credit[:,0].min(), X_credit[:,1].min(), X_credit[:,2].min())
# # print(X_credit[:,0].max(), X_credit[:,1].max(), X_credit[:,2].max())

# from sklearn.preprocessing import StandardScaler
# scaler_credit = StandardScaler()
# X_credit = scaler_credit.fit_transform(X_credit)