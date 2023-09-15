import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
import pandas as pd
import pandas as pd
import os

# Define the path to the folder containing the CSV files
folder_path = '12_06_to_24_06'

# List all files in the directory with the .csv extension
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Initialize an empty list to store individual dataframes
dfs = []

# Loop through all csv files and read them into dataframes
for file in all_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all the individual dataframes into one dataframe
final_df = pd.concat(dfs, ignore_index=True)

print(final_df)

