
# Lab 7: PCA and SVD for Dimensionality Reduction

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, TruncatedSVD

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Original Dataset Shape:", X.shape)

# Standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("\nPCA Results:")
print("Reduced Dataset Shape:", X_pca.shape)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Apply SVD
svd = TruncatedSVD(n_components=2, random_state=42)
X_svd = svd.fit_transform(X_scaled)

print("\nSVD Results:")
print("Reduced Dataset Shape:", X_svd.shape)
print("Explained Variance Ratio:", svd.explained_variance_ratio_)

# Visualize PCA results
plt.figure(figsize=(8, 6))
for i, name in enumerate(iris.target_names):
    plt.scatter(
        X_pca[y == i, 0],
        X_pca[y == i, 1],
        label=name
    )

plt.title("PCA - Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.savefig("Lab7/PCA-SVD/PCA_Visualization.png")
plt.show()

# Visualize SVD results
plt.figure(figsize=(8, 6))
for i, name in enumerate(iris.target_names):
    plt.scatter(
        X_svd[y == i, 0],
        X_svd[y == i, 1],
        label=name
    )

plt.title("SVD - Iris Dataset")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.legend()
plt.savefig("Lab7/PCA-SVD/SVD_Visualization.png")
plt.show()
