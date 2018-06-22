import pydotplus
import collections
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv('vermelho.csv', delimiter=';')
test = pd.read_csv('testevermelho.csv', delimiter=';')

data_feature_name = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
cols2 = ['quality']

features = train.as_matrix(data_feature_name)
labels = train.as_matrix(cols2)
x_test = test.as_matrix(data_feature_name)
y_test = test.as_matrix(cols2)

clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best') #, random_state=5
clf = clf.fit(features, labels)

outputs = clf.predict(x_test)

print(mean_squared_error(y_test, outputs))

plt.plot(np.linspace(-1, 1, len(y_test)), y_test, label='data', color='black')
plt.plot(np.linspace(-1, 1, len(y_test)), outputs, label='prediction', color='red')
plt.show()

dot_data = tree.export_graphviz(clf, feature_names=data_feature_name, out_file=None,filled=True,rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('turquoise', 'orange')

edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))
    
for edge in edges:
    edges[edge].sort() 
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])
        
graph.write_png('tree.png')