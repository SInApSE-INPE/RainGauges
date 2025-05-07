import numpy as np
import pandas as pd

def normalize_series(series):
    min_val = series.min()
    max_val = series.max()
    
    output = 2 * (series - min_val) / (max_val - min_val) - 1

    return output

def test(series):
    min_val = series.min()
    max_val = series.max()
    
    output = 2 * (series - min_val) / (max_val - min_val) - 1

    return output