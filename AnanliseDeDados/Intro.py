import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

credit_base = pd.read_csv('AnanliseDeDados\credit_data.csv')
credit_base # defaulted
# print(credit_base.head())
# print(credit_base.tail())
# print(credit_base.describe())
# print(credit_base[credit_base['income'] >= 69995.685578])
print(credit_base[credit_base['loan'] <= 1.377630])