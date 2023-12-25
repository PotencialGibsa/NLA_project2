import numpy as np
import matplotlib.pyplot as plt

# Viewing a random MNIST image

def mnist_random_example():
    idx = np.random.randint(70000)
    exp = mnist_data[idx].reshape(image_size_px,image_size_px)
    print("The number in the image below is:", mnist_label[idx])
    plt.imshow(exp)


def num_show(data, label):
    print("The number in the image below is:", label)
    image_size_px = int(np.sqrt(data.shape[0]))
    plt.imshow(data.reshape(image_size_px,image_size_px))


# creating a normalization function

def normalize(data):
    mean = np.mean(data, axis=1, keepdims=True)
    std = np.std(data, axis=1, keepdims=True)
    data_normalized = (data - mean)/std
    return data_normalized

