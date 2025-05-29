import os
from extract import load_raw_data
from transform import clean_and_transform
from load import save_processed_data

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_data_path = os.path.join(base_dir, "data/raw/marketing_campaign.csv")
    processed_data_path = os.path.join(base_dir, "data/processed/marketing_campaign_cleaned.csv")

    print("Loading raw data...")
    df_raw = load_raw_data(raw_data_path)

    print("Transforming data...")
    df_cleaned = clean_and_transform(df_raw)

    print("Saving cleaned data...")
    save_processed_data(df_cleaned, processed_data_path)

    print("Pipeline executed successfully.")

if __name__ == "__main__":
    main()
