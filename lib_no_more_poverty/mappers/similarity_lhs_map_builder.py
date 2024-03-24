from sklearn.cluster import DBSCAN

class CandleGroupClusterAggregator:
    def __init__(self, cluster_managers, tolerance):
        self.cluster_managers = cluster_managers
        self.tolerance = tolerance

    def aggregate(self):
        # Convert the groups attribute of each CandleGroupClusterManager instance to a 2D array
        data = [manager.return_pattern() for manager in self.cluster_managers]
        # Use the DBSCAN algorithm to group the data
        dbscan = DBSCAN(eps=self.tolerance).fit(data)

        # Create a dictionary to store the grouped CandleGroupClusterManager instances
        aggregated_clusters = {}
        for i, label in enumerate(dbscan.labels_):
            if label not in aggregated_clusters:
                aggregated_clusters[label] = []
            aggregated_clusters[label].append(self.cluster_managers[i])

        return list(aggregated_clusters.values())