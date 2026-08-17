import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mygene

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("results/deseq2_results.csv", index_col=0)

print("Raw shape:", df.shape)

# =========================
# CLEAN DATA
# =========================
df = df.dropna(subset=["padj", "log2FoldChange"])
df = df[df["baseMean"] > 10]

df["neg_log10_padj"] = -np.log10(df["padj"])

print("After cleaning:", df.shape)

# =========================
# SIGNIFICANT GENES
# =========================
sig = df[(df["padj"] < 0.05) & (abs(df["log2FoldChange"]) > 1)]

print("Significant genes:", sig.shape)

# top 10 most significant
top10 = sig.sort_values("padj").head(10)

# =========================
# ANNOTATE GENE IDS → SYMBOLS
# =========================
mg = mygene.MyGeneInfo()

gene_ids = top10.index.astype(str).tolist()

annot = mg.querymany(
    gene_ids,
    scopes="entrezgene",
    fields="symbol",
    species="human"
)

id_to_symbol = {}
for a in annot:
    if "symbol" in a:
        id_to_symbol[a["query"]] = a["symbol"]
    else:
        id_to_symbol[a["query"]] = a["query"]

# =========================
# PLOT
# =========================
plt.figure(figsize=(10, 7))

# all genes
plt.scatter(
    df["log2FoldChange"],
    df["neg_log10_padj"],
    s=5,
    alpha=0.4,
    color="grey"
)

# significant genes
plt.scatter(
    sig["log2FoldChange"],
    sig["neg_log10_padj"],
    s=10,
    color="red",
    alpha=0.8
)

# labels
for gene_id, row in top10.iterrows():
    label = id_to_symbol.get(str(gene_id), gene_id)

    plt.text(
        row["log2FoldChange"],
        row["neg_log10_padj"],
        label,
        fontsize=9
    )

# threshold line
plt.axhline(-np.log10(0.05), linestyle="--", color="black", linewidth=1)

# styling
plt.xlabel("log2 Fold Change (Responder vs Non-responder)")
plt.ylabel("-log10(FDR)")
plt.title("DESeq2 Volcano Plot (GSE126044)")

plt.tight_layout()

# =========================
# SAVE OUTPUT
# =========================
output_file = "results/volcano_FINAL.png"
plt.savefig(output_file, dpi=300)

print("Saved →", output_file)