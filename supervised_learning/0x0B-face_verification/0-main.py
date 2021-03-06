#!/usr/bin/env python3

from utils import load_images
import matplotlib.pyplot as plt

images, filenames = load_images('HBTN', as_array=True)
print(type(images), len(images), images.shape)
print(type(filenames), len(filenames))
idx = filenames.index('HaroldoVélezLora.jpg')
print(idx)
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i+idx])
    plt.title(filenames[i+idx])
plt.tight_layout()
plt.show()
