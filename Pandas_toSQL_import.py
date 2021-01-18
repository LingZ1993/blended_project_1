#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Imports
import pandas as pd
from sqlalchemy import create_engine

# Our CSVs  have a header don't need to pass column names as an argument.


# Load in the data
df = pd.read_csv(
    "cardio_demo_corrected.csv"
)

# Instantiate sqlachemy.create_engine object
engine = create_engine('postgresql://postgres:01eellv01@group-cardio-project-database-1993.clviqkfcmhow.us-east-2.rds.amazonaws.com:5432/Cardio_secrets')

# Save the data from dataframe to
# postgres table "cardio_demo"
df.to_sql(
    'cardio_demo_3', 
    engine,
    index=False # Not copying over the index
)


# In[ ]:


get_ipython().system('pip install psycopg2-binary')


# In[ ]:




