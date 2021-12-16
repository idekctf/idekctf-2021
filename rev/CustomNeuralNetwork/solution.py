import numpy as np
import tensorflow as tf

def Conv2dBackPropagate(out, layer):
    in_data = np.zeros(layer.input.shape[1:])
    stride = layer.kernel.shape[0]
    for i in range(layer.kernel.shape[-1]):
        for j in range(layer.kernel.shape[-2]):
            for x in range(in_data.shape[0] // stride):
                for y in range(in_data.shape[1] // stride):
                    in_data[x * stride : (x + 1) * stride,
                            y * stride : (y + 1) * stride,
                            j] += out[x,y,i] * layer.kernel.numpy()[:,:,j,i]
    return in_data

def GenerateSolution(filename):
    flag_model = tf.keras.models.load_model(filename)

    layer_1_out = Conv2dBackPropagate(np.array([[[1]]]), flag_model.layers[2])
    layer_0_out = Conv2dBackPropagate(layer_1_out, flag_model.layers[1])
    model_input = Conv2dBackPropagate(layer_0_out, flag_model.layers[0])

    flag_image = np.insert(model_input, range(0,55,9), -1, axis=1)
    flag_image = np.insert(flag_image, range(0,55,9), -1, axis=0)

    return flag_image
