import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 

dataset = pd.read_csv('petrol_consumption.csv') 

dataset.head()  

dataset.describe()

X = dataset[['Petrol_tax', 'Average_income', 'Paved_Highways',  
       'Population_Driver_licence(%)']]
y = dataset['Petrol_Consumption']  


from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)  

print(regressor.intercept_)  

print(regressor.coef_)  

#Prints R Square value
regressor.score(X_train, y_train) 

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
coeff_df  

y_pred = regressor.predict(X_test) 


df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df 

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
