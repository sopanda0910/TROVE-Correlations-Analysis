import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Time dependence
# Only consider high final scores (for any of the final scores)
threshold_score = 0.3
high_scorers = full_data[(full_data['KN'] > threshold_score) | (full_data['KN-in-SN'] > threshold_score) | (full_data['KN-in-SN'] > threshold_score)]
candidate_names = high_scorers['name']

plotting_data = full_data[full_data['name'].isin(candidate_names)]
times = plotting_data['dt']
phot_KN = plotting_data['phot_KN']
phot_SK = plotting_data['phot_super-KN']
phot_KIS = plotting_data['phot_KN-in-SN']

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].scatter(times, phot_KN, label="Time vs phot_KN", color='black', marker='x')
ax[0, 0].set_xlabel("Time (D)")
ax[0, 0].set_ylabel("phot_KN Difference")
ax[0, 0].set_title("Time vs phot_KN")

ax[0, 1].scatter(times, phot_SK, label="Time vs phot_super-KN", color="black", marker='x')
ax[0, 1].set_xlabel("Time (D)")
ax[0, 1].set_ylabel("phot_super-KN Difference")
ax[0, 1].set_title('Time vs phot_super-KN Difference')

# This looks almost identitical to the phot_KN
ax[1, 0].scatter(times, phot_KIS, label="Time vs phot_KN-in-SN", color="black", marker='x')
ax[1, 0].set_xlabel("Time (D)")
ax[1, 0].set_ylabel("phot_KN-in-SN Difference")
ax[1, 0].set_title('Time vs phot_KN-in-SN')

plt.tight_layout()
plt.savefig('./out/deep_dive/corrs/photometry_analysis/high_scorers_phot_time.jpg')