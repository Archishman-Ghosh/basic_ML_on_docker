import joblib
model = joblib.load("myModel.pkl")
print()
print(model.predict([[7.6]]))
print()
