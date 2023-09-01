# Load libraries
import joblib
import pandas as pd
import numpy as np

# load saved model
nba_model = joblib.load("./models/best_model/nba_draft_prediction.joblib")

# load test data
df_test = pd.read_csv('./data/raw/test.csv')
df_test_processed = pd.read_csv('./data/processed/week_3b/test.csv')

# make prediction on test set
y_test_prob = nba_model.predict_proba(df_test_processed)[:, 1] 
y_test_prob_rounded = np.round(y_test_prob, 3)

# make a csv file to submit on kaggle with player id 
output = pd.DataFrame({'player_id': df_test.player_id, 'drafted': y_test_prob_rounded})
output.to_csv('./submission_files/pred_rand_forest_week3b.csv', index=False)
print("Sucessfully saved submission file!")
