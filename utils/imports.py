# Standard library
import os
import sys
import warnings
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Union

# Data manipulation
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# ML/DL
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms

# Scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Utilities
from tqdm.auto import tqdm

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')
