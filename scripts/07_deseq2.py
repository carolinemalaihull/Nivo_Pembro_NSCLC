import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# -------------------------
# LOAD RAW COUNTS
# -------------------------
counts = pd.read_csv("results/clean_counts_matrix.csv", index_col=0)

meta = pd.read_csv("results/sample_metadata.csv")
meta["GSM"] = meta["GSM"].astype(str).str.strip()
meta = meta.set_index("GSM")

# align samples
counts = counts.loc[:, meta.index]

# -------------------------
# BUILD DESIGN MATRIX
# -------------------------
meta["response"] = meta["response"].astype("category")

# -------------------------
# CREATE DESEQ2 OBJECT
# -------------------------
dds = DeseqDataSet(
    counts=counts.T,        # samples x genes
    metadata=meta,
    design_factors="response",
    refit_cooks=True,
)

# run DESeq2
dds.deseq2()

# -------------------------
# STAT TESTING
# -------------------------
stat_res = DeseqStats(dds, contrast=("response", "responder", "non-responder"))
stat_res.summary()

res = stat_res.results_df

# -------------------------
# CLEAN OUTPUT
# -------------------------
res = res.sort_values("log2FoldChange", ascending=False)

print(res.head())

res.to_csv("results/deseq2_results.csv")

print("Saved → results/deseq2_results.csv")
