import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# load data
df = pd.read_csv("results/log_counts_matrix.csv", index_col=0)
meta = pd.read_csv("results/sample_metadata.csv")

print("Expression samples:", df.shape)
print("Metadata samples:", meta.shape)

# clean GSM formatting
meta["GSM"] = meta["GSM"].astype(str).str.strip()

# PCA
X = df.T
pca = PCA(n_components=2)
components = pca.fit_transform(X)

pca_df = pd.DataFrame(components, columns=["PC1", "PC2"])
pca_df["GSM"] = X.index

print("PCA samples:", pca_df.shape)

# merge
merged = pd.merge(pca_df, meta, on="GSM", how="inner")

print("Merged shape:", merged.shape)
print(merged.head())

# STOP EARLY IF EMPTY
if merged.empty:
    print("❌ MERGE FAILED — GSM IDs do not match")
    print("Example PCA GSMs:", pca_df["GSM"].head().tolist())
    print("Example META GSMs:", meta["GSM"].head().tolist())
    exit()

# plot
plt.figure(figsize=(7,6))

colors = {
    "responder": "red",
    "non-responder": "blue",
    "unknown": "gray"
}

for group in merged["response"].unique():
    subset = merged[merged["response"] == group]
    plt.scatter(subset["PC1"], subset["PC2"],
                label=group,
                c=colors.get(group, "black"))

plt.legend()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA - GSE126044")

plt.tight_layout()
plt.savefig("results/pca_colored.png", dpi=300)

print("Saved → results/pca_colored.png")