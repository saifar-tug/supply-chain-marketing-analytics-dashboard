import pandas as pd

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform the marketing dataset:
    - Handle missing values
    - Feature engineering for ML model
    """

    #basic cleaning ->>>
  
    # Convert to datetime
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
    ref_date = pd.to_datetime("2025-01-01")
    df['Customer_Duration'] = (ref_date - df['Dt_Customer']).dt.days

    #total children at home
    df['Total_Kids'] = df['Kidhome'] + df['Teenhome']

    #impute missing income based on education + marital group
    df['Income'] = df.groupby(['Education', 'Marital_Status'])['Income']\
                     .transform(lambda x: x.fillna(x.mean()))

    #feature engineering ->>>

    #total amount spent on products
    spend_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                  'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    df['Total_Spent'] = df[spend_cols].sum(axis=1)

    #total accepted campaigns
    cmp_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
    df['TotalAcceptedCmp'] = df[cmp_cols].sum(axis=1)

    #campaign engaged (binary)
    df['Campaign_Engaged'] = (df['TotalAcceptedCmp'] > 0).astype(int)

    #avg spending per visit (avoid division by 0)
    total_visits = df['NumStorePurchases'] + df['NumWebPurchases'] + df['NumCatalogPurchases']
    df['Avg_Spend_Per_Visit'] = df['Total_Spent'] / (total_visits + 1)

    return df
