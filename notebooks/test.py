import torch, os
from utils.paths import *

print("Torch:", torch.__version__)
print("CUDA:", torch.cuda.is_available())
print("DATA_DIR:", DATA_DIR)