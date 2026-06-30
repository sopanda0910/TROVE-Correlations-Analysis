import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Photometry Differences based on different timestamps
full_data = full_data.sort_values(by=['name', 'dt'])

full_data['phot_KN-diff'] = full_data.groupby('name')['phot_KN'].diff()
full_data['phot_KIS-diff'] = full_data.groupby('name')['phot_KN-in-SN'].diff()
full_data['phot_SK-diff'] = full_data.groupby('name')['phot_super-KN'].diff()
full_data = full_data.dropna(subset=['phot_KN-diff', 'phot_KIS-diff', 'phot_SK-diff'])

# Only consider high final scores (for any of the final scores)
threshold_score = 0.3
high_scorers = full_data[(full_data['KN'] > threshold_score) | (full_data['KN-in-SN'] > threshold_score) | (full_data['KN-in-SN'] > threshold_score)]
candidate_names = high_scorers['name']

plotting_data = high_scorers # full_data or high_scorers

times = plotting_data['dt']
phot_KN_diff = plotting_data['phot_KN-diff']
phot_SK_diff = plotting_data['phot_SK-diff']
phot_KIS_diff = plotting_data['phot_KIS-diff']

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].scatter(times, phot_KN_diff, label="Time vs phot_KN Difference", color='black', marker='x')
ax[0, 0].set_xlabel("Time (D)")
ax[0, 0].set_ylabel("phot_KN Difference")
ax[0, 0].set_title("Time vs phot_KN Difference")

ax[0, 1].scatter(times, phot_SK_diff, label="Time vs phot_super-KN Difference", color="black", marker='x')
ax[0, 1].set_xlabel("Time (D)")
ax[0, 1].set_ylabel("phot_super-KN Difference")
ax[0, 1].set_title('Time vs phot_super-KN Difference')

ax[1, 0].scatter(times, phot_KIS_diff, label="Time vs phot_KN-in-SN Difference", color="black", marker='x')
ax[1, 0].set_xlabel("Time (D)")
ax[1, 0].set_ylabel("phot_KN-in-SN Difference")
ax[1, 0].set_title('Time vs phot_KN-in-SN Difference')

plt.tight_layout()
plt.savefig('./out/deep_dive/corrs/photometry_analysis/high_scorers_phot_diffs_time.jpg')

# full_data.to_csv('data/processed/phot_diffs.csv')

# Generally need more information to understand what is significantly causing these drops