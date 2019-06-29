################################
# import pandas and scikit learn
################################
import pandas as pd
from sklearn import linear_model

################################
# load dataset
################################
sqfeet = pd.DataFrame([1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])
price = pd.DataFrame([119000, 126000, 133000, 150000, 161000, 163000, 169000, 182000, 201000, 209000])

################################
# train the model
################################
model = linear_model.LinearRegression()
model.fit(sqfeet, price)

################################
# make prediction
################################
model.predict( pd.DataFrame([1750]))
