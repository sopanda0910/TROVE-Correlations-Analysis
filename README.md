## TROVE Data Correlation Analysis
Checking correlations between various columns in the data in a static and time-series 
Output files are in the out folder, containing correlations CSV matrices and plots of correlations over time

# Notes 
Due to the method of scoring, the correlations are artificially inflated because of the harsh upper bound,
because the final scores are simply a product of several subscores bounded between 0 and 1, so given that one of the 
sub scores are 0.5, the final score mathematically cannot be greater than 0.5. Due to this, much emphasis is not being spent
on correlation analysis currently. 

Another note is that the correlations between final scores are extremely high. This is natural because each of the final scores are calculated with almost all of the same sub_scores. An interesting thing to consider is the correlation between the various photometry scores. This actually is not interesting. The photometry scores are a direct rescaling of the final scores since all candidates, so they have the exact same correlations and plots, but just rescaled. Check out/deep_dive/corrs/final_scores.jpg compared to out/deep_dive/corrs/photometry_analysis/photometry_scatter_plots.jpg. They effective look identical

Additionally, it is shown that each photometry score is the key bifurcation between final scores, which is also 
intuitive because that is the only subscore that it is individual to each final score and different, so by filtering 
out certain high phot_KN scores for example, that decreases the number of candidates that have high scores in multiple final scores. 
Check out/deep_dive/phot_KN_filtered_final_scores.jpg for example, and compare this to out/deep_dive/final_scores.jpg
The final scores plot has 3 key lines (candidates that have high scores in both final scores, and then only high scores in one of the final scores). After filtering for high phot_KN scores, the only "high scores in KN_in_SN" or super-KN dramatically decreases.

Something that could be considered in the scoring is to softmax or a similar operation that suppresses other photometry scores if there is one that is extremely good. This introduces a non-linearity to the final score calculations, and also will likely decrease the correlation between final scores. However, because the theoretical models for these photometry scores have not been empirically tested due to lack of data, this may potentially suppress candidates scores even if they should be much higher. This should be given some more thought

Another interesting thing to analyze is to consider the plots of candidates that have similar final scores, and plot them with time. 
If there are any significant changes in the final score, try to determine what underlying subscore changed that caused the most significant changes.