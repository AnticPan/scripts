from PIL import Image
import numpy as np
import sys

if __name__ == "__main__":
    png_name = sys.argv[1]
    jpg_name = png_name.replace(".png",".jpg")
    img = Image.open(png_name)
    if img.mode == "RGBA":
        arr = np.array(img)
        alpha = arr[:,:,3]/255
        mask = alpha==0
        arr = arr*alpha[:,:,None] + 255*(1-alpha[:,:,None])
        arr = arr[:,:,:3].astype(np.uint8)
        img = Image.fromarray(arr)
    img.save(jpg_name, quality=100, subsampling=0)
