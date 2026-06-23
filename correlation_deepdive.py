import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Final Scores Correlation Plotting
# KN = np.array(full_data['KN'].values)
# KN_in_SN = np.array(full_data['KN-in-SN'].values)
# super_KN = np.array(full_data['super-KN'].values)

# fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# ax[0, 0].scatter(KN, KN_in_SN, label="KN vs KN-in-SN", color='black', marker='x')
# ax[0, 0].set_xlabel("KN")
# ax[0, 0].set_ylabel("KN-in-SN")
# ax[0, 0].set_title("KN vs KN-in-SN")

# ax[0, 1].scatter(KN, super_KN, label="KN vs super-KN", color="black", marker='x')
# ax[0, 1].set_xlabel("KN")
# ax[0, 1].set_ylabel("super-KN")
# ax[0, 1].set_title('KN vs super-KN')

# ax[1, 0].scatter(KN_in_SN, super_KN, label="KN-in-SN vs super-KN", color="black", marker='x')
# ax[1, 0].set_xlabel("KN-in-SN")
# ax[1, 0].set_ylabel("super-KN")
# ax[1, 0].set_title('KN-in-SN vs super-KN')

# plt.tight_layout()
# plt.savefig('./out/deep_dive/corrs/final_scores.jpg')

# General Conclusion from these plots
'''
For the final scores, there appears to be a very strong positive linear correlation, however for all 3 of the plots, there is also 
a weaker line which contains many transients that only have high scores in one of the final scores and not both. 
Additionally, there are many points that are clustered near 0, which shows that most transients have very low scores in general,
but there still is a strong positive correlation. 
These plots contain the data across all times and transients
'''

# Dist and Final Score Plotting
# dist = np.array(full_data['distance'])

# fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# ax[0, 0].scatter(dist, KN, label="dist vs KN", color="black", marker='x')
# ax[0, 0].set_xlabel("dist")
# ax[0, 0].set_ylabel("KN")
# ax[0, 0].set_title('dist vs KN')

# ax[0, 1].scatter(dist, KN_in_SN, label="dist vs KN-in-SN", color='black', marker='x')
# ax[0, 1].set_xlabel("dist")
# ax[0, 1].set_ylabel("KN-in-SN")
# ax[0, 1].set_title("dist vs KN-in-SN")

# ax[1, 0].scatter(dist, super_KN, label="dist vs super-KN", color="black", marker='x')
# ax[1, 0].set_xlabel("dist")
# ax[1, 0].set_ylabel("super-KN")
# ax[1, 0].set_title('dist vs super-KN')

# plt.tight_layout()
# plt.savefig('./out/deep_dive/corrs/dist_final_scores.jpg')

# General Conclusion
'''
The relationship between distance and the final scores are very similar across all 3 final scores. It shows a weak positive correlation with a 
strong limit at the y=x line. This is because of how the scoring works because all of the other subscores are restricted to between 0 and 1,
so the maximum possible value for the final score is the distance score, assuming that all other subscores are 1. This may be artificially 
inflating the correlation
'''

# Filter out the values based on different subscores and then plot the various final scores
filtered_data = full_data[full_data['predet_KN'] > 0.5]

KN = np.array(filtered_data['KN'].values)
KN_in_SN = np.array(filtered_data['KN-in-SN'].values)
super_KN = np.array(filtered_data['super-KN'].values)

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].scatter(KN, KN_in_SN, label="KN vs KN-in-SN", color='black', marker='x')
ax[0, 0].set_xlabel("KN")
ax[0, 0].set_ylabel("KN-in-SN")
ax[0, 0].set_title("KN vs KN-in-SN")

ax[0, 1].scatter(KN, super_KN, label="KN vs super-KN", color="black", marker='x')
ax[0, 1].set_xlabel("KN")
ax[0, 1].set_ylabel("super-KN")
ax[0, 1].set_title('KN vs super-KN')

ax[1, 0].scatter(KN_in_SN, super_KN, label="KN-in-SN vs super-KN", color="black", marker='x')
ax[1, 0].set_xlabel("KN-in-SN")
ax[1, 0].set_ylabel("super-KN")
ax[1, 0].set_title('KN-in-SN vs super-KN')

plt.tight_layout()
plt.savefig('./out/deep_dive/corrs/predet_KN_filtered_final_scores.jpg')