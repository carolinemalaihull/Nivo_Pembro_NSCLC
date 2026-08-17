import pandas as pd
import gseapy as gp
import mygene
import os

# =========================
# LOAD DE RESULTS
# =========================
df = pd.read_csv("results/deseq2_results.csv", index_col=0)

df = df.dropna(subset=["log2FoldChange"])
df = df[df["baseMean"] > 10]

print("DE shape:", df.shape)

# =========================
# MAP ENTREZ IDs → SYMBOLS
# =========================
mg = mygene.MyGeneInfo()

gene_ids = df.index.astype(str).tolist()

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

# replace index with symbols
df["symbol"] = df.index.astype(str).map(id_to_symbol)
df = df.dropna(subset=["symbol"])

df = df.set_index("symbol")

print("After annotation:", df.shape)

# =========================
# CREATE RANKED LIST (SYMBOLS)
# =========================
ranked = df["log2FoldChange"].sort_values(ascending=False)

os.makedirs("results", exist_ok=True)

rnk_file = "results/ranked_genes_symbol.rnk"
ranked.to_csv(rnk_file, sep="\t", header=False)

print("Saved ranked list →", rnk_file)

# =========================
# RUN GSEA
# =========================
pre_res = gp.prerank(
    rnk=rnk_file,
    gene_sets="KEGG_2021_Human",
    organism="human",
    outdir="results/gsea_kegg",
    seed=42,
)

print("KEGG GSEA saved → results/gsea_kegg")

pre_res_go = gp.prerank(
    rnk=rnk_file,
    gene_sets="GO_Biological_Process_2023",
    organism="human",
    outdir="results/gsea_go",
    seed=42,
)

print("GO GSEA saved → results/gsea_go")