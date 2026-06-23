import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

full_data = pd.read_csv("data/S251112cm_candidates_2026-06-12_scores_merged.csv")
# Removing unnecessary columns like ID and names
full_data = full_data.drop(full_data.columns[0:2], axis=1)
# print(full_data.head())

# Filter for extremely small distances and any empty fields
threshold = 1e-3
full_data = full_data.dropna(axis=0)
full_data = full_data[full_data['dist'] >= threshold]

# Output spearman correlations of every column with respect to every other column
# Produces a symmetric matrix with ones along its diagonal
full_data.corr('spearman').to_csv('./out/static/corrs.csv')