""" Coordinates the functioning of all the program """

# imports
from Clean import normalize
from Supervised_FS import rankFeatures
from Unsupervised_FS import correlationMatrix, cleanCorrelated
from Hypothesis import findHypothesis


# input routes
path_joined_dataset = r'data\input\SPECTF_join'

# output routes
# norm
path_norm = r'data\output\clean\SPECTF_join_norm'
path_norm_visual = r'data\output\clean\SPECTF_join_norm_visual'
# filter rank
path_filter_rank = r'data\output\filter\filter_rank'
path_filter_rank_visual = r'data\output\filter\filter_rank_visual'
# correlation
path_correlation_matrix = r'data\output\correlation\corr_matrix'
path_correlation_matrix_visual = r'data\output\correlation\corr_matrix_visual'
path_correlation_features = r'data\output\correlation\corr_features'
path_correlation_features_visual = r'data\output\correlation\corr_features_visual'
# hypothesis
path_hypothesis = r'data\output\hypothesis'


# Coordinate
def coordinate():
    # 1) normalize
    numCols = 44
    normalize(
        numCols, path_joined_dataset, path_norm, path_norm_visual)
    # 2) Filter Ranking
    rankFeatures(path_norm, path_filter_rank, path_filter_rank_visual)
    # 3) Filter by correlation
    correlationMatrix(path_filter_rank, path_correlation_matrix,
                      path_correlation_matrix_visual)
    threshold = 0.8
    cleanCorrelated(path_filter_rank, path_correlation_matrix,
                    path_correlation_features, path_correlation_features_visual, threshold)
    # 4) Hypothesis
    findHypothesis(path_correlation_features,
                   path_hypothesis, 3, 5, 20)
