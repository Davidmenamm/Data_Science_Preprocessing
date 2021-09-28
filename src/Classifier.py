""" Run Classifier functions"""

# imports
from sklearn import metrics


# Run base classifier
# Return accuracy for dataset subset
def runClassifier(Classifier, featureTrain, targetTrain, featureTest, targetTest):
    # run classifier
    Classifier.fit(featureTrain, targetTrain)
    # predict
    prediction = Classifier.predict(featureTest)
    # accuracy
    accuracy = metrics.accuracy_score(targetTest, prediction)
    # returns
    return accuracy
