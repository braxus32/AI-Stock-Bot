import pandas as panda
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = panda.read_csv('BB.csv')
data.head()

y=data.temp
x=data.drop('temp',axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
x_train.head()