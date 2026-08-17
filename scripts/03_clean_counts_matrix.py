import pandas as pd

# load counts matrix
df = pd.read_csv(
    "results/raw_counts_loaded.csv"
)

# set GeneID as index
df = df.set_index("GeneID")

# convert all columns to numeric
df = df.apply(pd.to_numeric, errors="coerce")

# remove rows with missing values
df = df.dropna()

# remove genes with all zero counts
df = df.loc[(df.sum(axis=1) > 0)]

print("Clean matrix shape:", df.shape)
print(df.head())

# save cleaned matrix
df.to_csv("results/clean_counts_matrix.csv")

print("Clean counts matrix saved.")
