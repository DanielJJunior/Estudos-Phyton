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


## Divisão entre previsores e classe
# X_census = base_census.iloc[:, 0:14].values
# print(X_census)
# y_census = base_census.iloc[:, 14].values
# print(y_census)

##LabelEncoder
# from sklearn.preprocessing import LabelEncoder
# label_encoder_teste = LabelEncoder()
# print(X_census[:,1])
# teste = label_encoder_teste.fit_transform(X_census[:,1])
# print(X_census[0])
# label_encoder_workclass = LabelEncoder()
# label_encoder_education = LabelEncoder()
# label_encoder_marital = LabelEncoder()
# label_encoder_occupation = LabelEncoder()
# label_encoder_relationship = LabelEncoder()
# label_encoder_race = LabelEncoder()
# label_encoder_sex = LabelEncoder()
# label_encoder_country = LabelEncoder()

# X_census[:,1] = label_encoder_workclass.fit_transform(X_census[:,1])
# X_census[:,3] = label_encoder_education.fit_transform(X_census[:,3])
# X_census[:,5] = label_encoder_marital.fit_transform(X_census[:,5])
# X_census[:,6] = label_encoder_occupation.fit_transform(X_census[:,6])
# X_census[:,7] = label_encoder_relationship.fit_transform(X_census[:,7])
# X_census[:,8] = label_encoder_race.fit_transform(X_census[:,8])
# X_census[:,9] = label_encoder_sex.fit_transform(X_census[:,9])
# X_census[:,13] = label_encoder_country.fit_transform(X_census[:,13])


##OneHotEncoder
#len(np.unique(base_census['workclass'])) # 1 0 0 0 0 0 0 0, 0 0 0 0 1 0 0 0 0
# len(np.unique(base_census['occupation']))
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
# # onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder='passthrough')
# X_census = onehotencoder_census.fit_transform(X_census).toarray()
# print(X_census)
# print(X_census[0])
# print(X_census.shape)