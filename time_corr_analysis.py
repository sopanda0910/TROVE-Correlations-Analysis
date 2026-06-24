import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Important Column Names to reference for the matrices
# Removing the labels of dt and names since that is not used in correlation analysis
col_names = full_data.columns.delete(0).delete(0)

# All of the different time stamps
times = np.array(full_data[full_data.columns[0]].values)
# Rounding all dt values to nearest 10
rounded_down = list(set(np.floor(times / 10) * 10))
times = sorted(rounded_down)
times = [0.01, 0.5, 1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 100.0]

matrices = dict()

def generate_matrix():
    for time in times:
        curr_df = full_data[full_data['dt'] == time]
        curr_df = curr_df.drop('dt', axis=1)
        curr_df = curr_df.drop('name', axis=1)

        path = f'./out/time/corr_matrices/{time}_corr.csv'
        corr_curr_matrix = curr_df.corr('spearman')

        matrices[time] = np.array(corr_curr_matrix)

        corr_curr_matrix.to_csv(path)

def generate_plots(time_stamps):
    # Only checking the correlations between sub scores and final scores (or final scores with other final scores)
    for i in range(12):
        for j in range(9, 12):
            # Removes the trivial correlation coefficient of 1 with itself
            if i == j:
                continue
            corr_vals = list()
            for key in matrices.keys():
                curr_mat = matrices[key]
                corr_vals.append(curr_mat[i][j])
            
            avg_corr = np.array(corr_vals).mean()
            path = f'./out/time/plots/{col_names[i]}_{col_names[j]}.jpg'

            corr_data = np.column_stack((np.array(time_stamps), np.array(corr_vals)))
            df = pd.DataFrame(corr_data)
            df.to_csv(f'./out/time/plotting_data/{col_names[i]}_{col_names[j]}.csv')

            plt.figure(figsize=(10,8))
            plt.ylim(-1, 1)
            plt.plot(time_stamps, corr_vals, 'kx')
            plt.axhline(y=avg_corr, linestyle='--', label=f'Average Correlation {avg_corr:.3f}')

            plt.xlabel('Time (Days)')
            plt.ylabel('Spearman Correlation')
            plt.legend()
            plt.title(f'Time Evolution of Correlations between {col_names[i]} and {col_names[j]}')
            plt.tight_layout()
            plt.savefig(path)
            plt.close()

generate_matrix()
time_stamps = list(matrices.keys())
generate_plots(time_stamps)

# General Conclusion
'''
There is a very high correlation between dist and the final scores (near 0.8-0.9), whereas most other sub scores have values 
between 0 to 0.3

There is a very high positive correlation between the different final score subgroups
'''