""" Supervised Feature Selection Functions """

# imports
import pandas as pd
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from ReadWrite import writeAll


# Rank features correlation with target
# returns a dataset of equal dimension, but
# ordered from left to right in feature importance
def rankFeatures(inputFile, outputCsv, outputVisual):
    # read dataset
    complete_df = pd.read_csv(inputFile, engine='c')
    # only target
    target = complete_df.iloc[:, 0]
    # only features
    features = complete_df.drop('Targ', 1)
    # filter paradigm using chi2
    colNum = len(features.columns)
    feature_selection = SelectKBest(score_func=chi2, k=colNum)
    feature_selection.fit_transform(features, target)
    # sort by most important inputs
    scores = zip(list(feature_selection.scores_), range(colNum))
    sortedScores = sorted(scores, key=lambda item: item[0], reverse=True)
    sortedIndex = [pos for scr, pos in sortedScores]
    sortedFeatures = features[features.columns[sortedIndex]]
    # join target
    complete_df_sorted = sortedFeatures.copy()
    complete_df_sorted.insert(0, target.name, target.values)
    # print to csv and visualization
    writeAll(outputCsv, outputVisual, complete_df_sorted)
