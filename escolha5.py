from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()


X = iris.data
y = iris.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


clf = DecisionTreeClassifier()


clf.fit(X_train, y_train)


score = clf.score(X_test, y_test)


print("Acurácia do modelo:", score)
