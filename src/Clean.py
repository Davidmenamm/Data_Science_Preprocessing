""" Cleaning and Organizing functions"""

# imports
import pandas as pd
from ReadWrite import writeAll


# normalize
def normalize(numCols, inputFile, outputCsv, outputVisual):
    # read dataset to df
    # columns
    columnNames = ['Targ']
    columnNames.extend(['Col'+str(x) for x in range(1, numCols + 1)])
    complete_df = pd.read_csv(inputFile, engine='c', names=columnNames)
    # only target
    target = complete_df.iloc[:, 0]
    # only features
    features = complete_df.drop('Targ', 1)
    # normalize min max
    normalized_df = (features-features.min())/(features.max()-features.min())
    # add target
    complete_df_normalize = normalized_df.copy()
    complete_df_normalize.insert(0, target.name, target.values)
    # print to csv and visualization
    writeAll(outputCsv, outputVisual, complete_df_normalize)
