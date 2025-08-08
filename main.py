import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.utils.class_weight import compute_class_weight
np.random.seed(12049)

base_dir = "D:\TENSOR\Dataset"
train_path = os.path.join(base_dir, 'train')
test_path = os.path.join(base_dir, 'test')
print ("done")

