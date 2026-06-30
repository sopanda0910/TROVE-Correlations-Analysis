import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Experiment with different score thresholds
full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
high_scorers = full_data[(full_data['KN'] >= 0.3) | (full_data['KN-in-SN'] >= 0.3) | (full_data['super-KN'] >= 0.3)]

diffs_data = pd.read_csv('./data/processed/phot_diffs.csv')
high_diffs = diffs_data[(diffs_data['phot_KN-diff'] >= 0.09) | (diffs_data['phot_KIS-diff'] >= 0.09) | (diffs_data['phot_SK-diff'] >= 0.09)]
high_diffs = diffs_data[(diffs_data['KN'] >= 0.3) | (diffs_data['KN-in-SN'] >= 0.3) | (diffs_data['super-KN'] >= 0.3)]
high_diffs_names = high_diffs['name'].unique()
print(f'{len(high_diffs)/len(high_scorers)} is the ratio of High diffs to High Scorers')
print(f'{len(high_diffs)} candidates satisfy criteria')

for name in high_diffs_names:
    name_data = full_data[full_data['name'] == name]

    times = name_data['dt']
    KN = name_data['KN']
    KIS = name_data['KN-in-SN']
    SK = name_data['super-KN']

    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    ax[0, 0].scatter(times, KN, label="Time vs KN", color='black', marker='x')
    ax[0, 0].set_xlabel("Time (D)")
    ax[0, 0].set_ylabel("KN")
    ax[0, 0].set_title("Time vs KN")

    ax[0, 1].scatter(times, KIS, label="Time vs KN-in-SN", color="black", marker='x')
    ax[0, 1].set_xlabel("Time (D)")
    ax[0, 1].set_ylabel("KN-in-SN")
    ax[0, 1].set_title('time vs KN-in-SN')

    ax[1, 0].scatter(times, SK, label="Time vs super-KN", color="black", marker='x')
    ax[1, 0].set_xlabel("Time (D)")
    ax[1, 0].set_ylabel("super-KN")
    ax[1, 0].set_title('Time vs super-KN')

    plt.tight_layout()
    plt.savefig(f'./out/deep_dive/corrs/photometry_analysis/high_diffs/{name}_scores_time.jpg')
    
    plt.close()

    print(f'Plotted {name}\'s Final Scores over Time')

# Ratio of 0.931 of High Diffs to High Scorers
# This is somewhat intuitive, but when there is a large difference in the photometry, it is likely that it is also a high scorer
# Also, these candidates are sometimes also high scorers in only 1 final score, meaning they are well determined