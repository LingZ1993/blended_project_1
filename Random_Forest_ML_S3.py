#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Random_Forest_ML


# In[1]:


# Import dependencies for Random_Forest
from path import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


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


# remove the column : Unnamed:0
# df.columns

df = df.drop(columns=["Unnamed: 0", "id"], axis= 1)


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
    # looks good- 52500, 12 for the train.


# In[10]:


X_test.shape
    # again, looks good. 17500, 12


# In[ ]:


# # # splitting data up into the _train, _test ***USING RANDOM STATE 1
# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 1)

# X_train.shape
# #     # looks good- 52500, 13 for the train.


# In[11]:


# Scale 

# Creating a StandardScaler instance.
scaler = StandardScaler()
# Fitting the Standard Scaler w/ training data.
X_scaler = scaler.fit(X_train)

# Scaling the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[12]:


# Fit the random forest model 

# Create a random forest classifier.

randomforest_model = RandomForestClassifier(n_estimators=500, random_state=1)


# In[13]:


# fitting the model
randomforest_model = randomforest_model.fit(X_train_scaled, y_train)
randomforest_model


# In[14]:


# Making predictions using the testing data
predictions = randomforest_model.predict(X_test_scaled)
predictions


# In[15]:


# Eval the model using confusion_matrix

# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)
cm


# In[16]:


# Create a Df from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual True", "Actual False"], columns=["Predicted True", "Predicted False"])
cm_df


# In[17]:


# Calculating the accuracy score.
acc_score = accuracy_score(y_test, predictions)


# In[18]:


# Displaying results
print("Confusion Martix")
display(cm_df)
print(f"Accuracy Score : {acc_score}")
print("Classification_Report")
print(classification_report(y_test, predictions))


# In[19]:


# Calculate feature importance ranking in the Random Forest model.
importances = randomforest_model.feature_importances_
importances

# out is array of scores for the features in the X_test set (sum = 1.0)


# In[20]:


# Can sort features by their importance
sorted(zip(randomforest_model.feature_importances_, X.columns), reverse=True)

# the sorted function will sort the zipped list of features
# with their column name (X.columns) in reverse order—
# more important features first—with reverse=True.

