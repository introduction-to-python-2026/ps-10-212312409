from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
  image = Image.open(path)
  image = np.array(image)
  return image
def edge_detection(image):
    dog_gray = np.mean(image, axis=2)
    kernelY = np.array([[1, 2, 1],
                      [0, 0, 0],
                      [-1, -2, -1]])
    kernelX = np.array([[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]])
    edgeX = convolve2d(dog_gray, kernelX, mode='same', boundary='symm')
    edgeY = convolve2d(dog_gray, kernelY, mode='same', boundary='symm')
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG

