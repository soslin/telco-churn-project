import numpy as np
import pandas as pd
from env import host, user, password

# Data import
url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'

def wrangle_telco():
    telco_data = pd.read_sql('''SELECT * FROM customers AS c
JOIN contract_types AS ct
	ON c.contract_type_id = ct.contract_type_id
JOIN internet_service_types AS i
	ON i.internet_service_type_id = c.internet_service_type_id
JOIN payment_types AS p
	ON c.payment_type_id = p.payment_type_id
WHERE tenure > 0 OR total_charges > 0;''', url)
    return telco_data
wrangle_telco()

telco_df = wrangle_telco()

def peekatdata(telco_df):
    telco_df.head()
    telco_df.tail()
    telco_df.sample(10)
    telco_df.shape
    telco_df.describe()
    telco_df.info()
    return telco_df
peekatdata(telco_df)


def df_value_counts(telco_df):
    df.groupby('a').count()