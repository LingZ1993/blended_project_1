#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Tuning the Random Forest ML model


# In[2]:


# Random Forest imports 

import pandas as pd
from path import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


# In[3]:


# import from AWS

from AWS_DB import get_data
data = get_data()
data = pd.DataFrame(data)
data.head()


# In[4]:


# Import the dataset 
df = pd.read_csv("cardio_complete.csv")
df.head()


# In[5]:


# remove the column : Unnamed:0, "id", "alco", "smoke", "active", "gender"


df= df.drop(["Unnamed: 0", "id", "alco", "smoke", "active", "gender"], axis=1)
df


# In[6]:


df = df.rename(columns = {"age" : "age_days"})


# In[7]:


# splitting the df into two - target variable (cardio) and the features sans cardio.

y = df["cardio"]
X = df.drop(columns="cardio")


# In[8]:


X


# In[9]:


# # splitting data up into the _train, _test ***USING RANDOM STATE 1
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state= 1)

X_train.shape
#     # looks good- 52500, 8 for the train.


# In[10]:


# Creating a StandardScaler instance.

scaler = StandardScaler()

# Fitting the Standard Scaler w/ training data.

X_scaler = scaler.fit(X_train)

# Scaling the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[11]:


# Fit the random forest model 

# Create a random forest classifier.

randomforest_model = RandomForestClassifier(n_estimators=500, random_state=1)


# In[12]:


# fitting the model
randomforest_model = randomforest_model.fit(X_train_scaled, y_train)
randomforest_model


# In[13]:


# Making predictions using the testing data
predictions = randomforest_model.predict(X_test_scaled)
predictions


# In[14]:


# Eval the model using confusion_matrix

# Calculating the confusion matrix
cm = confusion_matrix(y_test, predictions)
cm


# In[15]:


# Create a Df from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual True", "Actual False"], columns=["Predicted True", "Predicted False"])
cm_df


# In[16]:


# Calculating the accuracy score.
acc_score = accuracy_score(y_test, predictions)


# In[17]:


# Displaying results
print("Confusion Martix")
display(cm_df)
print(f"Accuracy Score : {acc_score}")
print("Classification_Report")
print(classification_report(y_test, predictions))


# In[18]:


# Calculate feature importance ranking in the Random Forest model.
importances = randomforest_model.feature_importances_
importances


# In[19]:


# Sort features by their importance
sorted(zip(randomforest_model.feature_importances_, X.columns), reverse=True)


# In[ ]:


# Dropping those columns didn't increase the accuracy score, and just added more importance to the age of the subject
# and the other features.  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




