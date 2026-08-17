import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# load log matrix
df = pd.read_csv("results/log_counts_matrix.csv", index_col=0)

# transpose: samples as rows
X = df.T

# PCA
pca = PCA(n_components=2)
components = pca.fit_transform(X)

pca_df = pd.DataFrame(
    components,
    columns=["PC1", "PC2"],
    index=X.index
)

print("Explained variance:", pca.explained_variance_ratio_)

# plot
plt.figure(figsize=(6,5))
plt.scatter(pca_df["PC1"], pca_df["PC2"])

# label points
for sample in pca_df.index:
    plt.annotate(sample, (pca_df.loc[sample, "PC1"], pca_df.loc[sample, "PC2"]), fontsize=7)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA - GSE126044 RNA-seq")

plt.tight_layout()

# IMPORTANT: save file
plt.savefig("results/pca_plot.png", dpi=300)

print("Saved PCA plot → results/pca_plot.png")