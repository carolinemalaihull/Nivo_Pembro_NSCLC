import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("results/deseq2_results.csv", index_col=0)

# remove NaNs
df = df.dropna(subset=["padj", "log2FoldChange"])

# avoid infinite / extreme noise
df = df[df["baseMean"] > 10]

# define significance
df["neg_log10_padj"] = -np.log10(df["padj"])

# top genes
top10 = df.sort_values("padj").head(10)