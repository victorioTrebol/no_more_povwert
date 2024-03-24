

class ClusterFormer:
    def __init__(self, groups, similarity_map):
        self.groups = groups
        self.similarity_map = similarity_map

    def form_clusters(self):
        visited = set()
        clusters = []
        for i in range(len(self.groups)):
            if i not in visited:
                cluster = self.__form_cluster(i, visited)
                clusters.append(cluster)
        return clusters

    def __form_cluster(self, index, visited):
        to_visit = [index]
        cluster = []
        while to_visit:
            current = to_visit.pop()
            if current not in visited:
                visited.add(current)
                cluster.append(self.groups[current])
                to_visit.extend(self.similarity_map.get(current, []))
        return cluster