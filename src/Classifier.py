""" Run Classifier functions"""

# imports
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from numpy import mean


# Run base classifier
# Return accuracy for dataset subset
def runClassifier(classifier, features, target, nFolds):
    # cross validation strategy
    cross_val_func = StratifiedKFold(n_splits=nFolds, shuffle=True)
    # evaluate model
    scores = cross_val_score(
        classifier, features, target, scoring='accuracy', cv=cross_val_func, n_jobs=-1)  # njob -1 uses all processors
    # mean accuracy
    acc = mean(scores)
    # returns
    return acc
