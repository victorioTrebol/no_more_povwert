from lib_no_more_poverty.clustering_patterns.cluster_former import ClusterFormer
from lib_no_more_poverty.clustering_patterns.pattern_comparator import PatternComparator
from lib_no_more_poverty.mappers.similarity_map_builder import SimilarityMapBuilder

class CandleGroupClusterManager:
    def __init__(self, groups, tolerance):
        self.groups = groups
        self.tolerance = tolerance

    def group_clusters(self):
        comparator = PatternComparator(self.tolerance)
        # builder = SimilarityMapBuilder(self.groups, comparator)
        builder= LSHSimilarityMapBuilder(self.groups, comparator)
        similarity_map = builder.build()
        former = ClusterFormer(self.groups, similarity_map)
        self.grouped_clusters = former.form_clusters()
