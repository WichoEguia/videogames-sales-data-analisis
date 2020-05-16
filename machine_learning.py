import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

def machine_learning():
  dataset = pd.read_csv('winequality-red.csv')
  dataset.isnull().any() # Limpiando dataset

  print('\nValores del campo quality:')
  print(dataset['quality'].value_counts()) # Los valores quality tienen un rango de 2 a 8

  # Clasificando la calidad del vino [quality] en malo y bueno según el rango
  bins = (2, 6.5, 8)
  group_names = ['malo', 'bueno']
  dataset['quality'] = pd.cut(dataset['quality'], bins = bins, labels = group_names)

  # Conviertiendo categorias "buena" y "mala" en valores numericos
  # -> 0 = malo
  # -> 1 = bueno
  label_quality = LabelEncoder()
  dataset['quality'] = label_quality.fit_transform(dataset['quality'])
  dataset['quality'].value_counts()

  X = dataset.iloc[:, :-1]
  Y = dataset.iloc[:, -1].values # Obteniendo propiedad quality

  # Entrenando X y Y
  # Dividiendo conjunto de prueba y entrenamiento
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

  # Optimizando el resultado con escalado estandar
  sc = StandardScaler()
  X_train = sc.fit_transform(X_train)
  X_test = sc.fit_transform(X_test)

  # Prediciendo usado una Maquina de Soporte Vectorial
  svc = SVC()
  svc.fit(X_train, Y_train)
  pred_svc = svc.predict(X_test)

  print()
  print(classification_report(Y_test, pred_svc))