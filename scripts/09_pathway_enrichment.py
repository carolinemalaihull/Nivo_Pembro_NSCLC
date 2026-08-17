import pandas as pd
import gseapy as gp

# =========================
# LOAD DE RESULTS
# =========================
df = pd.read_csv("results/deseq2_results.csv", index_col=0)

# clean
df = df.dropna(subset=["padj", "log2FoldChange"])

# =========================
# CREATE RANKED LIST
# =========================
# gene ranking for GSEA-style analysis
ranked = df["log2FoldChange"].sort_values(ascending=False)

ranked_list = ranked.to_dict()

# =========================
# RUN ENRICHMENT (GO + KEGG)
# =========================
enr_go = gp.enrichr(
    gene_list=list(df[df["padj"] < 0.05].index.astype(str)),
    gene_sets=["GO_Biological_Process_2023"],
    organism="human",
    outdir="results/enrichment_go",
)

enr_kegg = gp.enrichr(
    gene_list=list(df[df["padj"] < 0.05].index.astype(str)),
    gene_sets=["KEGG_2021_Human"],
    organism="human",
    outdir="results/enrichment_kegg",
)

print("GO enrichment saved → results/enrichment_go")
print("KEGG enrichment saved → results/enrichment_kegg")