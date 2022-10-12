import matplotlib.pyplot as pyplot
import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pandas.get_dummies(pandas.read_csv("breast_cancer.csv"))
tags = data.get("diagnosis_B", "diagnosis_M")
data.drop(["Unnamed: 32", "diagnosis_B", "diagnosis_M", "id"], axis=1, inplace=True)

scaler = StandardScaler()
data = scaler.fit_transform(data)

data_train, data_test, tags_train, tags_test = train_test_split(data, tags, test_size=0.3, train_size=0.7,
                                                                random_state=0)
results = []
probability = []

for i in range(1, 100, 1):
    logic_regression = LogisticRegression(C=(i / 100))
    logic_regression.fit(data_train, tags_train)
    prediction = logic_regression.predict(data_test)
    results.append(accuracy_score(prediction, tags_test))
    probability.append(i / 100)

pyplot.plot(probability, results)
pyplot.show()
