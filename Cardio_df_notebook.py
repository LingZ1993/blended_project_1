#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies 

import pandas as pd
import numpy as np


# In[2]:


# Read in file

cardio_path = "cardio_train.csv"
cardio_df = pd.read_csv(cardio_path)
cardio_df


# In[3]:


# Create new column- BMI

cardio_df["BMI"] = cardio_df["weight"]/ (cardio_df["height"]/100)**2


# In[4]:


# Check to see that it applied BMI 

cardio_df.head()


# In[6]:


# Rename columns 

# 

cardio_df = cardio_df.rename(columns={"weight" : "weight(kg)", "height" : "height(cm)", "ap_hi" : "systolic_bp", "ap_lo" : "diastolic_bp"})
cardio_df.head()


# In[7]:


cardio_df = cardio_df.round({'BMI': 2})
cardio_df


# In[8]:


# rename age -> age(days) in cardio_df 

cardio_df = cardio_df.rename(columns= {"age" : "age(days)"})
cardio_df


# In[9]:


# Make secondary dataFrame that includes the demographic sort of data | cardio_demo | 

cardio_demo = cardio_df[["id", "age(days)", "gender", "weight(kg)", "height(cm)", "BMI"]]


# In[10]:


# Check it

cardio_demo.head()


# In[14]:


# forgot to add target variable! cardio!!! Or do I need to add it?
cardio_demo["cardio"] = cardio_df["cardio"]
cardio_demo


# In[ ]:


# Make 2nd table/df. includes ID (to join on later) + systolic_bp, diastolic_bp, cholesterol, gluc, smoke, alco, active, cardio


# In[11]:


# 2nd table w/ target variable 
cardio_vitals = cardio_df[["id", "systolic_bp", "diastolic_bp", "cholesterol", "gluc", "smoke", "alco", "active", "cardio"]]


# In[12]:


# Check second table 
cardio_vitals.head()


# In[15]:


# export the (2) tables as .csv so we can upload them in SQLite | cardio_vitals | 

cardio_vitals.to_csv(r"In_progress\cardio_vitals.csv")

# sample_df.to_csv(r'In_Progress\Sample_data.csv')


# In[16]:


# export | cardio_demo | to .csv for SQLite

cardio_demo.to_csv(r"In_progress\cardio_demo.csv")


# In[ ]:




