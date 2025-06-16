import pandas as pd
import joblib
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

#cleaned dataset
df = pd.read_csv("data/processed/marketing_campaign_cleaned.csv")

#one-hot encode for categorical variables 
df_encoded = pd.get_dummies(df, drop_first=True)
''''before encoding we encountered this error
"ValueError: could not convert string to float: 'Graduation'"
...
because our process was trying to fit the RandomForestClassifier on data 
that still contains categorical strings — like Education = "Graduation" 
— instead of encoded numeric features.
'''

#split features and target
X = df_encoded.drop("Response", axis=1)
y = df_encoded["Response"]

#train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

#SMOTE
sm = SMOTE(random_state=42)
X_train_sm, y_train_sm = sm.fit_resample(X_train, y_train)

model = RandomForestClassifier(random_state=42)
model.fit(X_train_sm, y_train_sm)

#save model + feature names
joblib.dump((model, list(X.columns)), "models/marketing_response_model.pkl")
print("Model + features saved to models/marketing_response_model.pkl")

#save feature column names used during training
feature_cols = list(X_train_sm.columns)
with open("models/feature_columns.json", "w") as f:
    json.dump(feature_cols, f)
print("Feature columns saved to models/feature_columns.json")
