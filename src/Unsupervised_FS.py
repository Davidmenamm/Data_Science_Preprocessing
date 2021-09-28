""" Unsupervised Feature Selection Functions """

# imports
import pandas as pd
from ReadWrite import writeAll
import numpy as np


# Correlation matrix of data
def correlationMatrix(inputFile, outputCsv, outputVisual):
    # read dataset
    complete_df = pd.read_csv(inputFile, engine='c')
    # only target
    target = complete_df.iloc[:, 0]
    # only features
    features = complete_df.drop('Targ', 1)
    # correlation
    corr_df = features.corr(method='pearson')
    # prints to csv and visualization
    writeAll(outputCsv, outputVisual, corr_df)


# clean correlated variables
def cleanCorrelated(inputFileDataSet, inputFileCorr, outputCsv, outputVisual, threshold):
    # read correlation
    corr = pd.read_csv(inputFileCorr, engine='c')
    corr_abs = corr.abs()
    # read dataset
    complete_df = pd.read_csv(inputFileDataSet, engine='c')
    # only target
    target = complete_df.iloc[:, 0]
    # only features
    features = complete_df.iloc[:, 1: len(complete_df.columns)-1]
    # upper triangular matrix
    upper_tri = corr_abs.where(
        np.triu(np.ones(corr_abs.shape), k=1).astype(np.bool), other=0)
    # list to drop correlated index
    drop = [column for column in upper_tri.columns if any(
        upper_tri[column] > threshold)]
    # clean correlated
    clean_df = complete_df.drop(drop, axis=1)
    # print to csv and visualization
    writeAll(outputCsv, outputVisual, clean_df, drop)
