import pandas as pd
import os

def save_processed_data(df: pd.DataFrame, output_path: str):
    """
    Save the cleaned and transformed dataset to the processed folder.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
