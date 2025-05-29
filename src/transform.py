import pandas as pd

def clean_and_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform the marketing dataset:
    - Handle missing Income
    - Feature engineering (Total_Kids, Customer_Duration, Total_Spent, etc.)
    """
    
    #date to datetime
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
    ref_date = pd.to_datetime("2025-01-01")
    df['Customer_Duration'] = (ref_date - df['Dt_Customer']).dt.days

    # total kids
    df['Total_Kids'] = df['Kidhome'] + df['Teenhome']

    # impute Income using group-based mean
    df['Income'] = df.groupby(['Education', 'Marital_Status'])['Income']\
                     .transform(lambda x: x.fillna(x.mean()))

    #total spending
    spend_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                  'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    df['Total_Spent'] = df[spend_cols].sum(axis=1)

    #Campaigns accepted
    cmp_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
    df['TotalAcceptedCmp'] = df[cmp_cols].sum(axis=1)

    return df
