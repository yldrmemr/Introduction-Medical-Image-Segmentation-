# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:05:43 2021

@author: Dell
"""





BonePath = 'C:/Users/Dell/bone_image_dir/49_21.jpg'
MaskPath = 'C:/Users/Dell/mask_dir/49_21_HGE_Seg.jpg'
BrainPath= 'C:/Users/Dell/brain_image_dir/49_21.jpg'


def ApplyMaskForSegmentation(İmage,Mask ):
    import matplotlib.pyplot as plt
    
    brain_image = plt.imread(İmage)    # print(brain_image.shape)
    # bone_image = plt.imread(Bone)      # print(bone_image.shape)
    mask = plt.imread(Mask)        # print(mask.shape)

    plt.imshow(brain_image, cmap='gray')
    plt.imshow(mask, cmap='Reds', alpha=0.7)


ApplyMaskForSegmentation(BrainPath, MaskPath)

