import pandas as pd
import numpy as np

# load data
expr = pd.read_csv("results/log_counts_matrix.csv", index_col=0)
meta = pd.read_csv("results/sample_metadata.csv")

meta["GSM"] = meta["GSM"].astype(str).str.strip()

# align samples
expr = expr.T  # samples x genes

df = expr.merge(meta, left_index=True, right_on="GSM")

res = df[df["response"] == "responder"]
non = df[df["response"] == "non-responder"]

genes = expr.columns

# mean expression per gene
res_mean = res[genes].mean()
non_mean = non[genes].mean()

log2fc = res_mean - non_mean

# simple variance-based pseudo statistics
res_var = res[genes].var()
non_var = non[genes].var()

n1, n2 = len(res), len(non)

se = np.sqrt(res_var/n1 + non_var/n2)

t_stat = log2fc / se.replace(0, np.nan)

pvals = np.exp(-np.abs(t_stat))

results = pd.DataFrame({
    "log2FC": log2fc,
    "pval": pvals
})

results["neg_log10_pval"] = -np.log10(results["pval"] + 1e-10)

results.to_csv("results/de_results.csv")

print("DE results saved:", results.head())