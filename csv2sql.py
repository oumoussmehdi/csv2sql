
# coding: utf-8

# In[ ]:


import pandas as pd


# In[27]:


def csv2sql(csv_file_path, sql_file_path, table_name):
    df = pd.read_csv(csv_file_path)
    for col in df.select_dtypes(include = object).columns:
        df[col] = df[col].apply(lambda x : "'"+x+"'")
    
    first_column = df.columns[0] # ""
    last_column = df.columns[-1]
    query = "INSERT INTO [dbo].["+table_name+"] VALUES (" 
    
    df[first_column] = df[first_column].apply(lambda x : query+ str(x))
    df[last_column] = df[last_column].apply(lambda x : str(x) + ");")
    
    df.to_csv(sql_file_path, header=False, index=False)


# In[30]:


csv_file_path = "DataScienceInArabic\\data\\WA_American-Time-Use-Survey-lite.csv"
sql_file_path =  "DataScienceInArabic\\data\\WA_American-Time-Use-Survey-lite.csvWA_American-Time-Use-Survey-lite.sql"
table_name = 'American-Time-Use-Survey-lite'


# In[31]:


csv2sql(csv_file_path, sql_file_path, table_name)

