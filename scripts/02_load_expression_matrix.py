import pandas as pd

# Load raw RNA-seq counts matrix
file_path = "data/GSE126044_raw_counts_GRCh38.p13_NCBI.tsv.gz"

df = pd.read_csv(
    file_path,
    sep="\t",
    compression="gzip"
)

print("Matrix shape:", df.shape)
print(df.head())

# Save loaded matrix
df.to_csv("results/raw_counts_loaded.csv", index=False)

print("Counts matrix loaded successfully.")
