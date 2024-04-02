import pandas as pd
import numpy as np

pro_file = pd.read_csv('AB_NYC_2019.csv')

pro_file.head()

pro_file.tail()

pro_file.price.describe()

pro_file.info()

pro_file.isnull().sum()

lower_limit, upper_limit = pro_file.price.quantile([0.001, 0.99])
lower_limit, upper_limit

outliers = pro_file[(pro_file.price>upper_limit) | (pro_file.price<lower_limit)]
outliers.price.sample(10)

new_pro_file = pro_file[(pro_file.price<upper_limit) & (pro_file.price>lower_limit)]
new_pro_file.tail()

new_pro_file.head()

new_pro_file.price.describe()