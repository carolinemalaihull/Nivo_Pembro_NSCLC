import pandas as pd

file_path = "data/GSE126044_series_matrix.txt"

gsm_ids = []

with open(file_path, "r") as f:
    for line in f:
        if line.startswith("!Series_sample_id"):
            line = line.strip().split("\t")[1]
            gsm_ids = line.split()

# clean quotes just in case
gsm_ids = [g.replace('"', '') for g in gsm_ids]

meta = pd.DataFrame({"GSM": gsm_ids})

print(meta)

meta.to_csv("results/sample_metadata.csv", index=False)

print("Saved clean sample metadata → results/sample_metadata.csv")