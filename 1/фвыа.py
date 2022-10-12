import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Чтение файла датасета
df = pd.read_csv('breast_cancer.csv')
# Отображение таблицы с полученными данными
pd.get_dummies(df)
#############################################################################
# Присвоим значению X (объекты) все колонки, кроме diagnosis, id, Unnamed: 32
X = df.drop(columns=(['diagnosis', 'id', 'Unnamed: 32']))
# Присвоим значению y (ответы) присвоили колонку diagnosis
y = df['diagnosis']

# Разделяем выборку на обучающую и тестовую
X_train, X_test, y_train, y_test = train_test_split(X, y)
# Создадим лист для дальнейшего сохранения доли верных ответов модели
k_list = []
# Значение наилучшего k
best_k = 0
# Номер лучшего k
index_of_best_k = []
# Изменяем число соседей от 1 до 50
for i in range(1, 50):
    #   Задаем количество ближайших соседей
    knn = KNeighborsClassifier(n_neighbors=i)
    #   Обучение (тренировка) модели на обучающей выборке X, y
    knn.fit(X_train, y_train)
    #   Предсказание значения целевого признака по входным признакам для новых объектов
    y_test_predict = knn.predict(X_test)
    #   Оцениваем долю верных ответов модели
    acc = accuracy_score(y_test, y_test_predict)
    #   Заполнение листа ответами
    k_list.append(acc)
    #   Определение наилучшего значения
    if (acc > best_k):
        best_k = acc

# Определяем лучшее число соседей
for j in range(49):
    if (k_list[j] == best_k):
        index_of_best_k.append(j + 1)

# Визуализация полученных данных
plt.title("k-nearest neighbors")
plt.xlabel("Number of neighbors")
plt.ylabel("Share of correct answers")
plt.plot(k_list)

print('Лучшее количество соседей - ', index_of_best_k, ', с долей верных ответов ', best_k)
#############################################################################
# Генератор разбиения. Выставляем количество блоков в генераторе разбиения
kf = KFold(n_splits=5, shuffle=True)
# Создадим новый лист для сохранения доли верных ответов модели
kf_list = []
# Значение наилучшего k при кросс-валидации
best_kf = 0
# Номер лучшего k при кросс-валидации
index_of_best_kf = []

# Изменяем число соседей от 1 до 50
for i in range(1, 50):
    #   Задаем количество ближайших соседей
    knn = KNeighborsClassifier(n_neighbors=i)
    #   Проведем алгоритм кросс-валидации
    calc = cross_val_score(knn, X, y, cv=kf, scoring='accuracy')
    #   Рассчитаем среднее значение для опытов после кросс-валидации и занесем их в лист
    result = sum(calc) / len(calc)
    kf_list.append(result)
    #   Определение наилучшего значения
    if (result > best_kf):
        best_kf = result

# Определяем лучшее число соседей
for j in range(49):
    if (kf_list[j] == best_kf):
        index_of_best_kf.append(j + 1)

plt.title("k-nearest neighbors")
plt.xlabel("Number of neighbors")
plt.ylabel("Share of correct answers")
plt.plot(kf_list)

print('Лучшее количество соседей - ', index_of_best_kf, ', с долей верных ответов ', best_kf)
#############################################################################
# Логистическая регрессия
from sklearn.linear_model import LogisticRegression
import numpy as np

# Лист с результатами после логитической регрессии
lr_results = []
# Создадим массив, заполненный расчетными точками
C_mass = np.arange(0.01, 1, 0.01)
# Значение наилучшего С
best_C = 0
# Номер лучшего С
index_of_best_C = []
# Проходимся по всем элементам массива
for i in range(99):
    # Зададим логистическую регрессию
    lr = LogisticRegression(C=C_mass[i], max_iter=10000)
    #   Производим кросс-валидацию
    calc = cross_val_score(lr, X, y, cv=kf, scoring='accuracy')
    #   Вычисляем среднее значение и заносим в таблицу
    acc = sum(calc) / len(calc)
    lr_results.append(acc)
    #   Определение наилучшего С
    if (acc > best_C):
        best_C = acc

# Определяем лучшее значение С
for j in range(99):
    if (lr_results[j] == best_C):
        index_of_best_C.append((j + 1) / 100)

# Визуализация графика
plt.title("Logistic regression")
plt.xlabel("Value of the coefficient C")
plt.ylabel("Share of correct answers")
plt.plot(C_mass, lr_results)

print('Лучшее значение С - ', index_of_best_C, 'c долей верных ответов ', best_C)
#############################################################################
# Метод k-ближайших соседей с масштабированием
from sklearn.preprocessing import StandardScaler

# Осуществим масштабирование
scaler = StandardScaler()
X = scaler.fit_transform(X)
# Создадим новый лист для сохранения доли верных ответов модели
kf_list_scal = []
# Значение наилучшего k при кросс-валидации
best_kf = 0
# Номер лучшего k при кросс-валидации
index_of_best_kf = []
for i in range(1, 50):
    #   Задаем количество ближайших соседей
    knn = KNeighborsClassifier(n_neighbors=i)
    #   Проведем алгоритм кросс-валидации
    calc = cross_val_score(knn, X, y, cv=kf, scoring='accuracy')
    #   Рассчитаем среднее значение для опытов после кросс-валидации и занесем их в лист
    result = sum(calc) / len(calc)
    kf_list_scal.append(result)
    #   Определение наилучшего значения
    if (result > best_kf):
        best_kf = result

# Определяем лучшее число соседей
for j in range(49):
    if (kf_list_scal[j] == best_kf):
        index_of_best_kf.append(j + 1)

# Визуализация графика
plt.title("k-nearest neighbors")
plt.xlabel("Number of neighbors")
plt.ylabel("Share of correct answers")
plt.plot(kf_list_scal)

print('Лучшее количество соседей - ', index_of_best_kf, ', с долей верных ответов ', best_kf)
#############################################################################
lr_results_scal = []
# Создадим массив, заполненный расчетными точками
C_mass = np.arange(0.01, 1, 0.01)
# Значение наилучшего С
best_C = 0
# Номер лучшего С
index_of_best_C = []
# Проходимся по всем элементам массива
for i in range(99):
    # Зададим логистическую регрессию
    lr = LogisticRegression(C=C_mass[i], max_iter=10000)
    #   Производим кросс-валидацию
    calc = cross_val_score(lr, X, y, cv=kf, scoring='accuracy')
    #   Вычисляем среднее значение и заносим в таблицу
    result = sum(calc) / len(calc)
    lr_results_scal.append(result)
    #   Определение наилучшего С
    if (result > best_C):
        best_C = result

# Определяем лучшее значение С
for j in range(99):
    if (lr_results_scal[j] == best_C):
        index_of_best_C.append((j + 1) / 100)

# Визуализация графика
plt.title("Logistic regression")
plt.xlabel("Value of the coefficient C")
plt.ylabel("Share of correct answers")
plt.plot(C_mass, lr_results_scal)

print('Лучшее значение С - ', index_of_best_C, 'c долей верных ответов ', best_C)
