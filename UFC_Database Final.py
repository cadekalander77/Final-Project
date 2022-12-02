#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import psycopg2
connstring = "postgresql+psycopg2://root:#Argyl0814*@ufc-database.cahc99ahc4gb.us-east-1.rds.amazonaws.com:5432/UFC_Database"
engine = create_engine(connstring)


# In[2]:


import pandas as pd
with engine.connect() as conn:
    df = pd.read_sql('SELECT * FROM "Data"."Fights" AS a LEFT JOIN "Data"."Fighters" AS b ON a."ID#" = b."ID#"', conn)


# In[3]:


df


# In[ ]:




