# Load libraries
import joblib

# load saved models
ohe = joblib.load("../../models/ohe.joblib")
scaler = joblib.load("../../models/scaler.joblib")
lr = joblib.load("../../models/log_reg_week1.joblib")

