#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies 

import pandas as pd
import numpy as np


# In[7]:


# Read in CSV file

health_data = pd.read_csv("diabetes_sample.csv")
health_df = pd.DataFrame(health_data)
health_df.head()


# In[8]:


health_df.info


# In[9]:


# trying to add additional columns so i can get 13 like we have in our real dataset
add_df = health_df


# In[19]:


# data = np.random.randint(5,30,size=10)
gender_binary = np.random.randint(1,3,size = 768)
gender_df = pd.DataFrame(gender_binary, columns= ["gender"])
gender_df.head()


# In[21]:


# alcohol, smoking, family_history

# data = np.random.randint(5,30,size=(10,3))
# df = pd.DataFrame(data, columns=['random_numbers_1', 'random_numbers_2', 'random_numbers_3'])

binary_variables = np.random.randint(1,3, size=(768,3))
binary_df = pd.DataFrame(binary_variables, columns=["Alcohol", "Smoker", "Family_History"])
binary_df.head(20)


# In[22]:


# merging the 4 columns I created to get to the 13 x 1 that the cardio dataset is in
gender_df.merge(binary_df, left_index=True, right_index=True)


# In[25]:


created_df = gender_df.merge(binary_df, left_index=True, right_index=True)
created_df


# In[26]:


# merging the diabetes data (9 columns) w/ the 4 variable columns I've made

health_df.merge(created_df, left_index=True, right_index=True)


# In[27]:


sample_df = health_df.merge(created_df, left_index=True, right_index=True)


# In[30]:


sample_df = sample_df[["gender","Alcohol", "Smoker", "Age","Family_History", "BMI", "Insulin", "DiabetesPedigreeFunction", "SkinThickness", "BloodPressure", "Glucose", "Pregnancies", "Outcome"]]


# In[31]:


sample_df.head()


# In[32]:


sample_df.to_csv(r'In_Progress\Sample_data.csv')


# In[ ]:




