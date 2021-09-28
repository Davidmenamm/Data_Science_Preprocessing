""" Coordinates the functioning of all the program """

# imports
from Clean import normalize
from Supervised_FS import rankFeatures


# input routes
path_joined_dataset = r'data\input\SPECTF_join'

# output routes
# norm
path_norm = r'data\output\clean\SPECTF_join_norm'
path_norm_visual = r'data\output\clean\SPECTF_join_norm_visual'
# filter
path_filter_rank = r'data\output\filter\filter_rank'
path_filter_rank_visual = r'data\output\filter\filter_rank_visual'


# Coordinate
def coordinate():
    # 1) normalize
    numCols = 44
    normalize(
        numCols, path_joined_dataset, path_norm, path_norm_visual)
    # 2) Filter Ranking
    rankFeatures(path_norm, path_filter_rank, path_filter_rank_visual)
