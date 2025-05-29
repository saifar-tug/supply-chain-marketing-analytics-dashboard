import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load the raw marketing campaign data from CSV with correct separator.
    """
    df = pd.read_csv(path, sep=';')
    return df
