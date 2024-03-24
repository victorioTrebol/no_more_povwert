from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist, squareform
import numpy as np

class PatternGrouper:

    # def _calculate_percentage_difference(self, val1, val2):
    #     """
    #     Calculates the percentage difference between two values.
    #
    #     :param val1: First value for comparison.
    #     :param val2: Second value for comparison.
    #     :return: The percentage difference between the two values.
    #     """
    #     return abs(val1 - val2) / ((val1 + val2) / 2)
    #
    # def _cluster_rows(self):
    #     """
    #     Clusters rows based on the Euclidean distance between them and groups them according to the given tolerance.
    #
    #     :return: A list of groups, where each group is a list of rows (sublists from the original matrix) that are similar.
    #     """
    #     # Calculate Euclidean distance between all pairs of rows
    #     distances = pdist(self.matrix, 'euclidean')
    #     # Convert distances to a square matrix
    #     distance_matrix = squareform(distances)
    #     # Determine an appropriate distance threshold based on tolerance
    #     threshold_distance = np.mean(distance_matrix) * self.tolerance
    #     # Perform hierarchical clustering
    #     Z = linkage(distances, 'single')
    #     # Form groups based on the distance threshold
    #     group_assignments = fcluster(Z, t=threshold_distance, criterion='distance')
    #
    #     # Organize rows into groups based on their assignments
    #     groups = {}
    #     for i, group_id in enumerate(group_assignments):
    #         groups.setdefault(group_id, []).append(self.matrix[i].tolist())
    #
    #     return list(groups.values())
    #
    # def group_rows(self):
    #     """
    #     Public method to group rows of the matrix based on their pattern similarity within the given tolerance.
    #
    #     :return: A list of groups, where each group is a list of rows that are similar to each other.
    #     """
    #     return self._cluster_rows()

    def is_within_tolerance(self,val1, val2, tolerance):
        # Considera el caso donde ambos son cero
        if val1 == 0 and val2 == 0:
            return True
        # Evita la división por cero y maneja el caso de ceros adecuadamente
        if val1 == 0 or val2 == 0:
            return False
        # Calcula la diferencia porcentual con respecto al promedio de los dos valores
        percentage_difference = abs(val1 - val2) / ((abs(val1) + abs(val2)) / 2)
        return percentage_difference <= tolerance

    # Revisar la lógica de agrupación con la nueva función de comparación
    def group_rows_corrected(self,matrix, tolerance):
        groups = []
        for row in matrix:
            found_group = False
            for group in groups:
                if all(self.is_within_tolerance(val, group[0][i], tolerance) for i, val in enumerate(row)):
                    group.append(row)
                    found_group = True
                    break
            if not found_group:
                groups.append([row])
        return groups
