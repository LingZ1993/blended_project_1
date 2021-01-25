#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Charts 


# In[1]:


# Import Dependencies 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:



x_axis = ["Logistic Regression", "Random Forest", "Tuned Random Forest"]


y_axis = [.713, .715, .706]


# In[7]:


# Create the plot.
plt.bar(x_axis, y_axis, color="deepskyblue", label='Accuracy')
# Create labels for the x and y axes.
plt.xlabel("Type of Model")
plt.ylabel("Accuracy Score(%)")
# Create a title.
plt.title("Accuracy Scores of the ML Models")
# Add the legend.
plt.legend()


# In[ ]:




