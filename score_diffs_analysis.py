import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Filter based on candidates that have similar scores
full_data['KN_KIS_diff'] = full_data['KN'] - full_data['KN-in-SN']
full_data['KN_SK_diff'] = full_data['KN'] - full_data['super-KN']
full_data['SK_KIS_diff'] = full_data['super-KN'] - full_data['KN-in-SN']

full_data.to_csv('data/processed/diffs_all.csv')

# large_diffs = full_data[full_data['KN_KIS_diff'] > 0.1]

# Plot how these differences evolve over time