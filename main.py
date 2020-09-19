import numpy as np
import nibabel as nib

HOME_DIR = "./data"
DATA_DIR = HOME_DIR

def load_case(image_nifty_file, label_nifty_file):
    # load the image and label file
    image = nib.load(image_nifty_file)
    label = nib.load(label_nifty_file)

    # print the information for loaded image
    print(image.shape)

    # convert the image into 4d array, and then into numpy array
    image_arr = np.array(image.get_fdata())
    label_arr = np.array(label.get_fdata())

    return image_arr, label_arr

image, label = load_case(DATA_DIR + "/images/BRATS_003.nii.gz", DATA_DIR + "/labels/BRATS_003.nii.gz")
print(image)