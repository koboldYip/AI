import matplotlib.pyplot as pyplot
import pandas
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pandas.get_dummies(pandas.read_csv("breast_cancer.csv"))
tags = data.get("diagnosis_B")
data.drop(["Unnamed: 32", "diagnosis_B", "diagnosis_M", "id"], axis=1, inplace=True)
data_train, data_test, tags_train, tags_test = train_test_split(data, tags, test_size=0.3, train_size=0.7,
                                                                random_state=0)
results = []
train_results = []
neighbours = []

print(data.columns)

for i in range(2, 50):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(data_train, tags_train)
    prediction = model.predict(data_test)
    results.append(accuracy_score(prediction, tags_test))
    train_prediction = model.predict(data_train)
    train_results.append(accuracy_score(train_prediction, tags_train))
    neighbours.append(i)

print("Наилучший результат при количесвте соседей =", neighbours[results.index(max(results))])

pyplot.plot(neighbours, results, '.-b')
pyplot.plot(neighbours, train_results, '.-r')
pyplot.show()
