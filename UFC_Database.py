#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine
import psycopg2
connstring = "postgresql+psycopg2://root:#Argyl0814*@ufc-database.cahc99ahc4gb.us-east-1.rds.amazonaws.com:5432/UFC_Database"
engine = create_engine(connstring)


# In[12]:


import pandas as pd
with engine.connect() as conn:
    df = pd.read_sql('Select * from "Data"."UFC"', conn)


# In[13]:


df


# In[ ]:




