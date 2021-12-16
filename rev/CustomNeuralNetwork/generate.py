import sys

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

import solution
import cnn_flag_checker

FONT = {
    "A": [[ 4, 0, 5],
          [ 0, 1, 0],
          [ 0,11, 0]],
    "B": [[ 0,11,14],
          [ 0,11, 5],
          [ 0, 9, 6]],
    "C": [[ 4,11, 5],
          [ 0, 1, 1],
          [ 7, 9, 6]],
    "D": [[ 0,11, 5],
          [ 0, 1, 0],
          [ 0, 9, 6]],
    "E": [[ 0,11,11],
          [ 0,11, 1],
          [ 0, 0, 0]],
    "F": [[ 0,11,11],
          [ 0,11, 1],
          [ 0, 1, 1]],
    "G": [[ 4,11, 5],
          [ 0, 1, 9],
          [ 7, 9, 3]],
    "H": [[ 0, 1, 0],
          [ 0,11, 0],
          [ 0, 1, 0]],
    "I": [[ 1, 0, 1],
          [ 1, 0, 1],
          [ 1, 0, 1]],
    "J": [[11,11, 0],
          [ 1, 1, 0],
          [ 7, 9, 6]],
    "K": [[ 0,12, 6],
          [ 0, 5, 1],
          [ 0, 7, 5]],
    "L": [[ 0, 1, 1],
          [ 0, 1, 1],
          [ 0, 9, 4]],
    "M": [[ 5, 1, 4],
          [ 0,15, 0],
          [ 0, 1, 0]],
    "N": [[ 5, 1, 0],
          [ 0, 2, 0],
          [ 0, 1, 7]],
    "O": [[ 4,11, 5],
          [ 0, 1, 0],
          [ 7, 9, 6]],
    "P": [[ 0,11, 5],
          [ 0, 9, 6],
          [ 0, 1, 1]],
    "Q": [[ 4,11, 5],
          [ 0, 1, 7],
          [ 7, 9, 2]],
    "R": [[ 0,11, 5],
          [ 0, 9, 6],
          [ 0, 1, 5]],
    "S": [[ 4,11, 2],
          [11,11, 5],
          [ 7, 9, 6]],
    "T": [[ 6, 0, 7],
          [ 1, 0, 1],
          [ 1, 0, 1]],
    "U": [[ 0, 1, 0],
          [ 0, 1, 0],
          [ 7, 9, 0]],
    "V": [[ 0, 1, 0],
          [ 0, 1, 6],
          [ 7, 3, 1]],
    "W": [[ 0, 1, 0],
          [ 0,13, 0],
          [ 7, 1, 6]],
    "X": [[ 7, 5, 3],
          [ 1, 0, 1],
          [ 3, 7, 5]],
    "Y": [[ 5, 1, 3],
          [ 7, 5, 1],
          [ 1, 0, 1]],
    "Z": [[ 6,11, 6],
          [ 1, 3, 1],
          [ 4, 0, 0]],
    "{": [[ 1, 6, 1],
          [12,10, 1],
          [ 1, 5, 1]],
    "}": [[ 1, 7, 1],
          [ 1, 8,14],
          [ 1, 4, 1]],
    "_": [[ 1, 1, 1],
          [ 1, 1, 1],
          [ 9, 9, 9]],
    " ": [[ 1, 1, 1],
          [ 1, 1, 1],
          [ 1, 1, 1]],}

def norm(kern):
    r = ((0.5-kern)*2.0)
    return r

def main():
    with open("flag.txt", "r") as f:
        flag = f.read().strip().upper()
    
    for char in flag:
        assert char in FONT
    
    img_size = int(np.ceil(np.sqrt(len(flag))))
    flag += " " * (img_size ** 2 - len(flag))

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(16, (3, 3), activation='linear',strides=(3,3),input_shape=(img_size * 9, img_size * 9, 1)))
    model.add(tf.keras.layers.Conv2D(30, (3, 3), activation='linear',strides=(3,3)))
    model.add(tf.keras.layers.Conv2D(1, (img_size, img_size), activation='linear'))
    
    kern = np.zeros((3,3,1))
    model.layers[0].kernel[:,:,:,0].assign(norm(kern).copy())
    model.layers[0].kernel[:,:,:,1].assign((norm(1-kern)).copy())
    kern[0,:,0] = [0,1,1]
    kern[1,:,0] = [1,0,1]
    kern[2,:,0] = [1,1,0]
    model.layers[0].kernel[:,:,:,2].assign(norm(kern).copy())
    model.layers[0].kernel[:,:,:,3].assign(norm(kern)[:,::-1,:].copy())
    kern[0,:,0] = [1,1,0]
    kern[1,:,0] = [1,0,0]
    kern[2,:,0] = [0,0,0]
    model.layers[0].kernel[:,:,:,4].assign(norm(kern).copy())
    model.layers[0].kernel[:,:,:,5].assign(np.rot90(norm(kern),3).copy())
    model.layers[0].kernel[:,:,:,6].assign(np.rot90(norm(kern),2).copy())
    model.layers[0].kernel[:,:,:,7].assign(np.rot90(norm(kern),1).copy())
    kern[0,:,0] = [1,1,0]
    kern[1,:,0] = [1,1,0]
    kern[2,:,0] = [1,1,0]
    model.layers[0].kernel[:,:,:,8].assign(norm(kern).copy())
    model.layers[0].kernel[:,:,:,9].assign(np.rot90(norm(kern),3).copy())
    model.layers[0].kernel[:,:,:,10].assign(np.rot90(norm(kern),2).copy())
    model.layers[0].kernel[:,:,:,11].assign(np.rot90(norm(kern),1).copy())
    kern[0,:,0] = [1,1,0]
    kern[1,:,0] = [1,0,0]
    kern[2,:,0] = [1,1,0]
    model.layers[0].kernel[:,:,:,12].assign(norm(kern).copy())
    model.layers[0].kernel[:,:,:,13].assign(np.rot90(norm(kern),3).copy())
    model.layers[0].kernel[:,:,:,14].assign(np.rot90(norm(kern),2).copy())
    model.layers[0].kernel[:,:,:,15].assign(np.rot90(norm(kern),1).copy())
    
    expanded_font = {}
    for k,v in FONT.items():
        img = np.zeros((9,9,1))
        for i in range(3):
            for j in range(3):
                img[i*3:(i+1)*3,j*3:(j+1)*3,:] = model.layers[0].kernel[:,:, :,v[i][j]]
        expanded_font[k] = np.copy(img < 0)

    valid_chars = list(FONT.keys())
    for i,v in enumerate(valid_chars):
        fm = FONT[v]
        for j in range(16):
            model.layers[1].kernel[:,:,j,i].assign((np.array(fm) == j) * 1.0)

    model.layers[2].weights[0].assign(np.zeros((6,6,30,1)))
    for i in range(img_size):
        for j in range(img_size):
            for k,v in enumerate(valid_chars):
                if v == flag[i*img_size + j]:
                    model.layers[2].weights[0][i,j,k,0].assign(1)

    model.compile()
    model.save('flag_model.h5')
    
    flag_image = solution.GenerateSolution('flag_model.h5')
    
    assert cnn_flag_checker.CheckImage(flag_image, 'flag_model.h5')
    
    plt.imshow(flag_image)
    plt.show()
    
if __name__ == '__main__':
    sys.exit(main())
