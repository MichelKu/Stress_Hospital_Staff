# Efter att tidtagit de olika modellerna föll valet på Random forest. 

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import sqlite3


sc = StandardScaler()
classifier11 = RandomForestClassifier(n_estimators = 150, random_state = 0)
#classifier12 = RandomForestClassifier(n_estimators = 150, random_state = 0)

def train_col11():
  con = sqlite3.connect("StressDatabase.db")
  
  dataset = pd.read_sql_query("SELECT * FROM stress", con)
  X = dataset.iloc[:, [0,1,2,4,5,7,8,9]].values  # change columns here to find out effect. 
  y = dataset.iloc[:, 10].values    # put the dependent varible here.

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)
  
  X_train = sc.fit_transform(X_train)

  classifier11.fit(X_train, y_train)


def predict_col11(age, gender, Specialization, workHours, patientPerDay, overtimeWorkInterest, overtimeWorkPaid, sector):
  y_pred = classifier11.predict(sc.transform([[age, gender, sector, Specialization, workHours, patientPerDay, overtimeWorkInterest, overtimeWorkPaid]]))
  #print('from inside ML_model col11: ', y_pred)
  y_pred = int(y_pred)
  return { "col11_predict": y_pred }




# def train_col12():
#   con = sqlite3.connect("StressDatabase.db")
 
#   dataset = pd.read_sql_query("SELECT * FROM stress", con)
#   X = dataset.iloc[:, [0,1,2,4,5,7,8,9]].values  # change columns here to find out effect. 
#   y = dataset.iloc[:, 11].values    # put the dependent varible here.

#   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)
  
#   X_train = sc.fit_transform(X_train)

#   classifier12.fit(X_train, y_train)

# def predict_col12(age, gender, Specialization, workHours, patientPerDay, overtimeWorkInterest, overtimeWorkPaid, sector):
#   y_pred = classifier12.predict(sc.transform([[age, gender, sector, Specialization, workHours, patientPerDay, overtimeWorkInterest, overtimeWorkPaid]]))
#   #print('from inside ML_model col12: ', y_pred)
#   y_pred = int(y_pred) 
#   return{"col12-predict": y_pred}


#train_col11()
#train_col12()

#predict_col11(2,1,6,1,1,1)
# predict_col12(2,2,2,2,2,1)
