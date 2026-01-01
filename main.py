import image_utils
load_image('dog.JPG')

from skimage.filters import median
from skimage.morphology import ball

clean_image = median(dog, ball(3))
edge_detection(clean_image) 
plt.figure(figsize=(5,5))
plt.imshow(edge_detection(clean_image), cmap='gray')
binary_image = edgeMAG > 50

from PIL import Image
edge_image = Image.fromarray(binary_image)
edge_image.save('my_edges.png')
