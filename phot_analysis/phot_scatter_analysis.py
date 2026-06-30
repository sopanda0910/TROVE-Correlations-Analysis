import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Photometry Scatter Plots
phot_KN = np.array(full_data['KN'].values)
phot_KN_in_SN = np.array(full_data['KN-in-SN'].values)
phot_super_KN = np.array(full_data['super-KN'].values)

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].scatter(phot_KN, phot_KN_in_SN, label="phot_KN vs phot_KN-in-SN", color='black', marker='x')
ax[0, 0].set_xlabel("phot_KN")
ax[0, 0].set_ylabel("phot_KN-in-SN")
ax[0, 0].set_title("phot_KN vs phot_KN-in-SN")

ax[0, 1].scatter(phot_KN, phot_super_KN, label="phot_KN vs phot_super-KN", color="black", marker='x')
ax[0, 1].set_xlabel("phot_KN")
ax[0, 1].set_ylabel("phot_super-KN")
ax[0, 1].set_title('phot_KN vs phot_super-KN')

ax[1, 0].scatter(phot_KN_in_SN, phot_super_KN, label="phot_KN-in-SN vs phot_super-KN", color="black", marker='x')
ax[1, 0].set_xlabel("phot_KN-in-SN")
ax[1, 0].set_ylabel("phot_super-KN")
ax[1, 0].set_title('phot_KN-in-SN vs phot_super-KN')

plt.tight_layout()
plt.savefig('./out/deep_dive/corrs/photometry_analysis/photometry_scatter_plots.jpg')