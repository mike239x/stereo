"""
An implementation of a stereo algorith based on Lucas-Kanade method
"""

import sys, os, time

import skimage
import numpy as np

def preprocess_image(path):
    return list(skimage.transform.pyramid_gaussian(
        skimage.color.rgb2gray(
            skimage.io.imread(path)
        ),
        max_layer = 8,
        multichannel = False,
    ))
            
im_prmd_0 = preprocess_image('data/Classroom1-perfect/im0.png')
im_prmd_1 = preprocess_image('data/Classroom1-perfect/im1.png')

dx = list(map(skimage.filters.scharr_v, im_prmd_0))

dt = list(a - b for a,b in zip(im_prmd_0, im_prmd_1))

skimage.io.imshow_collection([
    dx[-1],
    dt[-1],
    dt[-1] / dx[-1], # disparity based on the last lvl of image pyramids
])
skimage.io.show()

