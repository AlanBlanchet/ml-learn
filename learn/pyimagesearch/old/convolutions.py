# import the necessary packages
import argparse

import cv2
import numpy as np
from skimage.exposure import rescale_intensity


def convolve(image, K):
    # grab the spatial dimensions of the image and kernel
    (iH, iW) = image.shape[:2]
    (kH, kW) = K.shape[:2]
    # allocate memory for the output image, taking care to "pad"
    # the borders of the input image so the spatial size (i.e.,
    # width and height) are not reduced
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float")

    # loop over the input image, "sliding" the kernel across
    # each (x, y)-coordinate from left-to-right and top-to-bottom
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # extract the ROI of the image by extracting the
            # *center* region of the current (x, y)-coordinates
            # dimensions
            roi = image[y - pad : y + pad + 1, x - pad : x + pad + 1]
            # perform the actual convolution by taking the
            # element-wise multiplication between the ROI and
            # the kernel, then summing the matrix
            k = (roi * K).sum()
            # store the convolved value in the output (x, y)-
            # coordinate of the output image
            output[y - pad, x - pad] = k
