import os
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


#Script de redimensionnement d'image créé à partir du script proposé dans le cadre du projet SILKNOW
#Présenté dans l'article de Clermont et al., 2020 (voir le document silk_classification_class.py au sein du GitHub "silknow_image_classification" URL : https://github.com/silknow/image-classification )

def rescaleImages(directory):
    imgpath_load = directory + r"/images/"
    imgpath_save = directory + r"_rescaled/"
    if not os.path.exists(imgpath_save):
        os.makedirs(imgpath_save)

    imglist = os.listdir(imgpath_load)
    print("\nTotal number of images: ", len(imglist))

    # for img_file in tqdm(imglist):
    deadlist_load = []
    deadlist_scale = []
    print("\nIterating over images (download): ")
    for img_file in tqdm(imglist, total=len(imglist)):

        # Skip images that are already scaled
        if os.path.exists(imgpath_save + img_file): continue

        # Try to open images, skip else
        try:
            img = plt.imread(imgpath_load + img_file)
        except:
            deadlist_load += [img_file]
            continue

        try:
            # get dimensions of image
            if len(img.shape) == 2:
                width, heigth = img.shape
                img_new = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.uint8)
                img_new[:, :, 0], img_new[:, :, 1], img_new[:, :, 2] = img, img, img
                img = img_new
            elif len(img.shape) == 3:
                width, heigth, _ = img.shape

            smaller_side = np.minimum(heigth, width)
            scale_factor = 500. / smaller_side

                # If Downscaling, apply gaussian blur
            if scale_factor < 1.:
                sigma = 1. / scale_factor
                kernelsize = int(sigma * 6) + (1 - (int(sigma * 6) % 2))
                img = cv2.GaussianBlur(img, (kernelsize, kernelsize), sigma)

            img_new = cv2.resize(img, (int(heigth * scale_factor), int(width * scale_factor)),
                                     interpolation=cv2.INTER_CUBIC)
            plt.imsave(imgpath_save + img_file, img_new)
        except:
            print("Erreur de mise à l'échelle:"+img_file)
            deadlist_scale += [img_file]

    if len(deadlist_load) > 0:
        print("\nThe following images could not be opened: ")
        for deadload in deadlist_load:
            print(deadload)
    if len(deadlist_scale) > 0:
        print("\nThe following images could not be scaled: ")
        for _ in deadlist_scale:
            print(deadlist_scale)