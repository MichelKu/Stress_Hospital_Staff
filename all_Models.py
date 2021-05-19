import numpy as np
import pandas as pd

# Data maipulations and statistics
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

# Database
import sqlite3

# Classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
import xgboost as xgb

# initalize clissifiers
classifierNB = GaussianNB()
classifierSVC = SVC(kernel = 'rbf', random_state = 0)
classifierRF = RandomForestClassifier(n_estimators = 150, random_state = 0)
classifierKNN = KNeighborsClassifier(n_neighbors=3)
classifierXGB = xgb.XGBClassifier(random_state = 0)
classifierLR = LogisticRegression(random_state=0)

# initializing StandardScaling
sc = StandardScaler()

# making multiple global varibles that is used in all functions.
con = sqlite3.connect("StressDatabase.db")
dataset = pd.read_sql_query("SELECT * FROM stress", con)
X = dataset.iloc[:, [0,1,2,3,5,6,8,9]].values  # change columns here to find out effect. 
y = dataset.iloc[:, 11].values    # Choose 10 for Stressedduringwork and 11 for Feelingonjob
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)
X_train = sc.fit_transform(X_train)

# Naive-Bayes

def train_NB():
  classifierNB.fit(X_train, y_train)
  y_pred = classifierNB.predict(sc.transform(X_test))

  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix and accuracy for Naive-Bayes \n")
  print(cm)
  print(accuracy_score(y_test, y_pred))

# SVC
def train_SVC():
  classifierSVC.fit(X_train, y_train)
  y_pred = classifierSVC.predict(sc.transform(X_test))

  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix and accuracy for SVC\n")
  print(cm)
  print(accuracy_score(y_test, y_pred))

# Random Forest
def train_RF():
  classifierRF.fit(X_train, y_train)
  y_pred = classifierRF.predict(sc.transform(X_test))

  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix and accuracy for Random forest \n")
  print(cm)
  print(accuracy_score(y_test, y_pred))

# K Nearest Neighbours
def train_Knn():
  classifierKNN.fit(X_train, y_train)
  y_pred = classifierKNN.predict(sc.transform(X_test))

  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix and accuracy for K Nearest neighbours \n")
  print(cm)
  print(accuracy_score(y_test, y_pred))

# Xgboost
def train_Xgb():
  classifierXGB.fit(X_train, y_train)
  y_pred = classifierXGB.predict(sc.transform(X_test))

  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix and accuracy for XGB \n")
  print(cm)
  print(accuracy_score(y_test, y_pred))

# Linear Regression
def train_LR():
  classifierLR.fit(X_train, y_train)
  y_pred = classifierLR.predict(sc.transform(X_test))

  cm = confusion_matrix(y_test, y_pred)
  print("Confusion matrix and accuracy for Linear regression\n")
  print(cm)
  print(accuracy_score(y_test, y_pred))

