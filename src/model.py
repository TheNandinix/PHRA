import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# load data
data = pd.read_csv("data/data.csv")

# input and output
X = data[['age','bmi','sleep','exercise','smoking','alcohol','stress','water']]
y = data['risk']

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "model.pkl")

print("Model trained and saved!")