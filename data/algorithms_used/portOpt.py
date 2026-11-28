#imports
import pandas as pd
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

class portOpt:
    def __init__(self, covariancePath):
        covariance = pd.read_csv(covariancePath)
        self.tiker = covariance.columns[1:].to_list()
        self.cov = covariance.iloc[:,1:].values

