# works well with Spyder

from matplotlib import cm 
import matplotlib.pyplot as plt
#import pylab
from sklearn.decomposition import PCA

from numpy import genfromtxt
data = genfromtxt('faces94.csv', delimiter=',')

# Visualize original image
def plotImg(x):
    fig, ax = plt.subplots()
    ax.pcolor(x.reshape(45, 50).T, cmap=cm.gray)
    ax.set_ylim([45, 0])
    ax.axis("off")
    fig.tight_layout()

# Apply PCA to compress and decompress the image
def plot_pca_img(img,n_pc = None):
    fig, ax = plt.subplots()
    x = img.reshape(45,50).T
    ax.set_ylim([45, 0])               
    pca = PCA(n_components= n_pc)
    pca.fit(x)
    compressed_x = pca.fit_transform(x)
    decompressed_x = pca.inverse_transform(compressed_x)
    plt.imshow(decompressed_x, cmap='gray')
    ax.axis("off")
    fig.tight_layout()

# Plot first image:    
print("Original image")
plotImg(data[15, :])

print("Downprojection to 99%") 
plot_pca_img(data[15], 0.99)

print("Downprojection to 95%") 
plot_pca_img(data[15], 0.95)

print("Downprojection to 90%") 
plot_pca_img(data[15], 0.90)

print("Downprojection to 75%") 
plot_pca_img(data[15], 0.75)
    
print("Downprojection to 50%") 
plot_pca_img(data[15], 0.50)

# Plot second image:
print("Original image")
plotImg(data[20, :])

print("Downprojection to 99%") 
plot_pca_img(data[20], 0.99)

print("Downprojection to 95%") 
plot_pca_img(data[20], 0.95)

print("Downprojection to 90%") 
plot_pca_img(data[20], 0.90)

print("Downprojection to 75%") 
plot_pca_img(data[20], 0.75)
    
print("Downprojection to 50%") 
plot_pca_img(data[20], 0.50)
