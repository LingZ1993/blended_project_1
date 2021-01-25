#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Working on testing out different ML models for the dataset


# In[1]:


# Import dependencies
from path import Path
import numpy as np
import pandas as pd


# In[2]:


# import 

from AWS_DB import get_data
data = get_data()
data = pd.DataFrame(data)
data.head()


# In[3]:


# Import the dataset 
df = pd.read_csv("cardio_complete.csv")
df.head()


# In[4]:


# remove the columns : Unnamed:0, id
df = df.drop(columns=["Unnamed: 0", "id"], axis= 1)


# check to make sure it's gone.


# In[5]:


df = df.rename(columns = {"age" : "age_days"})
df


# In[6]:


# splitting the df into two - target variable (cardio) and the features sans cardio.

y = df["cardio"]
X = df.drop(columns="cardio")


# In[7]:


# checking on target variable 
y.head(5)
#looks good


# In[8]:


# checking on features 

X.head(5)


# In[9]:


# splitting data up into the _train, _test ***USING RANDOM STATE 1
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 1, stratify= y)

X_train.shape
    # looks good- 52500, 13 for the train.


# In[10]:


X_test.shape
    # again, looks good. 17500, 13


# In[11]:


# take a quick look at y_train -> looks good.
y_train.shape


# In[ ]:


# CREATING THE LOGISTIC REGRESSION MODEL


# In[12]:


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver ='lbfgs',
                                max_iter=200,
                                random_state=1)


# In[13]:


# Fit (Train) the data 
classifier.fit(X_train, y_train)


# In[ ]:


# Make a predictions DF


# In[14]:


# y_pred = classifier.predict(X_test)
# results = pd.DataFrame({"Prediction": y_pred, "Actual": y_test}).reset_index(drop=True)
# results.head(20)

y_prediction = classifier.predict(X_test)
results = pd.DataFrame({"Prediction": y_prediction, "Actual": y_test}).reset_index(drop=True)
results.head(25)


# In[15]:


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_prediction))


# In[ ]:


# SECTION ABOVE IS FOR LOGISTIC REGRESSSION | ACCURACY SCORE WAS .713

