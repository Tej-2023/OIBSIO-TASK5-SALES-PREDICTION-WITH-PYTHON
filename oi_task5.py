

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error

df=pd.read_csv('Advertising.csv')
df

df.head()

df.tail()

df.drop("Unnamed: 0",axis=1,inplace=True)
df.columns=['TV','Radio','Newspaper','Sales']
df.head()

df.shape

df.describe()

df.info()

df.dtypes

df.isnull().sum()

df.duplicated().sum()

for col in df:
  sns.boxplot(data=df[col])
  plt.xlabel(col)
  plt.show()

sns.pairplot(df)
plt.show()

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),cmap="Blues",annot=True)

x=df[['TV','Radio', 'Newspaper']]
y=df['Sales']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

print("x_train:",x_train.shape)
print("y_train:",y_train.shape)
print("x_test:",x_test.shape)
print("y_test:",y_test.shape)

Lr=LinearRegression()
Lr.fit(x_train,y_train)

y_pred=Lr.predict(x_test)

Ac=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
Ac.head(10)

eva1=r2_score(y_test,y_pred)
eva1*=100
print("Accuracy:",eva1,'%')

MAE=mean_absolute_error(y_test,y_pred)
print("Mean Absolute Error:",MAE)

MsE=mean_squared_error(y_test,y_pred)
print("Mean Sqared Error:",np.sqrt(MsE))

"""**Insights**

**About the Dataset**

The Advertising Sales dataset includes information about advertising budgets and sales of a product in different media channels (TV, radio, and newspaper) The objective is to predict sales based on advertising expenditure. An Over View of The Dataset is given Below:

Features: The dataset typically includes three features or independent variables, TV Advertising budget spent on TV commercials. Radio: Advertising budget spent on radio commercials, Newspaper: Advertising budget spent on newspaper advertisements. Target Variable. The target variable or dependent variable is the sales figure associated with the advertising expenditures.

Size. The dataset usually consists of a modest number of observations or examples, commonly around 200-300

The purpose of using this dataset is to build a regression model that can predict sales based on the advertising budgets allocated to different media channels By analyzing the relationship between advertising expenditures and sales, marketers can gain insights into how effective each channel is in driving sales and optimize their advertising strategies accordingly

The Advertising Sales dataset serves as a valuable resource for studying the impact of advertising on sales and conducting predictive analysis in the marketing domain.


**Conlusion About The Dataset**

Here i have done exploratory data analysis on This data and then Build a Linear regression model.

By doing EDA on the dataset we will Get basic idea about the data. Moreover my aim is to make a linear regression model, for that i need a basic knowledge of the correlation between the feature's

Heatmap will give an idea about this. from analysing heatmap we can understand that The dependent variable Sales is highly correlated with the independent variables Tv, Radio and Newspaper.

There for We can Train a Model using these independant variables for the dependent variable 'Sales', Here i have stored them on X,Y respectively.

After traing the dataset i have fit a linear regression model using the fuction Linear Regression() This model have 92% accuracy Which means the predicted value and the actual value have great similarity.So we can say that which is a good Model.
"""
