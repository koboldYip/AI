import matplotlib.pyplot as pyplot
import pandas
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = pandas.get_dummies(pandas.read_csv("breast_cancer.csv"))

tags = data.get("diagnosis_B", "diagnosis_M")
data.drop(["Unnamed: 32", "diagnosis_B", "diagnosis_M", "id"], axis=1, inplace=True)

scaler = StandardScaler()
data = scaler.fit_transform(data)

kfold = KFold(n_splits=5, shuffle=True, random_state=0)
results = []
neighbours = []

for i in range(2, 50):
    model = KNeighborsClassifier(n_neighbors=i)
    array = cross_val_score(model, data, tags, cv=kfold, scoring="accuracy")
    results.append(sum(array) / 5)
    neighbours.append(i)

print("Наилучший результат при количесвте соседей =", neighbours[results.index(max(results))])
pyplot.plot(neighbours, results, '.-b')
pyplot.show()
