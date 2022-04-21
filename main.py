import glob
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from umap import UMAP
from sklearn.decomposition import PCA

from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Slider, ImageURL
from bokeh.layouts import layout

# Dependencies
# Make sure to install the additional dependencies noted in the requirements.txt using the following command:
# pip install -r requirements.txt

# You might want to implement a helper function for the update function below or you can do all the calculations in the
# update callback function.

####### HOW TO RUN ################
# Run EXACTLY this in your terminal
# no, really, exactly this ;-) otherwise the images don't show up
#
# python -m bokeh serve --show .
###################################


#############################
# Preprocessing #     1 Point
#############################


# Fetch the number of images using glob or some other path analyzer
N = len(glob.glob("static/*.jpg"))

# Find the root directory of your app to generate the image URL for the bokeh server
ROOT = os.path.split(os.path.abspath(os.path.dirname(__file__)))[1] + "/"

# Number of bins per color for the 3D color histograms
N_BINS_COLOR = 15

# Define an array containing the 3D color histograms. We have one histogram per image each having N_BINS_COLOR^3 bins.
# i.e. an N * N_BINS_COLOR^3 array
colorHistogram = []

r = np.random.randn(100,3)

# initialize an empty list for the image file paths
imageFilePath = []

# Compute the color and channel histograms
for idx, f in enumerate(glob.glob("static/*.jpg")):
    # open image using PILs Image package
    img = Image.open(f)

    # Convert the image into a numpy array and reshape it such that we have an array with the dimensions (N_Pixel, 3)
    a = np.asarray(img).reshape((img.width*img.height, 3))

    # Compute a multi dimensional histogram for the pixels, which returns a cube
    # reference: https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html
    histogram, edges = np.histogramdd(a, bins=(N_BINS_COLOR, N_BINS_COLOR, N_BINS_COLOR))
    # However, later used methods do not accept multi dimensional arrays, so reshape it to only have columns and rows
    # (N_Images, N_BINS^3) and add it to the color_histograms array you defined earlier
    # reference: https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
    p = np.reshape(histogram, (1, N_BINS_COLOR**3))
    colorHistogram.append(p)
    # Append the image url to the list for the server
    url = ROOT + f
    imageFilePath.append(url)
colorHistogram = np.reshape(colorHistogram, (121, N_BINS_COLOR**3))
print(colorHistogram.shape)
def compute_umap(n_neighbors=15) -> np.ndarray:
    """performes a UMAP dimensional reduction on color_histograms using given n_neighbors"""
    # compute and return the new UMAP dimensional reduction
    pass
    # return ...


def on_update_umap(old, attr, new):
    """callback which computes the new UMAP mapping and updates the source_umap"""
    # Compute the new t-sne using compute_umap

    # update the source_umap

    pass


def compute_tsne(perplexity=4, early_exaggeration=10) -> np.ndarray:
    """performes a t-SNE dimensional reduction on color_histograms using given perplexity and early_exaggeration"""
    # compute and return the new t-SNE dimensional reduction
    pass
    # return ...


def on_update_tsne(old, attr, new):
    """callback which computes the new t-SNE mapping and updates the source_tsne"""
    # Compute the new t-sne using compute_tsne

    # update the source_tsne

########################################
# Section ColumnDataSources # 0.5 Points
########################################

# Calculate the indicated dimensionality reductions
# references:
# https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
# https://umap-learn.readthedocs.io/en/latest/basic_usage.html

# Calculate the indicated dimensionality reductions


# Construct three data sources, one for each dimensional reduction,
# each containing the respective dimensional reduction result and the image paths
# source_pca =
# source_tsne =
# source_umap =


#############################
# Section Plots #  0.5 Points
#############################

# Create a first figure for the PCA data. Add the wheel_zoom, pan and reset tools to it.

# And use bokehs image_url to plot the images as glyphs
# reference: https://docs.bokeh.org/en/latest/docs/reference/models/glyphs/image_url.html

# Create a second plot for the t-SNE result in the same fashion as the previous.

# Create a third plot for the UMAP result in the same fashion as the previous.

# Create a slider to control the t-SNE hyperparameter "perplexity" with a range from 2 to 20 and a title "Perplexity"


#################################
# Section Callbacks #  1.0 Points
#################################

# Create a callback, such that whenever the value of the slider changes, on_update_tsne is called.
# Tipp: Using "value_throttled" instead of "value" ensures the callback is only fired when the mouse has stopped moving
# this helps reducing computation when the callback is expensive to compute
# ref https://stackoverflow.com/questions/38375961/throttling-in-bokeh-application

# Create a second slider to control the t-SNE hyperparameter "early_exaggeration"
# with a range from 2 to 50 and a title "Perplexity"

# Connect it to the on_update_tsne callback in the same fashion as the previous slider


# Create a third slider to control the UMAP hyperparameter "n_neighbors"

# Connect it to the on_update_umap callback in the same fashion as the previous slider

# You can use the command below in the folder of your python file to start a bokeh directory app.
# Be aware that your python file must be named main.py and that your images have to be in a subfolder name "static"

# bokeh serve --show .
# python -m bokeh serve --show .

# dev option:
# bokeh serve --dev --show .
# python -m bokeh serve --dev --show .
