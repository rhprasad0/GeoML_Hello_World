# Entry point script for SageMaker inference instance deployment. Referenced by Deploy.ipynb

import joblib
import os

def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.pkl"))
    return clf
