
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('C:/Users/nidha_5c/OneDrive/Desktop/task/pdf_app/Student_Marks.csv')


print(df.head())

X = df[['number_courses', 'time_study']]
y = df['Marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


joblib.dump(model, 'trained_model.pkl')


print(f"Model training score: {model.score(X_test, y_test)}")
