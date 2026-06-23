import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

transient = 'AT2024aeuy'

filtered = full_data[full_data['name'] == transient]
times = np.array(filtered['dt'].values)
KN = np.array(filtered['KN'].values)
KN_in_SN = np.array(filtered['KN-in-SN'].values)
super_KN = np.array(filtered['super-KN'].values)


fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].scatter(times, KN, color='black', marker='x')
ax[0, 0].set_xlabel("Time (Days)")
ax[0, 0].set_ylabel("KN")
ax[0, 0].set_title("Time vs KN")

ax[0, 1].scatter(times, KN_in_SN, color="black", marker='x')
ax[0, 1].set_xlabel("Time (Days)")
ax[0, 1].set_ylabel("KN-in-SN")
ax[0, 1].set_title('Time vs KN-in-SN')

ax[1, 0].scatter(times, super_KN, color="black", marker='x')
ax[1, 0].set_xlabel("Time (Days)")
ax[1, 0].set_ylabel("super-KN")
ax[1, 0].set_title('Time vs super-KN')

plt.tight_layout()
plt.savefig(f'./out/deep_dive/time_dependence/{transient}_final_scores.jpg')

# This is the framework, but this should deep dive into some of the transients with 2 or 3 high final scores