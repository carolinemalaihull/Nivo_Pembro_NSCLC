import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "results/gsea_kegg/gseapy.gene_set.prerank.report.csv"

df = pd.read_csv(file_path)

print("Loaded shape:", df.shape)
print("Columns:", df.columns)

# =========================
# CLEAN DATA
# =========================
df = df.dropna(subset=["NES"])

# keep only meaningful results (optional but recommended)
df = df[df["NES"].abs() > 0]

# =========================
# TOP PATHWAYS
# =========================
top = df.sort_values("NES", ascending=False).head(10)

print(top[["Term", "NES", "FDR q-val"]])

# =========================
# PLOT
# =========================
plt.figure(figsize=(10, 6))

plt.barh(top["Term"], top["NES"])
plt.gca().invert_yaxis()

plt.xlabel("NES (Normalized Enrichment Score)")
plt.title("Top Enriched KEGG Pathways (GSEA)")

plt.tight_layout()

# =========================
# SAVE
# =========================
os.makedirs("results", exist_ok=True)

out_file = "results/gsea_top_pathways.png"
plt.savefig(out_file, dpi=300)

print("Saved →", out_file)