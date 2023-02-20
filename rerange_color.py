from PIL import Image
import numpy as np
import math
import random

def pack_color(img):
    return (img[:,:,0]<<16)+(img[:,:,1]<<8)+img[:,:,2]

def unpack_color(img):
    unpacked_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    unpacked_img[:,:,2] = img % 256
    img = img >> 8
    unpacked_img[:,:,1] = img % 256
    img = img >> 8
    unpacked_img[:,:,0] = img
    
    return unpacked_img

def sort_block(img, block_size):
    for x in range(math.ceil(img.shape[0]/block_size)):
        for y in range(math.ceil(img.shape[1]/block_size)):
            select_block = img[x*block_size:(x+1)*block_size, y*block_size:(y+1)*block_size]
            origin_size = select_block.shape
            select_block = select_block.flatten()
            select_block.sort()
            img[x*block_size:(x+1)*block_size, y*block_size:(y+1)*block_size] = select_block.reshape(origin_size)
    return img

def shuffle_block(img, block_size):
    np.random.seed(123)
    for x in range(math.ceil(img.shape[0]/block_size)):
        for y in range(math.ceil(img.shape[1]/block_size)):
            select_block = img[x*block_size:(x+1)*block_size, y*block_size:(y+1)*block_size]
            origin_size = select_block.shape
            select_block = select_block.flatten()
            np.random.shuffle(select_block)
            img[x*block_size:(x+1)*block_size, y*block_size:(y+1)*block_size] = select_block.reshape(origin_size)
    return img

def pipeline_sort(img_path, save_path, block_size):
    img = np.array(Image.open(img_path),dtype=np.uint32)
    packed_img = pack_color(img)
    sorted_img = sort_block(packed_img, block_size)
    unpacked = unpack_color(sorted_img)
    final_img = Image.fromarray(unpacked)
    final_img.save(save_path)
    return final_img

def pipeline_shuffle(img_path, save_path, block_size):
    img = np.array(Image.open(img_path),dtype=np.uint32)
    packed_img = pack_color(img)
    sorted_img = shuffle_block(packed_img, block_size)
    unpacked = unpack_color(sorted_img)
    final_img = Image.fromarray(unpacked)
    final_img.save(save_path)
    return final_img

if __name__ == "__main__":
    pipeline_sort("imgs/src.jpg", "imgs/src.rerange.block3.jpg", 3)
    pipeline_sort("imgs/src.jpg", "imgs/src.rerange.block5.jpg", 5)
    pipeline_sort("imgs/src.jpg", "imgs/src.rerange.block16.jpg", 16)
    pipeline_sort("imgs/src.jpg", "imgs/src.rerange.block32.jpg", 32)
    pipeline_sort("imgs/src.jpg", "imgs/src.rerange.block64.jpg", 64)
    pipeline_sort("imgs/src.jpg", "imgs/src.rerange.block256.jpg", 256)
