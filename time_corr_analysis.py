import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

full_data = pd.read_csv("data/_S251112cm_candidates_2026-06-19_scores_tpost-all-merged.csv")
full_data = full_data.drop(full_data.columns[0], axis=1)

# Important Column Names to reference for the matrices
col_names = full_data.columns.delete(0).delete(0)

# All of the different time stamps
times = np.array(full_data[full_data.columns[0]].values)
# Rounding all dt values to nearest 10
rounded_down = list(set(np.floor(times / 10) * 10))
times = sorted(rounded_down)

matrices = dict()

def generate_matrix():
    for i in range(len(times) - 1):
        t_start = times[i]
        t_end = times[i+1]
        curr_df = full_data[(full_data['dt'] >= t_start) & (full_data['dt'] <= t_end)]
        curr_df = curr_df.drop('dt', axis=1)
        curr_df = curr_df.drop('name', axis=1)

        path = f'./out/time/corr_matrices/{int(t_start)}_{int(t_end)}.csv'
        corr_curr_matrix = curr_df.corr('spearman')

        matrices[str((t_start + t_end)/2)] = np.array(corr_curr_matrix)

        corr_curr_matrix.to_csv(path)

def generate_plots(time_stamps):
    for i in range(12):
        for j in range(i+1, 12):
            corr_vals = list()
            for key in matrices.keys():
                curr_mat = matrices[key]
                corr_vals.append(curr_mat[i][j])
            
            path = f'./out/time/plots/{col_names[i]}_{col_names[j]}.jpg'

            corr_data = np.column_stack((np.array(time_stamps), np.array(corr_vals)))
            df = pd.DataFrame(corr_data)
            df.to_csv(f'./out/time/plotting_data/{col_names[i]}_{col_names[j]}.csv')

            plt.figure(figsize=(10,8))
            plt.plot(time_stamps, corr_vals, 'kx')

            plt.xlabel('Time')
            plt.ylabel('Spearman Correlation')
            plt.title(f'Time Evolution of Correlations between {col_names[i]} and {col_names[j]}')
            plt.tight_layout()
            plt.savefig(path)
            plt.close()


generate_matrix()
time_stamps = list(matrices.keys())
generate_plots(time_stamps)