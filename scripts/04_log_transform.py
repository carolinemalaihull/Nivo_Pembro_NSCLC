import pandas as pd
import numpy as np

# load cleaned matrix
df = pd.read_csv("results/clean_counts_matrix.csv", index_col=0)

# log2 transform
log_df = np.log2(df + 1)

print("Log-transformed matrix shape:", log_df.shape)
print(log_df.head())

# save
log_df.to_csv("results/log_counts_matrix.csv")

print("Log-transformed matrix saved.")
