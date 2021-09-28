""" Hypothesis Features building """

# imports
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from Classifier import runClassifier
import pandas as pd
from ReadWrite import writeAll


# find top hypothesis features
# print results to file
def findHypothesis(inputCleanDataSet, outputFolder, division, nSelected):
    # read dataset
    complete_df = pd.read_csv(inputCleanDataSet, engine='c')
    # only target
    target = complete_df.iloc[:, 0]
    # only features
    features = complete_df.iloc[:, 1: len(complete_df.columns)-1]
    # feature divisions
    colNum = len(features.columns)
    chunks = []
    accuracies = []
    count = 0
    for i in range(0, colNum, division):
        previous = []
        if(count > 0):
            previous.extend(chunks[count-1])
        new = list(features.columns[i:i + division])
        # appends previous and new
        allElem = previous + new
        chunks.append(allElem)
        # split subset
        X_train, X_test, y_train, y_test = train_test_split(
            features[chunks[count]], target, test_size=0.33, stratify=target)
        featureOption = features[chunks[count]]
        # test accurracy
        acc = runClassifier(GaussianNB(), X_train, y_train, X_test, y_test)
        accuracies.append(acc)
        # counter
        count += 1
    # sort by accuracy
    chunksAccuracy = zip(chunks, accuracies)
    chunkSorted = sorted(
        chunksAccuracy, key=lambda item: item[1], reverse=True)
    # print to file top n
    for i in range(nSelected):
        fileCsv = outputFolder + r'\hypothesis_' + str(i)
        fileVisual = outputFolder + r'\hypothesis_visual_' + str(i)
        # subset dataset
        subsetFeatures, subsetAcc = chunkSorted[i]
        subset = features[subsetFeatures]
        # add target
        subset_complete = subset.copy()
        subset_complete.insert(0, target.name, target.values)
        # print to csv and visualization
        writeAll(fileCsv, fileVisual, subset_complete, subsetAcc)
